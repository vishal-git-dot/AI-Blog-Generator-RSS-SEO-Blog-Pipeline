---
title: "Two Groups With Identical ROC Curves, Identical TPR and FPR to the Last Bit, and a 13-Point Selection Gap"
slug: "two-groups-with-identical-roc-curves-identical-tpr-and-fpr-to-the-last-bit-and-a-13-point-selection-gap"
author: "Devanshu Biswas"
source: "devto_python"
published: "Sat, 29 Aug 2026 20:23:34 +0000"
description: "Measure a model on one dataset and you ask about accuracy. Measure it separately on two groups and a different question appears: which of the equalities you ..."
keywords: "gap, two, groups, not, score, cut, identical, selection"
generated: "2026-08-29T20:45:19.186769"
---

# Two Groups With Identical ROC Curves, Identical TPR and FPR to the Last Bit, and a 13-Point Selection Gap

## Overview

Measure a model on one dataset and you ask about accuracy. Measure it separately on two groups and a different question appears: which of the equalities you would like can hold at the same time? That turns out to be arithmetic , not policy — so this page computes instead of arguing. See it: https://dev48.infy.uk/ml/day74-group-fairness-impossibility.html The world is built so nothing is confounded The class-conditional score distribution is identical in both groups. The two ROC curves are the same curve; the AUC gap is exactly 0 . The decision is a function of the score bin alone, so fairness through unawareness already holds for free. The only difference between the groups is the base rate: 30% against 8% . At the payoff-optimal cut, both groups get true-positive rate 0.7759 and false-positive rate 0.1719 — to the last bit. And 35.31% of group A is flagged against 22.02% of group B. The gap is one product selection gap = (piA - piB) * J where J = TPR - FPR (Youden's J) = (0.30 - 0.08) * 0.6040 = 0.1329 exactly The whole disparity is a single product of two things you already knew: the prevalence gap and how good the score is. Nothing about the model is unfair; the arithmetic simply does not permit equal selection rates and equal error rates at once when base rates differ. The largest that gap can ever get is the total-variation distance between the two score laws — a bound, not an estimate. The Bayes cut that does not exist The closed-form optimal cut returns null exactly where the score is uninformative. That is not a gap in the code; it is the correct answer. There is no cut to find when the likelihood ratio is 1, and a verifier that assumes an index there crashes — which is precisely what happened when this page's verifier was written. Verified over 120 worlds , 1,439 asserts in exact rational arithmetic, 0 failures.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/two-groups-with-identical-roc-curves-identical-tpr-and-fpr-to-the-last-bit-and-a-13-point-7mb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
