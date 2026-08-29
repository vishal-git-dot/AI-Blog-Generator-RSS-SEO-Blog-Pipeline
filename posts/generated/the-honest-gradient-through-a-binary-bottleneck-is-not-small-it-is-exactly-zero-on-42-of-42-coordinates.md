---
title: "The Honest Gradient Through a Binary Bottleneck Is Not Small. It Is Exactly Zero on 42 of 42 Coordinates."
slug: "the-honest-gradient-through-a-binary-bottleneck-is-not-small-it-is-exactly-zero-on-42-of-42-coordinates"
author: "Devanshu Biswas"
source: "devto_python"
published: "Sat, 29 Aug 2026 20:24:15 +0000"
description: "The bottleneck is six binary units, h = sign(pre) . The task is built so that a discrete bottleneck is exactly the right model: the true conditional depends ..."
keywords: "not, pre, gradient, exactly, through, bottleneck, zero, exact"
generated: "2026-08-29T20:45:19.186516"
---

# The Honest Gradient Through a Binary Bottleneck Is Not Small. It Is Exactly Zero on 42 of 42 Coordinates.

## Overview

The bottleneck is six binary units, h = sign(pre) . The task is built so that a discrete bottleneck is exactly the right model: the true conditional depends on x only through m binary features, so a zero-excess student provably exists , the teacher scores exactly 0, and the score is a mean KL above a conditional-entropy floor of 0.8161 nats over 4 classes — with the whole 64-point input space enumerated. Run it: https://dev48.infy.uk/dl/day74-straight-through-estimators.html The derivative is not small method result reverse mode 0.0e+0 on all 42 parameters below the bottleneck forward-mode dual numbers 0.0e+0 central difference exactly zero on 42 of 42 coordinates That is an identity , not a tolerance. A perturbation that flips no code leaves the two forward passes bit-identical , so the difference is exactly zero — and the page asserts that equivalence in both directions. So gradient descent on the encoder is not slow. It is arithmetically the same thing as not training the encoder . What the straight-through estimator actually is It is usually described as an approximation to a derivative that does not exist, which makes it sound like a hack with an error term to bound. It is something more specific: h = q ( pre ) + ( pre - pre . detach ()) # forward: q(pre). backward: d/d pre = 1 That is the exact derivative of a different function — one where the quantiser's output is treated as the input plus a constant shift. There is no error term. The page builds that second path over dual numbers and checks the identity rather than asserting it. The part that goes against the intuition If it is a surrogate, you would tune it by making it resemble the true gradient more closely. Measured here, that is backwards: the configurations whose route most resembles the exact gradient are the unclipped ones, which is precisely why they lose a sign-flipped route reduces the loss on 100% of trials, while its cosine with the exact gradient is −0.8536 — the bit-exact negation of the correct route's +0.8536 The question is never how good an approximation is it . It is whether the surrogate's descent directions get you somewhere on the objective you actually care about. 298 verifier asserts, 475 in-page checks, 0 failures.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/the-honest-gradient-through-a-binary-bottleneck-is-not-small-it-is-exactly-zero-on-42-of-42-4nbl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
