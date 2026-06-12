---
title: "Your AI Agent Needs a Memory: Using Memory Sidecar for Persistent Context Across Sessions"
slug: "your-ai-agent-needs-a-memory-using-memory-sidecar-for-persistent-context-across-sessions"
author: "Manoir Yantai"
source: "devto_ai"
published: "Fri, 12 Jun 2026 15:23:34 +0000"
description: "We've all been there. You're deep in a project with your AI coding assistant — you've discussed architecture, debated trade-offs, and started implementation...."
keywords: "agent, you, memory, sidecar, your, session, layer, context"
generated: "2026-06-12T15:28:32.970982"
---

# Your AI Agent Needs a Memory: Using Memory Sidecar for Persistent Context Across Sessions

## Overview

We've all been there. You're deep in a project with your AI coding assistant — you've discussed architecture, debated trade-offs, and started implementation. Then you restart your terminal, open a new session, and... it's like talking to a stranger. The agent has no idea who you are, what you were building, or why you chose that particular library. For anyone building serious work with AI agents, this statelessness is the single biggest productivity killer. You end up repeating context, re-explaining decisions, and wasting time re‑establishing the shared mental model that makes these tools actually useful. Enter Memory Sidecar. It's exactly what it sounds like: a sidecar process that runs alongside your agent — Hermes, Claude Code, Cursor, Codex, or anything else — and gives it a real, persistent memory. No patching the agent internals, no vendor lock‑in. The agent writes its session logs to a shared directory, and the sidecar picks them up, processes them, and feeds relevant history back into future prompts. How it works (in a nutshell) The sidecar is a separate Python process (3.9+). It reads session files from a designated folder and indexes them into three retrieval layers: Hot Layer — a small (5KB cap) recent context buffer for immediate recall of the last few exchanges. Warm Layer — a PostgreSQL‑backed semantic search that retrieves related conversations based on meaning, not just keywords. Cold Layer — a knowledge graph ( gbrain ) combined with FTS5 full‑text search for long‑term archival and cross‑session topic discovery. When the agent needs context, the sidecar injects relevant memories directly into the system prompt. The agent doesn't even know it's happening — it just sees a richer, more informed prompt. Architecture at a glance Agent writes sessions → state.db + session files ↓ Sidecar reads checkpoint, processes new sessions ↓ ┌───────────┼───────────┐ │ │ │ ▼ ▼ ▼ Hot Layer Warm Layer Cold Layer (memory (Hindsight (gbrain graph tool, PostgreSQL) + FTS5 search) 5KB cap) ↓ Tiered context injection → agent's system prompt Why not just paste the conversation history? Because it doesn't scale. A long session becomes a massive prompt, costs skyrocket, and you still lose cross‑session knowledge. Memory Sidecar is designed for production: it summarises, deduplicates, and prioritises. You can also track important entities (people, projects, recurring bugs) and create standalone dossiers for them. Key tools included memory_watermark.py — automatic memory layer detection and archival when capacity is reached. memory_snapshot_backup.py — periodic snapshot backups of the memory state. hindsight‑service.py — a simplified daemon for running the warm‑layer PostgreSQL service. hindsight_mcp_bridge.py — inline format fix and MCP integration for agents like Claude Code. session_to_gbrain.py — now uses environment‑based token config, no more hardcoded keys. Getting started Clone the repo: git clone https://github.com/mage0535/hermes-memory-installer Install dependencies ( pip install -r requirements.txt ) Configure your agent to write sessions to a directory (usually a few lines of code) Run the sidecar: python memory_sidecar.py That's it. The sidecar will watch for new sessions, index them, and start answering context requests from your agent. When not to use this If you only need in‑session recall (like a simple chat history), a sliding window is fine. Memory Sidecar adds operational overhead: you need to run a separate process and optionally PostgreSQL. It's best for projects where you regularly interact with an agent over days or weeks and need it to remember decisions, codebase details, and past discussions. Final thoughts I've been running this alongside Hermes and Claude Code for a few months, and it's completely changed how I use them. No more repeating myself. No more "you already told me that" moments. The agent just knows . If you're tired of your AI agent forgetting yesterday's conversation, give Memory Sidecar a try. It's open source (MIT), and contributions are welcome. Repo: https://github.com/mage0535/hermes-memory-installer Have you tried other approaches to agent memory? What worked or didn't? I'd love to hear your experiences.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/manoir_yantai_f22f01340f0/your-ai-agent-needs-a-memory-using-memory-sidecar-for-persistent-context-across-sessions-50i5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
