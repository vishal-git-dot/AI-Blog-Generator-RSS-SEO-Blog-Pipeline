---
title: "Quantile regression: don't predict the average, tilt the loss — pinball ρτ(r)=max(τr,(τ 1)r) fits a line through any percentile"
slug: "quantile-regression-dont-predict-the-average-tilt-the-loss-pinball-rmaxr-1r-fits-a-line-through-any-percentile"
author: "Devanshu Biswas"
source: "devto_python"
published: "Wed, 29 Jul 2026 18:58:29 +0000"
description: "A single best-fit line hides most of what you need to know. Ordinary least squares reports the conditional mean and quietly assumes the noise around it is fi..."
keywords: "quantile, loss, mean, tau, line, each, fit, you"
generated: "2026-07-29T19:24:36.663961"
---

# Quantile regression: don't predict the average, tilt the loss — pinball ρτ(r)=max(τr,(τ 1)r) fits a line through any percentile

## Overview

A single best-fit line hides most of what you need to know. Ordinary least squares reports the conditional mean and quietly assumes the noise around it is fixed and symmetric. Real data breaks both: incomes, delays and prices are skewed, and the spread often fans out as the input grows. Quantile regression fits a line through any chosen percentile instead — the 10th, the median, the 90th — by swapping squared error for the pinball loss , an asymmetric tilt whose minimizer is exactly the quantile you asked for. I built a demo that fits it live in the browser with plain-JS subgradient descent on data you place yourself. Here's what it taught me. The pinball loss tilts the penalty Everything hangs on one loss on the residual r = y − ŷ : function pinball ( r , tau ){ return r >= 0 ? tau * r : ( tau - 1 ) * r ; } Under-predicting (truth above the line) costs τ·r ; over-predicting costs (1−τ)·|r| . For τ=0.9 an undershoot is nine times more expensive than an overshoot, so the fitted line is forced up until only 10% of points sit above it. At τ=0.5 both arms have slope ½, so ρ = ½|r| — plain absolute error, whose minimizer is the median, not the mean. On skewed data that difference is real: the mean is pulled toward the long tail while the median holds its ground, which is already a reason to prefer the quantile view. Why its minimizer is the τ-quantile Differentiate Σ ρτ(yᵢ − c) with respect to c : each point above contributes −τ , each below +(1−τ) . Set the sum to zero and it rearranges to (#below)/n = τ — the fraction of points under the line settles at exactly τ. That balance point is the τ-quantile, by definition. Fitting by subgradient descent The only new idea is the subgradient — constant on each side, with no dependence on distance, which is what makes it robust to outliers: function psi ( r , tau ){ return r > 0 ? tau : ( r < 0 ? tau - 1 : tau - 0.5 ); } The gradient of the total loss is −Σ ψ(rᵢ)·[1, xᵢ] . Each point contributes a fixed tug of size τ or 1−τ. I standardize x so one learning rate suits both coefficients, warm-start the intercept at the empirical quantile, and use a decaying step because the loss is piecewise-linear and chatters at its kinks — so I keep the best iterate. const r = pt . y - ( a0 + a1 * z [ i ]); const pv = psi ( r , tau ); g0 += pv ; g1 += pv * z [ i ]; // −∇loss = Σ ψ(r)·[1,z] const step = lr / ( 1 + 0.01 * t ); // decaying step a0 += step * g0 / n ; a1 += step * g1 / n ; Fit several τ and you get an interval that fans out Fit {0.1, 0.5, 0.9} at once and the band between the outer two lines is an 80% prediction interval. The demo's data is deliberately heteroscedastic — the true mean is a straight y = 1 + 0.8x but the noise width grows as 0.6 + 0.8x . So the quantile lines fan open to the right , and the interval widens exactly where the data is noisier. A dashed OLS mean line sits alongside it, reporting one flat spread everywhere — it structurally cannot show the fan. The one gotcha the demo flags: because each τ is fit independently, two lines with slightly different slopes can cross out where data is sparse, producing a 90th percentile below the 50th. The fix is quantile rearrangement — sort the predictions at each x, provably non-worsening. Mean vs median vs quantile It's the same GLM-family story as squared → absolute → pinball: each loss estimates the mean, the median, and the τ-quantile respectively. The payoff of tilting the loss is three-fold — it's robust to outliers, it makes no assumption about symmetric or constant-width noise, and fitting several τ hands you a risk band for free. In production the same loss powers statsmodels quantreg , sklearn's QuantileRegressor , and gradient boosting with loss="quantile" . The takeaway I now carry: the moment you need a floor, a ceiling, a typical value or a risk band, don't fit the average — tilt the loss and fit the quantile. Drop some points, drag τ, and watch the quantile lines fan out from the OLS mean: https://dev48v.infy.uk/ml/day48-quantile-regression.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/quantile-regression-dont-predict-the-average-tilt-the-loss-pinball-rtrmaxtrt-1r-fits-a-29i2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
