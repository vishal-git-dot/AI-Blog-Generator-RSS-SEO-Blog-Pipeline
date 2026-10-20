---
title: "Six SaaS metric formulas and the edge cases that break them"
slug: "six-saas-metric-formulas-and-the-edge-cases-that-break-them"
author: "牛云鹏"
source: "devto_webdev"
published: "Tue, 20 Oct 2026 04:12:40 +0000"
description: "Every SaaS metric calculator is five lines of arithmetic. The bugs are all in the edges. I wrote six of them — LTV:CAC, CAC payback, quick ratio, MRR/ARR, ch..."
keywords: "ltv, cac, mrr, const, null, not, payback, ratio"
generated: "2026-10-20T04:19:10.499737"
---

# Six SaaS metric formulas and the edge cases that break them

## Overview

Every SaaS metric calculator is five lines of arithmetic. The bugs are all in the edges. I wrote six of them — LTV:CAC, CAC payback, quick ratio, MRR/ARR, churn rate and runway — and wrote the tests before the UI. Below are the cases that return an answer which looks completely reasonable and is completely wrong. They are worth knowing even if you never build a calculator, because the same arithmetic sits inside every spreadsheet that reports these numbers. 1. Zero churn makes LTV infinite Average customer lifetime is 100 / monthlyChurnPct . At zero churn that is Infinity , so LTV is Infinity , so the LTV:CAC ratio is Infinity . Nothing throws. The UI renders a number. The number is unbeatable. const lifetimeMonths = churnPct <= 0 ? null : 100 / churnPct const ltv = lifetimeMonths === null ? null : arpu * grossMargin * lifetimeMonths Return null and render "unbounded" with a note that real cohorts always churn eventually. An explicit null beats a helpful default, because a default can be silently summed into a total while null has to be handled. Same trap on the other side: CAC = 0 makes the ratio infinite. Zero CAC is never true, it means the denominator was not filled in. 2. Annual contracts booked as one month A $1,200 annual plan is $100 of MRR. Booking the cash when it lands gives you this: March MRR jumps by $1,200 April MRR falls by $1,100 relative to March Every chart downstream — net new MRR, growth rate, quick ratio — inherits the spike and the crash The twelve-fold error is not a rounding problem, it is a definition problem: MRR is a rate, not a receipt. Amortise the contract across its term before it reaches any metric. const mrr = billingPeriod === ' annual ' ? planPrice / 12 : planPrice 3. LTV on revenue instead of gross profit The 3x rule of thumb assumes gross profit. Using revenue inflates LTV by 1 / grossMargin — at an 80% margin that is 25% too high, at 50% it is double. // wrong: compares revenue to a cost const ltv = arpu * lifetimeMonths // right: compares profit to a cost const ltv = arpu * grossMargin * lifetimeMonths This one is nasty because the result still looks like a number. At a 70% margin a business at 2.1x looks like 3.0x, and the conclusion flips from "underinvesting" to "healthy". 4. CAC payback without the margin const paybackMonths = cac / ( arpu * grossMargin ) Drop grossMargin and payback shrinks by the margin: at 80% a real 6.25-month payback reports as 5.0. The rule of thumb is "under 12 months", so a 15-month payback reported as 12 sits exactly on the boundary and passes. 5. Quick ratio when nothing churned const quickRatio = mrrLost === 0 ? null : mrrGained / mrrLost A month with no churn is either a tiny base or a data problem. Rendering Infinity makes it indistinguishable from a genuinely excellent month, and it will be copied into a board deck. 6. Money is not a float 0.1 + 0.2 is 0.30000000000000004 . It does not matter at these magnitudes until you start summing and comparing — and then paybackMonths <= 12 is false for what a human computes as 12.0. For a single calculation, round only at the point of display. If you are summing rows, store integer cents. const round = ( n : number , dp = 2 ) => Math . round ( n * 10 ** dp ) / 10 ** dp The general rule Every one of these is the same bug wearing a different hat: a missing value is not zero, and an unbounded value is not a large one. A calculator whose inputs are optional and whose outputs are numbers needs a third state. null in the model, an explicit "not enough information" in the UI. The alternative is a dashboard that is confidently wrong, which is worse than one that is visibly empty. I put these six into free, no-signup calculators — LTV:CAC , CAC payback , quick ratio , MRR & ARR , churn and runway . Every one shows its formula and its derivation, and the edge cases above are covered by tests rather than by hope.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/optimetricshub/six-saas-metric-formulas-and-the-edge-cases-that-break-them-377l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
