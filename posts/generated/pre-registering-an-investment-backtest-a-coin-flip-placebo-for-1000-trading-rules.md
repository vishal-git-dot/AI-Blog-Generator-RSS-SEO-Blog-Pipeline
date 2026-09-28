---
title: "Pre-registering an investment backtest: a coin-flip placebo for 1,000 trading rules"
slug: "pre-registering-an-investment-backtest-a-coin-flip-placebo-for-1000-trading-rules"
author: "AI Portfolio Investing"
source: "devto_python"
published: "Mon, 28 Sep 2026 22:45:12 +0000"
description: "Backtests are cheap, and the one that looks good is the one that gets shown. The reader never learns how many candidates it was picked from. Here is an exper..."
keywords: "rules, trend, winner, coin, sharpe, flip, selection, period"
generated: "2026-09-28T23:06:03.072011"
---

# Pre-registering an investment backtest: a coin-flip placebo for 1,000 trading rules

## Overview

Backtests are cheap, and the one that looks good is the one that gets shown. The reader never learns how many candidates it was picked from. Here is an experiment built to measure that, and the process choices that keep it honest. 1. Pre-register the experiment and hash the spec Before any result was computed, the experiment's conditions (rules, periods, metrics, what counts as success) were written into a spec document, and a short hash of that document was recorded ( fe8de486fe2ec6be ). Change one character of the conditions and the hash changes, so the record shows the rules were not moved after the results came in. Corrections are logged too. This experiment was rerun twice: once to fix a division by zero, and once because monthly average prices had created a fake trend that flattered trend rules (switched to month-end prices and dividends, new hash). 2. Add a placebo arm Two families, 1,000 rules each, all switching between US stocks and a deposit: Trend rules: moving-average and momentum combinations. Coin-flip rules: the same shape, but in or out of stocks is decided by a coin. We know their true skill is zero. The coin-flip family plays the role of a placebo in a drug trial: it measures how good a rule can look purely because many were tried. The winner of each family is picked on 1980–2009 and then followed from 2010. US, selection period 1980–2009 Trend rules Coin-flip rules Winner's Sharpe 0.67 0.74 Median Sharpe 0.52 0.36 Rank correlation, selection vs. test 0.29 0.09 Probability of backtest overfitting (PBO) 62.9% 69.6% As a group the trend rules were better. But the placebo produced the more impressive winner. 3. Account for the number of trials The expected Sharpe of the top coin-flip rule rises with the number of rules tried, with no skill at all: Rules tried 1 10 100 1,000 Expected Sharpe of the top rule (US) 0.35 0.52 0.63 0.74 Buy and hold earned 0.42 over the same period. So "Sharpe 0.7" means nothing until you know how many rules it was chosen from. This curve is the yardstick. The PBO row is a second check that needs no hold-out: cut the selection period into 16 pieces, pick the winner on half, check it on the other half, over 2,000 splits. The US trend winner fell below the middle 62.9% of the time. 4. Publish the failures After 2010, only 6 of the 1,000 US trend rules beat buy and hold (0.6%), down from 70.6% in the selection period. The trend winner earned a test-period Sharpe of 0.63 against buy and hold's 0.90. In Korea the trend rules as a group did beat buy and hold after 2016, but the selection winner (0.44) still fell short of it (0.50). Both results are reported as they came out. 5. Make it reproducible Rule definitions, periods (US 1980–2009 → 2010–2026, Korea 2000–2015 → 2016–2026), metrics, spec hashes and the correction log are all in the book. Source: Chapter 3 of Invest Only What the Evidence Supports (AI Portfolio Investing, Book 2), https://www.amazon.com/dp/B0HKRVB4FX . The free research sites: https://aiportfolioinvesting.com/?src=devto and https://airetirementinvesting.com/en/?src=devto General research and education, not investment advice. All figures are hypothetical results computed on past data.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aiportinvest/pre-registering-an-investment-backtest-a-coin-flip-placebo-for-1000-trading-rules-246j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
