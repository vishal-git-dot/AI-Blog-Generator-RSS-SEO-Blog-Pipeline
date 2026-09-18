---
title: "GRPO doesn't remove the reward model. It removes the critic."
slug: "grpo-doesnt-remove-the-reward-model-it-removes-the-critic"
author: "Arun Kumar"
source: "devto_ai"
published: "Fri, 18 Sep 2026 04:00:00 +0000"
description: "Every time GRPO comes up I see the same slip — someone says it "gets rid of the reward model". It doesn't. It gets rid of the value model. Those are two diff..."
keywords: "reward, model, grpo, one, ppo, critic, than, not"
generated: "2026-09-18T04:07:04.909961"
---

# GRPO doesn't remove the reward model. It removes the critic.

## Overview

Every time GRPO comes up I see the same slip — someone says it "gets rid of the reward model". It doesn't. It gets rid of the value model. Those are two different networks doing unrelated jobs, and telling them apart is most of understanding the algorithm. Worth going back to what the DeepSeekMath paper actually claims, because it's more modest than the version that travels. It's a variant, not a successor Shao and colleagues introduce GRPO as "a variant of Proximal Policy Optimization (PPO)". Not a replacement. A variant. It keeps PPO's clipped ratio, and it keeps the reference model. Three things change: the critic goes, the baseline becomes group-relative, and the KL term moves. That's narrower than "GRPO replaces PPO", which is how I usually see it written up. What the critic was costing PPO is actor-critic, so the critic gets trained alongside the policy. The paper is blunt about the bill. That value function is "typically another model of comparable size as the policy model", and so "it brings a substantial memory and computational burden". You're training two large models to ship one. There's a second complaint I found more interesting than the memory one. In language-model RL, "usually only the last token is assigned a reward score by the reward model". A signal that sparse "may complicate the training of a value function that is accurate at each token". So the critic is expensive and hard to fit well. Both halves matter, and only the first one usually gets mentioned. What replaces it Sampling. For each question GRPO samples a group of outputs, scores every one with a reward model — still present, still doing its job — and uses the group's average as the baseline. Those rewards get "normalized by subtracting the group average and dividing by the group standard deviation". So an output's advantage answers a relative question: was this better or worse than its siblings? The paper argues that suits how reward models are built in the first place, since they're trained on comparisons between outputs for the same question. Model count goes four to three: PPO: policy, reference, reward, value GRPO: policy, reference, reward The reward model is right there in the second list. It never left. The trade that isn't in the headline None of this is free. You now need several generations per question instead of one. DeepSeek-R1-Zero sampled 16 outputs per question. GRPO trades memory for generation. Memory-bound, that's a good deal. Throughput-bound, maybe not. The KL term moved, it didn't vanish Second thing I see stated wrong: that GRPO drops KL regularisation. PPO adds "a per-token KL penalty from a reference model in the reward at each token". GRPO works "instead of adding KL penalty in the reward" and "regularizes by directly adding the KL divergence" to the loss. Same idea, different address. GRPO also uses an unbiased estimator "which is guaranteed to be positive". The finding I didn't expect This one rarely survives into summaries, and it's the part I'd most want people to take away. The DeepSeekMath authors measured Pass@K and Maj@K before and after RL. The result was asymmetric: "RL enhances Maj@K's performance but not Pass@K". Read that slowly. The model got better at reliably surfacing an answer it could already produce. It did not start producing answers that were previously out of reach. The authors draw the conclusion themselves — the gain is "attributed to boosting the correct response from TopK rather than the enhancement of fundamental capabilities". That is a considerably narrower claim than the one usually made for RL fine-tuning. Two things worth keeping straight The value model went, the reward model stayed. If someone says GRPO removed the reward model, they've merged two different networks. R1's rule-based rewards were a separate decision. DeepSeek-R1 did drop neural reward models for reasoning tasks, but for another reason entirely: "neural reward models are susceptible to reward hacking during large-scale reinforcement learning". That's a robustness call, not a memory one, and it applied to reasoning tasks specifically. It gets folded into the GRPO story where it doesn't belong. Longer version with every quote sourced at diffstudy.com . Sources: arXiv 2402.03300 (DeepSeekMath), arXiv 2501.12948 (DeepSeek-R1), arXiv 1707.06347 (PPO).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/narotra05hp/grpo-doesnt-remove-the-reward-model-it-removes-the-critic-2pnp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
