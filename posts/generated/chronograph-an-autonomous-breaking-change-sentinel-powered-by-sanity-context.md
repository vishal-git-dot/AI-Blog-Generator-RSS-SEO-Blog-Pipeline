---
title: "ChronoGraph: An Autonomous Breaking-Change Sentinel Powered by Sanity Context"
slug: "chronograph-an-autonomous-breaking-change-sentinel-powered-by-sanity-context"
author: "Sundas Naeem"
source: "devto_ai"
published: "Sun, 04 Oct 2026 11:52:15 +0000"
description: "This is a submission for the Sanity Challenge, Path One: Ship an Agent That Queries Real Content What I Built ChronoGraph is a breaking-change sentinel for m..."
keywords: "sanity, agent, dataset, context, live, knowledge, base, one"
generated: "2026-10-04T12:05:49.594788"
---

# ChronoGraph: An Autonomous Breaking-Change Sentinel Powered by Sanity Context

## Overview

This is a submission for the Sanity Challenge, Path One: Ship an Agent That Queries Real Content What I Built ChronoGraph is a breaking-change sentinel for microservice teams. You paste an API diff, and it tells you — before merge — which downstream services and squads it will break, using multi-hop dependency traversal over a live Sanity dataset. On top of the deterministic AST analysis, a Gemini-powered agent independently queries a Sanity Context MCP endpoint backed by a Knowledge Base of OpenAPI specs, consumer changelogs and on-call runbooks. When the dataset and the documentation disagree about a field's contract — nullability, type, deprecation status — the agent surfaces both claims side by side with their sources instead of picking one. Demo Live app: https://ai-agent-production-0558.up.railway.app/ Demo video: https://drive.google.com/file/d/1Cu4TBtItlFaiB4IAgMoAFFanlpAdlZwn/view?usp=sharing Code https://github.com/sundanaeem-systems/AI-agent How I Used Sanity I pointed Sanity Context at a Knowledge Base built from three documents I wrote: an OpenAPI spec for the billing service, a consumer changelog from the mobile client, and an on-call runbook — all intentionally containing contract details that conflict with the live dataset (e.g. the dataset says a field is optional, the OpenAPI spec says it became required). The agent connects to two Sanity Context MCP endpoints: one serving the live dataset (GROQ mode) and one serving the Knowledge Base, calling docs_ initial_context and docs _knowledge_base_search to retrieve real content before reasoning. Every tool call is shown live in an "Agent Trace" panel, and detected contradictions render as a card with both sourced claims — a human can rule on the contradiction, and that ruling is written back to Sanity as a contractDecision document so future runs don't re-ask. Sanity Project Details Sanity Project ID: d7ujf5vw Dataset: production The service/endpoint graph (services, apiEndpoint contracts with fieldContracts and consumer bindings) lives in this dataset and is seeded from lib/sanity/sanityData.ts via scripts/seed.ts. The Knowledge Base used by the agent (billing-openapi-v3.md, consumer-changelog-mobile-bff.md, runbook-billing-oncall.md) is built from the files in kb-content/ in the repo, served through a separate Sanity Context Knowledge Base endpoint. Agent Session

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sundas_naeem_6f4864a7c69d/chronograph-an-autonomous-breaking-change-sentinel-powered-by-sanity-context-1db0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
