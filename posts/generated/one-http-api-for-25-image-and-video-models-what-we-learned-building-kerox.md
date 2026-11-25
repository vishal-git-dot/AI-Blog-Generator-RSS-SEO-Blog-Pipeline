---
title: "One HTTP API for 25 image and video models: what we learned building Kerox"
slug: "one-http-api-for-25-image-and-video-models-what-we-learned-building-kerox"
author: "Jackson"
source: "devto_ai"
published: "Wed, 25 Nov 2026 07:51:19 +0000"
description: "Most teams that add image or video generation end up wiring three or four vendor SDKs: one for ByteDance Seedance, one for Seedream, one for Wan, one for Kli..."
keywords: "one, you, own, model, not, its, task, api"
generated: "2026-11-25T07:53:48.786969"
---

# One HTTP API for 25 image and video models: what we learned building Kerox

## Overview

Most teams that add image or video generation end up wiring three or four vendor SDKs: one for ByteDance Seedance, one for Seedream, one for Wan, one for Kling. Each has its own auth, its own polling model, its own error shape and its own price page that changes without notice. We built Kerox to flatten that into one call, and here is what the API surface looks like today. One endpoint, then poll or get a webhook curl -X POST https://kerox.ai/v1/tasks \ -H "Authorization: Bearer $KEROX_KEY" \ -H "Content-Type: application/json" \ -d '{"model":"seedream-5.5","input":{"prompt":"a paper boat on a rainy street"}}' You get a task id back. Then either poll GET /v1/tasks/{id} or pass a callback URL and receive a signed webhook when the generation finishes. Outputs are hosted on a CDN for seven days, so you do not need your own bucket on day one. Billing follows the task, not the request The part we cared most about: you are charged per successful generation, and the price for each model is shown before you generate. A failed or timed-out task is refunded in full. Estimated cost is held when you submit and settled when the task completes, on a prepaid USD balance that starts at $5 and does not expire. No subscription tier to outgrow. Built for agents as well as people A growing share of our traffic is not a human reading docs but an agent looking for a tool. So the same catalog is exposed as llms.txt , a markdown docs bundle, an OpenAPI spec and an MCP server, and there is a browser Studio that runs the same models on the same balance for people who do not want to write code at all. If you are picking a model for a product, the useful question is rarely "which vendor is best" but "which one is cheapest for this specific prompt at this resolution". A single API with a public price table per model makes that comparison a lookup instead of a spreadsheet.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jackson_def719af7dc64ef1f/one-http-api-for-25-image-and-video-models-what-we-learned-building-kerox-3bd4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
