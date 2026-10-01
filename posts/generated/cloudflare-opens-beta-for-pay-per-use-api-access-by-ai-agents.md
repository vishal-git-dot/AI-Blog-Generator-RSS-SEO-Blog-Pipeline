---
title: "Cloudflare Opens Beta for Pay-Per-Use API Access by AI Agents"
slug: "cloudflare-opens-beta-for-pay-per-use-api-access-by-ai-agents"
author: "Mikhail Savchenko"
source: "devto_ai"
published: "Thu, 01 Oct 2026 05:00:03 +0000"
description: "Cloudflare opened a closed beta for its Monetization Gateway, a system that lets domain owners charge AI agents for access to websites, APIs, MCP tools or da..."
keywords: "agents, payment, cloudflare, per, api, pay, access, pricing"
generated: "2026-10-01T05:13:42.623237"
---

# Cloudflare Opens Beta for Pay-Per-Use API Access by AI Agents

## Overview

Cloudflare opened a closed beta for its Monetization Gateway, a system that lets domain owners charge AI agents for access to websites, APIs, MCP tools or datasets on a per-use basis. The mechanism relies on the HTTP 402 "Payment Required" status code: sellers define pricing rules matching a request's URL, headers or query parameters, and buyers receive payment instructions, sign an authorization, and get the resource once payment settles through Coinbase's x402 Facilitator. Payments settle in USDC on the Base blockchain. Four customers are already running it in production. Cloudflare's own AI Gateway now accepts the header Payment-Method: x402 so U.S.-based customers can pay for inference at request time instead of maintaining a prepaid credit balance. Ceramic.ai, a web search API built for agents with an index of more than 40 billion pages, uses fixed pricing so agents can pay per search without an API key. Stocktwits built a separate agent-facing path to sell stock sentiment, message-volume, follower and trending signals per request, while keeping its existing data licenses unchanged. API2PDF, a PDF-generation API, now returns an HTTP 402 response to unauthenticated requests and uses variable pricing tied to the compute and bandwidth each job actually consumes. Access is currently limited to eligible U.S.-based sellers and buyers, with Cloudflare saying support for other geographies is planned. Future additions mentioned include discoverability tooling for agents, transaction logs, support for more payment rails, and identity primitives.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mikefluff/cloudflare-opens-beta-for-pay-per-use-api-access-by-ai-agents-2o30

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
