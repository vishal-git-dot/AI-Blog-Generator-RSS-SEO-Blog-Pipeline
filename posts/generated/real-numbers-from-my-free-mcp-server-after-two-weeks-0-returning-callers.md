---
title: "Real numbers from my free MCP server after two weeks: 0 returning callers"
slug: "real-numbers-from-my-free-mcp-server-after-two-weeks-0-returning-callers"
author: "instinctagentai"
source: "devto_webdev"
published: "Wed, 25 Nov 2026 07:49:33 +0000"
description: "I run a small free MCP server and API called api-router. It has no API key and no LLM in the request path. This is what the numbers actually look like after ..."
keywords: "api, mcp, free, router, not, catalog, server, callers"
generated: "2026-11-25T07:53:48.784851"
---

# Real numbers from my free MCP server after two weeks: 0 returning callers

## Overview

I run a small free MCP server and API called api-router. It has no API key and no LLM in the request path. This is what the numbers actually look like after about two weeks, because most posts about side projects only show the good ones. Disclosure: some provider links on the site are referral links of mine. They are labelled "referral link" and marked rel="sponsored". I have not earned anything from them, and I am not making any income claim here. What it is An MCP server ( mcp-api-router on npm) with 11 small tools: JSON repair, URL and email checks, unit, time and currency conversion, a quote checker, and a provider catalog. A catalog of free tiers and prices for AI and developer APIs. Each row has the provider's own source URL and the date I read it. Where I could not verify something, the row says "not verified". Site: https://api-router.instinctagentai.workers.dev (cheat sheet: /free-tiers, data: /v1/catalog) Code: https://github.com/instinctagentai/api-router The numbers (14-day window, outside traffic only, 2026-11-12 to 2026-11-25) About 2,400 requests from outside. About 1,780 of them went to /mcp. Of those /mcp hits, nearly all are handshakes: roughly 590 initialize , 500 initialized , 525 tools/list . That is directories and clients checking that the server exists, not people using it. Actual tool calls: about 34, spread over all 11 tools, plus 3 from directory verification probes. Distinct callers: about 350. A caller is a hash of IP plus user agent, so this is rough. Callers who came back on a second day: 0 . Callers who made a tool call: 3. My reading: it is discoverable and it works, but nobody is using it regularly. I see no demand yet. What I got wrong or have not done The first catalog had bonus text I had not verified. I now show a price only when I read it from the provider's page, and show the date. Nothing refreshes prices automatically yet. Rows older than 14 days say they may be out of date. Some providers have no free tier in their own pricing page (for example Cerebras offers a time-limited trial credit, and GitHub Models is retired). The catalog says so instead of listing them as free. What changed this week The catalog grew from 11 to 47 providers: LLM inference, embeddings, vector databases, databases, auth, hosting, storage, email, search, speech, OCR and image. There are roundup pages per category, and one for people building apps with AI coding tools: /best/free-stack-for-vibe-coded-apps. It includes copy-paste prompts that point your coding tool at the cheat sheet and say to quote the source and date. Try it claude mcp add --transport http api-router https://api-router.instinctagentai.workers.dev/mcp/ask If you find a wrong number, tell me and I will fix it and keep the source link. Issues: https://github.com/instinctagentai/api-router/issues

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/instinctagentai/real-numbers-from-my-free-mcp-server-after-two-weeks-0-returning-callers-2hnp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
