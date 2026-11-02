---
title: "Keeping a fee calculator correct when exchanges change their tiers"
slug: "keeping-a-fee-calculator-correct-when-exchanges-change-their-tiers"
author: "aleax h"
source: "devto_python"
published: "Mon, 02 Nov 2026 15:06:16 +0000"
description: "Every exchange fee calculator I have seen starts the same way: a table of maker/taker rates, copied from the exchange's fee page into a constant, and a multi..."
keywords: "decimal, fee, not, rate, you, rounding, tier, schedule"
generated: "2026-11-02T15:18:23.749461"
---

# Keeping a fee calculator correct when exchanges change their tiers

## Overview

Every exchange fee calculator I have seen starts the same way: a table of maker/taker rates, copied from the exchange's fee page into a constant, and a multiply. It works for about six weeks. Then the exchange adds a tier, changes the token discount, or introduces a promotional rate for one pair, and the calculator keeps confidently returning yesterday's number. The interesting engineering problem is not the multiplication. It is keeping the multiplication correct while the inputs move underneath you. Here is the model I ended up with. Model the schedule as data, not as constants A fee schedule is a versioned document, not a set of numbers in your source: { " exchange " : " okx " , " version " : " 2026-10-01 " , " fetched_at " : " 2026-10-01T09:12:00Z " , " tiers " : [ { " min_volume_30d " : 0 , " maker " : " 0.00080 " , " taker " : " 0.00100 " }, { " min_volume_30d " : 100000 , " maker " : " 0.00070 " , " taker " : " 0.00090 " }, { " min_volume_30d " : 1000000 , " maker " : " 0.00060 " , " taker " : " 0.00080 " } ], " token_discount " : { " OKB " : " 0.20 " }, " rounding " : " ceiling " } Two properties matter here and both are easy to get wrong. Rates are decimal strings, not floats. 0.0008 is not representable in binary floating point, and the error compounds the moment you sum fees across many fills. Keep them as strings in the document and parse them into Decimal at the boundary. The schedule carries its own fetched_at and version . A number without a timestamp is indistinguishable from a stale number, and staleness is the failure mode you actually care about. The lookup is a bisect, not an if-chain Tier selection is "the highest tier whose minimum volume the account meets". That is a binary search over sorted thresholds, and writing it as a chain of if volume > X is how the off-by-one at the boundary gets in: import bisect from decimal import Decimal def pick_tier ( tiers , volume_30d : Decimal ): thresholds = [ t [ " min_volume_30d " ] for t in tiers ] idx = bisect . bisect_right ( thresholds , volume_30d ) - 1 return tiers [ max ( idx , 0 )] bisect_right minus one is the tier you are in ; bisect_left silently gives you the tier you are about to reach. The difference is one boundary, and boundaries are exactly where people screenshot a calculator and complain. Effective rate is a product, and order does not matter — until rounding does Effective rate is base rate times the token discount: def effective_rate ( base : Decimal , token_discount : Decimal ) -> Decimal : return base * ( Decimal ( 1 ) - token_discount ) Multiplication is commutative, so the order is irrelevant. Rounding is not. Exchanges differ on whether the fee is rounded up, rounded half-even, or truncated at the asset's precision, and the difference shows up at scale: 10,000 trades of 100 USDT at a 0.08% rate, rounded up to 8 decimal places each, versus rounded half-even, is a measurable spread that a "comparison" site will happily report as a difference between exchanges. So the rounding rule belongs in the schedule document, next to the rates, and the fee function takes it as an argument rather than deciding for you: def fee ( notional : Decimal , rate : Decimal , rounding ) -> Decimal : return ( notional * rate ). quantize ( Decimal ( " 0.00000001 " ), rounding = rounding ) Mark stale data instead of hiding it Fee schedules change rarely, so caching them is correct — and caching them without a staleness marker is how a calculator becomes quietly wrong. What worked for me: cache the whole document, not the computed rate; keep the previous version so a diff is possible when the schedule changes; expose fetched_at to the UI and show "estimated" once it is older than your TTL, instead of pretending the number is current. A calculator that says "based on the schedule from 3 days ago" is more trustworthy than one that says nothing and is wrong. The properties worth testing The arithmetic is simple enough that unit tests mostly restate it. The useful tests are properties: fee is monotonically non-decreasing in notional (for a fixed rate); fee of zero notional is zero; fee never exceeds notional for any sane rate; the tier lookup is stable exactly at each threshold — test threshold - 1 , threshold , threshold + 1 ; a schedule missing a field fails loudly at load, not at compute time. That last one is the one that saves you: a missing rounding key should not fall back to a default that silently changes every number on the page. Where this ends up I keep a working implementation of this model as a reference when comparing exchanges — the interesting part is not the UI but the schedule documents and the tier boundary handling: the fee calculator I use for spot pairs . If you are building your own, the fee endpoints and the maker/taker tier definitions are in the exchange API docs rather than the marketing pages, and they are the only source that stays consistent with what you are actually charged: OKX V5 API reference . The short version: treat fees as data with a version and a timestamp, keep decimals out of floats, put the rounding rule in the document, and test the boundaries instead of the middle.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aleax_h_9843add3eb7d8575e/keeping-a-fee-calculator-correct-when-exchanges-change-their-tiers-305n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
