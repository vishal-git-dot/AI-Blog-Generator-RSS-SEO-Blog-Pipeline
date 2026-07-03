---
title: "We ran blind AI agents against real WooCommerce stores. Here's what they actually read."
slug: "we-ran-blind-ai-agents-against-real-woocommerce-stores-heres-what-they-actually-read"
author: "Giuseppe Socci"
source: "devto_ai"
published: "Fri, 03 Jul 2026 14:18:28 +0000"
description: "TL;DR — On a production store with no agent infrastructure, blind agents failed product discovery while fetching 27 pages of theme HTML. With two cheap machi..."
keywords: "one, store, signals, agents, agent, discovery, badge, structured"
generated: "2026-07-03T14:21:09.821600"
---

# We ran blind AI agents against real WooCommerce stores. Here's what they actually read.

## Overview

TL;DR — On a production store with no agent infrastructure, blind agents failed product discovery while fetching 27 pages of theme HTML. With two cheap machine-readable signals, they succeeded 3 runs out of 3 — one run explicitly credited the HTTP Link header for the pivot. The human-visible badge was irrelevant. Structured catalog summaries cut the listing payload by 93%. The question Everyone is talking about agentic commerce — ChatGPT handles on the order of 50M shopping queries a day, and AI-referred traffic to retail sites grew roughly 8x year over year in early 2026. But almost nobody has published primary data on the most basic question: when an AI agent lands on your store with a task, what does it actually do? So we tested it. Blind agents (a small GPT-class model, no system-prompt hints, no URLs beyond the homepage), a concrete task — find product X on this store and verify its price — against real WooCommerce stores in production. Then we varied one thing at a time. The setup Baseline — a production store (~1,000 SKUs) with no agent infrastructure beyond a robots.txt mention. Full signals — a store running our open-source plugin exposing a structured catalog API, plus two discovery signals: an HTML comment in <head> and an HTTP Link rel="kalicart-agent" response header pointing to a machine-readable discovery document. Signals, badge off — same as 2, with the human-visible "agent-ready" badge disabled. What happened Cell Runs Outcome Baseline (no signals) 1 ❌ Failed discovery — 27 fetches, robots.txt seen and ignored, answered from HTML fragments Full signals 3 ✅ 3/3 — found discovery doc, switched to structured API, verified price & stock Signals, badge off 3 ✅ 3/3 — identical behavior; badge never mentioned Baseline: the agent scraped category HTML like a 2015 crawler, burned its budget on theme markup, and produced an answer from fragments. It saw the robots.txt hint — and ignored it. With signals: in one run the attribution was surgical — the agent's own reasoning cited the Link header as the reason it pivoted to the structured API. One HTTP response header, the cheapest possible intervention, flipped the outcome. Badge off: agents never needed it. The badge is for humans. If you're adding "AI-ready" stickers to your storefront for the agents' sake, save the pixels. The economics nobody mentions We also measured the cost of a cold visit. Without structure, the cold start on the baseline store weighed about 134 KB of fetched content — and the homepage HTML alone was 90 KB, 67% of the entire budget , before a single product appeared. With discovery in place, the same task starts at roughly 44 KB . Inside the catalog itself: serving listing results as structured summaries instead of full records dropped one page of results from 40,382 to 4,686 bytes — −93% . Tokens are money and latency. A store that is expensive to read is a store agents will read badly — or not at all. Why this matters for WooCommerce specifically Shopify solved this wholesale: Shopify Catalog auto-enrolled over a million merchants into ChatGPT's shopping surface with zero merchant action. WooCommerce — powering more stores than any other platform — has no native equivalent today. Every Woo merchant is, right now, the baseline cell of this experiment. That gap is why we built KaliCart Bridge (open source, on WordPress.org): structured catalog API, MCP endpoint, the discovery signals tested above, an OpenAI-spec product feed generator, and telemetry showing which agents already visit your store. Install-and-forget — because the clearest lesson of the experiment is that defaults win . Honest limits Small n (three runs per cell plus one baseline), one model family, two stores, one task type. This is a flashlight, not a floodlight. We are instrumenting more stores and will publish 30 days of live agent-traffic telemetry next — including which crawlers (ClaudeBot and OAI-SearchBot are already in our logs) actually read which surfaces. The one-line takeaway: agents don't reward beauty, they reward legibility . And legibility, today, is one HTTP header away. Originally published at bridge.kalicart.com/blog .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kalicart-bridge/we-ran-blind-ai-agents-against-real-woocommerce-stores-heres-what-they-actually-read-4kom

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
