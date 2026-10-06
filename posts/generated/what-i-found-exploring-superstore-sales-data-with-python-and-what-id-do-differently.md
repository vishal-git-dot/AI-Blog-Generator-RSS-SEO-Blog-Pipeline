---
title: "What I Found Exploring Superstore Sales Data with Python (and What I'd Do Differently)"
slug: "what-i-found-exploring-superstore-sales-data-with-python-and-what-id-do-differently"
author: "Vishal Prajapati"
source: "devto_python"
published: "Tue, 06 Oct 2026 05:24:47 +0000"
description: "I recently finished an exploratory data analysis (EDA) project on the Superstore sales dataset as part of the Nexgen Analytics Internship. The brief: load th..."
keywords: "profit, sales, data, what, outliers, date, category, plt"
generated: "2026-10-06T05:48:43.496673"
---

# What I Found Exploring Superstore Sales Data with Python (and What I'd Do Differently)

## Overview

I recently finished an exploratory data analysis (EDA) project on the Superstore sales dataset as part of the Nexgen Analytics Internship. The brief: load the data, clean it, visualize it, and detect outliers using Pandas, Matplotlib, and Seaborn. Here's how I approached it, what stood out, and what I'd change next time. Full code: superstore-eda-python on GitHub The dataset Superstore is a popular practice dataset of retail orders. Each row is an order line with sales, quantity, discount, profit, product category, customer segment, region, and ship mode. It's realistic enough to be interesting and small enough to explore on a laptop. Step 1: Loading and a first look Before any charts, I wanted to know what I was dealing with: size, column types, and obvious gaps. import pandas as pd df = pd . read_csv ( " superstore.csv " ) print ( df . shape ) df . info () print ( df . describe ()) info() and describe() are the fastest way to catch problems early. I checked that numeric columns like Sales and Profit were actually numeric, and that the date columns were not. Step 2: Cleaning Cleaning was mostly about making the data trustworthy before analyzing it: Checked for missing values and duplicate rows Converted Order Date and Ship Date from strings to datetime Standardized column names so they were easier to work with in code print ( df . isnull (). sum ()) print ( df . duplicated (). sum ()) df = df . drop_duplicates () df [ " Order Date " ] = pd . to_datetime ( df [ " Order Date " ]) df [ " Ship Date " ] = pd . to_datetime ( df [ " Ship Date " ]) df . columns = df . columns . str . strip (). str . replace ( " " , " _ " ) Converting the dates early paid off later, because it made time-based grouping and plotting straightforward. Step 3: Visualizing the data I used Matplotlib and Seaborn to answer a few basic business questions: which categories sell most, which regions perform best, and how sales and profit are distributed. import seaborn as sns import matplotlib.pyplot as plt sns . barplot ( data = df , x = " Category " , y = " Sales " , estimator = sum , errorbar = None ) plt . title ( " Total Sales by Category " ) plt . show () sns . barplot ( data = df , x = " Region " , y = " Profit " , estimator = sum , errorbar = None ) plt . title ( " Total Profit by Region " ) plt . show () What I noticed: ✅ Technology and Office Supplies tend to carry the business, and Technology usually leads on profit. ✅ Regional performance isn't even. Some regions generate similar sales but noticeably different profit. Sales and profit are not the same story. A category or region can look strong on revenue and weak on margin, which is why I plotted both. Step 4: Detecting outliers Sales and profit are heavily skewed, so I used the IQR method and box plots to flag extreme values. Q1 = df [ " Profit " ]. quantile ( 0.25 ) Q3 = df [ " Profit " ]. quantile ( 0.75 ) IQR = Q3 - Q1 lower = Q1 - 1.5 * IQR upper = Q3 + 1.5 * IQR outliers = df [( df [ " Profit " ] < lower ) | ( df [ " Profit " ] > upper )] print ( f " { len ( outliers ) } outlier rows " ) sns . boxplot ( data = df , x = " Profit " ) plt . show () ✅ The outliers turned out to be real orders rather than data errors. Many of the big losses were heavily discounted orders, and many of the big profits were large technology purchases. That changed how I treated them: removing them would have hidden the most interesting part of the data. What I'd do differently Look at discounts earlier. Discount level seems closely tied to the worst-profit orders, and I'd analyze that relationship directly rather than only noticing it in the outliers. Go beyond category level. Sub-category analysis would show which specific products drag margins down. Add a time-series view. Monthly sales and profit trends would show seasonality that totals hide. Build a dashboard. The same questions would work well as an interactive Power BI or Tableau report for non-technical users. Wrapping up The biggest lesson was that EDA is less about producing charts and more about asking whether the data can be trusted and what each pattern actually means. Handling outliers thoughtfully mattered more than any single plot. If you've worked with this dataset, I'd love to hear what you found, and feedback on the code is very welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vpraja92/what-i-found-exploring-superstore-sales-data-with-python-and-what-id-do-differently-43e2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
