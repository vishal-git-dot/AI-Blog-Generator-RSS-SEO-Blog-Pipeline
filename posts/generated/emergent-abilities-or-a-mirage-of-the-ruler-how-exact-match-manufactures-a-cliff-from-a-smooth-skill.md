---
title: "Emergent abilities, or a mirage of the ruler? How exact-match manufactures a cliff from a smooth skill"
slug: "emergent-abilities-or-a-mirage-of-the-ruler-how-exact-match-manufactures-a-cliff-from-a-smooth-skill"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Wed, 22 Jul 2026 08:31:18 +0000"
description: "Scaling laws say a model's loss falls as a smooth, forecastable power law. But downstream skills can behave differently: on many tasks a model scores essenti..."
keywords: "skill, smooth, cliff, model, metric, scale, exact, match"
generated: "2026-07-22T08:36:37.030945"
---

# Emergent abilities, or a mirage of the ruler? How exact-match manufactures a cliff from a smooth skill

## Overview

Scaling laws say a model's loss falls as a smooth, forecastable power law. But downstream skills can behave differently: on many tasks a model scores essentially 0% across a huge range of sizes, then — past some threshold — accuracy leaps. That's an "emergent ability" (Wei et al. 2022), and it's unsettling, because you can't read the jump off the smooth loss curve. Then came the counter-argument (Schaeffer et al. 2023, "Are Emergent Abilities a Mirage?" ): much of that sudden jump is an artifact of a harsh, all-or-nothing metric. I built a simulator that computes both stories from one smooth latent-skill function, and watching the cliff appear and dissolve is the clearest way to see the debate. One smooth latent skill drives everything Start with a single, gently-rising probability that the model gets one step — one token, one reasoning move — right. It's a plain sigmoid in log-scale, perfectly smooth, with no cliff anywhere. Everything else is derived from this. def skill ( x , x0 = 9.2 , k = 1.55 ): return 1 / ( 1 + np . exp ( - k * ( x - x0 ))) # s(x) in (0,1), x = log10(params) # x0 = the scale where a single step is 50% likely to be correct The harsh metric manufactures a cliff A task counts as solved only if all n steps are correct. Under exact-match that's s ** n . Because s is below 1, raising it to a large power keeps the score pinned near zero until s is nearly perfect — then it rockets up. That knee is the "emergent ability". def exact_match ( x , x0 , n ): return skill ( x , x0 ) ** n # all n steps must be right # s rises GENTLY, but s**n stays ~0 until s is close to 1, then SHOOTS up. # bigger n (longer task) => the cliff appears at a LARGER scale. This also explains a real observation: harder, longer tasks emerge later. It's not that the model suddenly "gets" long tasks — it's that a bigger n needs a higher per-step skill before sⁿ clears 50%. Swap the ruler, and the cliff dissolves Now score the same model with metrics that give partial credit. Token accuracy, edit-distance similarity and average log-prob all read s directly (or a monotone function of it), so they inherit its smooth, forecastable shape. No cliff. def token_accuracy ( x , x0 ): return skill ( x , x0 ) # fraction of steps right def edit_similarity ( x , x0 ): return skill ( x , x0 ) # 1 - norm. edit distance ~ s def avg_log_prob ( x , x0 ): return np . log ( skill ( x , x0 )) # continuous, concave, smooth Sweep scale once and plot exact-match against token accuracy on the same axis. The only difference between the cliff and the smooth curve is the metric — the underlying s(x) is identical. That is the core of the "mirage" argument. The threshold lives in the metric, not the model You can prove the threshold is an artifact of n . Find where exact-match crosses 50% by inverting the sigmoid at the skill level s = 0.5 ** (1/n) . Crank n up and the apparent threshold slides to larger scale — even though the latent skill never moved. def apparent_threshold ( x0 , n , k = 1.55 ): s = 0.5 ** ( 1 / n ) # skill needed so that s**n = 0.5 return x0 + np . log ( s / ( 1 - s )) / k # invert the sigmoid -> log10(params) # apparent_threshold(9.2, 5) -> emerges earlier # apparent_threshold(9.2, 40) -> emerges much later; skill(x) unchanged The "phase transition" is a property of the metric times the task length, not a switch flipping inside the model. The honest verdict — and why it's a safety issue Not all emergence is a mirage. Genuine sharp transitions may exist, and users often do care about all-or-nothing outcomes — a proof either checks out or it doesn't, code compiles or it doesn't. So the takeaway is disciplined measurement, not complacency: # practical guardrails: # 1) always report a CONTINUOUS metric alongside exact-match — it forecasts. # 2) smooth loss does NOT imply smooth capability. # 3) exact-match matters when the USER needs the whole answer right. # 4) for safety: keep monitoring for ABRUPT new abilities as you scale. A lot of "emergence" is a mirage of the harsh ruler; some jumps are real and worth watching. Both readings are important, and the simulator lets you feel exactly where each one comes from — the same function s(x) , viewed two ways. Drag the scale, flip the metric, and watch the cliff appear and vanish: https://dev48v.infy.uk/ai/days/day41-emergent-abilities.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/emergent-abilities-or-a-mirage-of-the-ruler-how-exact-match-manufactures-a-cliff-from-a-smooth-1aga

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
