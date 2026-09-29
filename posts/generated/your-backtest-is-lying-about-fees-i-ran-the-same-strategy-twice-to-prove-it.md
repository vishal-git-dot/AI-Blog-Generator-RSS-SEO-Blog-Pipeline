---
title: "Your backtest is lying about fees (I ran the same strategy twice to prove it)"
slug: "your-backtest-is-lying-about-fees-i-ran-the-same-strategy-twice-to-prove-it"
author: "HonestFill"
source: "devto_webdev"
published: "Tue, 29 Sep 2026 21:50:45 +0000"
description: "The Experiment I took the exact same strategy — RSI mean-reversion on BTC/USD 4h candles, Jun 28 to Sep 26 2026 (720 bars) — and ran it twice through my back..."
keywords: "fold, backtest, fees, walk, forward, one, run, trades"
generated: "2026-09-29T22:04:59.852202"
---

# Your backtest is lying about fees (I ran the same strategy twice to prove it)

## Overview

The Experiment I took the exact same strategy — RSI mean-reversion on BTC/USD 4h candles, Jun 28 to Sep 26 2026 (720 bars) — and ran it twice through my backtest engine. Run 1: Zero fees (how 90% of backtests get run) Net PnL: +$85.96 Trades: 7 Win rate: 71% Profit factor: 1.33 Run 2: Real Kraken fees (16/26 bps maker/taker) + 5 bps spread + 5 bps slippage Net PnL: -$1,503.48 Trades: 7 Win rate: 14% Profit factor: 0.22 The only difference was honesty. Fees didn't just reduce the profit — they flipped 5 of 7 trades from winners to losers. Cost drag: $1,589.44 across 7 trades (~$227/round-trip). The Second Lie: One-Shot Windows But maybe that window was just unlucky? That's the right instinct — and it's the second lie. One-shot backtests fit the past. So I ran walk-forward validation: 6 rolling folds, each training on the past and testing on unseen future bars. Zero-fee walk-forward (out-of-sample folds only): Fold 1: -$310 Fold 2: -$4 Fold 3: +$30 Fold 4: +$62 Fold 5: -$87 Fold 6: +$207 A coin flip. The 71% win rate edge evaporates the moment it's tested on data it never saw in training. Real-fee walk-forward (same folds): Fold 1: -$344 Fold 2: -$876 Fold 3: -$29 Fold 4: -$563 Fold 5: -$412 Fold 6: +$45 5 of 6 folds negative. The one green fold made $45 before you count your time. The Rules I Now Follow Two lies, one fix: No fees = fictional results. If the backtest ignores the rake, it's marketing, not math. No walk-forward = fit to the past. One green window proves nostalgia, not edge. Every backtest I run now ships fee-adjusted AND walk-forward-tested, or it doesn't count. See the Live Proof I built a backtesting tool that enforces this by default — fees, spread, slippage and walk-forward honesty baked in, itemized per trade. Live sample report (real Kraken data): https://honestfill.vercel.app/report Backtest page (try it yourself): https://honestfill.vercel.app/backtest

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/honestfill/your-backtest-is-lying-about-fees-i-ran-the-same-strategy-twice-to-prove-it-262f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
