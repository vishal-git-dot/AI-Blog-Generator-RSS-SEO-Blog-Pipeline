---
title: "SMOTE from scratch: fixing imbalanced data without just copy-pasting rows"
slug: "smote-from-scratch-fixing-imbalanced-data-without-just-copy-pasting-rows"
author: "Devanshu Biswas"
source: "devto_python"
published: "Mon, 13 Jul 2026 19:00:22 +0000"
description: "Train a fraud detector where 1% of transactions are fraud, and the lazy model that predicts "never fraud" scores 99% accuracy while catching zero criminals. ..."
keywords: "minority, smote, you, points, data, synthetic, rows, class"
generated: "2026-07-13T19:35:56.130827"
---

# SMOTE from scratch: fixing imbalanced data without just copy-pasting rows

## Overview

Train a fraud detector where 1% of transactions are fraud, and the lazy model that predicts "never fraud" scores 99% accuracy while catching zero criminals. That's the class-imbalance problem, and one of the most-used fixes is SMOTE — Synthetic Minority Over-sampling Technique. I built a 2-D visualiser for it, and the key idea is smaller than the acronym suggests. The naive fixes first Random over-sampling — duplicate minority rows until the classes are balanced. Problem: you're not adding information, just weight. The model sees the exact same rare points many times and overfits to them. Random under-sampling — throw away majority rows until balanced. Problem: you're deleting real data, often the most of it. SMOTE does something better: it invents new minority points that are plausible but not identical to the ones you have. The algorithm For each minority point: Find its k nearest neighbours among the minority class (typically k=5). Pick one of those neighbours at random. Create a new synthetic point somewhere on the straight line between the two: new = x + r · (neighbour − x) , where r is random in [0, 1]. Repeat until the minority class reaches the target size. Because each synthetic point is a convex combination of two real minority points, it lands inside the region the minority already occupies — filling it in, not duplicating corners. In the visualiser you can literally watch new points appear along the segments between existing ones, thickening the minority cloud, and see the decision boundary shift to give that class real estate it never had. The rules that actually matter Only resample the training split. If synthetic points leak into your test set — or if you SMOTE before the train/test split — you get data leakage and a score that lies. SMOTE happens inside the training fold, every fold. Don't judge with accuracy. Use precision, recall, F1, or the PR curve. Balancing the data is pointless if you then grade on the metric that imbalance already fooled. SMOTE can hurt. If minority and majority overlap heavily, interpolating across the boundary manufactures noisy, ambiguous points. That's why variants exist — Borderline-SMOTE (only near the boundary), ADASYN (more where it's hard), SMOTETomek (SMOTE + cleanup). What it teaches SMOTE is a great reminder that "more data" and "better data" aren't the same. Duplicating rows adds weight; interpolating adds coverage. The whole trick is one line of linear interpolation between a point and a neighbour — everything else is knowing when it helps and how to measure it. See synthetic points fill the minority region live, compare it to duplication and under-sampling, and watch the boundary move: https://dev48v.infy.uk/ml/day32-smote.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/smote-from-scratch-fixing-imbalanced-data-without-just-copy-pasting-rows-3bn2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
