---
title: "Three Things I Found When I Revisited My Gender Classification Project"
slug: "three-things-i-found-when-i-revisited-my-gender-classification-project"
author: "Ayush S Pangaonkar"
source: "devto_python"
published: "Sun, 11 Oct 2026 04:00:00 +0000"
description: "I went back to my Gender Classification project, a learning exercise on a small tabular dataset, and found three things worth writing down. (It is a classroo..."
keywords: "dataset, model, logistic, regression, decision, tree, found, project"
generated: "2026-10-11T05:08:30.393107"
---

# Three Things I Found When I Revisited My Gender Classification Project

## Overview

I went back to my Gender Classification project, a learning exercise on a small tabular dataset, and found three things worth writing down. (It is a classroom-style dataset of facial and physical measurements, not something I would build a real product on.) The setup The dataset, gender_classification.csv , has 5,001 rows. The features are long_hair , forehead_width_cm , forehead_height_cm , nose_wide , nose_long , lips_thin and distance_nose_to_lip_long . The target is Male or Female. My pipeline: drop duplicates, encode the target with LabelEncoder , scale with MinMaxScaler , split 80/20 ( random_state=42 ), then compare Logistic Regression, KNN (k=3) and a Decision Tree. 1. A third of the dataset was duplicates 1,768 of the 5,001 rows, about 35%, were duplicates. After dropping them, 3,233 rows remained. The class balance also moved, from an almost even 2,500 / 2,501 to 1,783 Male (55.1%) and 1,450 Female (44.9%). I now run duplicated().sum() before I trust any dataset's size or balance. 2. The simplest model generalized best Model Train acc Test acc Logistic Regression 95.1% 96.0% KNN (k=3) 97.0% 94.4% Decision Tree 99.8% 94.4% The Decision Tree has the biggest train/test gap (99.8% vs 94.4%), the same overfitting pattern from my admissions project. For Logistic Regression, precision and recall are balanced across both classes (F1 of 0.958 for Female, 0.962 for Male). 3. The feature I expected to matter did not Looking at the Logistic Regression coefficients on the scaled features: Feature Coefficient magnitude nose_wide 3.60 lips_thin 3.34 distance_nose_to_lip_long 3.28 nose_long 3.27 forehead_width_cm 2.18 forehead_height_cm 1.81 long_hair 0.07 I would have guessed hair length mattered most. Its coefficient is 0.07, next to nothing. The facial measurements carry the model. Two corrections to my old write-up My original README said the model used "age and height". Neither column exists in this dataset, and I rewrote it to list the real features. I also found a copy-paste bug where the Decision Tree's accuracy print statement shows the KNN variable. It only affects that printed line, not the final comparison. Takeaway Accuracy tells you a model works. The coefficients tell you why. Code: github.com/bluntjudg/Gender_Classification Series: Part 7 of 7 in my ML fundamentals revisit. That wraps up the seven basics. Next, I move on to the apps I deployed. Live projects I built after these basics: ATS Resume Analyzer , a Streamlit app that scores resumes against job descriptions AI-Based Loan Verification System , a Streamlit app for automated loan eligibility checks Subreach , a two-agent Reddit tool More of my work is on GitHub .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ayush_pangaonkar/three-things-i-found-when-i-revisited-my-gender-classification-project-13mb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
