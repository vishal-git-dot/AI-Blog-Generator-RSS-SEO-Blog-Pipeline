---
title: "Bandit or fixed split? How to pick when your site doesn't get much traffic"
slug: "bandit-or-fixed-split-how-to-pick-when-your-site-doesnt-get-much-traffic"
author: "EvolveAB Admin"
source: "devto_webdev"
published: "Fri, 20 Nov 2026 15:00:00 +0000"
description: "Every experiment in evolveAB is one of two kinds, and you can't change the choice once it starts. An A/B/n test splits traffic evenly and keeps it that way. ..."
keywords: "traffic, you, bandit, variant, test, split, every, visitors"
generated: "2026-11-20T15:10:11.461906"
---

# Bandit or fixed split? How to pick when your site doesn't get much traffic

## Overview

Every experiment in evolveAB is one of two kinds, and you can't change the choice once it starts. An A/B/n test splits traffic evenly and keeps it that way. A bandit starts even and then moves traffic toward whichever variant is doing better. Bandits sound like the obvious pick, since why keep sending half your visitors to a loser? But they answer a different question, and on a site with modest traffic the difference shows up fast. Measuring versus earning A fixed split is for measuring . Every arm gets the same share for the whole test, so at the end you have a fair estimate for each variant, losers included. If you need to know whether the new pricing copy is 4% better or 20% better because that number feeds another decision, run a fixed split. A bandit is for earning while it learns . It wants more conversions during the test and cares much less about how bad the weak arms are. Once a losing variant stops getting traffic you learn little more about it, which is fine, because you weren't going to ship it. How the bandit moves traffic It uses Thompson sampling. For each variant the cloud keeps a Beta posterior over the conversion rate, Beta(1 + conversions, 1 + visitors − conversions) for a yes/no goal. It draws from all of them 20,000 times and counts how often each arm comes out on top. That share, P(best), becomes the arm's traffic weight. Left alone, that rule would overreact, so four limits hold it back: Warm-up. Weights stay equal until every arm has 100 visitors, because before that the posteriors are too wide to mean much. Floors. Control always keeps at least 10% of traffic, since every variant gets compared with it. Every other arm keeps at least 5% (less when there are many arms), so a variant with a bad first week can recover. Pace. The cloud recomputes at most hourly and only when new data has arrived. It publishes new weights only when one moves by 2 percentage points or six hours have passed. Sticky visitors. New weights affect new visitors only; someone who saw variant B last week keeps seeing B. What happens on a small site With a few hundred visitors a week, the warm-up alone takes a while and the posteriors stay wide long after it. The bandit will still shift traffic, but slowly and with some wobble. You can still use a bandit on a small site, but give it a fast goal. A bandit only learns from conversions it has already seen, and a goal with a 30-day window gives it almost nothing to work with in the first month. We recommend bandits for goals with a window of 7 days or less, and autopilot requires it. Also, don't read the traffic split as a verdict. If variant C has 60% of traffic, that only means the bandit currently thinks C is most likely best. The results table still reports P(beat control), the interval and the state, computed the same way as for a fixed split, and that's where you make the call. A quick guide You want to Use Know how big the effect is, for every variant A/B/n test Make a ship-or-don't call you'll defend later A/B/n test Get more sign-ups during the test itself Bandit Keep testing new AI challengers on one region, indefinitely Bandit, with autopilot Test something with a slow goal (churn, 30-day revenue) A/B/n test, and patience If you're unsure, start with a fixed split on your most important page. Bandits pay off once you're running a steady stream of variants on the same region, which is what autopilot does. Originally published on the Evolve blog .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/evolveab/bandit-or-fixed-split-how-to-pick-when-your-site-doesnt-get-much-traffic-3b2j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
