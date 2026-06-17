---
title: "How I built my Delta-Neutral Arbitrage Bot on Hyperliquid (Python)"
slug: "how-i-built-my-delta-neutral-arbitrage-bot-on-hyperliquid-python"
author: "Tir3d_23"
source: "devto_python"
published: "Wed, 17 Jun 2026 20:06:37 +0000"
description: "Crypto is fun, but gambling on price direction isn't really my thing. I wanted to build something more reliable: Funding Rate arbitrage . Right now, Hyperliq..."
keywords: "you, api, hyperliquid, python, but, funding, spot, market"
generated: "2026-06-17T20:21:04.201069"
---

# How I built my Delta-Neutral Arbitrage Bot on Hyperliquid (Python)

## Overview

Crypto is fun, but gambling on price direction isn't really my thing. I wanted to build something more reliable: Funding Rate arbitrage . Right now, Hyperliquid is a great playground for this: zero fees on the Spot market and deep liquidity on Perpetuals. The plan was simple: write a Python bot to automate a carry trade strategy. But diving into their API and SDK was... a bit of a ride. The Strategy: Delta-Neutral Carry Trade The concept is straightforward. When the market is bullish, Long traders pay a "Funding Rate" to Short traders on perpetual contracts. The algorithm detects this yield: it shorts the Perp to collect the funding, and simultaneously buys the exact same amount of the Spot asset to hedge. Result: Delta = 0. You don't care if the market pumps 20% or dumps 20%, your exposure is flat and you just collect the hourly fee passively. The API Struggle Wiring this up properly actually took some work. I ran into a few annoying roadblocks: The "U" token trap: In the Hyperliquid ecosystem, Bitcoin is called BTC on the Perp market, but UBTC on Spot. The official SDK doesn't natively map matching pairs. I had to build a dynamic resolver to auto-map the 280+ assets without hardcoding tickers. Async everywhere: On a decentralized orderbook, speed is everything. If you send synchronous API requests, slippage will eat your edge before the hedge even fills. I had to wrap the core execution in asyncio to fire both legs of the trade at the exact same time. The execution loop: Knowing when to enter is easy, but exiting when the funding drops, scaling capital dynamically, and handling the overall state requires a robust backend loop. The Result Fast forward a few dozen hours, and I finally packaged a clean, working framework. The bot runs in the background, scans the overlap between Spot and Perp markets, handles the risk math, and runs a local aiohttp web dashboard so I can monitor my PnL directly in the browser. If you're a developer or a Python tinkerer looking to build on Hyperliquid, I decided to share my full source code. It’ll save you from spending a week fighting the API quirks and writing boilerplate. It's not a SaaS or a black box. Just clean, object-oriented Python code, with a built-in DRY_RUN mode to test strategies on live data without risking real money. Grab it, tweak it, do whatever you want with it. 👉 Get the full source code here Disclaimer: This code is for educational purposes. Always test in DRY_RUN first, protect your API wallets, and remember this is sold "as-is" with no tech support.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tir3d_377c8049d/how-i-built-my-delta-neutral-arbitrage-bot-on-hyperliquid-python-jh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
