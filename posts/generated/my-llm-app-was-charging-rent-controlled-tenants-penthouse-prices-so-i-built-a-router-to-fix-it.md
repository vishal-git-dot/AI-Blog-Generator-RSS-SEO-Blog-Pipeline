---
title: "My LLM App Was Charging Rent-Controlled Tenants Penthouse Prices — So I Built a Router to Fix It"
slug: "my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it"
author: "Ayush Singh Tomar"
source: "devto_python"
published: "Mon, 27 Jul 2026 03:30:15 +0000"
description: "Every LLM app I've built has the same expensive habit: one model, every request. "What is FastAPI?" and "compare these five architectures in depth" go to the..."
keywords: "model, llm, router, what, cost, you, one, every"
generated: "2026-07-27T03:38:46.275815"
---

# My LLM App Was Charging Rent-Controlled Tenants Penthouse Prices — So I Built a Router to Fix It

## Overview

Every LLM app I've built has the same expensive habit: one model, every request. "What is FastAPI?" and "compare these five architectures in depth" go to the same endpoint, at the same price. That's fine right up until you look at the bill — you're paying big-model rates for questions a much smaller model answers just as well. So I built a router that sits in front of two models and decides which one actually earns the request. Live demo: llm-cost-router.streamlit.app Repo: github.com/ayush-s-tomar/llm-cost-router What it does Ask it anything. It classifies the question, then routes it to one of two models on Groq: Llama 3.1 8B Instant — simple, direct questions Llama 3.3 70B Versatile — genuinely complex, multi-part, or open-ended ones Every request is logged with what it actually cost, and what it would have cost on the big model every time. The dashboard tracks all of it live — requests, actual spend, hypothetical spend, savings, percentage saved. Watching it decide Here's the router handling a simple and a complex question back to back, picking a different model each time without being told which to use: "What is FastAPI?" → routed to the 8B model → complete, correct answer → $0.000020 . "Compare LangGraph and CrewAI in depth, covering architecture trade-offs" → routed to the 70B model → because a shallow answer here wouldn't hold up → $0.000691 . Same interface. Same person asking. Two different models, chosen automatically, with the price difference sitting right there instead of buried in a monthly invoice. Across a mixed session like the one above, the dashboard lands around 33% cheaper than defaulting everything to the 70B model. That number isn't fixed — it moves with what you actually ask. A session of simple lookups saves more; a session of genuinely hard questions saves less, because more of them should be going to the big model. That's the entire design goal: not a flat discount, the right spend per question. How the classifier decides No embeddings. No cheap pre-classification LLM call — that would defeat the point of a cost router before it even started. Just a lightweight heuristic in router_logic.py : Query length — long queries default to the big model Complexity keywords — "compare," "analyze," "design," "trade-off," "step by step" Simple-query patterns — "what is," "who is," "define," "list" It won't catch everything — a short question that's secretly hard can slip through — but it costs nothing to run, which is the entire point. An LLM call to decide which LLM to call would eat the savings you're trying to create. Here's the actual decision path — first match wins, everything else falls through to the cheap model by default: What it doesn't do yet No semantic caching — a near-identical question still hits the model every time Only two tiers — a mid-size model would give the router more room to be precise instead of picking a side The keyword heuristic can misfire on short-but-hard questions; a confidence threshold with a fallback path would help Why this is the bigger lever Most "cut your AI costs" content is prompt-engineering theater — shave a few tokens, cache a response, feel productive. None of it touches the actual lever. The model you pick is the cost. Everything else is rounding error. Stack FastAPI backend React frontend Streamlit for the live public demo Groq for both models (Llama 3.1 8B Instant + Llama 3.3 70B Versatile) Try it Live demo: llm-cost-router.streamlit.app Repo: github.com/ayush-s-tomar/llm-cost-router If you're running LLM calls at any real volume, a router like this is one of the higher-ROI things you can build — a small amount of logic that pays for itself the first time it downgrades a request. What's the one API call in your stack that's been quietly overpaying for a year and nobody's checked?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ayushsinghtomar/my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it-38cl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
