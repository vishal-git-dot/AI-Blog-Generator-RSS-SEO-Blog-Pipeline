---
title: "Your AI Bill Is a Routing Problem, Not a Model Problem"
slug: "your-ai-bill-is-a-routing-problem-not-a-model-problem"
author: "Vinicius Fagundes"
source: "devto_python"
published: "Tue, 21 Jul 2026 03:00:00 +0000"
description: "The price spread right now: open-weight models around $0.14 per million input tokens. Frontier flagships at $5.00. That's a 35x gap — and most pipelines send..."
keywords: "cheap, tier, frontier, route, task, model, per, traffic"
generated: "2026-07-21T03:19:30.888787"
---

# Your AI Bill Is a Routing Problem, Not a Model Problem

## Overview

The price spread right now: open-weight models around $0.14 per million input tokens. Frontier flagships at $5.00. That's a 35x gap — and most pipelines send every request to the expensive one, because routing everything to the best model is the architecture you get when you don't make an architecture decision. The fix is boring. Which is my favorite kind of fix. Step one: classify the workload, not the model Stop asking "which model is best?" and start asking "which tasks are cheap-safe?" The split is almost always the same: High-volume, low-ambiguity — extraction, classification, formatting, summarization → cheap tier Multi-step reasoning, anything customer-facing → frontier tier Same interface in front of both, so callers never know or care which tier answered. Step two: the router is maybe 200 lines Here's the skeleton — a task registry, two tiers, one dispatch function: from dataclasses import dataclass PRICE_PER_MTOK = { " cheap " : 0.14 , " frontier " : 5.00 } # $/1M input tokens @dataclass class Route : tier : str # "cheap" or "frontier" eval_threshold : float # min accuracy on the golden set to KEEP this route ROUTES = { " extract_invoice_fields " : Route ( " cheap " , 0.95 ), " classify_ticket " : Route ( " cheap " , 0.92 ), " format_to_json " : Route ( " cheap " , 0.98 ), " summarize_call " : Route ( " cheap " , 0.90 ), " multi_step_analysis " : Route ( " frontier " , 0.00 ), # never downgraded " customer_reply " : Route ( " frontier " , 0.00 ), } def route ( task : str , eval_scores : dict [ str , float ]) -> str : r = ROUTES [ task ] if r . tier == " cheap " and eval_scores . get ( task , 0.0 ) < r . eval_threshold : return " frontier " # automatic fallback: evals gate the cheap tier, not vibes return r . tier # Last eval run on the golden datasets: eval_scores = { " extract_invoice_fields " : 0.97 , " classify_ticket " : 0.94 , " format_to_json " : 0.99 , " summarize_call " : 0.86 } # summarize regressed for task in ROUTES : print ( f " { task : 24 s } -> { route ( task , eval_scores ) } " ) extract_invoice_fields -> cheap classify_ticket -> cheap format_to_json -> cheap summarize_call -> frontier multi_step_analysis -> frontier customer_reply -> frontier Notice summarize_call : it wanted the cheap tier, but its eval score dropped below threshold, so the router bounced it back to frontier automatically. Nobody woke up at 3am. That's the whole design — the golden dataset per task and the threshold are the safety net; the router is just an if . And that's the honest part of this post: the router is trivial. The eval harness is the real work. Building golden datasets per task, scoring them on every model change, wiring the scores into dispatch — that's where the engineering hours go. Teams that skip it end up routing on vibes, and vibes always route to the expensive model, because nobody gets fired for picking the flagship. Step three: the arithmetic that sells it upstairs monthly_mtok = 100 # 100M input tokens/month def bill ( cheap_share : float ) -> float : return monthly_mtok * ( cheap_share * PRICE_PER_MTOK [ " cheap " ] + ( 1 - cheap_share ) * PRICE_PER_MTOK [ " frontier " ]) for share in [ 0.0 , 0.3 , 0.5 , 0.7 ]: print ( f " { share : . 0 % } of traffic on cheap tier -> $ { bill ( share ) : ,. 0 f } /month " ) 0% of traffic on cheap tier -> $500/month per 100M tokens 30% of traffic on cheap tier -> $354/month per 100M tokens 50% of traffic on cheap tier -> $257/month per 100M tokens 70% of traffic on cheap tier -> $160/month per 100M tokens Route just half the traffic and the bill drops nearly in half — the cheap tier is so much cheaper that its contribution barely registers. Scale those numbers to your actual token volume; the ratios hold. This isn't theoretical. One large exchange rebuilt exactly this across 1,200 agents and cut its AI spend nearly in half. Not better prompts. Not a new model. A router and a workload map. The resolution is the usual one: this is a data problem wearing an AI costume. The workload map comes from your usage logs. The golden datasets are labeled data pipelines. The eval scores live in a table. The teams that treat their AI traffic as a dataset get the 35x spread working for them. Where does your traffic go today — one model for everything, or tiers? I'm Vinicius Fagundes — principal data engineer, independent consultant, and MBA lecturer in São Paulo. I write about data pipelines and the economics that run on top of them, and take on a few platform projects per quarter through vf-insights.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fagundesv/your-ai-bill-is-a-routing-problem-not-a-model-problem-18aa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
