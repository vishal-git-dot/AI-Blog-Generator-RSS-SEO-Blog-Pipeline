---
title: "Build Your First Scikit-learn Pipeline"
slug: "build-your-first-scikit-learn-pipeline"
author: "EricMWaimiri"
source: "devto_python"
published: "Mon, 31 Aug 2026 12:55:50 +0000"
description: "If you're new to scikit-learn, "Pipelines" can sound like an advanced topic to save for later. They're not. In this tutorial, we'll build one from scratch us..."
keywords: "pipeline, step, you, one, import, sklearn, titanic, columns"
generated: "2026-08-31T13:15:26.826168"
---

# Build Your First Scikit-learn Pipeline

## Overview

If you're new to scikit-learn, "Pipelines" can sound like an advanced topic to save for later. They're not. In this tutorial, we'll build one from scratch using the classic Titanic dataset, explaining every line along the way. By the end, you'll have a single object that cleans your data, encodes it, and makes predictions — all in one call. Step 1: Load the Data We'll use the Titanic dataset from seaborn, which comes bundled with the library. import seaborn as sns titanic = sns . load_dataset ( " titanic " ) titanic . head () We're trying to predict survived (0 or 1) using features like pclass , sex , age , and fare . features = [ " pclass " , " sex " , " age " , " fare " , " embarked " ] X = titanic [ features ] y = titanic [ " survived " ] Step 2: Split Before You Touch Anything Else This is the step beginners skip, and it's the most important one. Split your data before any cleaning or scaling. from sklearn.model_selection import train_test_split X_train , X_test , y_train , y_test = train_test_split ( X , y , test_size = 0.2 , random_state = 42 ) Why first? Because any preprocessing (like filling missing ages) should learn its parameters only from training data. If you clean the full dataset first, information from the test set leaks into training. Step 3: Look at What Needs Cleaning X_train . isnull (). sum () You'll see age has missing values, and embarked has a couple too. sex and embarked are text, not numbers — models can't use those directly. This is exactly what a pipeline will handle for us. Step 4: Build a Mini-Pipeline for Numeric Columns Numeric columns ( pclass , age , fare ) need two things: fill missing values, then scale them. from sklearn.pipeline import Pipeline from sklearn.impute import SimpleImputer from sklearn.preprocessing import StandardScaler numeric_features = [ " pclass " , " age " , " fare " ] numeric_pipeline = Pipeline ([ ( " imputer " , SimpleImputer ( strategy = " median " )), ( " scaler " , StandardScaler ()) ]) Read this like a recipe: "First impute, then scale." Each named step runs in order. Step 5: Build a Mini-Pipeline for Categorical Columns Text columns ( sex , embarked ) need missing values filled differently, then need to become numbers via one-hot encoding. from sklearn.preprocessing import OneHotEncoder categorical_features = [ " sex " , " embarked " ] categorical_pipeline = Pipeline ([ ( " imputer " , SimpleImputer ( strategy = " most_frequent " )), ( " onehot " , OneHotEncoder ( handle_unknown = " ignore " )) ]) handle_unknown="ignore" prevents errors if the test set ever contains a category the training set didn't have. Step 6: Combine Both with ColumnTransformer Now we tell scikit-learn which pipeline applies to which columns using ColumnTransformer . from sklearn.compose import ColumnTransformer preprocessor = ColumnTransformer ([ ( " num " , numeric_pipeline , numeric_features ), ( " cat " , categorical_pipeline , categorical_features ) ]) This single object now knows: numeric columns go through one path, categorical columns go through another. Step 7: Add a Model to Make the Full Pipeline Finally, we chain the preprocessor into a full pipeline with a classifier as the last step. from sklearn.ensemble import RandomForestClassifier full_pipeline = Pipeline ([ ( " preprocessing " , preprocessor ), ( " classifier " , RandomForestClassifier ( random_state = 42 )) ]) Step 8: Fit and Predict — One Call Each full_pipeline . fit ( X_train , y_train ) predictions = full_pipeline . predict ( X_test ) That's it. One .fit() call trains the imputers, the scaler, the encoder, and the model together. One .predict() call applies all of them to new data in the correct order. Step 9: Check the Score from sklearn.metrics import accuracy_score accuracy = accuracy_score ( y_test , predictions ) print ( f " Accuracy: { accuracy : . 2 f } " ) You should see something around 0.80–0.83 depending on the random split. Why This Matters Without a pipeline, you'd need to manually remember to: fill missing ages the same way on both train and test, scale using train-set statistics only, one-hot encode consistently, and apply all of it in the right order every single time you touch the data — including in production. The pipeline does all of this for you, automatically, and prevents the subtle bugs that come from doing it by hand. What's Next Once this feels comfortable, the natural next step is plugging this same full_pipeline into GridSearchCV to tune the RandomForestClassifier 's hyperparameters, or into cross_val_score for more reliable accuracy estimates — no changes needed to the pipeline itself.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ericmwaimiri/build-your-first-scikit-learn-pipeline-5gpi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
