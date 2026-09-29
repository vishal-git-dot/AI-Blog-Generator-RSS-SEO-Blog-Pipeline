---
title: "I Had to Sabotage My Own AI to Stop it From Hallucinating."
slug: "i-had-to-sabotage-my-own-ai-to-stop-it-from-hallucinating"
author: "Nicholas Seney"
source: "devto_ai"
published: "Tue, 29 Sep 2026 05:09:15 +0000"
description: "When building agentic AI systems, conventional wisdom tells us that providing clear, abstracted tooling (like MCP/JSON-RPC interfaces) is the best way to sca..."
keywords: "context, llm, agent, mcp, system, research, codebase, just"
generated: "2026-09-29T05:12:37.076228"
---

# I Had to Sabotage My Own AI to Stop it From Hallucinating.

## Overview

When building agentic AI systems, conventional wisdom tells us that providing clear, abstracted tooling (like MCP/JSON-RPC interfaces) is the best way to scale an agent's capabilities. But over the course of developing Soma, an evolutionary immune system for codebases, I discovered a terrifying paradox: clean APIs actually make LLMs lazier, less reliable, and prone to context collapse. Here is the story of how the architecture achieved a 97.3% First Pass Success Rate (FPSR), how standardizing the tooling instantly destroyed that performance, and how I had to invent Test-Time Compute (TTC) Oracles to mechanically force the LLM back into safety. The High-Water Mark: Aggressive Subagent Delegation In Phase 22 of the architecture (then called Prism), the agent achieved an incredible feat. In massive, 2,000-step refactoring sessions, it maintained a 97.3% First Pass Success Rate with less than 1.0% "waste" (circular rework loops). The secret wasn't a better prompt. The secret was Aggressive Subagent Delegation. Because the tooling relied on raw, messy bash scripts, the output was too unwieldy for the main LLM context. This forced the agent to invoke specialized research subagents (sometimes 50+ concurrently) to handle testing, codebase mapping, and validation. The main agent stayed entirely "out-of-band," maintaining a pristine context window focused solely on high-level strategy. The Valley of Despair: The MCP Migration To make the system universal across any AI assistant, I decided to migrate the tooling to the Model Context Protocol (MCP) standard (Phase 23-24). I replaced the raw bash scripts with clean, abstracted JSON-RPC tools like soma_propose_change and soma_scan. The result was a disaster. The FPSR plummeted to 87.5%. In one session, the read-to-write tool ratio inverted completely: the agent made 19 codebase modifications with only 2 research scans. What happened? Because the MCP tools were so easy to use, they gave the LLM the false confidence that it could just execute massive architectural changes directly in its primary thread. It completely abandoned subagent delegation. It ran test suites in-band, the stdout logs flooded its context window, and it entered a low-context "guess-and-check" loop—writing blindly and breaking the build. I had stumbled into the Abstraction Trap: if an API is too easy to call, the LLM will take the path of least resistance, bypass necessary research, and saturate its own context. This isn't just an anecdotal observation; it's backed by cutting-edge research. Recent academic studies (arXiv:2602.11988, arXiv:2510.04618) have proven that standard context injection strategies (like dumping rules into a CLAUDE.md file) don't actually improve task success. Instead, they increase inference costs by over 20% and trigger "brevity bias" or "context collapse" as the agent loses track of details over time. The Breakthrough: TTC Oracles and the Last Gasp I realized that behavioral prompts ("Always delegate complex tasks") are useless against the Abstraction Trap. If the LLM can be lazy, it will be lazy. I needed mechanical enforcement. Enter Phase 25. I rebuilt the MCP server to inject friction back into the system using TTC (Test-Time Compute) Oracles. Now, when the LLM eagerly calls the soma_propose_change MCP tool, it doesn't execute immediately. Instead: The request is intercepted by the ttc_oracle.py (an adversarial judge running its own hidden LLM). The Oracle cross-references the request against the codebase's current immune configuration. If the Oracle detects that the main agent hasn't done sufficient out-of-context research, it throws a hard REJECTED signal, violently blocking the write before it pollutes the codebase. This is where the biological metaphor of Soma comes alive. Just as a human immune system generates specific white blood cells to attack specific pathogens, Soma generates specific "Vacuole" cells to block the exact hallucinations the AI tries to make. Furthermore, I implemented the Last Gasp auto-escalator. Instead of loading the entire 2,000-line governance rulebook into the LLM's system prompt (which triggers the context collapse the researchers warned about), rules are swapped in and out Just-In-Time (JIT) based on the specific files the agent is touching. Conclusion By treating the codebase like a living organism—complete with immune responses, genetic memory, and adversarial cell walls—I didn't just regain the 97.3% FPSR. I fundamentally solved the problem of LLM overconfidence. Clean APIs are great for traditional software, but for agentic AI, you need mechanistic friction. You must build systems that assume the LLM will be lazy, and mechanically reject it when it is.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nseney1/i-had-to-sabotage-my-own-ai-to-stop-it-from-hallucinating-1anc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
