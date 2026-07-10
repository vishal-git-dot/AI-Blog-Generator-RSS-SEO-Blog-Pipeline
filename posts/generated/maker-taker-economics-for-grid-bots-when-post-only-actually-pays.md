---
title: "Maker-taker economics for grid bots: when post-only actually pays"
slug: "maker-taker-economics-for-grid-bots-when-post-only-actually-pays"
author: "Jack Chen"
source: "devto_python"
published: "Fri, 10 Jul 2026 03:36:14 +0000"
description: "Grid bots don't win by predicting direction — they win on fee bps. Every rung you fill is one leg of a round trip, and a grid that trades 400 times a day tur..."
keywords: "bps, maker, only, taker, post, fee, grid, fills"
generated: "2026-07-10T03:51:00.819450"
---

# Maker-taker economics for grid bots: when post-only actually pays

## Overview

Grid bots don't win by predicting direction — they win on fee bps. Every rung you fill is one leg of a round trip, and a grid that trades 400 times a day turns a 1 bps fee gap into real money. The question isn't "maker or taker" in the abstract; it's whether forcing post-only actually earns its keep once you count the fills you miss by insisting on being a maker. Here's the trade-off in one line: post-only guarantees the maker rate but rejects any order that would cross the book, so in fast markets some rungs never fill and you lose that grid step. A taker order fills every time but pays the higher rate. The break-even is easy to model. Let: m = maker fee (bps) t = taker fee (bps) p = probability a post-only rung actually fills before price walks away g = grid step captured per successful round trip (bps) A post-only rung's expected value per attempt is p * (g - 2m) . A taker rung's is g - 2t (it always fills). Post-only wins when: def post_only_wins ( g , m , t , p ): ev_maker = p * ( g - 2 * m ) # fills with prob p, pays maker both legs ev_taker = ( g - 2 * t ) # always fills, pays taker both legs return ev_maker > ev_taker # 5 bps grid step, maker 2 bps, taker 5 bps for p in ( 0.6 , 0.72 , 0.9 , 1.0 ): print ( p , post_only_wins ( 5 , 2 , 5 , p )) # 0.60 False # 0.72 True (right at the edge) # 0.90 True # 1.00 True With a 5 bps step and a 2/5 maker-taker split, post-only stops paying off once your fill probability drops below ~0.72. On a tight, liquid pair where post-only fills 90%+ of the time, maker-only is clearly correct. On a thin pair during a move, where half your post-only rungs get rejected, you're better off just taking. Net cost per round trip (both legs) at a few fee tiers: maker/taker (bps) maker round trip taker round trip crossover fill-prob (g=5) 2 / 5 4 bps 10 bps 0.72 1 / 4 2 bps 8 bps 0.60 0 / 5 0 bps 10 bps 0.50 The practical takeaway: measure your actual post-only fill rate per pair — most bot frameworks log rejected orders, so count them — plug it in, and stop assuming maker-only is free. It isn't; the hidden cost is the fills you never got. I keep the raw per-exchange fee tiers I use for this in a public dataset: https://github.com/jack0752168/crypto-exchange-fee-data A longer write-up on grid fee optimization with worked examples is here: https://www.jacktrader.xyz/en/blog/grid-bot-fee-optimization.html Not financial advice — just the arithmetic. Your fill rates and fee tiers are yours to measure.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jacktrader/maker-taker-economics-for-grid-bots-when-post-only-actually-pays-4ihm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
