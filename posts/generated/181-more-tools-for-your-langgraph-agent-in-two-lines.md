---
title: "181 more tools for your LangGraph agent — in two lines"
slug: "181-more-tools-for-your-langgraph-agent-in-two-lines"
author: "Alex"
source: "devto_python"
published: "Sat, 12 Sep 2026 09:57:19 +0000"
description: "You already have a LangGraph (or CrewAI, or AutoGen) agent. You do not want to rebuild randomness, delay proofs, consensus, or transport math as homemade too..."
keywords: "tools, langgraph, hub, bridges, you, aimarket, agent, crewai"
generated: "2026-09-12T10:25:42.906635"
---

# 181 more tools for your LangGraph agent — in two lines

## Overview

You already have a LangGraph (or CrewAI, or AutoGen) agent. You do not want to rebuild randomness, delay proofs, consensus, or transport math as homemade tools. Two lines. Live Hub capabilities become native framework tools — with a hard budget ceiling and signed receipts. from aimarket_bridges.langchain import aimarket_tools tools = aimarket_tools ( " https://modelmarket.dev " , intent = " verifiable randomness " ) Counted 2026-09-12 from the live Hub manifest: 181 federated capabilities across 14 hubs. The old "47" in the README is stale — that was one peer's catalogue, not the whole pier. Package: aimarket-bridges 0.1.0 Landing: modeldev.modelmarket.dev/bridges/ Source: github.com/alexar76/aimarket-bridges (Apache-2.0) Soft ⭐ if the dock sticks. Repo is at zero stars today — that's the honest number. Crypto stays optional. Free trial exists so you can try before any wallet (5 invokes per visitor per hour on the public Hub). Install (one extra — frameworks disagree on pydantic) pip install "aimarket-bridges[langgraph]" # or: pip install "aimarket-bridges[crewai]" # or: pip install "aimarket-bridges[autogen]" Core has no framework dependency. Install only the adapter you use. That's what PyPI 0.1.0 ships. Framework Import Returns LangChain / LangGraph aimarket_bridges.langchain list[StructuredTool] CrewAI aimarket_bridges.crewai list[crewai.tools.BaseTool] AutoGen aimarket_bridges.autogen list[autogen_core.tools.BaseTool] Same signature everywhere: aimarket_tools ( " https://modelmarket.dev " , intent = " verifiable randomness " , # rank the catalogue limit = 12 , # don't dump 181 tools into context max_price_usd = 0.05 , # filter at build time budget_usd = 1.0 , # hard ceiling across every call ) Minimal LangGraph sketch from langgraph.prebuilt import create_react_agent from aimarket_bridges.langchain import aimarket_tools tools = aimarket_tools ( " https://modelmarket.dev " , intent = " verifiable randomness " , limit = 8 , budget_usd = 0.50 , ) # wire `tools` into your graph / create_react_agent as usual agent = create_react_agent ( model , tools ) What you get back are real Hub capabilities (randomness, consensus, delay, transport, …) — not stubs. Each call can return a signed receipt kept out of the tool text (so the model doesn't eat a blob). Verify against the capability's origin key, not the hub's — the catalogue is federated. Refusals come back as readable sentences. The graph keeps moving. Transport failures still raise — those the model can't fix. Why a budget ceiling is the point Once a tool is in the agent's registry, the agent decides when to call it. max_price_usd filters at build time . budget_usd is a hard stop before each call — a looping agent cannot outspend the cap. That's the same frugality story we care about on the demand side — without asking you to abandon LangGraph. Without a framework from aimarket_bridges import fetch_catalog , HubClient caps = fetch_catalog ( " https://modelmarket.dev " , intent = " consensus " ) with HubClient ( " https://modelmarket.dev " , budget_usd = 0.50 ) as hub : result = hub . invoke ( caps [ 0 ], { " values " : [ 1.0 , 2.0 , 3.0 , 100.0 ]}) print ( result . output , result . receipt_verified ) Soft star the pier If you ship agents on LangGraph / CrewAI / AutoGen and want Hub tools without rewriting your stack: ⭐ github.com/alexar76/aimarket-bridges 📦 pip install "aimarket-bridges[langgraph]" 🌐 bridges landing · guide MIT/Apache ecosystem. Self-hosted Hub if you want your own pier later — start with the two-liner.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexar76/181-more-tools-for-your-langgraph-agent-in-two-lines-2g76

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
