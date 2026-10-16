---
title: "1,285 strategy sleeves, frozen before the test: the year-by-year table is the warning"
slug: "1285-strategy-sleeves-frozen-before-the-test-the-year-by-year-table-is-the-warning"
author: "Arhan Canli"
source: "devto_python"
published: "Fri, 16 Oct 2026 10:59:46 +0000"
description: "Most backtest write-ups report one number for the whole test window. I want to show what happens when you split the same test by year. The protocol We built ..."
keywords: "test, costs, year, frozen, crypto, sleeves, two, search"
generated: "2026-10-16T11:05:26.344959"
---

# 1,285 strategy sleeves, frozen before the test: the year-by-year table is the warning

## Overview

Most backtest write-ups report one number for the whole test window. I want to show what happens when you split the same test by year. The protocol We built 1,285 small strategies ("sleeves") in two blocks: 1,026 stock sleeves: 27 signals, each run inside every industry with at least 10 names, long the best-ranked and short the worst. 259 crypto sleeves: cash-and-carry per coin, long spot and short the same coin's perpetual, switched on while funding pays. Everything was chosen on search years (stocks 1998 to 2017, crypto 2020 to 2022). The selection was written to a file, frozen_selection.json , and its SHA-256 ( 8d1803de7e04d3ee... ) was pushed before the test ran. Then the frozen list was tested once on years the search never saw. The headline Block Test years Sharpe after costs Before costs Worst drawdown Stocks, 1,026 sleeves 2018-01 to 2026-06 0.73 (t 2.12) 0.85 -14.8% Crypto, 259 coins 2023-01 to 2026-09 4.19 (t 8.03) 8.03 -6.1% Both at equal risk 2023-01 to 2026-06 3.42 (t 6.35) -17.2% The two blocks' correlation was 0.02. The stock block earned about half its search-year Sharpe (1.43), which is the usual decay. Read alone, the last row is the kind of number that gets posted. The same test, by year Year Stocks Crypto Both 2023 1.54 7.12 4.59 2024 2.13 11.99 8.05 2025 0.31 0.42 0.41 2026 to date -0.05 -3.01 -2.05 Since January 2025 the combined book's Sharpe is -0.44 (t -0.53, 366 days). The strong overall figure comes from 2023 and 2024. The crypto side shows why. The average daily funding collected while a position was on was 0.0449% in 2024, 0.0095% in 2025 and about zero in 2026 (-0.0003%). The carry lives on that income. With it gone, switching coins on and off around zero funding costs more than it earns: before costs the 2026 crypto Sharpe is +0.98, after costs -3.01. Two other things the search taught Costs do not diversify. Every sleeve's costs add up while its noise cancels. Holding overlapping portfolios and trading through a no-trade band cut the stock book's costs to about 1.2% a year (0.0118 in the result file). One bug, published. The first test run left out the frozen no-trade band (a runner bug). Its result (stocks 0.52, combined 3.16) is kept in the repo as test_result_run1_without_frozen_band.json . The corrected run applies the band the frozen file already named; nothing in the frozen file changed. What this does not show No sleeve is admitted to a live book. The forward record is the only clean test left, and the yearly table says the edge may be thinner now than the window average. A freeze and a single test protect you from fooling yourself during the search; they do not make the market keep paying. Try it The protocol, the frozen file and both result files are in the research/breadth-lab branch of github.com/arhancanli/alphac. The validation tools (deflated Sharpe, placebo tests) live in github.com/arhancanli/canlicapital, and canli-mcp is a free MCP server (MIT, no API key, runs locally): npx -y canli-mcp . How do you report a test window whose last two years disagree with the first two: the average, the split, or both? If this was useful to you, a star on the canlicapital repo is appreciated, and so is sending this to someone who'd use it. Written with AI assistance. Every number is from test_result.json and RESULTS.md in research/breadth_lab on the alphac repo (saved in drafts/data on 2026-10-16).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arhancanli/1285-strategy-sleeves-frozen-before-the-test-the-year-by-year-table-is-the-warning-2np4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
