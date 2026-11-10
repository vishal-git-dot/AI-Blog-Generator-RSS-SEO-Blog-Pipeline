---
title: "Rounding is a business rule: what your fee calculation actually charges"
slug: "rounding-is-a-business-rule-what-your-fee-calculation-actually-charges"
author: "aleax h"
source: "devto_python"
published: "Tue, 10 Nov 2026 01:14:22 +0000"
description: "A fee calculator is mostly arithmetic, and the arithmetic is mostly correct. The part that produces support tickets is the last step: rounding. It looks like..."
keywords: "rounding, fee, not, rate, then, decimal, precision, round"
generated: "2026-11-10T01:21:53.735504"
---

# Rounding is a business rule: what your fee calculation actually charges

## Overview

A fee calculator is mostly arithmetic, and the arithmetic is mostly correct. The part that produces support tickets is the last step: rounding. It looks like formatting. It is actually a business rule that decides whether the number on screen matches the number that was charged, and in a fee-heavy product those two disagree more often than anyone expects. Here is what rounding actually does in a fee pipeline, and the three places it silently changes the answer. Rounding direction is a decision, not a default Every language gives you several: half-up, half-even (banker's), ceiling, floor, truncation. They differ only on ties and on negatives, which is exactly where money lands when a refund is involved. The important thing is that this is not a technical choice. Ceiling on a fee means the platform always collects a little more than the formula says; floor means it collects a little less. Over ten thousand small trades, "a little" is a line item. So the rounding mode belongs in the fee schedule as data, next to the rates — not hardcoded in the formatter where nobody will look for it. schedule = { "rate" : Decimal ( "0.0008" ) , "rounding" : "ceiling" , # business decision, stored with the rate "precision" : 8 , # asset precision, not display precision } If the mode lives in code and the rates live in the database, then a venue changing its rounding rule is a deploy, and until that deploy your numbers are wrong by a fraction of a basis point that nobody can see. The order of operations changes the result Fees are frequently computed as amount * rate , then converted, then rounded, then summed. Each of those steps is a place to round, and rounding early loses money in one direction and invents it in the other. Two rules that hold up: Keep full precision through the pipeline , round once at the boundary where the number becomes money. Round per line item, then sum — not sum then round — if the venue charges per fill. The difference is small per trade and systematic over a month. The failure mode is a total that does not equal the sum of its parts, which is the single most common complaint about any fee report. Floating point is not the villain, but it is a trap 0.1 + 0.2 != 0.3 is famous enough that most people avoid floats for money. The subtler trap is mixing: a Decimal rate applied to a float amount silently becomes a float, and the precision you carefully preserved is gone. If the amount arrives from JSON, it arrives as a float or a string, and which one it is depends on the client. So the boundary matters: parse to Decimal at the edge, from the string, and never let a float into the calculation. Decimal(str(value)) , not Decimal(value) . Testing rounding is different from testing arithmetic You cannot test rounding with assertEqual on a computed value alone, because the interesting cases are the ties. Three tests that catch almost everything: the tie case for each mode you support, with a value that lands exactly on the boundary; the negative case , because refunds round differently from charges under half-up; the reconciliation case : the sum of rounded line items equals the reported total, for a random batch of a thousand rows. That third one is the one that finds real bugs, because it tests the invariant rather than a number. I have never written it and had it pass first time. Why this matters more than the rate Users compare rates and then check the total. If the rate is 0.08% and the total implies 0.083%, the conversation is not about rounding — it is about trust. The fee page is where a trading product is most likely to be accused of something it did not do, and rounding is usually the actual explanation. The working version of this — schedules with the rounding mode stored as data, Decimal end to end, per-line rounding reconciled against the total — is what runs the spot fee calculator I use: the spot fee calculator with per-venue rounding rules . Two earlier notes in this series cover the adjacent problems: modelling fee schedules as data rather than constants and keeping that data consistent when it changes rarely . The short version Rounding is a business rule, so store it with the rates. Keep full precision until the money boundary, round per line item, reconcile the sum, and test the ties. The rate is the part everyone argues about; the rounding is the part that is actually wrong.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aleax_h_9843add3eb7d8575e/rounding-is-a-business-rule-what-your-fee-calculation-actually-charges-2dmf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
