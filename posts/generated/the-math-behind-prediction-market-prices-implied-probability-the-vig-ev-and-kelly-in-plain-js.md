---
title: "The Math Behind Prediction Market Prices: Implied Probability, the Vig, EV and Kelly (in plain JS)"
slug: "the-math-behind-prediction-market-prices-implied-probability-the-vig-ev-and-kelly-in-plain-js"
author: "Clarence Yu"
source: "devto_webdev"
published: "Fri, 05 Jun 2026 15:09:47 +0000"
description: "If you've looked at Polymarket, Kalshi or Manifold and wondered what a "YES share at $0.40" actually means — or why two opposite outcomes don't add up to 100..."
keywords: "you, kelly, probability, const, market, vig, yes, price"
generated: "2026-06-05T15:19:56.045304"
---

# The Math Behind Prediction Market Prices: Implied Probability, the Vig, EV and Kelly (in plain JS)

## Overview

If you've looked at Polymarket, Kalshi or Manifold and wondered what a "YES share at $0.40" actually means — or why two opposite outcomes don't add up to 100% — this post walks through the four pieces of math you need, with copy-pasteable JavaScript. I recently built a small zero-dependency calculator for exactly this, and the functions below are the heart of it. 1. The price is the probability A binary prediction-market contract settles at $1 if the event happens and $0 if it doesn't. So the current YES price, in dollars, is just the market's implied probability : // price in cents (0–100) → implied probability (0–1) const impliedProb = ( priceCents ) => priceCents / 100 ; impliedProb ( 40 ); // 0.40 → the market says 40% No separate "odds" object, no vig baked into a moneyline — the number on the screen is the probability. That's what makes prediction markets so readable compared to a sportsbook. If you do want to cross-check against sportsbook formats: const toOdds = ( p ) => ({ decimal : 1 / p , american : p > 0.5 ? - Math . round ( 100 * p / ( 1 - p )) : Math . round ( 100 * ( 1 - p ) / p ), // fractional: odds-against = (1 - p) / p }); toOdds ( 0.40 ); // { decimal: 2.5, american: 150 } 2. Removing the vig (overround) Here's the gotcha that trips up newcomers: the YES price and the NO price almost never sum to exactly 100¢. The excess is the vig (a.k.a. overround) — the margin baked into the two-sided market. Before you compare a price across two platforms, you have to strip it out: function deVig ( yesCents , noCents ) { const y = yesCents / 100 , n = noCents / 100 ; const sum = y + n ; return { fairYes : y / sum , // normalised, vig removed fairNo : n / sum , overround : sum - 1 , // the vig itself }; } deVig ( 56 , 47 ); // { fairYes: 0.5437, fairNo: 0.4563, overround: 0.03 } // raw 56% looks like the answer, but the *fair* number is 54.4% Skip this step and you'll think you found an edge that's really just two different vigs. I go deeper on this on the reference page for implied probability . 3. Expected value and edge Once you have a fair probability you trust (your own estimate p ), buying a YES share at cost c has a dead-simple EV: function ev ( costCents , trueProbPct , stake ) { const c = costCents / 100 , p = trueProbPct / 100 ; const shares = stake / c ; // each share pays $1 on YES return { edge : p - c , // your advantage, per $1 of payout evDollars : shares * ( p - c ), // expected profit on this stake roi : ( p - c ) / c , }; } ev ( 40 , 50 , 100 ); // { edge: 0.10, evDollars: 25, roi: 0.25 } The trap: positive EV is an average over many independent, correctly-estimated bets — never a guarantee on any single market. The number is only as good as your p . 4. Kelly sizing EV tells you whether to bet; Kelly tells you how much . For a binary contract bought at price c with true probability p , the full-Kelly fraction of bankroll is: function kelly ( costCents , trueProbPct , bankroll , fraction = 0.5 ) { const c = costCents / 100 , p = trueProbPct / 100 ; const full = ( p - c ) / ( 1 - c ); // full-Kelly fraction const applied = Math . max ( 0 , full * fraction ); return { fullPct : full , stake : applied * bankroll }; } kelly ( 40 , 50 , 1000 , 0.5 ); // { fullPct: 0.1667, stake: 83.33 } → half-Kelly on a $1000 bankroll Real-world probability estimates are noisy, so almost nobody runs full Kelly — quarter-to-half Kelly cuts the variance (and the gut-wrenching drawdowns) dramatically while keeping most of the growth. Putting it together Those four functions — impliedProb , deVig , ev , kelly — are basically the whole toolkit. No dependencies, runs anywhere. I wired them into a single-page UI you can play with here: prediction market probability calculator . And if you want live numbers to feed into it, U-Town Market tracks real YES/NO probabilities from Polymarket, Kalshi and Manifold and refreshes every few hours. A couple of implementation notes if you build your own: Clamp probabilities to [0.0001, 0.9999] before converting to odds, or you'll hit divide-by-zero at the extremes. Validate the de-vig inputs — if a user types a YES + NO that sum below 100 you've got an arbitrage (or bad data), worth flagging in the UI. Keep it dependency-free . This is arithmetic; pulling in a stats library is overkill and bloats your bundle. Happy to answer questions in the comments — and if you've built something similar for prediction markets, I'd love to see how you handled cross-platform de-vigging.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/clarencyuboop/the-math-behind-prediction-market-prices-implied-probability-the-vig-ev-and-kelly-in-plain-js-1ibl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
