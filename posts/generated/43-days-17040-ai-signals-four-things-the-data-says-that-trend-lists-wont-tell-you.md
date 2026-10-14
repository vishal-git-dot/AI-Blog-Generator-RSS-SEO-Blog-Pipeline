---
title: "43 days, 17,040 AI signals: four things the data says that trend lists won't tell you"
slug: "43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you"
author: "John"
source: "devto_python"
published: "Wed, 14 Oct 2026 04:00:07 +0000"
description: "I've been running a small pipeline that collects AI signals from public sources for 43 days now — 17,040 items, ~398 a day. I built it to power a daily diges..."
keywords: "you, one, api, day, than, top, json, not"
generated: "2026-10-14T04:22:01.693882"
---

# 43 days, 17,040 AI signals: four things the data says that trend lists won't tell you

## Overview

I've been running a small pipeline that collects AI signals from public sources for 43 days now — 17,040 items, ~398 a day. I built it to power a daily digest, but the dataset turned out to be more interesting than the digest, mostly because of what it can't tell me. Here are the four findings I'd want to know before building anything on top of AI trend data. 1. Only 23 of 1,493 tracked models have enough history to compute a trend This is the big one. My collector snapshots trending lists — GitHub trending, Hugging Face trending, and so on. Those lists rotate. A model that's #4 today may be gone tomorrow, taking its history with it. The result: tracked ranked with ≥20 days of history Hugging Face models 1,493 228 23 GitHub repos 63 63 14 So when a tool shows you "momentum" for an AI model, ask what its baseline is. If the entity was only observed twice, a "trend" is two points and a straight line. I chose to publish unranked with the reason rather than fill the gap with something plausible — every row in my JSON either has a derivable number or an explicit "not ranked, here's why". That decision cost me a lot of "wow" numbers. It's still the right one: an invented rank is indistinguishable from a real one to whatever consumes it downstream. The fix, if you're building this yourself: track a fixed set (top N by a stable metric, every day) in addition to the rotating trending lists. Rotation gives you discovery; a fixed set gives you a time series. Without the second one you have neither. 2. Top entities are boringly stable — the interesting signal is churn I expected the leaders to move. Over 48 days of daily snapshots: Biggest Hugging Face download change: −11.7% ( moonshotai/Kimi-K3 ) Biggest increase in the same column: +7.6% ( deepseek-ai/DeepSeek-R1 ) Everything else in the top 8: −5% to −10% GitHub stars, top repos: +0.08% to +0.54% over 48 days So the leaderboard is nearly static, and most large models slowly decay in downloads. Growth is the exception, not the norm. Meanwhile, a single day's deltas (2026-10-12 → 2026-10-13) looked like this: 2 models entered, 41 were not seen again, 201 changed rank. That's where the motion is — at the edges, not the top. If you're building alerts, alert on entry and exit , not on rank movement at the top. "This model appeared for the first time / this one vanished" carried far more information than "+3 places". 3. Most of the volume is one source, and it isn't the interesting one Over 43 days, by source: source items share hot-topic aggregation 6,455 38% arXiv 2,551 15% Hugging Face 2,107 12% arena boards 2,041 12% silicon-valley news 1,198 7% hardware/chips 1,089 6% GitHub 860 5% YouTube 739 4% The aggregation source alone is more than a third of everything. It's cheap to collect and it mostly duplicates what you already have from the primary sources. The four sources that actually produce the digest (GitHub, Hugging Face, YouTube, Silicon Valley news) are 29% of the volume . If you rank sources by item count, you'll optimize for the loudest one instead of the useful one. I ended up tracking per-source yield and dedup rate , not raw volume — volume is the metric that makes a pipeline look productive while producing nothing. 4. Derive numbers from raw snapshots, or don't publish them Every derived number I publish (rank, rank change, 7-day momentum, position in an arXiv category) is recomputed from raw snapshots by an automated audit, and the audit also reconciles the rendered pages against the JSON endpoints. If the two disagree, that's a failure, not a rounding difference. Two reasons this matters more than it sounds: Derived numbers drift silently. A rank computed at write time and stored is a claim from the past; recomputed, it's a claim you can defend. It catches your own bugs. The audit has caught things like a "content quality" check passing on pages whose body was actually empty, and mismatch between a daily edition and the API response for the same date. I'd rather ship a boring number I can re-derive than an exciting one I can't. What I'm doing with this The pipeline is unattended (collects 4×/day, one published edition/day, self-audited daily). The data is public and free: Daily dataset (CC BY 4.0): github.com/jiangzhangcc-glitch/ai-signals-daily — plus a bulk signals.jsonl (all 17,040 rows) on the releases page Today's signals as JSON: https://data.jiangzhang.ca/signals4/api/today.json What changed since the previous snapshot: .../api/changes.json Ranked models/repos with citations: .../api/models.json , .../api/repos.json As MCP tools for Claude/Cursor: signals-api-mcp One gotcha worth passing on: if you call the API with a bare Python-urllib User-Agent (or none), you'll get a 403 from the CDN, at the edge — your request never reaches the server, and the server's logs show nothing. It looks exactly like an API that's down. requests , httpx , aiohttp , Go, node-fetch, axios and curl are all fine. Set a User-Agent in examples. If you need more than the free tier — 8 sources instead of 4, four updates a day, and full history behind a stable key — that's the paid feed: what it includes . And if you're building something similar: I'd genuinely like to know how you handle the rotating-list problem. It's the part I underestimated most.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/signals_api/43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you-5edd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
