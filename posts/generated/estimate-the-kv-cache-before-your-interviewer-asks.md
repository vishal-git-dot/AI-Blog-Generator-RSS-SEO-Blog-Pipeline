---
title: "Estimate the KV cache before your interviewer asks"
slug: "estimate-the-kv-cache-before-your-interviewer-asks"
author: "Valenx"
source: "devto_ai"
published: "Fri, 27 Nov 2026 20:53:55 +0000"
description: "Most AI engineer loops now include some version of "How much memory does the KV cache need?" Candidates who only define it get a polite nod. Candidates who e..."
keywords: "token, cache, one, per, layers, heads, estimate, bytes"
generated: "2026-11-27T20:56:45.961716"
---

# Estimate the KV cache before your interviewer asks

## Overview

Most AI engineer loops now include some version of "How much memory does the KV cache need?" Candidates who only define it get a polite nod. Candidates who estimate it get the next question. What it is (one sentence): the KV cache stores the attention keys and values of every token already processed, so each new token does not recompute the whole prefix. The estimate, said out loud Per token = 2 (K and V) × layers × KV heads × head dim × bytes. For a model with 32 layers, 8 KV heads, head dim 128, 16-bit values: 2 × 32 × 8 × 128 × 2 = 131,072 bytes = 128 KiB per token. One 8k-token request: 8,192 × 128 KiB ≈ 1 GiB. Ten concurrent requests ≈ 10 GiB on top of the weights. layers , kv_heads , head_dim , bytes_per = 32 , 8 , 128 , 2 per_token = 2 * layers * kv_heads * head_dim * bytes_per # 131072 bytes = 128 KiB per_8k = per_token * 8192 / 2 ** 30 # ~1.0 GiB per request print ( per_token , round ( per_8k , 2 ) ) The follow-up they are waiting for Why only 8 KV heads? Grouped-query attention shares K/V across query heads and shrinks the cache. Prefill vs decode: prefill processes the prompt in parallel and sets time to first token (compute bound). Decode makes one token per step and is limited by memory bandwidth. How do you serve more users? Paged KV cache, quantized KV, shorter contexts, prefix caching. 90-second drill: cover this page, say the formula, plug in the numbers, then name one way to cut the cache. Score yourself 1 to 5. 29 more questions in this format (what's tested, 4-step frame, follow-up): free Top 30 PDF → https://valenx.org/go/free-aie30?utm_source=devto&utm_medium=article&utm_campaign=dp1127&utm_content=D01 Valenx Press. Practice material. No company affiliation, no interview promise.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/valenx/estimate-the-kv-cache-before-your-interviewer-asks-5fc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
