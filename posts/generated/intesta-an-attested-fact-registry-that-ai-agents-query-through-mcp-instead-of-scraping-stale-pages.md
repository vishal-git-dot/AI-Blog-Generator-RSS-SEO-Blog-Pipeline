---
title: "Intesta: an attested fact registry that AI agents query through MCP instead of scraping stale pages"
slug: "intesta-an-attested-fact-registry-that-ai-agents-query-through-mcp-instead-of-scraping-stale-pages"
author: "Darius Ceponas"
source: "devto_python"
published: "Sun, 06 Sep 2026 14:38:04 +0000"
description: "AI agents already answer questions about small businesses. Most of the time they do it from stale pages, and when the page is missing they guess. After watch..."
keywords: "intesta, agents, facts, agent, through, mcp, questions, small"
generated: "2026-09-06T15:15:47.147377"
---

# Intesta: an attested fact registry that AI agents query through MCP instead of scraping stale pages

## Overview

AI agents already answer questions about small businesses. Most of the time they do it from stale pages, and when the page is missing they guess. After watching agents confidently misstate delivery terms for shops near me, I built Intesta — a public registry where a business publishes its own facts once and every agent reads the same attested source. Site: https://intesta.io · Benchmark vs. a scraping agent: https://intesta.io/benchmark · Public traffic stats: https://intesta.io/stats The model A business registers an entity and proves domain control (a DNS TXT record or a file under /.well-known/intesta ). It publishes facts: delivery, returns, fees, contacts, opening hours. Each fact is attested and appended to a ledger, so history is visible on the public passport page. Everyone reads the same core through two interfaces: Agents: an MCP endpoint and a plain HTTP API, plus an A2A agent card at /.well-known/agent.json and /llms.txt for discovery. People: a small "Verified facts" widget dropped on the business site with one script tag. The rule that matters: refuse instead of guessing The answer engine only answers from the passport. Retrieval is lexical first (token overlap with a stop-list and a threshold we measured — lowering it produced false answers), then a semantic fallback on embeddings (NVIDIA nemotron, cosine with absolute and relative thresholds). If nothing passes, the agent gets an explicit refusal and the question is logged for the owner as "uncovered". For humans there is an optional rephrasing step through a small LLM. Every generated sentence goes through a grounding verifier: at least 75 % of its tokens must come from the facts it cites, and every number, URL and e-mail must exist in those facts. A sentence that fails is dropped and the verbatim facts are shown instead. Off-topic questions ("what's the weather") are detected against the entity's vocabulary and answered with a scope message rather than a refusal, so the owner's "uncovered questions" list stays useful. Stack FastAPI + Postgres, nginx in front, systemd timers for backups, retention, traffic aggregation and IndexNow pings. Traffic stats are computed from the access log as counters only — no IPs or user agents are stored. Tests: 190 pytest cases, including an adversarial set of questions designed to make the engine invent things. What I'd like feedback on Is "refuse when the fact is missing" the right default for agents, or should there be a "best effort, flagged" mode? What would a small business actually want to put in its passport beyond delivery/returns/contacts? If you build sites for clients: would an "agent front" per site be a line in your price list? Registration and single queries are free. The MCP endpoint is listed on Glama and Smithery; try it with any MCP client.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/darius_ceponas_2b7889e363/intesta-an-attested-fact-registry-that-ai-agents-query-through-mcp-instead-of-scraping-stale-pages-48d9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
