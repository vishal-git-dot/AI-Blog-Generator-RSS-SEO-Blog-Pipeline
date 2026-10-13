---
title: "Show HN: Parsimony – an open-source benchmark for how much code AI models add"
slug: "show-hn-parsimony-an-open-source-benchmark-for-how-much-code-ai-models-add"
author: "lasu"
source: "hackernews"
published: "Tue, 13 Oct 2026 19:50:31 +0000"
description: "Existing benchmarks measure solve rate and token output/cost, but don't punish excess code, which makes a codebase harder to work with in the long term. I wa..."
keywords: "code, benchmarks, parsimony, models, measure, long, term, patches"
generated: "2026-10-13T22:28:13.078074"
---

# Show HN: Parsimony – an open-source benchmark for how much code AI models add

## Overview

Existing benchmarks measure solve rate and token output/cost, but don't punish excess code, which makes a codebase harder to work with in the long term. I wanted to measure this since it matters most for long-term projects. Method: it takes the patches that benchmarks already publish (DeepSWE, SWE-bench Verified, SWE-bench Live) and counts "coding units": syntax elements like statements, calls, names and literals. I didn't use lines of code, so cramming code isn't rewarded. Deleted code is subtracted, so it measures net units. GPT-6 and Claude 5.5 have no public patches yet, so I ran them myself on 3–10 tasks on my own subscriptions (shown as faded circles, not ranked). Any feedback or model contributions are welcome, especially public patch exports for newer models. GitHub: https://github.com/La5u/Parsimony Not affiliated with any of the benchmarks. Comments URL: https://news.ycombinator.com/item?id=50077619 Points: 19 # Comments: 1

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://parsimony.lasu.dev/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
