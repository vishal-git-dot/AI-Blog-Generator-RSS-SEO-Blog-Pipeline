---
title: "Most AI-crawler blocking doesn't happen in robots.txt"
slug: "most-ai-crawler-blocking-doesnt-happen-in-robotstxt"
author: "DEUS Automations"
source: "devto_webdev"
published: "Sat, 19 Sep 2026 20:19:52 +0000"
description: "Most AI-crawler blocking doesn't happen in robots.txt Numbers re-derived from the live Agent Web Index aggregate on 2026-09-19 (47,314 domains with a measure..."
keywords: "crawler, robots, txt, domains, agent, edge, one, domain"
generated: "2026-09-19T20:21:54.587978"
---

# Most AI-crawler blocking doesn't happen in robots.txt

## Overview

Most AI-crawler blocking doesn't happen in robots.txt Numbers re-derived from the live Agent Web Index aggregate on 2026-09-19 (47,314 domains with a measured verdict). Dataset CC BY 4.0: Zenodo DOI, GitHub DeusAcc/agent-web-index, Hugging Face DeusHorizon/agent-web-index. Live hub: https://shop.lumnika.com/ai-readiness/?src=devto Everyone audits robots.txt . We probed 47,314 domains the way an AI assistant actually fetches them — one request from a browser user-agent, then one from each published crawler user-agent — and compared what robots.txt permits with what the server really returns. 22.5% of measured domains block at least one major AI crawler. Most of those blocks are not in robots.txt . Crawler Served Blocked in robots.txt Blocked by the edge anyway Edge : robots ClaudeBot 39,946 2,077 6,571 3.2 : 1 GPTBot 40,150 2,595 6,250 2.4 : 1 PerplexityBot 42,518 1,233 4,391 3.6 : 1 OAI-SearchBot 42,507 826 4,513 5.5 : 1 "Blocked by the edge" means one thing only, and it is measured, not inferred: robots.txt allows the bot, a browser user-agent gets the page, and the crawler user-agent gets a different answer — a 403, a challenge, or a block page. Nobody wrote that rule for ClaudeBot. It came with a CDN setting. It depends on who answers for your domain Grouping by the edge vendor that serves the host, over crawler×domain pairs: Edge Domains Crawler pairs blocked Akamai 266 43.0% Google (Cloud/Frontend) 722 38.1% Sucuri 52 18.7% AWS CloudFront 2,903 16.4% Cloudflare 25,404 12.6% No identifiable edge 11,335 11.0% Azure Front Door 283 8.7% A site behind Akamai is roughly three and a half times more likely to refuse an AI crawler than a site behind Cloudflare — while both owners believe their robots.txt is the policy. Mean readability score across measured domains: 73.1 (median 74). Check yours Every domain has a page with its own evidence: https://shop.lumnika.com/ai-readiness/<domain>?src=devto . The same data is a public MCP server, no key, if you would rather have your assistant ask: POST https://shop.lumnika.com/ai-readiness/mcp {"jsonrpc":"2.0","id":1,"method":"tools/call", "params":{"name":"domain_readiness","arguments":{"host":"example.com"}}} Limits, stated by us first Single vantage point, one probe per crawler per domain, one point in time — a challenge page can be transient and we count it as a block. Percentages cover only domains that answered at all; unreachable domains are excluded, not counted as open. google-extended and applebot-extended are robots-only signals with no fetch to compare, so they carry no edge figure. Vendor rows with few domains (Sucuri, Akamai) have wide error bars — the direction is solid, the second decimal is not.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/deusautomations/most-ai-crawler-blocking-doesnt-happen-in-robotstxt-3gae

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
