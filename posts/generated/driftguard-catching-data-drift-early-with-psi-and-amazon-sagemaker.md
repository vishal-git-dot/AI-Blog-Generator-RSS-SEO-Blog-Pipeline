---
title: "DriftGuard: Catching Data Drift Early with PSI and Amazon SageMaker"
slug: "driftguard-catching-data-drift-early-with-psi-and-amazon-sagemaker"
author: "rasi321"
source: "devto_python"
published: "Tue, 20 Oct 2026 11:01:10 +0000"
description: "A hands-on MLOps mini-project using Python, scikit-learn and the Population Stability Index A model that performs well on launch day can quietly get worse as..."
keywords: "data, drift, psi, model, production, not, baseline, expected"
generated: "2026-10-20T11:14:04.641605"
---

# DriftGuard: Catching Data Drift Early with PSI and Amazon SageMaker

## Overview

A hands-on MLOps mini-project using Python, scikit-learn and the Population Stability Index A model that performs well on launch day can quietly get worse as the real world changes. The inputs it sees in production slowly stop looking like the data it was trained on. This is called data drift , and it is one of the most common reasons deployed models fail. In this post I walk through DriftGuard , a small project I built in an AWS SageMaker. It trains a model, simulates shifted production data, and uses the Population Stability Index (PSI) to detect drift. The full code is on GitHub: https://github.com/RashiTiwari12/ What is data drift? When you train a model, it learns patterns from a specific data distribution. If the data it receives in production looks different (customers behave differently, a sensor changes, a new region is added), predictions can degrade even though the model itself has not changed. Monitoring for drift means comparing production data against a baseline , usually the training data. What is PSI? The Population Stability Index measures how much a variable's distribution has shifted between two samples. You split the baseline into bins, compare the share of data in each bin for the baseline and for new data, and combine the differences into a single score. A common rule of thumb: Below 0.10 : no significant change 0.10 to 0.20 : moderate shift, keep an eye on it 0.20 or higher : significant drift These thresholds are guidelines, not universal rules. The workflow Train model -> create baseline -> simulate shifted data -> calculate PSI -> save report -> optional S3 upload 1. Set up SageMaker. I created a notebook instance in us-east-1 , opened JupyterLab and used a conda_python3 notebook with scikit-learn, pandas, NumPy and boto3. 2. Train a model. I generated synthetic data with three features and trained a LinearRegression model, saving it with pickle . 3. Create the baseline and production data. The baseline is the training data. For production, I generated fresh data and deliberately shifted feature_1 upward. 4. Calculate PSI. I bin each feature using quantiles from the baseline, compare the proportions in the production data, and apply the PSI formula. A tiny epsilon value prevents division by zero when a bin is empty. def calculate_psi ( expected , actual , bins = 10 ): expected = np . asarray ( expected , dtype = float ) actual = np . asarray ( actual , dtype = float ) edges = np . unique ( np . quantile ( expected , np . linspace ( 0 , 1 , bins + 1 ))) edges [ 0 ], edges [ - 1 ] = - np . inf , np . inf e_pct = np . clip ( np . histogram ( expected , bins = edges )[ 0 ] / len ( expected ), 1e-6 , None ) a_pct = np . clip ( np . histogram ( actual , bins = edges )[ 0 ] / len ( actual ), 1e-6 , None ) return float ( np . sum (( a_pct - e_pct ) * np . log ( a_pct / e_pct ))) 5. Save the report. Results are written to a CSV, with an optional upload to Amazon S3 (my restricted lab role may block this, so the script handles failures gracefully). Results feature PSI status feature_1 8.1939 Drift detected feature_2 0.2051 Drift detected feature_3 0.0855 Below threshold The deliberately shifted feature_1 was flagged by a huge margin, exactly as expected. The interesting part is feature_2 . I did not shift it, yet it just crossed the 0.20 threshold. The cause is sample size: with only 100 rows, random variation alone can create a noticeable PSI. This taught me an important lesson: drift metrics need enough data to be trustworthy , and a single threshold should not be treated as absolute truth. In production I would use larger windows and combine PSI with other statistical tests. Limitations The model is a regression on synthetic data, not a real churn classifier. It only checks input drift, not concept drift or model accuracy. Small samples make PSI noisy. What I would do next Use a real churn dataset with a classifier Schedule monitoring with SageMaker Model Monitor Add KS-test or Jensen-Shannon distance alongside PSI Trigger alerts or retraining when drift is detected Key takeaways Models need monitoring after deployment, not just before. PSI is a simple, interpretable way to quantify distribution shift. Thresholds are guidelines, and sample size matters. You can build a useful drift check with plain Python before reaching for managed tooling. Built a PSI-based data drift detector on AWS SageMaker with Python and scikit-learn; documented the project on GitHub and Medium.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rasi321/driftguard-catching-data-drift-early-with-psi-and-amazon-sagemaker-4dnm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
