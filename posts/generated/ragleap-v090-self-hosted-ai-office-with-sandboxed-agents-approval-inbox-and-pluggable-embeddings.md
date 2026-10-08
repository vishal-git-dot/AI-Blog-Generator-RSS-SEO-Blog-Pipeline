---
title: "RagLeap v0.9.0 — Self-hosted AI Office with sandboxed agents, approval inbox, and pluggable embeddings"
slug: "ragleap-v090-self-hosted-ai-office-with-sandboxed-agents-approval-inbox-and-pluggable-embeddings"
author: "RagLeap"
source: "devto_ai"
published: "Thu, 08 Oct 2026 12:56:27 +0000"
description: "RagLeap is an open-source AI-employee platform. v0.9.0 ships the AI Office. TL;DR Dashboard at /office ragleap CLI: launch, stop, status, logs, update (with ..."
keywords: "ragleap, office, approval, sandboxed, inbox, pluggable, embeddings, open"
generated: "2026-10-08T13:09:09.870070"
---

# RagLeap v0.9.0 — Self-hosted AI Office with sandboxed agents, approval inbox, and pluggable embeddings

## Overview

RagLeap is an open-source AI-employee platform. v0.9.0 ships the AI Office. TL;DR Dashboard at /office ragleap CLI: launch, stop, status, logs, update (with DB backup), key Pluggable embeddings (Ollama, OpenAI, Mistral, Gemini) + vector size check Agent loop: act-observe, sandboxed exec, MCP client, cron triggers Approval system: off/semi/full, taint after web fetch, network-less sandbox How settings work now Settings page > .env. UI shows source of each value. Keys are encrypted at rest, write-only in UI. Test connection button included. Safety by default API-key auth on all data routes, no stack traces to client SSRF-safe fetch, sandbox has no network Approval inbox for all tool calls in semi/full mode Install curl -fsSL ... | bash or pip install ragleap-core ragleap launch Open PRs and issues welcome. I need clean-machine testers for installer. Repo: github.com/antonyrag/ragleap-core Release: v0.9.0 - f11d458

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ragleap/ragleap-v090-self-hosted-ai-office-with-sandboxed-agents-approval-inbox-and-pluggable-1fjg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
