---
title: "LIMIT 20 is not a sampling strategy"
slug: "limit-20-is-not-a-sampling-strategy"
author: "Mads Hansen"
source: "devto_ai"
published: "Sat, 15 Aug 2026 01:21:47 +0000"
description: "“Show me twenty examples” sounds harmless. The generated SQL adds LIMIT 20 without a stable order. The database returns whichever rows happen to arrive first..."
keywords: "sampling, limit, use, not, stable, sample, cases, examples"
generated: "2026-08-15T01:34:58.731741"
---

# LIMIT 20 is not a sampling strategy

## Overview

“Show me twenty examples” sounds harmless. The generated SQL adds LIMIT 20 without a stable order. The database returns whichever rows happen to arrive first. The assistant finds a pattern, and the team treats that pattern as evidence. But a row limit is not a sample design. Physical layout, indexes, query plans, parallel workers, recent inserts, and cache state can all change which rows appear. Before examples support a conclusion, define: the population and cutoff authorization scope the sampling method stable row identity seed and algorithm version strata and weights redaction what the sample cannot prove Use deterministic ordering for debugging. Use a stable hash sample for repeatable pseudo-random selection. Use stratification when important cohorts must be represented. Oversample rare cases deliberately—and disclose the bias. Most importantly, separate observation from inference. “7 of 20 sampled cases had a missing category” does not automatically mean “35% of all cases are missing a category.” Use an approved aggregate when prevalence matters. A sampling receipt should make the population, method, seed, version, limits, freshness, source coverage, and result checksum reviewable. LIMIT protects the system. A sampling contract protects the conclusion. Full guide: ChatGPT database queries need a deterministic sampling contract

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mads_hansen_27b33ebfee4c9/limit-20-is-not-a-sampling-strategy-1o04

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
