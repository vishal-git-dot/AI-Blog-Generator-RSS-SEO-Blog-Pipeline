---
title: "Project Elpis: Why AI Coding Agents Need a System Layer"
slug: "project-elpis-why-ai-coding-agents-need-a-system-layer"
author: "Masih Maafi"
source: "devto_python"
published: "Wed, 15 Jul 2026 18:48:48 +0000"
description: "Project Elpis: Why AI Coding Agents Need a System Layer AI coding agents are remarkably capable, but their performance degrades over long sessions. If you ha..."
keywords: "elpis, context, agent, runtime, model, file, user, tui"
generated: "2026-07-15T19:19:36.616904"
---

# Project Elpis: Why AI Coding Agents Need a System Layer

## Overview

Project Elpis: Why AI Coding Agents Need a System Layer AI coding agents are remarkably capable, but their performance degrades over long sessions. If you have used Aider, Cursor, or Claude Dev on non-trivial tasks, you have likely run into the wall: the agent starts hallucinating, forgetting constraints, executing redundant commands, and blowing through token budgets. The reason is simple: we are treating LLM agents as stateless chatbots instead of operating systems. We feed them raw transcripts, duplicate file bodies, verbose terminal outputs, and stale instructions. This bloats the context window and dilutes the active goal. Project Elpis is an open-source agent environment built in Rust designed to solve this by introducing an explicit System Layer between the user, the agent runtime, and the codebase. The Core Architecture: Separating Context from Execution Elpis does not try to build a new foundation model. Instead, it owns the surrounding environment: the TUI, runtime selection, context assembly, durable memory, provider-neutral session mirror, and approval contracts. Whichever model or runtime is active (Codex, Gemini, Claude, or a custom local adapter), it must assimilate into the control environment governed by Elpis. User -> Elpis TUI (presentation, approvals, context visibility) -> Elpis Control Layer (runtime choice, context sovereignty, memory, policy) -> Active Agent Runtime (Codex app-server, Claude, Gemini, etc.) -> Elpis Retrieval Services (Python MCP server) -> Workspace + Durable Elpis State (~/.elpis) 1. Enforcing Context Sovereignty In Elpis, context is a strictly budgeted working set, not a dump of the session archive. We implement five key pipelines to enforce context sovereignty: Ephemeral Context Pruning We separate the on-disk session history from what the model actively sees. Stale directory listings, redundant file reads, and failed terminal probes are immediately pruned from the working context once they have answered a question. Compact Receipts Instead of appending full terminal outputs or entire file contents pre- and post-edit, Elpis replaces them with compact, structured receipts: Operation target and exit status. A concise change summary or diff reference. Specific verification tests performed. A pointer for the agent to reread the full artifact if absolutely necessary. Guarded Compaction When context limits are reached, instead of a simple sliding window that drops the beginning of the conversation, Elpis executes a structured checkpoint. This checkpoint summarizes the active goals, decisions, file modifications, and blockers, ensuring the agent doesn't "wake up" inside a vacuum. 2. Layered Runtime Ownership & Approvals To ensure safety and predictability, Elpis routes all file writes, system edits, and shell command executions through explicit sandbox and approval contracts. sequenceDiagram participant Model as Agent Runtime participant Elpis as Elpis Control Layer participant User as Rust TUI / User Model->>Elpis: Request Command Execution / File Write Note over Elpis: Check Sandbox Rules Elpis->>User: Render Approval Modal (Diff/Command) User-->>Elpis: Approve / Reject / Escalate Elpis->>Model: Return Executed Output (or block) The model owns the low-level turn it is designed to execute. Elpis projects context into that turn, bridges approvals, and mirrors the visible transcript to protect the host machine. 3. Implementation Status & Tech Stack Elpis is currently a working prototype consisting of: Rust TUI : A terminal UI built to render streaming tokens, active token counts, and approval modals. Codex App-Server Adapter : Integrates with the Codex runtime as a first working milestone. Python MCP Server : Exposes local retrieval and semantic memory services to the agent. Verification and Test Suite To run the local unit and integration test suite: cd tui CC = /usr/bin/cc CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_LINKER = /usr/bin/cc cargo test cd .. .venv/bin/python -m compileall -q src 🚀 The Vision: Get Involved We want to build a truly sovereign, local environment where coding agents can work with greater continuity, restraint, and transparency. If you are a systems, TUI, or hardware-savvy engineer interested in context window optimization and agent sandboxing, we welcome contributions. GitHub Repository : github.com/MasihMoafi/Elpis Main Website : masihmoafi.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/masihmoafi/project-elpis-why-ai-coding-agents-need-a-system-layer-4dia

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
