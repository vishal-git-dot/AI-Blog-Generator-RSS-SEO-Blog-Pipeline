---
title: "The HSTS Header You Just Marked 'Pass' Doesn't Protect the Request That Actually Matters"
slug: "the-hsts-header-you-just-marked-pass-doesnt-protect-the-request-that-actually-matters"
author: "Rocky"
source: "devto_webdev"
published: "Tue, 25 Aug 2026 18:30:46 +0000"
description: "You're doing a quick pass on a header checklist before the real testing starts. curl -I comes back with Strict-Transport-Security: max-age=31536000 . HSTS pr..."
keywords: "header, request, browser, hsts, you, before, max, age"
generated: "2026-08-25T18:46:02.102438"
---

# The HSTS Header You Just Marked 'Pass' Doesn't Protect the Request That Actually Matters

## Overview

You're doing a quick pass on a header checklist before the real testing starts. curl -I comes back with Strict-Transport-Security: max-age=31536000 . HSTS present, box checked, on to the next line item. Except the header you just verified doesn't protect the one request an attacker on that network would actually want. HSTS works on a promise the browser can only keep after it's already heard from the server once: the header tells the browser "for the next max-age seconds, upgrade every request to this domain to HTTPS automatically, don't even try plaintext." That promise only exists in the browser's memory after it has received the header at least once over a connection nobody tampered with. The very first request a given browser ever sends to a domain, a first-ever visit, a fresh install, a cleared cache, a public terminal, has no stored HSTS state to enforce anything. It goes out however the browser or the address bar entry says to go out, and if that's plain HTTP, an attacker sitting on the same network segment (a coffee shop AP, an ARP-spoofed office LAN) gets a real shot at intercepting and downgrading that specific request before HSTS ever has a chance to matter. This is documented, well-understood behavior, not an edge case: it's usually called trust-on-first-use, and it's exactly why the header alone was never the whole control. The fix that closes the gap isn't a bigger max-age. It's the HSTS preload list: a hardcoded list shipped inside the browser itself, checked before any network request happens at all, so there is no first request to intercept because the browser already knew to go HTTPS-only before it ever asked DNS a question. Getting on that list requires includeSubDomains , a max-age of at least a year, and a preload directive in the header, then actually submitting the domain at hstspreload.org and waiting for the next browser release cycle to ship it. A header with none of that is still real protection for request two through however many, and it is still, on its own, an incomplete answer to "is this domain protected against downgrade." That's the header. The protocol underneath it has just as many places where "I see the thing" and "I verified the thing does what I assume" quietly diverge: TLS handshake details that decide whether a downgrade is even possible, HTTP/2's binary framing changing what a request smuggling attempt even looks like on the wire, HTTP/3 running over QUIC instead of TCP entirely. None of that shows up if the extent of your protocol knowledge is reading header names off a curl output and pattern-matching them against a list you memorized once. Codelivly's HTTP Protocol Book for Developers is built for exactly that gap, the protocol-level literacy underneath the headers, so "HSTS: present" turns into an actual judgment call about what it does and doesn't cover instead of a box you checked because the string was there.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rockyyy/the-hsts-header-you-just-marked-pass-doesnt-protect-the-request-that-actually-matters-4eih

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
