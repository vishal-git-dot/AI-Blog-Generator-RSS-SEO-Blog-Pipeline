---
title: "I Built an Open-Source Reliability Tester for Multi-Agent AI Systems — Here's What It Catches"
slug: "i-built-an-open-source-reliability-tester-for-multi-agent-ai-systems-heres-what-it-catches"
author: "suraj kumar"
source: "devto_python"
published: "Sun, 21 Jun 2026 04:18:07 +0000"
description: "A multi-agent system where each agent is 95% reliable, chained 14 deep, is only about 49% reliable end-to-end. 0.95^14 ≈ 0.49. Every additional agent multipl..."
keywords: "agent, swarm, test, agents, run, what, system, failure"
generated: "2026-06-21T04:54:47.253667"
---

# I Built an Open-Source Reliability Tester for Multi-Agent AI Systems — Here's What It Catches

## Overview

A multi-agent system where each agent is 95% reliable, chained 14 deep, is only about 49% reliable end-to-end. 0.95^14 ≈ 0.49. Every additional agent multiplies the failure surface, and standard testing doesn't catch the failures that emerge from agent interaction — only the ones inside a single agent. I built swarm-test to test the interactions. It's open source, free, and works across CrewAI, LangGraph, AutoGen, and custom orchestrators. Here's what it does. Reliability scoring (0-100) Every system gets a Swarm Score from 8 structural chaos tests: cascade_failure — does one agent's failure take down others blast_radius — which agents are single points of failure context_leakage — does sensitive data flow where it shouldn't intent_drift — do agents stray from their assigned role collusion_detection — are agents forming tight cliques timeout_resilience — fragile single-upstream dependencies contract_violation — output schema mismatches between agents sensitive_data — secrets and PII in agent payloads A clean system scores high. A fragile one scores low. The score is the headline. Agent role classification swarm-test classifies each agent by its position in the graph — orchestrator, worker, validator, gateway, aggregator, monitor — and adjusts how it reads risk. An orchestrator with 90% blast radius is expected by design; it needs a fallback, not a redesign. A worker with 90% blast radius is a design smell. Security-sensitive roles like validators get their severity automatically upgraded. Historical tracking It saves every run and compares against the last: Swarm Score: 31/100 — AT RISK Trend: ↑ +19 (was 12) — improving Recent: 12 → 12 → 31 ✓ 6 findings resolved since last run Findings are diffed using stable IDs, so identical runs show zero change and a real fix shows exactly what resolved. This turns a snapshot into a feedback loop. Built for real workflows A GitHub Action that gates PRs and annotates them with findings Output contract validation (per-agent JSON schemas) An interactive HTML report with a D3 agent graph, heatmap, and trend chart Graph export to Mermaid, DOT, or PNG — paste topology straight into a README A plugin system for custom tests YAML config for thresholds and CI behavior Try it pip install swarm-test swarm-test run my_crew.py GitHub: github.com/surajkumar811/swarm-test I test it on my own 14-agent passport-photo pipeline — first run surfaced 15 critical cascade failures I didn't know were there. If you run agents in production, I'd genuinely like to hear what failure modes you've hit that this doesn't cover yet.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/suraj_kumar_96bb8767435e2/i-built-an-open-source-reliability-tester-for-multi-agent-ai-systems-heres-what-it-catches-217i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
