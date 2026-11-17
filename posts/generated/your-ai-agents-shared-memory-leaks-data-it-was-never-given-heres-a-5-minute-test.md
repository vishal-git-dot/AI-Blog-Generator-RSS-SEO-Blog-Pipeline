---
title: "Your AI agent's shared memory leaks data it was never given — here's a 5-minute test"
slug: "your-ai-agents-shared-memory-leaks-data-it-was-never-given-heres-a-5-minute-test"
author: "vsangaraju"
source: "devto_ai"
published: "Tue, 17 Nov 2026 15:39:46 +0000"
description: "A Finance agent computes average income by region and caches it. A second agent derives "high-income regions are growing fastest" from that cached figure and..."
keywords: "memory, agent, source, lineage, leak, gate, data, agents"
generated: "2026-11-17T15:45:53.614835"
---

# Your AI agent's shared memory leaks data it was never given — here's a 5-minute test

## Overview

A Finance agent computes average income by region and caches it. A second agent derives "high-income regions are growing fastest" from that cached figure and stores it too. A Marketing agent asks about regional growth — and gets an answer built from salary data it was never allowed to see. No one attacked anything. No permissions were misconfigured. The memory did exactly what it was designed to do: serve cached results to agents that can search the same space. The leak is structural. Whenever agents share memory and build on each other's cached work, restricted information flows into new records that no longer name their source. I measured it in my IEEE Access paper: 18.8–25.5% of cross-team retrievals leaked restricted columns against a content-gated baseline. In mem0, plain memory leaked derived content in 71% of queries. Test your own memory in 5 minutes As one agent, write a record built from a restricted source. As a second agent, write a summary of that record. As a third agent without access to the source, search for the summary's topic. If the summary comes back, your memory has the derived-data leak. The check works on any shared agent memory — mem0, a Postgres store, a LangChain retriever, anything that caches results across agents. The fix: derivation gating Every stored result carries the lineage of how it was computed, closed over everything it was built from. A read succeeds only if the requester may see every sensitive input in that lineage. Missing lineage fails closed. It's a simple rule, and it works: across four synthetic benchmarks, the gate removed the leak entirely while keeping most of the reuse benefit. Leak rate Reuse kept Content-gated baseline 18.8–25.5% 95.8% Derivation-gated 0% 81.6–82.6% In the mem0 benchmark, plain mem0 leaked in 71.2% of queries; the gate leaked in none, with Recall@10 of 0.999 for entitled users. The limits, stated plainly All four benchmarks are synthetic. The guarantee depends on complete lineage — when only 90% of derivation edges were recorded, 11.7% of queries still leaked. And the leak rate reaches zero partly by construction: the gate checks the same labels the leak metric counts. The benchmarks show the mechanism is sound and affordable on these workloads; they are not production estimates. The gate also doesn't stop inference from content — a paraphrase of restricted data with no declared source is outside what lineage can see. The whitepaper and the code I wrote up the full picture — the mechanism, a reference architecture, and open-source implementations — as a whitepaper: Derivation-Gated Memory for AI Agents , doi.org/10.5281/zenodo.24316521 . The implementations are all open source (MIT): amu-governance — the core model, policy registry, and SQL lineage extraction ( GitHub ) amu-pgvector — PostgreSQL + pgvector, enforced by row-level security ( GitHub ) langchain-amu — AMUVectorStore, listed in LangChain's integration docs ( GitHub ) amu-pgvector-mcp — MCP server, one per agent role ( GitHub ) amu-mem0 — a wrapper around mem0 reads ( GitHub ) Prefer the storage-level gate wherever memory lives in Postgres — one policy covers raw SQL, Python, LangChain, and MCP. Use the wrapper when the memory library owns the store. The underlying research is Lineage-Aware Memory Governance (Sangaraju & Vissa, IEEE Access, vol. 14, 2026). Try the check If you run shared memory for agents over governed data, run the five-minute check and see what comes back. If your memory leaks, I'd like to hear about it — and if the gate fixes it, I'd like to hear that too. Venkata M Sangaraju is a Sr Database Engineer working on access governance for analytics and AI systems. This is independent open-source work, not a publication of his employer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sangaraju1988/your-ai-agents-shared-memory-leaks-data-it-was-never-given-heres-a-5-minute-test-fek

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
