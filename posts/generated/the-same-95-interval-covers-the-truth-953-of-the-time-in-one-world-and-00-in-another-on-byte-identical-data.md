---
title: "The Same 95% Interval Covers the Truth 95.3% of the Time in One World and 0.0% in Another, on Byte-Identical Data"
slug: "the-same-95-interval-covers-the-truth-953-of-the-time-in-one-world-and-00-in-another-on-byte-identical-data"
author: "Devanshu Biswas"
source: "devto_python"
published: "Sun, 23 Aug 2026 12:40:24 +0000"
description: "Every column in every dataset is a recording, and the recording is not the thing. Write w = x + u : you fit on w, the world runs on x. The textbook consequen..."
keywords: "world, one, every, same, interval, coverage, rho, recording"
generated: "2026-08-23T12:50:17.231458"
---

# The Same 95% Interval Covers the Truth 95.3% of the Time in One World and 0.0% in Another, on Byte-Identical Data

## Overview

Every column in every dataset is a recording, and the recording is not the thing. Write w = x + u : you fit on w, the world runs on x. The textbook consequence is attenuation — the slope comes back multiplied by the reliability λ — and the textbook reaction is that it is conservative, so never mind. Fix the observed law instead. Standardise Var(w) = 1, write c = Cov(w, y) and v = Var(y), and a world is then one number: β = c / λ σ²ᵤ = 1 - λ σ²ε = v - c²/λ <- the only constraint in the problem σ²ε >= 0 <=> λ >= c²/v = R² That is the Frisch bound, derived as a non-negativity condition rather than quoted — and confirmed a second, completely independent way as the point where the third latent noise coefficient stops being real. Every world, live: https://dev48.infy.uk/ml/day69-measurement-error.html One dataset, six truths, one interval The page draws the observed arrays once and reconstructs each world's latents as a linear map of the same three normals, so every world returns base.obs — the same object, asserted with === . The interval is therefore computed once and scored six times. world true β fitted slope coverage of β closed form no error, λ = 1 1.000 1.000 95.3% 95.0% classical, λ = 0.925 1.081 1.000 37.8% 37.1% classical, λ = 0.700 1.429 1.000 0.0% 0.0% classical, λ = λₘᵢₙ = 0.5 2.000 1.000 0.0% 0.0% Berkson, σ²ᵤ = 0.5 1.000 1.000 95.3% 95.0% Same endpoints, literally. And the identified set runs from c to v/c, a ratio of exactly 1/R² — so the weaker the fit the less the slope is pinned down, which is the opposite of the instinct that a weak fit means a small effect. Every diagnostic a residual plot, a holdout, a bootstrap or a heteroskedasticity test can reach is bit-identical across all of them. What separates the worlds is whether u is independent of the truth or of the recording, and u is never observed. The bias does not stay in its own column Two predictors, x₁ recorded with reliability 0.50, x₂ recorded perfectly, ρ = 0.7, and a true β₂ of exactly zero: beta2_hat = beta2 + d*rho*beta1 / (1 + d - rho^2) = 0.4636 beta1_hat = beta1*(1 - rho^2) / (1 + d - rho^2) = 0.3377 A variable with no effect at all is fitted at 0.4636 with |t| = 9.8 at n = 1,000 and 68.8 at n = 40,000 — and it outranks the variable that does have an effect. The bias formula contains no β₂ anywhere, and "conservative" turns out to be a one-predictor statement. What the measurement contradicted I asserted that every world with β ≠ c should be missed by the interval. Wrong: the λ = 0.925 world sits 2.3 standard errors from c and legitimately covers 37.8% of the time, matching a closed form of 37.1%. The assertion now compares against Φ(q−δ) − Φ(−q−δ) rather than against my expectation of it. The one that nearly shipped as a finding was worse. A measured 99.2% coverage over 250 reps read exactly like over-coverage — and was a property of the seed stream. 44000 + r*7907 fed to mulberry32 gives 99.2% at 250 reps and 97.3% at 1,000; multiplicative hashing of the same reps gives 95.2% and 94.9%. Replication seeds are now hashed, and an assertion guards it. 1,471 verifier assertions, 24 in-page checks, 25 seeds, 400 coverage replications. Part of a from-scratch series — one idea a day, vanilla JS, one file, dependency-free engine: https://dev48.infy.uk/machinelearningfromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/the-same-95-interval-covers-the-truth-953-of-the-time-in-one-world-and-00-in-another-on-1op1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
