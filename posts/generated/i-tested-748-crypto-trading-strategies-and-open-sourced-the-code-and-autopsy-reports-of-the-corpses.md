---
title: "I tested 748 crypto trading strategies and open-sourced the code and autopsy reports of the corpses"
slug: "i-tested-748-crypto-trading-strategies-and-open-sourced-the-code-and-autopsy-reports-of-the-corpses"
author: "Manish Kumbham"
source: "devto_python"
published: "Tue, 03 Nov 2026 22:45:55 +0000"
description: "A few weeks ago I wrote hundreds of hypotheses for crypto trading strategies, re-screened every bot from my last post ( https://www.reddit.com/r/algotrading/..."
keywords: "bots, strategies, can, one, new, testing, judge, trading"
generated: "2026-11-03T23:03:46.605986"
---

# I tested 748 crypto trading strategies and open-sourced the code and autopsy reports of the corpses

## Overview

A few weeks ago I wrote hundreds of hypotheses for crypto trading strategies, re-screened every bot from my last post ( https://www.reddit.com/r/algotrading/s/dF5qfUNaCa ) and open-sourced the whole pile: 748 strategies in total with full code and report cards showing exactly where each one died and why. (That's 416 from last time plus 332 new corpses. The new ones are smarter strategies than before for the most part...) https://github.com/CacheCarti/Crypto-Strategies The pipeline runs 7 stages on real Binance data: code safety, in-sample, OOS, rolling walk forward, randomized starts, slippage stress and a holdout slice that nothing touches. Ran it on cloud VMs this time instead of my dying laptop, so the screening could actually get stricter. What the new pipeline found: Re-ran the 416 bots from my last post. 0 of 416 re-passed in the strictest config, including all 10 of my "survivors". Most die at out-of-sample with negative OOS (-85 to -900bps). The best one, rel_strength_eth_v3, made it to stage 5 and died at holdout. So my "validated" bots were mostly my old screening being sloppy and luck :) In the second config (slightly more lenient) exactly 1 of 416 re-passed, and it was a bot I had originally rejected (weekend_season_eth_v6, +325bps OOS). My graveyard had the only bot that actually lived. The 332 new corpses came from 559 hand-written bots (mixed with another batch, messy to release all at once). 384 screened, 332 dead (published), 52 survived and stay private for further testing. (Yes yes I know 52 is stupidly high, there's a reason for this at the bottom!) Admits per batch: v2 5/42, v3d 0/26, v3h 0/96, v4 3/92, v5 17/52, v6 18/60, v6b 9/16. v3h went 0 for 96, which tracks, it was basically like a monkey typing random keys, just a sweep of untested ideas. v5-v6b were narrow parameter neighbors of a mechanism that already worked. Please don't read the admit rates as some kind of quality check for the batches!! Why the rebuild?: The comments on the last post were right about my sloppy methodology (it still admittedly is sloppy here, but it got better later). It's also built on Google VMs now so I can create a new batch and test faster. I'll drop the batches weekly: Stricter judge: higher OOS thresholds, enforced holdout and a dev/holdout split inside the window so one lucky slice can't pass Every report card shows the exact gate that killed the bot, so you can figure out how to improve it Every batch is hashed so you can check when it was judged and by what I later added a 6+ year certification and a combined replay on 2.75 years, with DSR, PBO, plateau, regime splits, trial-ledger correction. Those results are still being evaluated, they'll come later. One disclosure about report cards vs actual performance: I cross-checked some strategies against QuantConnect classics this week and it surfaced a bug I didn't notice. Some bots emit a "flat" signal and my screen sometimes treated it as "hold". Impact is mostly ±100-300bps per strategy, around 25% of bots may fluctuate by that amount. The later stages and live paths honored flat completely. Yeah so I found a bug in my own judge while checking it against someone else's judge. The judge judges all, including the judge. If anyone improves the strategies and gets different results I'd love to see it. Happy to add tests people think are missing. Every suggestion so far has killed more of my bots... That's the process now! (Btw about the 52 admits, I can already see you smirking at my stupidity... I mean I am stupid but there's a reason for such a high admit number, it just means the 52 are accepted into the next stages: correlation testing (less than 10 made it past this)->data testing on 6+ years->combination testing on 2.75 years->live paper trading->live trading possibly. But most importantly, my standards are deliberately lower!! The experiment I'm trying to conduct is testing a strategy of strategies router. Bots with known gaps can still be considered for entry, because my router should in theory route around these gaps of the bots, smartly. So I'm not only looking for extremely good bots that can one-shot your portfolio I'm also looking for slightly weaker bots to test my router's skill!)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cachecarti/i-tested-748-crypto-trading-strategies-and-open-sourced-the-code-and-autopsy-reports-of-the-corpses-55e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
