---
title: "A 15-line Python check for credit-based AI pricing: plan credits, top-ups and rollover"
slug: "a-15-line-python-check-for-credit-based-ai-pricing-plan-credits-top-ups-and-rollover"
author: "FIRAT"
source: "devto_python"
published: "Thu, 26 Nov 2026 07:40:51 +0000"
description: "Most AI tools now bill in credits. The pricing page shows a monthly fee, but three other numbers decide what you really pay: the cost of one plan credit, the..."
keywords: "credits, plan, top, price, you, credit, cost, basic"
generated: "2026-11-26T07:44:38.393721"
---

# A 15-line Python check for credit-based AI pricing: plan credits, top-ups and rollover

## Overview

Most AI tools now bill in credits. The pricing page shows a monthly fee, but three other numbers decide what you really pay: the cost of one plan credit, the cost of a top-up credit, and what happens to credits you do not use. Here is a small script that turns a pricing table into those numbers, with one live example. The example AI Flow Chat is a no-code canvas for AI content workflows. Its prices, read on aiflowchat.com on 26 November 2026 (USD, monthly billing): Plan Price Credits Rollover Top-up Basic $29 8,000 none listed $6 per 1,000 Scale $59 18,000 50% $6 per 1,000 Pro $119 40,000 100% $6 per 2,000 The script plans = { "Basic" : dict ( price = 29 , credits = 8_000 , topup_usd = 6 , topup_credits = 1_000 ) , "Scale" : dict ( price = 59 , credits = 18_000 , topup_usd = 6 , topup_credits = 1_000 ) , "Pro" : dict ( price = 119 , credits = 40_000 , topup_usd = 6 , topup_credits = 2_000 ) , } def per_1k ( usd , credits ) : return usd / credits * 1_000 for name , p in plans . items ( ) : plan_rate = per_1k ( p [ "price" ] , p [ "credits" ] ) topup_rate = per_1k ( p [ "topup_usd" ] , p [ "topup_credits" ] ) print ( f "{name:6} plan ${plan_rate:.2f}/1k top-up ${topup_rate:.2f}/1k " f "top-up premium {topup_rate / plan_rate - 1:+.0%}" ) def effective_rate ( price , used ) : """Cost per 1,000 credits you actually used in a month with no rollover.""" return per_1k ( price , used ) print ( f "Basic at half usage: ${effective_rate(29, 4_000):.2f}/1k" ) Output: Basic plan $3.62/1k top-up $6.00/1k top-up premium +66% Scale plan $3.28/1k top-up $6.00/1k top-up premium +83% Pro plan $2.98/1k top-up $3.00/1k top-up premium +1% Basic at half usage: $7.25/1k What the numbers say The plan discount is small. The largest plan is about 18% cheaper per credit than the smallest. On its own that rarely justifies a jump of two tiers. Top-ups are where the price doubles. On the two smaller plans a top-up credit costs 66% to 83% more than a plan credit. Five top-ups on Basic cost $30 for 5,000 credits; moving up one plan costs $30 and adds 10,000. Unused credits are the hidden cost. Use half of a plan with no rollover and your real rate doubles. If your workload comes in bursts, a plan that carries credits over can beat a cheaper plan that resets to zero. Use it on any tool Replace the dictionary with the plans of the tool you are comparing. Then answer three questions before you pay: How many credits does one unit of your real work cost? Measure it in the trial. Do unused credits expire at the end of the month? What is the top-up rate next to the plan rate? We keep dated price readings for a few hundred AI and SaaS tools as an open CSV, if you want more tables to run this on: https://kuponaut.com/ai-tool-pricing-statistics/ Disclosure: Kuponaut is an AI Flow Chat affiliate partner and may earn a commission if you buy through our site. Prices were read on the company's own page on 26 November 2026. This post was drafted with AI assistance and the arithmetic was checked by running the script.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kuponau/a-15-line-python-check-for-credit-based-ai-pricing-plan-credits-top-ups-and-rollover-2jdg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
