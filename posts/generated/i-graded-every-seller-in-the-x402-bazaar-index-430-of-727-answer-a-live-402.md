---
title: "I graded every seller in the x402 Bazaar index: 430 of 727 answer a live 402"
slug: "i-graded-every-seller-in-the-x402-bazaar-index-430-of-727-answer-a-live-402"
author: "edvyno"
source: "devto_webdev"
published: "Wed, 28 Oct 2026 21:53:20 +0000"
description: "The x402 Bazaar index is Coinbase's discovery catalog of x402 sellers. It is a machine-readable list of where agents can spend money — and almost nobody has ..."
keywords: "hosts, catalog, sellers, per, does, never, your, fix"
generated: "2026-10-28T22:24:29.416939"
---

# I graded every seller in the x402 Bazaar index: 430 of 727 answer a live 402

## Overview

The x402 Bazaar index is Coinbase's discovery catalog of x402 sellers. It is a machine-readable list of where agents can spend money — and almost nobody has asked how many of those listings actually work. I probed every host in it. Here is the census. The numbers 727 distinct hosts enumerated from the discovery API (100 resources per page) 430 of them answered a live 402 — the rest were unreachable, free, or dead Grade distribution: A 116 · B 36 · C 52 · D 160 · F 360 Grades weigh payment plumbing and discoverability, not product quality: does the listed URL answer, does the challenge decode, does the amount exist, is payTo and a CAIP-2 network present, is the price readable by a human reading a log, is there an MCP surface, and how fast does it answer. What actually breaks Top defects across all paid surfaces: no_well_known — 208 hosts no_paid_routes — 129 hosts no_catalog — 97 hosts wrong_status — 71 hosts unparseable_402 — 34 hosts no_well_known is the big one: no /.well-known/x402 document. An agent that discovers sellers by convention never finds you, no matter how good your route is. It costs nothing to add and it is the single most common gap in the catalog. Why this matters for sellers A dead or opaque listing is invisible revenue loss. If your catalog entry 402s but a buyer's client cannot parse the challenge, or your payTo is missing, the buyer's retry logic gives up — and you never see the failed call in your own logs. The seller never learns; the buyer never returns. What I built from it Free : score any host — grade, per-route status, and the fix list, no signup. The full scoreboard lists every seller I graded. $10 endpoint audit, $49 audit + prioritised fix plan (with two re-verification runs so the fix is provable). $99 catalog report : the whole graded census as JSON — per-host grade, defect ids, latency. Directory operators and facilitators use it to spot dead listings before their users do. And a different kind of product I publish from the same measurement discipline: model football picks where a last-6-form Poisson beats the live Polymarket moneyline by 10+ points. The free preview shows the settled record only — check it before you pay $0.50 for today's sheet. A pick sheet without its record is a sales pitch, not a product. Everything above is pay-per-call in USDC over x402. No signup, no API key, no invoices. Measurement date: 2026-10-28. Grades reflect payment plumbing and discoverability at that moment; sellers fix and break things weekly, so the census is refreshed and the full report is regenerated on each purchase.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/edvyno/i-graded-every-seller-in-the-x402-bazaar-index-430-of-727-answer-a-live-402-23ad

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
