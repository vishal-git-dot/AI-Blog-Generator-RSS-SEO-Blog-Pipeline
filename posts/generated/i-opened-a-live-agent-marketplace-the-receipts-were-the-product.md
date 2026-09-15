---
title: "I opened a live agent marketplace. The receipts were the product."
slug: "i-opened-a-live-agent-marketplace-the-receipts-were-the-product"
author: "Alex"
source: "devto_webdev"
published: "Tue, 15 Sep 2026 11:19:16 +0000"
description: "Most “agent economy” posts sell you a framework, a Discord, or a token. I wanted the boring thing: a public catalog where an agent can find a tool, call it, ..."
keywords: "not, you, hub, live, market, one, modelmarket, dev"
generated: "2026-09-15T11:28:03.175343"
---

# I opened a live agent marketplace. The receipts were the product.

## Overview

Most “agent economy” posts sell you a framework, a Discord, or a token. I wanted the boring thing: a public catalog where an agent can find a tool, call it, and keep a receipt — without me standing in the loop. That surface is live. It is called AIMarket Hub . The URL is modelmarket.dev . Crypto stays off this title on purpose. The shape here is discover → invoke → receipt. Counted 2026-09-15 from /ai-market/v2/stats/live : Invokes 710 (704 ok — 99.2%) External / self 700 / 10 Federated hubs 14 Capabilities 177 p50 latency (24h) 90 ms Revenue / hour $0.0010 That last number is the honesty tax. This is not Uniswap. It is a small live market that already meters calls. The screenshots below are the product, not a mock. The terminal. EN UI. MCP remote in the same chrome: https://modelmarket.dev/mcp . The thesis (one sentence) If your agent stack only works inside a demo transcript, you don't have a market — you have a screenshot. A market needs supply, demand, a place they meet, a price, and a way to fail out loud. The Hub is that place. Frameworks are how you talk to it. We already wrote the 15-minute “list your own HTTP tool” walkthrough ( publish-and-earn ) and the two-tool MCP door ( Hub MCP ). This piece is narrower: open the live terminal and read what it is actually doing. The grammar Discover. Type a job in English. Federation returns capability ids, prices, source_hub . Invoke. One POST. Hub 402 / failed call → the UI shows the failure. No canned weather. Receipt. Metered, signed, re-checkable. You do not have to trust the narrator. HTTP 402 is a product feature, not an error page: Channel → Invoke → Receipt → Settle. Settlement exists (USDC on Base, small demo funds). You do not need a wallet to watch the feed or run a free trial. What the feed is actually calling EXT = someone else paid. One weather row at 475 ms is free and red — fail loud, not a painted success. When I loaded the page, the tape was not a synthetic demo reel. It was: capability hub price latency gaia.weather.read@v1 iot.modelmarket.dev $0.001 ~80–97 ms sortes.draw@v1 oracles family $0.006 18 ms murmuration.aggregate@v1 oracles family $0.002 48 ms Weather dominates. That is honest demand, not a balanced pie chart. Sortes is the verifiable-draw capability other live surfaces actually spend. This article is not those products. One failed weather call sits in the same list as the successes. Pretty dashboards that hide the red row are cosplay. The decoder strip above the table is the same grammar: capability_id → route [LOCAL/FED] → traffic [EXT/SELF] → $ → ms → ✓/✗. Type a job. Don't browse a PDF. Match, not autocomplete theatre. Prices and “click to try free” on the same card. I typed fair randomness for a lottery . Back came, among others: sortes.verify@v1 — verify an ECVRF proof offline · $0.00101 · 10 ms platon.beacon@v1 — hash-chained randomness beacon · $0.00404 · 10 ms platon.random@v1 — signed chaos-VRF · $0.00404 · 13 ms Search is a catalogue . It is not a lottery. Read the description before you spend a trial. The Hub already has a free-trial path (a handful of invokes per visitor per hour) so you can feel a receipt before any wallet. Same box accepts other intents the landing already suggests: wildfire brief near a facility , protect a ship from navigation spoofing . Those are live SKUs with their own honesty footnotes. This article does not tour them. How to talk to it (without the monorepo) Three doors. Pick one. Do not install seventeen servers. Door What it is Terminal modelmarket.dev — search, try, watch the feed MCP https://modelmarket.dev/mcp — two tools: market_search , market_invoke CLI pip install aimarket-hub — publish your own capability If you want agents inside LangGraph/CrewAI to see the catalogue as native tools, that is a two-line bridge . If you want to list an endpoint you already have, that is the 15-minute article. This page is the room those posts assume is real. What I am not claiming Not TVL. $0.001/hour is the live meter. Small funds, small market. Not 10,000 agents. 710 invokes, 14 peers, 177 federated capabilities. Counted from JSON, not a pitch deck. Not a token. No airdrop, no points market. 402 is HTTP. Not the factory. AICOM ships pages. The Hub is where tools get used . Mixing both in one post converts nobody — we already made that mistake in our heads, so this article does not. Production listing still has gates (publish token, signed provider responses, supply-security). Start on the public terminal or a local hub. Don't paste a localhost invoke_url at prod and act surprised. Open it modelmarket.dev — type a job, watch one row land in the feed. Stats (the numbers above): stats/live Code: github.com/alexar76/aimarket-hub (MIT) If a market that fails loud and keeps receipts is your kind of boring, a ⭐ on the hub repo helps other people find the example. Concrete issues help more than a polite “cool stack.” Built in the open. The screenshots are the product, not a mock. Numbers from 2026-09-15.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexar76/i-opened-a-live-agent-marketplace-the-receipts-were-the-product-4hl1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
