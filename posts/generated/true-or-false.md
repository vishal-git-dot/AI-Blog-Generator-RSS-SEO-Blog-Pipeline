---
title: "True or false?"
slug: "true-or-false"
author: "Akbar Ali"
source: "devto_webdev"
published: "Fri, 04 Sep 2026 15:54:06 +0000"
description: "Someone emailed me a signed contract, and I forwarded it to myself to test something. Outlook did what Outlook does. Re-saved the attachment on the way throu..."
keywords: "one, file, certificate, not, signed, you, document, nothing"
generated: "2026-09-04T16:05:41.192854"
---

# True or false?

## Overview

Someone emailed me a signed contract, and I forwarded it to myself to test something. Outlook did what Outlook does. Re-saved the attachment on the way through. Same contract, same signatures, same everything a human would care about. Different bytes. My verifier, which at that point returned a boolean, looked at it and said invalid . That's the moment I realised I had built a liar (a very confident one, which is worse). The thing I got wrong I'm building Putmysign , a small app for sending PDFs out and collecting signatures. At the end of it there's a /verify page: you drop a signed PDF on it, and it tells you whether the thing in your hands is real. The obvious design is a checkbox. Valid or not valid. Green or red. The obvious design is wrong, and it took a mail client to teach me why. Because "these are not the exact bytes I produced" and "this is a forgery" are not the same sentence . I had been printing the second one every time I meant the first. If you tell someone holding a perfectly real contract that it's fake, you haven't built a security feature. You've built a way to ruin somebody's Tuesday. Two checks, not one So the verdict comes from two completely independent checks, which fail for completely different reasons. One. Does the SHA-256 of this file match a document we finalized? That's the strongest answer there is: these are the exact bytes we made. This is the only check that needs a database row. Two. Is the certificate inside the file authentically ours? That second one needs explaining. When a document is finalized, I stamp a small HMAC-signed payload into the PDF's Keywords metadata. Who signed, when, the hash of the original, the document id. Base64url, because Keywords is a flat PDF string and JSON's quotes and parentheses have to be escaped correctly by every reader that ever touches the file (one opaque token has nothing to get wrong). export const MANIFEST_PREFIX = " putmysign-certificate-v1: " ; export function encodeManifest ( manifest : CertificateManifest , signature ?: string ) { const payload = manifestPayload ( manifest ); return ` ${ MANIFEST_PREFIX }${ payload }${ signature ? `. ${ signature } ` : "" } ` ; } The point of that: the document can speak for itself. My retention job deletes files on a schedule, by design. Someone downgrades, records age out, a mail client re-saves an attachment. In every one of those cases the byte-for-byte lookup finds nothing, and the only thing left in the world that can still say we issued this, for this document, with these signers is the certificate riding along inside the file. A verifier that only recognises documents you still hold a row for will fail on everything you promised to delete. Five outcomes So there are five, strongest first: verified : the bytes match a document we finalized. Nothing has changed. certified : the certificate is authentically ours, but the bytes aren't the ones we made. The signings happened. This particular file just isn't the artifact we issued. This is my Outlook contract. self-signed : signed with the free browser-only tool. Nothing witnessed it, so the file's account of itself is all there is. tampered : carries a certificate that does not check out. unknown : no certificate, no matching record. Not one of ours. The middle three are the whole post. Collapsing any of them into "invalid" would be the wrong answer more often than the right one, and I have the receipts (one receipt, from my own inbox, but still). There's a smaller decision in there I'm oddly proud of. A certificate with no signature at all is reported as unknown , not tampered , because that's what a document looks like when it was finalized while no signing key was configured. A signature that's present and wrong is a different matter entirely. Saying "forged" to someone holding a real contract is the worst mistake this endpoint could possibly make, so it only says it when it's actually sure. if ( ! signature ) return { verdict : " unknown " }; if ( ! certificateIsAuthentic ( payload , signature )) return { verdict : " tampered " }; return { verdict : " certified " }; The self-signed one The free tool on the landing page signs a PDF entirely in the browser. The file never touches my server. That's the promise, and I'm not breaking it to make my verifier's life easier. Which means: nothing witnessed it. Nothing could have witnessed it. I still write a certificate into it. Unsigned, marked kind: "self" , and worth exactly nothing as proof. But it means /verify can say "this was signed with Putmysign, by this name, on this date, and we were deliberately not involved", instead of reporting my own product's output as a stranger. A claim about a file isn't proof, but it beats a shrug. (The verify page keeps the same promise, by the way. Your PDF is read with File.arrayBuffer() and never uploaded. What goes to the server is a 32-byte one-way digest and the certificate that was already in the file. Neither of those is content.) The bit I'd do differently HMAC was the cheap choice. One environment variable, no key distribution, no ceremony. The cost is that the check has to run on my server. A sceptical counterparty, the exact person this feature exists for, cannot verify a certificate without asking me to confirm my own honesty, which is a hilarious thing to build into a trust product. A public key fixes it. That's the better end state and I haven't done it yet (I will, right after the eleven other things). Anyway. My actual take, one sentence: A verifier that can only say yes or no will spend most of its life saying the wrong one. Have you had a boolean like this in your own code, a flag that quietly collapsed two very different failures into one answer? I'd genuinely like to hear about it, mostly so I feel less alone about the mail client thing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pulimoodan/true-or-false-4c1a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
