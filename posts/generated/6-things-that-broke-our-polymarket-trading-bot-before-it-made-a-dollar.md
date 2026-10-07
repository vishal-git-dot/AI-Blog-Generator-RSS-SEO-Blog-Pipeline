---
title: "6 things that broke our Polymarket trading bot before it made a dollar"
slug: "6-things-that-broke-our-polymarket-trading-bot-before-it-made-a-dollar"
author: "ekocam"
source: "devto_python"
published: "Wed, 07 Oct 2026 12:39:33 +0000"
description: "We spent a few weeks trying to build a profitable Polymarket bot. Arbitrage between linked markets, in-play market making, copying wallets that trade before ..."
keywords: "polymarket, you, bot, before, order, your, can, price"
generated: "2026-10-07T13:01:31.111299"
---

# 6 things that broke our Polymarket trading bot before it made a dollar

## Overview

We spent a few weeks trying to build a profitable Polymarket bot. Arbitrage between linked markets, in-play market making, copying wallets that trade before goals, betting against miscalibrated prices. We recorded the full order book for every football market, indexed on-chain trades and replayed each idea. None of them made money. The full research with numbers is on our blog , and the CSVs are on GitHub . This post is the engineering side: six things about the Polymarket API and our own pipeline that would have broken the bot even if a strategy had worked. 1. Your taker order waits a second, and you can't cancel it Sports markets have a field in the Gamma API called secondsDelay . Football is 1 , NBA is 0 . You can see it on any event: GET https://gamma-api.polymarket.com/events?slug=fif-sri-mri-2026-10-05 ... "secondsDelay": 1 ... Per the Order Lifecycle docs , a marketable order waits out that delay before matching, and "during either delay, the order is pending and cannot be canceled". Resting limit orders can still be cancelled. Some crypto and finance up/down markets have a 250 ms version of the same thing. What it did to us: our arbitrage detector found 369 mispriced sets across linked football markets in 18 hours. Of the 2c+ ones we rechecked one second later, all legs were still in the book in 3, worth $1.83 total. Makers pull their quotes inside your delay, or a faster taker takes the legs. If your bot sees a price and hits it, check secondsDelay first. 2. Fees are not a percentage Only takers pay, and the fee depends on price: def taker_fee ( shares : float , price : float , fee_rate : float ) -> float : # fee_rate from Gamma feeSchedule.rate, e.g. 0.05 for sports return shares * fee_rate * price * ( 1 - price ) It peaks at 0.50 ( p * (1 - p) = 0.25 ) and goes to zero near 0 and 1. A 1c edge on a 50c contract is mostly eaten. Rates and maker rebates are in the fees docs . 3. The mempool gives you nothing Orders and cancels are off-chain (EIP-712 signatures), only the settlement goes to Polygon. We measured: Source Lag behind matching Order book WebSocket ~17 ms On-chain settlement ~2 s median By the time a trade shows up in the Polygon mempool, it already happened and the book already moved. Watch the WebSocket, not the chain. 4. WebSocket events arrive out of order The exchange can send price_change (a level got eaten) before the last_trade_price event of the same trade. We replayed fills in arrival order at first, and every fill looked about 25% worse than it really was. Sort by the trade, not by arrival time, before you trust any replay. For what it's worth, a plain WebSocket recorder ( price_change , book , last_trade_price with tx hash) captured 99.9% of the trades that later appeared on-chain, so you don't need anything fancier to build a replay dataset. 5. Your backtest can lie with perfect data This one wasn't the API, it was us. We picked wallets that bought right before goals and simulated copying them 1-5 seconds later: +$4.23 per $10. Then we noticed we had only selected the buys that came right before goals. In real time you don't know which buys those are. Rerun on every buy by the same wallets, without looking at the outcome: -$0.41 per $10. Any filter that uses something you only learn later (a goal, a resolution, a price move) has to be removed from the selection step. If the result survives that, then you can start believing it. 6. Some "Polymarket bot" repos want your private key Before you reach for an existing open-source bot: StepSecurity found 20+ fake repos with bought stars ( polymarket-trading-bot-new , polymarket-copy-trading-bot-sports , ...) pulling typosquatted npm packages that steal keys and .env files. SafeDep found 9 npm packages ( polymarket-bot , polymarket-claude-code , ...) that ask you to paste your wallet key. Read the code and the dependency tree before anything touches a funded key. Smaller Gamma API notes offset pagination returns 422 somewhere after 2,100-2,500 records. Use the keyset endpoints for a full crawl. /events/keyset ignores the negRisk filter, filter on the market field instead. /markets/keyset respects end_date_min / end_date_max . Some requests fail without a User-Agent header. The data is CC BY 4.0. If you're building something on Polymarket and want to check our numbers, the repo has every CSV, and we'd like to hear where we got it wrong. Originally published on orcalayer.com . OrcaLayer is an independent Polymarket analytics provider, not affiliated with Polymarket.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ekocam/6-things-that-broke-our-polymarket-trading-bot-before-it-made-a-dollar-4efi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
