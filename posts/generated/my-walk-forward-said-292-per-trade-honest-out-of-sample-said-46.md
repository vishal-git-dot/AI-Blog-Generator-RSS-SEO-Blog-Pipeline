---
title: "My Walk-Forward Said +29.2 Per Trade. Honest Out-of-Sample Said -4.6."
slug: "my-walk-forward-said-292-per-trade-honest-out-of-sample-said-46"
author: "王伟"
source: "devto_python"
published: "Wed, 21 Oct 2026 16:44:29 +0000"
description: "A parameter set that won on folds 1-3 lost on folds 4-5. Same strategy, same data. I ran the standard walk-forward check. Three parameter sets, five sequenti..."
keywords: "sample, not, fold, gap, you, parameter, trade, out"
generated: "2026-10-21T16:57:15.637252"
---

# My Walk-Forward Said +29.2 Per Trade. Honest Out-of-Sample Said -4.6.

## Overview

A parameter set that won on folds 1-3 lost on folds 4-5. Same strategy, same data. I ran the standard walk-forward check. Three parameter sets, five sequential folds, about 400 trades. For each fold I picked the set that was best on the previous folds only, then scored it on the fold it had never seen. Here is the whole output: fold picked oos net oos t 2 k0.75 436.5 0.88 3 k0.75 827.9 1.56 4 k0.75 -941.2 -2.51 5 k1.00 -813.2 -1.96 Stitched out-of-sample: n=107 net=-489.99 mean=-4.58 t=-0.51 In-sample best mean : +29.17 per trade Optimism gap : 33.75 per trade The parameter set k0.75 looked best for three consecutive folds. It was the worst set for the next two. +29.17 per trade in sample. −4.58 out of sample. The gap is 33.75 per trade, which is larger than the entire in-sample edge — the sign flipped. What "out-of-sample" actually means Most people treat out-of-sample as a split. You cut the data at some date, fit on the left, evaluate on the right, and call the right side honest. That is not what makes it honest. Out-of-sample is a procedure, not a file. What makes it honest is that no choice in the evaluation was informed by the data being evaluated. Here is the distinction, concretely: What you did Is the score honest? Optimised on 2015-2020, tested on 2021-2023, and you never looked at 2021-2023 while designing yes Optimised on 2015-2020, tested on 2021-2023, then went back and tweaked because 2021-2023 looked bad no — that file is now in-sample Picked the parameter that maximised the whole period, then reported the second half no — the second half informed the pick Picked on folds 1..i-1, scored on fold i, never revisited yes The third row is the one that catches people. If you choose a parameter using any statistic computed over the test period — total return, Sharpe, whether the equity curve "looked right" — the test period has leaked into the choice, and the score is in-sample no matter which file it lives in. The gap is not a haircut The natural instinct is to treat the optimism gap as a discount: knock 20% off the in-sample number and move on. That does not work, because the gap is not proportional to the edge. It is roughly proportional to how much selection freedom you had . In this example: in-sample best mean: +29.17 honest out-of-sample: −4.58 The gap (33.75) was bigger than the edge (29.17). There was no discount that turns this back into a positive number, because the honest number is negative. When the gap exceeds the edge, what you measured was not a weak strategy. You measured the selection process. Why this happens Three mechanisms, all mundane: 1. Fold-to-fold variance is large. A fold with 20-25 trades has a standard error of roughly sd / sqrt(25) . If per-trade sd is around 100, the standard error of the mean is about 20 per trade. So a "best mean" of 29 is roughly one to two standard errors above zero — entirely reachable by luck. With three candidate sets, picking the top one at each step reliably picks the noisiest winner. 2. Regime change is not announced. The demo I used has the edge decaying after ~60% of the sample on purpose, which is a clean version of what real markets do more subtly. A parameter that suits the first regime is not obliged to suit the second. 3. The selection is repeated, not once. You do not choose a parameter once. You choose at fold 2, again at fold 3, again at fold 4. Each choice is a fresh chance to pick the lucky one, and the errors compound across the stitched result. How to run this yourself You need one thing beyond a trade log: a column saying which parameter set produced each trade. entry_time, exit_time, side, entry_price, exit_price, size, fee, param_set 2024-01-02T09:30:00,...,BUY,100.12,101.40,10,2.00,k0.75 2024-01-03T14:05:00,...,SELL,101.85,100.90,10,2.00,k1.00 With that column, the procedure is mechanical: Split trades into K sequential folds by time. For fold i (starting at i =2), compute each parameter set's mean on folds 1.. i −1. Pick the best one. Score it on fold i only. Stitch the fold- i results. That stitched series is your honest number. Compare it to the best in-sample mean. The difference is the gap. python backtest_kit.py folds trades.csv --k 5 Without the column, all you can do is split validation, which is weaker — it tells you about stability over time, not about selection. The tool says so rather than pretending otherwise. The part that stings I did not set out to fool myself. I had a parameter grid, I picked the winner on the development data, and I reported the number. That is the standard workflow, and it is exactly the workflow that produces this gap. The gap is not a sign of carelessness. It is the expected output of selecting on noise. Which means the fix is not "be more careful" — it is to make the selection procedure mechanical and to report the stitched number, including when it is negative. The uncomfortable question is not "was my gap large". It is: how many strategies do I still believe in because I never computed this number for them? The fold walk and the gap calculation are in a small open-source kit ( GitHub , MIT, no dependencies). If you have run this on your own grid and the gap came out smaller than the edge, I would like to see the setup — that is the interesting case.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wei-backtest/my-walk-forward-said-292-per-trade-honest-out-of-sample-said-46-km2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
