---
title: "U-Net Beats FNO on In-Distribution Heat Conduction — Until You Double the Resolution"
slug: "u-net-beats-fno-on-in-distribution-heat-conduction-until-you-double-the-resolution"
author: "pack petter"
source: "devto_python"
published: "Sat, 28 Nov 2026 06:48:02 +0000"
description: "I benchmarked three neural-operator surrogates — FNO, U-Net, and DeepONet — on 2D steady heat conduction, and the ranking flips depending on a question most ..."
keywords: "resolution, fno, net, surrogate, solver, distribution, surrogates, you"
generated: "2026-11-28T07:12:28.667624"
---

# U-Net Beats FNO on In-Distribution Heat Conduction — Until You Double the Resolution

## Overview

I benchmarked three neural-operator surrogates — FNO, U-Net, and DeepONet — on 2D steady heat conduction, and the ranking flips depending on a question most surrogate papers don't ask: what resolution will you actually deploy at? The setup (and why I verified the solver first) Before any learning, the reference finite-volume solver was verified: manufactured-solutions convergence order ≈ 2.00, a layered 1D analytic solution matched, and discrete energy balance to better than 3e-13. All three surrogates were then trained on identical budgets over 5 seeds, with out-of-distribution sets and a paired 64×64 / 128×128 resolution test. The point of verifying ground truth first: a surrogate can only be as honest as the solver it learns from. In-distribution, U-Net wins clearly Relative L2 error on in-distribution test data: Model Relative L2 U-Net 6.1% DeepONet 15.4% FNO 16.1% If you only ever run at the training resolution, this is a short story: use the U-Net. Zero-shot at 128×128, the ranking flips Same models, evaluated zero-shot at double resolution: Model Relative L2 at 128×128 FNO 15.9% U-Net 23.5% The U-Net's peak-temperature error balloons to 55% at the higher resolution. The FNO, built for resolution invariance, basically holds its error. This is the result that changed how I pick surrogates: the "best" model depends on the deployment grid, not just the test set. Two things that actually helped the FNO A physics-residual loss helped at every dataset size: at 1,200 samples, FNO error went from 16.3% to 12.9%. Mirror-symmetry augmentation helped similarly (down to 12.6%). Shrinking the model did not help. The honest negative result: don't optimise on the surrogate All three surrogates were then put to work in SIMP layout optimisation, with every proposed design re-checked by the solver. Optimising a layout directly on the surrogate gets exploited by the optimiser: the FNO under-predicts peak temperature by 27–52% at its own designs. One refinement round makes it honest (±8%), but still not competitive with adjoint optimisation. Takeaways Verify the ground-truth solver before benchmarking surrogates — otherwise you're ranking noise. Report errors at the deployment resolution, not just the training one. The in-distribution winner can be the zero-shot loser. Never trust a surrogate-optimised design without a solver re-check. The optimiser will find — and use — every blind spot your surrogate has. These are simulation results from a controlled benchmark (identical budgets, 5 seeds, paired resolution test), so treat the exact percentages as specific to this setup — but the resolution-flip pattern and the optimiser-exploitation problem are the parts I'd bet on generalising.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pack_petter_73cbede229ec2/u-net-beats-fno-on-in-distribution-heat-conduction-until-you-double-the-resolution-3kfo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
