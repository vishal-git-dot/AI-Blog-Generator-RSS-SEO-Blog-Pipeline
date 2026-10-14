---
title: "Two new x402 APIs: web-cache-poisoning probe + deep CORS preflight trace (2026-10-14)"
slug: "two-new-x402-apis-web-cache-poisoning-probe-deep-cors-preflight-trace-2026-10-14"
author: "HAL GOBVAN"
source: "devto_python"
published: "Wed, 14 Oct 2026 04:14:05 +0000"
description: "Two new $0.0005 USDC x402 endpoints shipped today in the URL Metadata API catalog. /api/cache-poisoning-vulnerability Active probe for the well-known web-cac..."
keywords: "api, cache, cors, url, poisoning, preflight, forwarded, probes"
generated: "2026-10-14T04:22:01.693168"
---

# Two new x402 APIs: web-cache-poisoning probe + deep CORS preflight trace (2026-10-14)

## Overview

Two new $0.0005 USDC x402 endpoints shipped today in the URL Metadata API catalog. /api/cache-poisoning-vulnerability Active probe for the well-known web-cache-poisoning vector class. Sends 5 unkeyed-header variants (X-Forwarded-Host + X-Original-URL + X-Forwarded-Prefix + X-Host + X-Forwarded-Server + X-Forwarded-For + X-Forwarded-Proto + X-Original-Host + X-Rewrite-URL), 4 cachebuster-query probes (cb + nocache + utm_source + gclid), and 4 web-cache-deception path probes (robots.txt + .css + .js + .png). Compares body-hash against a baseline fetch and flags any divergence without matching Vary disclosure. Returns web_cache_poisoning_score 0-100 A-F and a verdict. Tested on stripe.com: 5 poisoned headers detected without Vary disclosure. score=40 grade=D verdict=high_poisoning_risk. On example.com: score=100 grade=A no_poisoning_detected. Distinct from cdn-cache-key-collision (c139) and request-smuggling-evidence (c129): this one invokes the well-known poisoning payloads themselves. /api/preflight-cors-trace Deep CORS preflight OPTIONS audit. 6 sequenced probes (baseline GET + simple-Origin preflight + post+contenttype+auth + multi-header x-custom-1/x-custom-2 + credentials + DELETE-method). Per probe captures the full Access-Control-* response set (ACAO + ACAC + ACAM + ACEH + ACEX + ACMA + ACPN) plus Vary. Aggregates method_allowlist_observed + header_allowlist_observed across probes. Returns cors_preflight_score 0-100 A-F + a credential_risk matrix. Optional &origin= parameter overrides the test origin (default https://example.com ). Distinct from cors-policy (c89 single-shot one Origin): this sweeps the actual allowed-headers enumeration. Both routes are gated via x402 payTo 0xCa0a6c6Aa7A8F0D5893636CF166Ea2b44fb6500c USDC on Base mainnet. 402 envelope verified live via Cloudflare tunnel. Bogus X-PAYMENT on both returns 402 with malformed_payment_header from the real pay.openfacilitator.io facilitator (settlement is real, not stub). Both endpoints are the 197th and 198th paid routes in the catalog (195 -> 197 this cycle). See /.well-known/x402 or /openapi.json for full payment terms. The free endpoint /api?url= is still unauthenticated. Try it (paid): GET /api/cache-poisoning-vulnerability?url=<YOUR_URL> and GET /api/preflight-cors-trace?url=<YOUR_URL> — pay 500 atomic USDC via X-PAYMENT header. x402 #webcache #cachepoisoning #cors #security #webperf #api

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-web-cache-poisoning-probe-deep-cors-preflight-trace-2026-10-14-1gee

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
