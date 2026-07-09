---
title: "Build a CDR Usage Analytics Dashboard in Python"
slug: "build-a-cdr-usage-analytics-dashboard-in-python"
author: "Sonam"
source: "devto_python"
published: "Thu, 09 Jul 2026 19:09:39 +0000"
description: "Raw Call Detail Records are useful, but they are not exactly fun to read. If you are building with voice, messaging, or any communications workflow, CDR-styl..."
keywords: "telnyx, analytics, get, dashboard, python, code, https, com"
generated: "2026-07-09T19:54:26.400873"
---

# Build a CDR Usage Analytics Dashboard in Python

## Overview

Raw Call Detail Records are useful, but they are not exactly fun to read. If you are building with voice, messaging, or any communications workflow, CDR-style data can answer practical questions: How many calls happened in a date range? What did usage cost? Which hours are busiest? Which routes are most active? Are short calls or failed calls increasing? I put together a small Python example that turns Telnyx CDR data into a Flask analytics API, then uses Telnyx AI Inference to generate a short operational readout. Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/cdr-usage-analytics-dashboard-python What it exposes The example includes these routes: GET /cdrs GET /analytics/summary GET /analytics/peak-hours GET /analytics/top-routes GET /analytics/daily GET /analytics/ai-insights GET /health The analytics routes do the normal dashboard work in Python: total call count total, average, median, and p95 duration total, average, and max cost grouped counts by direction, call type, and status peak-hour distribution top route breakdowns daily call and cost totals Then /analytics/ai-insights takes a compact summary of the metrics and sends it to Telnyx AI Inference through the chat completions API. Why not ask the model to calculate everything? Because the model should not be the calculator here. For this kind of app, I like the split: Code calculates the metrics that need to be exact. The LLM explains the trend and suggests what to investigate next. That way, your totals and costs stay deterministic, but your dashboard can still give users a helpful plain-English summary. Run it Clone the examples repo: git clone https://github.com/team-telnyx/telnyx-code-examples.git cd telnyx-code-examples/cdr-usage-analytics-dashboard-python Create your .env file: cp .env.example .env Add your Telnyx API key: TELNYX_API_KEY=your_telnyx_api_key AI_MODEL=moonshotai/Kimi-K2.6 HOST=127.0.0.1 Install and run: pip install -r requirements.txt python app.py Test it: curl http://localhost:5000/health Get a summary: curl "http://localhost:5000/analytics/summary?start_date=2026-07-01&end_date=2026-07-08" | python3 -m json.tool Ask for AI insights: curl http://localhost:5000/analytics/ai-insights | python3 -m json.tool Where this could go This is intentionally small, but the pattern is useful: add a UI for support or ops teams store daily snapshots in a database send weekly summaries to Slack alert when costs spike detect unusual short-call patterns compare usage by campaign, customer, or region The repo is also agent-readable, so you can point a coding agent at the example and ask it to extend the dashboard, add charts, wire in auth, or adapt the metrics to your own workflow. Resources Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/cdr-usage-analytics-dashboard-python Telnyx AI skills and toolkits: https://github.com/team-telnyx/ai Telnyx AI Inference docs: https://developers.telnyx.com/docs/inference Chat Completions API: https://developers.telnyx.com/api/inference/chat-completions Telnyx Portal: https://portal.telnyx.com/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sonam_50a41a4ced7e6b4f3fa/build-a-cdr-usage-analytics-dashboard-in-python-1cbh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
