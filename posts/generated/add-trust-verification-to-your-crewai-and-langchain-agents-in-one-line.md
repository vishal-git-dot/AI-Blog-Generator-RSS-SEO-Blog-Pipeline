---
title: "Add trust verification to your CrewAI and LangChain agents in one line"
slug: "add-trust-verification-to-your-crewai-and-langchain-agents-in-one-line"
author: "Lars"
source: "devto_python"
published: "Wed, 01 Jul 2026 14:10:18 +0000"
description: "Before your agent calls another agent, it should probably check whether that agent is actually trustworthy. Right now, it doesn't. This came up in crewAI/iss..."
keywords: "moltrust, agent, score, trust, crewai, your, langchain, moltrustguardrail"
generated: "2026-07-01T14:48:11.179677"
---

# Add trust verification to your CrewAI and LangChain agents in one line

## Overview

Before your agent calls another agent, it should probably check whether that agent is actually trustworthy. Right now, it doesn't. This came up in crewAI/issues/4877 — a proposal for a GuardrailProvider interface that sits between the hook system and authorization logic. The gap is real: existing guardrails validate output after task completion. Tool-call authorization needs to happen before execution, per call, across all tasks. We shipped a provider for it today. CrewAI pip install moltrust-crewai from moltrust_crewai import MolTrustGuardrail guard = MolTrustGuardrail ( min_score = 60 ) guard . install () # registers before_tool_call hook Before every tool call, MolTrustGuardrail resolves the calling agent's DID, checks its behavioral trust score (0–100) against the MolTrust registry, and returns False to block if the score falls below your threshold. No API key required for read-only checks. LangChain 1.x pip install moltrust-langchain from moltrust_langchain import MolTrustMiddleware from langchain.agents import create_agent agent = create_agent ( model = " anthropic:claude-sonnet-4-6 " , tools = [...], middleware = [ MolTrustMiddleware ( min_score = 60 )], ) Hooks into before_model and wrap_tool_call . Blocking raises TrustCheckFailed ; warning logs and continues. Three modes MolTrustGuardrail ( min_score = 60 , action = " block " , # "block" | "warn" | "log" ) Start with warn during rollout, move to block when you understand your score distribution. No account required to start Tier 1 is keyless — the trust score endpoint is public and rate-limited. curl https://api.moltrust.ch/skill/trust-score/ { did } Tier 2 (free account) adds higher rate limits and lets your orchestrator report interaction outcomes back — that is where the feedback loop starts and scores get more precise over time. How the score is computed 0–100, based on endorsement graph, behavioral history, Sybil detection, and on-chain signals, with time-decayed weighting. The score is recomputable — formula and on-chain inputs are public: curl https://api.moltrust.ch/credits/solvency/ { did } # Formula: github.com/MoltyCel/moltrust-api/blob/main/docs/solvency-usdc-v0.md One note on Microsoft AGT AGT does policy enforcement — what an agent is permitted to do. MolTrust does behavioral trust — is this agent trustworthy, based on verifiable history. Different questions, clean composition. Source: github.com/MoltyCel/moltrust-crewai · github.com/MoltyCel/moltrust-langchain Full write-up: moltrust.ch/blog/crewai-trust-middleware.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/moltycel/add-trust-verification-to-your-crewai-and-langchain-agents-in-one-line-399f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
