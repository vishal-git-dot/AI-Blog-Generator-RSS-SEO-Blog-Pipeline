---
title: "HTTP 200 is not proof"
slug: "http-200-is-not-proof"
author: "Oroboro Labs"
source: "devto_webdev"
published: "Wed, 02 Sep 2026 20:38:33 +0000"
description: "HTTP 200 is not proof HTTP 200 is not proof Série Oroboro Labs — leia antes (3 notas anteriores desta série): The price the client sees is not the price you ..."
keywords: "not, check, you, one, content, your, hash, build"
generated: "2026-09-02T20:51:03.421087"
---

# HTTP 200 is not proof

## Overview

HTTP 200 is not proof HTTP 200 is not proof Série Oroboro Labs — leia antes (3 notas anteriores desta série): The price the client sees is not the price you typed Active is not sellable: one checkbox between a product and a store Uma guarda que recusa é uma guarda que funciona 2026-09-02 · field note from the publishing pipeline We publish a small static site through a build pipeline with a delay: you push, and for roughly two minutes the platform keeps serving the previous build. Our publisher used to "verify" each release the way most scripts do — it requested the page and checked for 200 OK. Then one day we sampled five pages right after a batch publish, and four of them returned a perfect 200 while serving the old content . Four out of five green checkmarks, lying. What a 200 actually answers A status code answers one question: is the server there and did it understand the request? It says nothing about which version of the file it handed you. Any pipeline with a build step, a CDN, or a cache sits between your push and your reader, and during the gap those layers answer 200 with yesterday's bytes. If your verification is a status check, your green light means "the site exists", not "your change shipped". The fix is a content hash, with one Windows-shaped twist The check that replaced ours is blunt: fetch the live URL with a cache-buster, hash the served bytes, and compare against a hash of the file on disk. Retry on a short window; if the hashes never meet, the publish failed — say so and exit non-zero. The twist: on a machine with core.autocrlf=true, the disk holds CRLF and the repository (what gets served) holds LF. A byte-for-byte hash reports every page as stale, forever. We measured one page at exactly 203 bytes of difference before anything else differed. The comparison has to normalize line endings first — what you want to detect is old content , not line-break style. Did it earn its keep? On its first real run, the new check caught the build mid-flight (a 404 during the deploy window), kept waiting, and only confirmed the release once the served HTML matched the disk. The stale check also behaves honestly on pages that did not change: it reports them as matching, so it isn't just crying "stale" at everything. We then extended the same pattern to the other publishing routes in the workshop, including the hash check against unchanged live pages and a public-content check on the mirror platform, where creation returns 201 — and 201 has exactly the same flaw as 200. Creation acknowledged is not content served. The transferable lesson Whenever you verify a system that has any distance between "accepted" and "served" — a queue, a build, a cache, a CDN — verify at the layer the user sees, and verify content , not signals. Ask for the bytes and hash them. And when your check starts flagging everything, check what your check is comparing before you conclude the site is broken: a wrong verifier that always fails is annoying, but a wrong verifier that always passes is how stale content ships with a smile. Read before or after: the price the client sees is not the price you typed — the same discipline applied to marketplace pricing. Transparency: numbers in this note are from our own publishing pipeline on 2026-09-02 — 5 samples after a batch publish (4 stale with 200), one production catch by the new check, one line-ending divergence measured at 203 bytes on an unchanged page. No third-party platform is named; the pattern is generic. Our storefront — vault template and the 54-note offline pack Originally published on the Oroboro Labs blog .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/oroborolabs/http-200-is-not-proof-35dm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
