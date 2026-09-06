---
title: "Using Scikit-learn Pipelines. A Titanic Walkthrough"
slug: "using-scikit-learn-pipelines-a-titanic-walkthrough"
author: "Kevin Ng'ang'a"
source: "devto_python"
published: "Sun, 06 Sep 2026 10:04:11 +0000"
description: "Introduction When you build a machine learning model, you rarely feed it raw data straight away. You usually clean it first by filling in missing values, sca..."
keywords: "one, model, pipeline, each, pipelines, you, data, every"
generated: "2026-09-06T10:39:35.963888"
---

# Using Scikit-learn Pipelines. A Titanic Walkthrough

## Overview

Introduction When you build a machine learning model, you rarely feed it raw data straight away. You usually clean it first by filling in missing values, scaling numbers, and turning categories into a format the model can use. If you do each of these steps by hand, it's easy to forget one, or to accidentally let information from your test data influence how you clean your training data. A pipeline in scikit-learn fixes this by chaining all the cleaning steps and the model together into a single object. You call .fit() once, and every step runs in the correct order automatically, every time. In this article, we will use the Titanic dataset dataset from Kaggle. It lists real passengers from the Titanic, along with details like their age, sex, ticket class, and fare, and the goal is to predict who survived. We will walk through a real pipeline built for that dataset, one step at a time, in the order it actually runs. 1. Imports This brings in the pipeline tools ( Pipeline , ColumnTransformer ), the cleaning tools ( SimpleImputer , StandardScaler , OneHotEncoder ), and the models that we will use later, like logistic regression, random forest, and SVM. None of these lines run any code by themselves, they just make the tools available for the steps that follow. 2. Two Small Pipelines, One per Column Type Titanic data has numeric columns (Age, Fare) and categorical columns (Sex, Embarked). Each one needs different treatment, so we create two small pipelines: numerical_pipeline fills missing numbers with the median (the middle value once sorted), then scales everything so no column dominates just because its numbers happen to be bigger. Median is used instead of average here because a few very old or very young passengers wouldn't be able to skew it, or in simpler terms, outliers. categorical_pipeline fills missing categories with the most common value , then one-hot encodes them, turning each category into its own 0/1 column. For example, "Sex" becomes two columns, "is_male" and "is_female", each holding a 0 or a 1. Each of these is already a small pipeline on its own. What I have learnt working with these pipelines, is that building small, focused pipelines like this first, then combining them, is a pattern worth reusing on other datasets too. 3. Combine Both with ColumnTransformer ColumnTransformer points each small pipeline at the right columns. It sends numeric columns through numerical_pipeline and categorical columns through categorical_pipeline . The result, preprocessor , handles the whole dataset correctly in one call, so every column gets the treatment it actually needs instead of one-size-fits-all cleaning. 4. Compare Models with Cross-Validation The block of code above first sets up StratifiedKFold(n_splits=5, shuffle=True, random_state=42) , which splits the training data into 5 parts while keeping the survived/died ratio balanced in every part, and this is important here, since more passengers died than survived, and an unbalanced split could make a model look better or worse than it really is. The loop then builds a fresh pipeline for each model, chaining preprocessor → model . That way every model gets its own correctly-run preprocessing, instead of sharing an already-fitted copy that might carry information it shouldn't have. cross_val_score(..., scoring="f1") trains and tests each pipeline 5 times, once per fold, scoring with F1 which is a measure that balances catching real survivors against false "survived" predictions. It is often preferred over plain accuracy when one outcome is more common than the other, as is the case here. The mean and standard deviation of those 5 scores get saved per model. The mean shows average performance, and the standard deviation shows how much it swung between folds. In this regard, a model with a high mean and low standard deviation is both strong and reliable. 5. Reading the Results svm came out on top overall, reaching as high as 0.785 on one fold. random_forest and gradient_boosting followed close behind. kneighbours scored lower and bounced around more between folds, which means it was less consistent, not just weaker on average. Looking at all 5 scores per model, rather than just one number, makes it possible to judge both how well a model performs and how much you can trust that performance to hold up on new data. Pattern Worth Noticing Every model reuses the same preprocessor , but a fresh pipeline gets built for each one, refit from scratch inside every fold. If preprocessor had been fitted once outside the loop and reused everywhere, information could leak from test folds into training which is the exact problem pipelines exist to prevent. Conclusion Across all five steps, the same idea keeps showing up, and this to build small pieces, combine them, and always test through the whole combined pipeline rather than one part in isolation. Two small pipelines handled the numeric and categorical columns separately. ColumnTransformer merged them into one preprocessor. A fresh full pipeline was built per model, and StratifiedKFold with cross_val_score tested each one fairly, five times over, without leaking data between folds. That combination is what made it possible to compare six very different models on equal footing, and to trust that the winning score was not just luck.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/olesuyaye/using-scikit-learn-pipelines-a-titanic-walkthrough-5g98

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
