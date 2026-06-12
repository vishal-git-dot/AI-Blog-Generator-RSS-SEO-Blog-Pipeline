---
title: "Why your AI agent logs are not evidence and what to do about it"
slug: "why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it"
author: "Jiří Joneš"
source: "devto_python"
published: "Fri, 12 Jun 2026 14:51:47 +0000"
description: "1. The problem Your agent failed in production. You look at the logs. They don't give you the full picture. So you run the agent again with the exact same in..."
keywords: "you, agent, run, span, logs, what, your, not"
generated: "2026-06-12T15:28:32.968875"
---

# Why your AI agent logs are not evidence and what to do about it

## Overview

1. The problem Your agent failed in production. You look at the logs. They don't give you the full picture. So you run the agent again with the exact same inputs. It succeeds. Or it fails differently. Classic. LLM calls, time-dependent code, tool side effects, and stochastic sampling mean "same inputs → same outputs" is completely false for AI systems. You now have no idea what actually happened in the first run. The original context is gone, and re-running is not replaying. 2. Logs vs evidence Logs are claims. Not evidence. A standard log or trace is just a JSON blob. A buggy retention job can orphan a span. An attacker can rewrite it. The agent itself might hallucinate and log bad data. This is not theoretical. If your trace data is mutable, it is not evidence. It is merely a claim about what happened, written after the fact. You cannot trust it for critical audits or true debugging. 3. What tamper-evident actually means in practice You need tamper-evident logs. This means a SHA-256 hash chain. Every event during an agent session is appended to an immutable ledger. The hash input covers the sequence, the previous hash, the exact payload, the parent span, the run ID, and the epoch. Change one byte of an old span - the hash recomputed from that row changes. The chain is broken. This is what separates a tamper-evident audit trail from standard LLM observability tools like LangSmith or Langfuse. Those show you what happened. A hash chain lets you prove it. Verification is a single API call: curl http://localhost:4001/api/runs/your-run-id/verify \ -H "Authorization: Bearer " # → {"valid": true, "span_count": 12} # → {"valid": false, "chain_broken_at_seq": 7} One changed byte anywhere in history - you know immediately. 4. The replay cost trap Debugging by re-running the agent is a trap. Every debug retry is another live LLM call. That costs money and latency. Debug replay should use a VCR-style cassette. Cassette replay costs $0. It reads the exact payload stream from the database and feeds it back to the system - no LLM, no API credits. Here's how you instrument an agent: import spanchain as gf gf . init ( endpoint = " http://localhost:4000 " , api_key = " your-api-key " , run_id = " agent-run-001 " , ) @gf.trace ( name = " agent_run " ) async def agent_run ( task ): async with gf . span ( " llm_call " ): result = await llm . complete ( task ) async with gf . span ( " tool_call " , tool_name = " search " ): results = await search ( task ) return result One thing worth noting: the SDK is intentionally dumb. It doesn't compute hashes or maintain the chain - it just exports spans as OTLP to the backend. All cryptographic sequencing happens server-side. This means the client can't forge a clean chain even if it tries. 5. Where this matters even more: model upgrades When you swap models, your agent's behavior changes. How do you know what broke? You replay old cassettes through the new model. Because you have the exact historical context, you run a structural comparison between the two runs. The system compares span trees side-by-side and flags the exact deviation point - not just "Run B was slower," but the first span where behavior diverged. If the new model added a tool call or skipped a step, the diff marks it. You stop guessing. 6. How I got here I kept running into the same wall: agent fails, logs tell you nothing useful, you re-run and get a different result. Existing observability tools weren't built for this - they're great for metrics and traces, but they produce mutable data with no replay capability. So I built Span Chain - an auditable harness for production AI agents. The backend runs on Elixir/OTP, where every agent session gets its own isolated BEAM process (~2 KB heap). A crash in one agent doesn't touch the others. That's how you get 1,000 concurrent agents, 10,000 spans, 571 spans/sec, and 0 corrupted chains - no global locks, no shared state. The core is MIT licensed and self-hosted: git clone https://github.com/ghostfactory-art/spanchain cd spanchain cp .env.example .env # Edit .env — set POSTGRES_PASSWORD and GF_API_KEY docker compose up # → http://localhost If it solves a problem you're dealing with, the repo is at github.com/ghostfactory-art/spanchain . *Footnote: If you operate in a regulated environment, EU AI Act Article 12 requires automatic event logging and traceability for high-risk AI systems (Annex III obligations now expected from December 2027, pending formal adoption of the AI Omnibus agreed in May 2026). The law doesn't mandate tamper-evidence - but a log that can be silently rewritten is hard to defend as the "traceability" the regulation asks for. Evidence-grade logs are how you make Article 12 records stand up to scrutiny. Note: spanchain will be on PyPI shortly. For now, install from source: pip install ./sdk/python *

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ghostfactory/why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it-4j61

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
