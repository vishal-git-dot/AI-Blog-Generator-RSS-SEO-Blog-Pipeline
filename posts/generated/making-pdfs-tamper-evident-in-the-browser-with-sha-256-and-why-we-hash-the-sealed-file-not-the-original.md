---
title: "Making PDFs tamper-evident in the browser with SHA-256 (and why we hash the sealed file, not the original)"
slug: "making-pdfs-tamper-evident-in-the-browser-with-sha-256-and-why-we-hash-the-sealed-file-not-the-original"
author: "trampto"
source: "devto_webdev"
published: "Fri, 13 Nov 2026 23:08:56 +0000"
description: "AI has made it trivial to edit an invoice, a quote or a contract so cleanly that nobody can spot the change by eye. A PDF has no memory: the file name, the d..."
keywords: "file, sealed, not, hash, bytes, sha, pdf, one"
generated: "2026-11-13T23:25:16.992682"
---

# Making PDFs tamper-evident in the browser with SHA-256 (and why we hash the sealed file, not the original)

## Overview

AI has made it trivial to edit an invoice, a quote or a contract so cleanly that nobody can spot the change by eye. A PDF has no memory: the file name, the date and the layout all look the same after someone changes "1,800 €" to "4,800 €". So instead of trying to detect a forgery by how it looks, we built TRAMPTO to prove that a document hasn't changed, with plain math. This post walks through how it works, the one design decision that bit us, and what this approach does not prove. The idea in one line Compute a SHA-256 fingerprint of the document, register it, and give the recipient a link where they can recompute it themselves. Change one byte and the fingerprint no longer matches. Hashing in the browser with Web Crypto No libraries needed. The whole thing runs client-side with the Web Crypto API: export async function sha256Hex ( bytes : Uint8Array ) : Promise < string > { // Copy only this view's bytes: a Uint8Array can be a window // into a larger ArrayBuffer, and hashing the whole buffer // would give you a different (wrong) fingerprint. const buffer = bytes . buffer . slice ( bytes . byteOffset , bytes . byteOffset + bytes . byteLength ) as ArrayBuffer ; const digest = await crypto . subtle . digest ( "SHA-256" , buffer ) ; return Array . from ( new Uint8Array ( digest ) ) . map ( ( b ) => b . toString ( 16 ) . padStart ( 2 , "0" ) ) . join ( "" ) ; } That slice(byteOffset, …) line looks redundant until it isn't. If the bytes come from a parser or a file reader that hands you a view over a bigger buffer, hashing bytes.buffer directly silently fingerprints the wrong data. Two codebases that both "compute SHA-256 of the file" will then disagree, and every verification fails. Because the hash is computed on the device, the document itself never leaves the browser . Only the fingerprint, the file name and a seal ID go to the register. Sealing: two hashes, not one When a document is sealed, we compute two fingerprints: contentHash : SHA-256 of the original file, before we touch it. We add a tiny visual micro-seal to each page (about 6 mm, 15% opacity, bottom-right corner, respecting page rotation) and write contentHash into the PDF metadata. stampedHash : SHA-256 of the final sealed PDF . const contentHash = await sha256Hex ( pdfBytes ) ; // original const pdfDoc = await PDFDocument . load ( pdfBytes ) ; for ( const page of pdfDoc . getPages ( ) ) drawDiscreetMark ( page ) ; pdfDoc . setSubject ( `TRAMPTO-HASH:${contentHash}` ) ; const sealedBytes = new Uint8Array ( await pdfDoc . save ( ) ) ; const stampedHash = await sha256Hex ( sealedBytes ) ; // public fingerprint The public verification link is /v/{stampedHash} . The decision that matters: hash the sealed file It's tempting to make the public fingerprint the hash of the original. Don't. The file people actually send around is the sealed one. If the link pointed at the original's hash, a recipient holding the sealed PDF could never reproduce it. The order is an invariant: hash original → seal → hash sealed . If you ever change the order, the seal drawing, or touch the PDF after computing stampedHash , every link you've already issued stops verifying. We treat that sequence like a database migration: it doesn't change casually. Verifying The recipient opens the link (or drops the file on the verify page). The browser recomputes SHA-256 of the file they have and looks it up in the register: Match → the file is byte-for-byte the one that was sealed, and we show when it was sealed. No match → something changed, even a single byte. One detail worth copying: distinguish "not found" from "network error" . If the backend is down, we must not tell someone their genuine document is fake. A failed lookup throws and asks to retry; only a clean "no row" means "not verified". Other formats Word, PowerPoint, images and text are converted to PDF in the browser first (heavy libraries like pdf-lib and mammoth are loaded on demand with dynamic import() so the app opens instantly). Then the same sealing flow runs. What this does not prove Being honest about limits matters more than the feature list: It proves integrity, not authorship. It shows the file hasn't changed since it was sealed. It doesn't prove who wrote it or that its content is true. It's not a qualified e-signature. It doesn't replace eIDAS qualified signatures or seals where the law requires them. The "when" relies on our register. The sealing date comes from TRAMPTO's database, not from a blockchain or a qualified timestamp authority. For quotes, contracts, invoices, reports and certificates, where the risk is "someone quietly changed the numbers", that's usually exactly the guarantee you need. Try it trampto.com : verifying is always free, and the first 3 seals are free. I'd love feedback from other devs, especially on the verification UX for people who have never heard of a hash.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/trampto_006da128a0ab6e1f6/making-pdfs-tamper-evident-in-the-browser-with-sha-256-and-why-we-hash-the-sealed-file-not-the-4k4c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
