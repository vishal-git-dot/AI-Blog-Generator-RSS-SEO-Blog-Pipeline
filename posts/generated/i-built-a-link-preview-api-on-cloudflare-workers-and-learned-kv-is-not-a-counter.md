---
title: "I built a link preview API on Cloudflare Workers — and learned KV is not a counter"
slug: "i-built-a-link-preview-api-on-cloudflare-workers-and-learned-kv-is-not-a-counter"
author: "Davis"
source: "devto_webdev"
published: "Wed, 10 Jun 2026 15:34:50 +0000"
description: "I shipped a link preview API in a day on Cloudflare Workers — and the most interesting bug had nothing to do with HTML parsing. What I built LinkPeek does on..."
keywords: "linkpeek, https, workers, github, link, counter, url, com"
generated: "2026-06-10T15:51:30.360549"
---

# I built a link preview API on Cloudflare Workers — and learned KV is not a counter

## Overview

I shipped a link preview API in a day on Cloudflare Workers — and the most interesting bug had nothing to do with HTML parsing. What I built LinkPeek does one thing: give it a URL, get back clean JSON with everything you need to render a link card — title, description, images, favicon, site name, canonical URL, RSS/Atom feeds, oEmbed endpoint, and the full OpenGraph + Twitter Card maps. curl "https://linkpeek.dpears.workers.dev/v1/preview?url=https://github.com" { "title" : "GitHub · Change is constant. GitHub keeps you ahead." , "siteName" : "GitHub" , "image" : "https://images.ctfassets.net/.../GH-Homepage-Universe-img.png" , "favicon" : "https://github.com/fluidicon.png" , "og" : { "site_name" : "GitHub" , "..." : "..." }, "twitter" : { "card" : "summary_large_image" , "..." : "..." } } There's also a tiny zero-dep client on npm: linkpeek-client . Why Workers is a great fit for this HTMLRewriter is the killer feature. Parsing arbitrary HTML on an edge function sounds expensive, but HTMLRewriter is a streaming parser — you register element handlers and it processes the response body as it flows through: const rewriter = new HTMLRewriter () . on ( " meta " , metaHandler ) . on ( " title " , { text ( t ) { titleText += t . text ; } }) . on ( " link " , feedAndFaviconHandler ); I cap parsing at 1MB and cancel the stream after that — a page's metadata lives in <head> , so there's no reason to chew through a 20MB page. KV as a response cache works great. 24h TTL, keyed by URL. Repeat lookups return in ~30ms globally. The bug worth writing about: KV is not a counter For the free tier I wanted a simple per-IP daily quota. First implementation: read a counter from KV, increment, write it back. It enforced nothing . I fired 27 sequential requests at it during verification and every one returned 200. KV is eventually consistent — reads can be served from a stale edge cache for up to 60 seconds. A burst of requests all read the same stale "0", increment to "1", and last-write-wins. Your counter crawls while traffic flies. The fix: Workers has a purpose-built Rate Limiting binding that does accurate per-colo counting: [[unsafe.bindings]] name = "ANON_LIMITER" type = "ratelimit" namespace_id = "1001" simple = { limit = 10 , period = 60 } const { success } = await env . ANON_LIMITER . limit ({ key : clientIP }); if ( ! success ) return json ({ error : " Rate limit exceeded… " }, 429 ); After the fix, a parallel burst of 16 requests: 5×200, 11×429. I kept the KV daily counter as a slow backstop — it does converge, just not fast enough to stop bursts on its own. Lesson: use KV for caching, use the rate-limit binding (or Durable Objects) for counting. Other things that mattered SSRF guard : reject localhost , RFC-1918 ranges, .local / .internal hosts before fetching. An URL-fetching API is an SSRF machine if you skip this. Honest status reporting : sites behind aggressive bot protection (e.g. Stack Overflow) return their challenge page. LinkPeek reports the target's real status instead of pretending. Non-HTML targets : a HEAD-ish fallback returns type: "file" with content type for images/PDFs instead of erroring. Try it Live demo + docs: https://linkpeek.dpears.workers.dev (25 req/day anonymous) Marketplace (500 req/mo free plan): https://rapidapi.com/davispearson93/api/linkpeek-link-preview-and-opengraph-metadata npm client: https://www.npmjs.com/package/linkpeek-client Source: https://github.com/daviscodesbugs/linkpeek Happy to answer questions about HTMLRewriter, the rate-limit binding, or Workers KV quirks in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/daviscodesbugs/i-built-a-link-preview-api-on-cloudflare-workers-and-learned-kv-is-not-a-counter-3d78

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
