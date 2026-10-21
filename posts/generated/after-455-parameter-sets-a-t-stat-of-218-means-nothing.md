---
title: "After 455 Parameter Sets, a t-Stat of 2.18 Means Nothing"
slug: "after-455-parameter-sets-a-t-stat-of-218-means-nothing"
author: "王伟"
source: "devto_python"
published: "Wed, 21 Oct 2026 16:44:56 +0000"
description: "The significance test you learned assumes you ran one test. You ran hundreds. I had a strategy with a t-statistic of 2.18 on 400 trades. Under the textbook r..."
keywords: "not, you, one, sample, sets, test, trades, best"
generated: "2026-10-21T16:57:15.636917"
---

# After 455 Parameter Sets, a t-Stat of 2.18 Means Nothing

## Overview

The significance test you learned assumes you ran one test. You ran hundreds. I had a strategy with a t-statistic of 2.18 on 400 trades. Under the textbook reading, that is significant. The conventional threshold for 5% two-sided is about 1.96, and 2.18 clears it. I had spent weeks on the parameter grid before that number appeared, evaluating roughly 455 parameter sets along the way. So I asked the question that killed it: if all 455 of those sets had zero edge, how big would the best of them look? The test nobody runs The standard t-test answers: "if the true mean were zero, how often would a sample like mine show a t of 2.18 or larger?" That question is conditional on one sample. I did not take one sample. I took 455, threw away 454 of them, and kept the largest. The quantity I am actually looking at is not a t-statistic from one draw — it is the maximum of 455 t-statistics . The distribution of a maximum is nothing like the distribution of a single value. The arithmetic rule of thumb people quote is: expected false positives = N × α . With 455 sets at 5%, that would predict about 22.8 sets "significant" by luck. That number is right about the count and useless about the threshold , because it does not tell you how big the biggest one gets. For that, simulate. The simulation I generated 455 strategies, each with: exactly zero edge (mean 0) 400 trades, same volatility as mine the same t-statistic formula then recorded the maximum t across the 455, and repeated that 2,000 times. Everything below is real output, not a sketch. Best-of-455 t under the null: median 2.99 p90 3.51 p95 3.71 p99 ~4.0 P(best-of-455 t >= your 2.18) = 0.999 The median best-of-455 t under pure zero edge is 2.99 . My 2.18 did not clear the median. It was below what search produces on a normal day. Why the bar moves so much The maximum of N draws grows, but slowly — roughly like sqrt(2 log N) for well-behaved tails. Two consequences worth internalising: The usual t = 3 bar is not conservative enough when N is in the hundreds. People treat t = 3 as "strict". Under a 455-wide search at my sample size, the median best is 2.99. You would need to clear something like the 95th percentile — 3.71 — to say anything at all. The bar depends on your sample size. More trades per strategy tightens the single-test distribution but does not shrink the selection effect; with 400 trades the null max still sits near 3. The two effects do not cancel, and it is easy to add trades while also adding grid points, netting out to nothing. The honest accounting Here is what I do now, and it is mechanical: Write down N before searching. Not after. If I planned 20 sets and ended up evaluating 455, the number I report is 455. Compute the selection-adjusted p-value , not the naive one. Simulate the null (or use a formula) and ask what the best of N looks like at my sample size. Report N alongside the t-statistic, every time. A t-statistic without N is not interpretable once you have searched. The third one is the cheapest and it is the one nobody does. "t = 2.18" sounds like a result. "t = 2.18 after 455 evaluations, where the null median is 2.99" is a different sentence entirely, and both are one line. What this does not mean It does not mean the strategy is bad. It means the evidence I had was insufficient to distinguish it from noise produced by searching. Those are different conclusions with different next actions: Conclusion Next action "The strategy has no edge" Drop it "The evidence is insufficient" Collect more data, or search less "The edge is real but unproven" Paper-trade with small size while accumulating Mine was the second. The honest move was to stop adding filters (each filter is a new search, and it would need its own out-of-sample) and instead increase trades per strategy while holding the grid fixed. The uncomfortable arithmetic Every additional parameter set you evaluate buys you a slightly higher chance of a good-looking result, and charges you a slightly higher bar to clear. Early on, the first effect dominates: going from 1 to 10 sets is clearly worth it, you learn something. Later, the second dominates: going from 400 to 455 mostly just raises the bar. There is a crossover, and it is usually much earlier than people think. Mine was somewhere in the low tens. The number of things you tried is not a detail of your process. It is a parameter of your test , and leaving it out is how a search gets reported as a discovery. The simulation is part of a small open-source kit ( GitHub , MIT, no dependencies): backtest_kit.py selection --tried N runs the null for your own N and sample size. It reports a probability, not a verdict — the verdict is yours.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wei-backtest/after-455-parameter-sets-a-t-stat-of-218-means-nothing-k3n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
