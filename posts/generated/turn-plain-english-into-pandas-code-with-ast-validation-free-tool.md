---
title: "Turn plain English into pandas code — with AST validation (free tool)"
slug: "turn-plain-english-into-pandas-code-with-ast-validation-free-tool"
author: "473185670"
source: "devto_python"
published: "Mon, 17 Aug 2026 00:41:33 +0000"
description: "If you use pandas daily, you have probably burned minutes hunting for the right syntax. .agg() takes a dict or a list? .rolling() then .mean() — what is the ..."
keywords: "you, pandas, code, not, syntax, what, data, english"
generated: "2026-08-17T01:39:21.437534"
---

# Turn plain English into pandas code — with AST validation (free tool)

## Overview

If you use pandas daily, you have probably burned minutes hunting for the right syntax. .agg() takes a dict or a list? .rolling() then .mean() — what is the window arg called? I built a tool: describe what you want in English, get syntax-validated pandas code back. Example Input: Group sales by month , calculate total revenue and average order size Output: df [ ' month ' ] = df [ ' date ' ]. dt . to_period ( ' M ' ) result = df . groupby ( ' month ' ). agg ( total_revenue = ( ' revenue ' , ' sum ' ), avg_order_size = ( ' order_size ' , ' mean ' ) ). reset_index () Note it auto-handled the datetime conversion — easy to miss on first write, then 10 minutes of debugging. How it works Three pieces, no black magic: Few-shot examples (22 curated patterns): groupby+agg, merge/join, datetime, string ops, missing values, pivot, viz, binning, filtering, chaining. Not a generic LLM wrapper — tuned for pandas. Schema-aware : upload a CSV or describe columns, and it knows df['date'] is datetime, df['user_id'] is string. No placeholder columns. AST validation : runs ast.parse() before returning. If the model hallucinates a nonexistent method, the validator flags it. You never get syntax-broken code — and it scans for dangerous ops ( eval , exec , subprocess , os.remove ). More examples 7-day rolling average: df [ ' rolling_avg ' ] = df [ ' close ' ]. rolling ( window = 7 ). mean () Quartile bins: df [ ' income_quartile ' ] = pd . qcut ( df [ ' income ' ], q = 4 , labels = [ ' Q1 ' , ' Q2 ' , ' Q3 ' , ' Q4 ' ]) Correlation heatmap: import seaborn as sns sns . heatmap ( df . corr ( numeric_only = True ), annot = True , cmap = ' coolwarm ' ) What it is not Not a black-box analyst. It generates code; you read and verify it. It does not know your data. 'revenue' in cents or yuan? null = N/A or zero? Domain knowledge stays yours. Not for 10-step exploratory pipelines (yet). 2-3 step combos work well. Honest value prop: saves the 20-30% of time spent on syntax lookup, so you spend it on the 70-80% that matters — understanding your data and reading results. Try it Free tier: 5 queries/day per IP, no signup. → PandasAI demo Type a data operation in English, get validated pandas code. If you hit a pattern it handles well (or badly), tell me in the comments — the edge cases on messy real-world data are what I care about most.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/473185670/turn-plain-english-into-pandas-code-with-ast-validation-free-tool-46el

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
