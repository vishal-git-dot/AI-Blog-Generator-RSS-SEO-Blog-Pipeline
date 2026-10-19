---
title: "Accuracy Lied to Me: Precision, Recall, ROC AUC and Cross-Validation in ML Zoomcamp Module 4"
slug: "accuracy-lied-to-me-precision-recall-roc-auc-and-cross-validation-in-ml-zoomcamp-module-4"
author: "marcos-Nieves-24"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 21:48:59 +0000"
description: "In Module 3 I trained a lead-scoring classifier and reported 0.645 accuracy. It sounded fine. Module 4 of ML Zoomcamp exists to destroy exactly that feeling ..."
keywords: "auc, accuracy, module, model, you, homework, solver, random"
generated: "2026-10-19T22:10:53.098081"
---

# Accuracy Lied to Me: Precision, Recall, ROC AUC and Cross-Validation in ML Zoomcamp Module 4

## Overview

In Module 3 I trained a lead-scoring classifier and reported 0.645 accuracy. It sounded fine. Module 4 of ML Zoomcamp exists to destroy exactly that feeling — accuracy hides everything interesting when classes are imbalanced. Here is what I actually learned, with the numbers from my homework notebook. AUC as a feature-importance flashlight Before training anything, I scored every numerical column by using it raw as the prediction and computing ROC AUC against the target (negating it when AUC < 0.5, which just means negative correlation): annual_income: 0.608 number_of_courses_viewed: 0.723 interaction_count: 0.765 lead_score: 0.788 ← winner Two lessons. First, lead_score alone already separates the classes decently — good to know before blaming the model. Second, the trap: if you loop over all numeric columns naively you also score converted against itself and get a perfect 1.000. I had that bug. Exclude the target. The model: AUC 0.732, and why accuracy is not the story One-hot encoding with DictVectorizer (fit on train only), logistic regression with solver="liblinear", C=1.0, probabilities from predict_proba. Validation AUC: 0.732. AUC'sasts interpretation is my favourite thing in the module: it is the probability that a random positive outranks a random negative. My model ranks a random converter above a random non-converter 73% of the time. One number, no threshold chosen, immune to class balance. Accuracy can’t say any of that. The threshold tradeoff is real (plot it!) Sweeping thresholds 0.00–1.00 in 0.01 steps: precision climbs, recall falls, they cross at 0.63 (P≈0.733, R≈0.725). F1 peaks earlier, at 0.41 (F1≈0.758). The default 0.5 threshold is optimal for nothing — it is just the default. If missing a converter costs you more than a wasted email, you live left of 0.5; if spam costs more, right of it. The plot decides, not the default. Cross-validation: std is the point, and the solver is the trap 5-fold CV (KFold(n_splits=5, shuffle=True, random_state=1)), fresh vectorizer per fold, AUC per fold: 0.731, 0.730, 0.736, 0.741, 0.721. Mean ≈ 0.732, std 0.007. The std is the deliverable — it says how much I’d trust this number on new data. And here is the bug that would have failed the homework: the spec says solver="liblinear". Writing just LogisticRegression(max_iter=1000) silently uses lbfgs, which throws ConvergenceWarning on this data and lands on std 0.013 — a different multiple-choice option. Same data, same seed, wrong solver, wrong answer. Read the spec, copy the constructor exactly. Tuning C: regularization you can see Same 5-fold loop over C in [1e-06, 0.001, 1]:C=1e-06 → 0.617 ± 0.019 (regularization crushes the weights: underfit) C=0.001 → 0.749 ± 0.010 ← best C=1 → 0.732 ± 0.007 Tiny C is not “safer”, it is a model that barely learns. The sweep makes the bias-variance tradeoff visible instead of theoretical. Takeaway: 0.65 accuracy told me my Module 3 model “works”. Module 4 told me what it actually does: ranks decently (0.732), forces a precision/recall choice nobody made at 0.5, is stable across folds (±0.007), and tunes to C=0.001. I trust the second description. Don’t report accuracy alone again. Repo: https://github.com/marcos-Nieves-24/machine-learning-zoomcamp/blob/main/homework-4/homework-4.ipynb

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/marcosnieves24/accuracy-lied-to-me-precision-recall-roc-auc-and-cross-validation-in-ml-zoomcamp-module-4-47n6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
