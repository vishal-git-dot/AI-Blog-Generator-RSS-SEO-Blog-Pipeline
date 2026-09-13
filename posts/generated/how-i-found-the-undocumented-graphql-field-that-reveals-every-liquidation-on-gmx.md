---
title: "How I Found the Undocumented GraphQL Field That Reveals Every Liquidation on GMX"
slug: "how-i-found-the-undocumented-graphql-field-that-reveals-every-liquidation-on-gmx"
author: "Jalvart Studio"
source: "devto_python"
published: "Sun, 13 Sep 2026 11:18:27 +0000"
description: "GMX (the perpetuals exchange on Arbitrum) has an official public subgraph. It's free, needs no API key, and nobody seems to document how to actually pull liq..."
keywords: "gmx, liquidation, same, every, liquidations, ordertype, both, api"
generated: "2026-09-13T11:28:47.304867"
---

# How I Found the Undocumented GraphQL Field That Reveals Every Liquidation on GMX

## Overview

GMX (the perpetuals exchange on Arbitrum) has an official public subgraph. It's free, needs no API key, and nobody seems to document how to actually pull liquidations out of it. Here's the exact path I took, including the two mistakes that cost me a duplicate-alert bug in production. The endpoint https://gmx.squids.live/gmx-synthetics-arbitrum:prod/api/graphql This is Subsquid infrastructure maintained by the GMX team itself (confirmed against their own SDK source, which points to the same URL). No auth header needed for reads. There's no liquidations field First instinct: introspect the schema and look for something called liquidations . There isn't one. GMX V2 doesn't model liquidations as a first-class entity — they're a tradeActions row with a specific orderType . { __type ( name : "TradeAction" ) { fields { name } } } Two fields matter here: orderType and liquidationFeeAmount . Confirming orderType 7 = Liquidation I didn't want to guess, so I cross-checked two ways: Empirically — filtering liquidationFeeAmount_gt: "0" returned rows, and every single one had orderType: 7 . Against source — GMX's own contracts define the enum: MarketSwap=0, LimitSwap=1, MarketIncrease=2, LimitIncrease=3, MarketDecrease=4, LimitDecrease=5, StopLossDecrease=6, Liquidation=7 . Both agreed. That's the confirmation bar I hold myself to before shipping anything that alerts real people about real money. The bug: every liquidation fired twice First working version filtered only on orderType_eq: 7 . It alerted the same liquidation twice — same transactionHash , same size, back to back. Turns out tradeActions logs both OrderCreated and OrderExecuted as separate rows for the same order, and both can carry orderType: 7 . The fix is one extra filter: { tradeActions ( where : { orderType_eq : 7 , eventName_eq : "OrderExecuted" , timestamp_gt : $since } orderBy : timestamp_ASC limit : 50 ) { account marketAddress sizeDeltaUsd isLong timestamp transactionHash } } Plus a transactionHash dedup set as a safety net, in case some other event pattern I haven't seen yet does the same thing. sizeDeltaUsd isn't in dollars It's scaled by 1e30 — standard GMX V2 precision for USD amounts. Verified by dividing five known liquidations and checking the results looked like real retail position sizes ($284–$29,805), not by trusting a blog post. from decimal import Decimal size_usd = Decimal ( raw_size_delta_usd ) / Decimal ( 10 ** 30 ) marketAddress isn't a symbol It's a contract address. To get "ETH" or "SOL" out of it, you need two hops: Subgraph: markets(id, indexToken) — maps the market to its index token address. GMX's official REST API: https://arbitrum-api.gmxinfra.io/tokens — maps token address to symbol. Both are free, both are official GMX infrastructure. Build this map once at startup, not on every poll. What it's for I used this to build a small Discord alert bot — polls every 30s, filters by a configurable USD threshold, posts an embed with asset, direction, size, and an Arbiscan link when something meaningful gets liquidated. Runs as a systemd service, nothing fancy. If you're building something similar and want the ready-made version instead of wiring this up yourself, I packaged it as a hosted Discord alert service: GMX Liquidation Alerts ($19/mo, 3-day free trial). Full source of the reasoning above — verified against GMX's own contracts and docs, not assumed — because an alert bot that's wrong about money is worse than no bot at all.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jalvart_studio_1b20374378/how-i-found-the-undocumented-graphql-field-that-reveals-every-liquidation-on-gmx-222f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
