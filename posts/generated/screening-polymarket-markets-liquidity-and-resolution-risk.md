---
title: "Screening Polymarket Markets: Liquidity and Resolution Risk"
slug: "screening-polymarket-markets-liquidity-and-resolution-risk"
author: "Blockchain Rust Engineer"
source: "devto_python"
published: "Tue, 21 Jul 2026 13:30:36 +0000"
description: "Most of what I've written about building a Polymarket bot so far assumes you're already trading a specific market - execution timing, position sizing. Neithe..."
keywords: "market, resolution, your, you, markets, execution, position, sizing"
generated: "2026-07-21T14:05:44.042034"
---

# Screening Polymarket Markets: Liquidity and Resolution Risk

## Overview

Most of what I've written about building a Polymarket bot so far assumes you're already trading a specific market - execution timing, position sizing. Neither of those matters if you're trading the wrong markets to begin with. Before any of that logic runs, you need a filter that decides which markets are even worth putting a bot in front of. Why market selection matters more than it looks Polymarket lists hundreds of markets at any given time, and the majority of them aren't worth trading algorithmically. Some have almost no depth. Some are structurally ambiguous and carry real resolution risk. Running your edge calculation and execution logic against a market that fails on either of these fronts isn't a minor inefficiency - it's where a lot of "my bot has a working model but still loses money" complaints actually originate. Filter one: liquidity depth The execution and sizing logic I've covered in previous posts assumes there's enough resting liquidity near the market price to fill your intended position without excessive slippage. That assumption fails silently on thin markets. def is_liquid_enough ( orderbook , intended_position_size , min_depth_ratio = 3.0 ): """ Checks whether top-of-book depth supports the intended position without excessive price impact. """ top_of_book_depth = sum ( level [ ' size ' ] for level in orderbook [ ' bids ' ][: 3 ]) return top_of_book_depth >= ( intended_position_size * min_depth_ratio ) This ties directly back to the staleness problem from execution: if depth is under roughly 3x your intended position, you're not just risking a stale fill - you shouldn't be sizing a full position into that market in the first place, regardless of how good your edge calculation looks. Filter two: resolution risk This one is specific to prediction markets and doesn't have a clean equivalent in traditional trading. Every Polymarket market resolves based on a defined resolution source and criteria - and not all of them are equally unambiguous. Markets with vague resolution criteria (subjective wording, dependent on a source that could plausibly be interpreted multiple ways) carry a real risk that has nothing to do with your probability model: the market could resolve in a way that doesn't match the "obvious" outcome, or get disputed and delayed. A perfectly calculated edge is worthless if the resolution itself is contested. Practical screening questions worth encoding into your filter : Does the resolution source come from a single, unambiguous, verifiable feed, or does it depend on subjective judgment? Has this market (or its category) had prior resolution disputes on Polymarket's UMA oracle? Is the resolution date clearly defined, or is there room for the window itself to be ambiguous? def resolution_risk_score ( market_metadata ): """ Simple scoring heuristic - lower is safer. Replace with your own calibrated weights based on historical dispute data. """ score = 0 if market_metadata . get ( ' has_prior_disputes ' ): score += 3 if market_metadata . get ( ' resolution_source_type ' ) == ' subjective ' : score += 2 if not market_metadata . get ( ' clear_resolution_date ' ): score += 1 return score Putting the filter together The combined screen isn't complicated - it's just a step most bot builders skip because it's less interesting than the pricing model: def should_trade_market ( market , orderbook , intended_size ): if not is_liquid_enough ( orderbook , intended_size ): return False if resolution_risk_score ( market [ ' metadata ' ]) > RISK_THRESHOLD : return False return True Run this before your edge calculation even fires, not after. There's no point spending compute or API calls pricing a market your risk logic would reject anyway. The pattern connecting all three pieces Execution timing, position sizing, and market selection are really the same underlying discipline applied at three different stages: don't trust a snapshot that might not reflect reality by the time you act on it. Execution timing is about book staleness. Sizing is about model confidence. Market selection is about whether the market itself is even a fair, tradeable proposition before you engage either of the other two systems. I build this kind of infrastructure - execution logic, sizing, and market screening - for prediction market bots, along with provably fair systems for casino platforms. If you're working through similar filtering logic, happy to compare notes.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/casatrick/screening-polymarket-markets-liquidity-and-resolution-risk-ak3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
