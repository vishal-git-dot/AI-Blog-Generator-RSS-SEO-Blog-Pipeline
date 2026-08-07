---
title: "I Built a Free 0/1 Knapsack Solver API (with a New Heuristic)"
slug: "i-built-a-free-01-knapsack-solver-api-with-a-new-heuristic"
author: "1111001001111"
source: "devto_python"
published: "Fri, 07 Aug 2026 06:48:27 +0000"
description: "Hi everyone 👋 Over the past few months I’ve been working on a small optimization engine for the classic 0/1 Knapsack Problem . It’s now live and completely f..."
keywords: "auto, api, free, knapsack, requests, per, new, heuristic"
generated: "2026-08-07T07:23:56.534521"
---

# I Built a Free 0/1 Knapsack Solver API (with a New Heuristic)

## Overview

Hi everyone 👋 Over the past few months I’ve been working on a small optimization engine for the classic 0/1 Knapsack Problem . It’s now live and completely free to use. You can try it here: https://psi-knapsack-api.onrender.com/solve What it supports The API has three modes: exact → classic dynamic programming fast → a new heuristic I developed auto → automatically chooses between them based on estimated runtime and the time budget you provide Quick Python example import requests url = " https://psi-knapsack-api.onrender.com/solve " payload = { " capacity " : 50 , " items " : [ { " id " : " laptop " , " weight " : 10 , " value " : 60 }, { " id " : " book " , " weight " : 20 , " value " : 100 }, { " id " : " camera " , " weight " : 30 , " value " : 120 } ], " mode " : " auto " , # "auto", "fast" or "exact" " time_budget_sec " : 5.0 } response = requests . post ( url , json = payload ) print ( response . json ()) Example response: { "selected_ids" : [ "camera" , "book" ], "metrics" : { "total_value" : 220 , "total_weight" : 50 , "latency_ms" : 1.24 , "fractional_bound_gap" : 0.0 }, "decision" : { "candidate_chosen" : "dp" , "mode_requested" : "auto" , "time_budget_sec" : 5.0 }, "reason" : "AUTO selected DP due to low ETA (0.0001s ± 0.0s)." } Limits Max items per request: 20,000 Rate limit: 20 requests per minute per IP Time budget: 0.1s – 30s per request Note: It’s running on a free-tier instance on Render, so the first request may take ~30 seconds (cold start). Subsequent requests respond in milliseconds. I’d love to hear any feedback, especially about: The quality of the new heuristic Whether the auto mode makes good decisions The overall API design Feel free to test it with your own instances and let me know what you think! Thanks for reading 🙌

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/1111001001111/i-built-a-free-01-knapsack-solver-api-with-a-new-heuristic-124a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
