---
title: "Does the month you start predict whether you keep a habit? 1.1M piano learners say yes"
slug: "does-the-month-you-start-predict-whether-you-keep-a-habit-11m-piano-learners-say-yes"
author: "Maria-Luise Volkmar"
source: "devto_python"
published: "Thu, 02 Jul 2026 19:05:51 +0000"
description: "Every January, a wave of people decide this is the year they finally learn something. New gym membership, new language app, new instrument. And every Februar..."
keywords: "month, resolution, you, spring, january, new, retention, dataset"
generated: "2026-07-02T19:40:41.064336"
---

# Does the month you start predict whether you keep a habit? 1.1M piano learners say yes

## Overview

Every January, a wave of people decide this is the year they finally learn something. New gym membership, new language app, new instrument. And every February, most of them quit. I wanted to test a narrower version of that folk wisdom with real data: does the calendar month you start a habit actually predict whether you are still doing it six months later? Not "do resolutions fail" (they do), but "is the resolution window itself a bad time to start"? There is a clean dataset for this. Skoove, an online piano-learning platform, tracked six-month retention by signup month across 1,137,446 learners from 2021 to 2024. The dataset is open on GitHub, so you can reproduce every number below. The headline figure Here is the finding in one sentence: the December-to-January resolution window, which pulls in roughly a quarter of all signups, has the worst six-month retention of any part of the year. People who start in spring stick with it far more. The dataset expresses each quantified month as a percentage difference from the average learner's six-month retention: start_month six_month_retention_vs_average_pct December -28 January -21 April +18 June +18 May +23 Load it yourself The dataset is a plain CSV on GitHub. No key, no download, pandas reads the raw URL directly: import pandas as pd url = ( " https://raw.githubusercontent.com/DatapulseResearch/ " " new-year-resolution-retention/main/data/retention_by_start_month.csv " ) df = pd . read_csv ( url ) # Sort worst-to-best on six-month retention vs the average learner ranked = df . sort_values ( " six_month_retention_vs_average_pct " ) print ( ranked [[ " start_month " , " six_month_retention_vs_average_pct " ]]) Sorting worst-to-best puts the story on one screen: start_month six_month_retention_vs_average_pct December -28 January -21 April 18 June 18 May 23 The two months sitting at the bottom are exactly the two months of the resolution season. The top of the table is spring. The counterintuitive part The intuitive model is that motivation is highest in January (fresh start, clean slate, public commitment), so January starters should do at least average. The data says the opposite: the most popular time to begin is one of the worst times to persist. A quick way to see the gap between "when people start" and "when starting works": resolution_window = df [ df [ " start_month " ]. isin ([ " December " , " January " ])] spring_window = df [ df [ " start_month " ]. isin ([ " April " , " May " , " June " ])] print ( " resolution window avg: " , round ( resolution_window [ " six_month_retention_vs_average_pct " ]. mean (), 1 )) print ( " spring window avg: " , round ( spring_window [ " six_month_retention_vs_average_pct " ]. mean (), 1 )) resolution window avg: -24.5 spring window avg: 19.7 That is a roughly 44 percentage-point swing in six-month retention between starting on a New Year's resolution and starting in spring. Same platform, same lessons, same learners, different month. Why might spring win? The dataset does not encode causes, so I will not overclaim. But two hypotheses are worth stating and testing elsewhere: resolution-season starters are often driven by a calendar deadline rather than genuine interest, and spring starters may self-select as people who decided to learn piano for its own reasons, on their own timing, with no crowd and no January pressure. An honest note on coverage The dataset only contains the months the underlying study actually quantified. February, March, and July through November are not in the CSV, and I have not invented values for them. Two of the figures are range bounds rather than point estimates: the study reported the spring lift as a "+18 to +23%" band, so April and June are entered at +18, the lower bound (the true spring effect is at least that large). December (-28), January (-21) and May (+23) are stated exactly. So the correct claim is narrow and defensible: among the months that were measured, the resolution window is the worst and spring is the best. It is not a claim about the eight months no one measured. Data and method Dataset (CC BY 4.0): new-year-resolution-retention on GitHub . The repo also ships a second CSV, resolution_stats_by_country.csv , with resolution-abandonment metrics by country and source. Sample: 1,137,446 Skoove piano learners, 2021 to 2024, six-month retention tracked by signup month. Source study: New Year's Resolution Retention (Skoove, 2021-2024) . Reproducibility: every number above comes straight from the raw CSV loaded in the snippets; run them and you will get the same output. Close If you are shipping a habit-formation feature, a learning product, or just your own side project, the "New Year, New You" spike is a tempting moment to launch into. This dataset is a small reminder that the crowded start line is not the same as the finish line. If you re-run the numbers or slice the country CSV differently, I would love to see what you find in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mlvolkmar/does-the-month-you-start-predict-whether-you-keep-a-habit-11m-piano-learners-say-yes-4970

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
