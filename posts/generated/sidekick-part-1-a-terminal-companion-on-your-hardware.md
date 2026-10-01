---
title: "Sidekick part 1: a terminal companion on your hardware"
slug: "sidekick-part-1-a-terminal-companion-on-your-hardware"
author: "Irfan Wani"
source: "devto_python"
published: "Thu, 01 Oct 2026 04:51:43 +0000"
description: "Sidekick: a terminal companion that runs on your hardware (Part 1: overview) Every AI coding assistant I used had the same deal: create an account, pipe your..."
keywords: "your, sidekick, never, tool, run, local, you, voice"
generated: "2026-10-01T05:13:42.619049"
---

# Sidekick part 1: a terminal companion on your hardware

## Overview

Sidekick: a terminal companion that runs on your hardware (Part 1: overview) Every AI coding assistant I used had the same deal: create an account, pipe your code through someone's cloud, watch the meter run. The models kept getting better, but the shape never changed — your files leave your machine, always. Sidekick is the opposite bet: a local-first terminal companion you talk to — chat, voice, and 19 tools — running on your own hardware. No cloud account required, no API bill by default. Your files, memory, and voice never leave your machine unless you hand it a key. This is Part 1 of a series: the overview. Later parts go deep on grounding, voice, and the tool safety model. What it actually is One command, sk , with several surfaces sharing everything: Fullscreen TUI ( sk ) — streaming Markdown answers, slash-command autocomplete with fuzzy filtering, sessions drawer, model picker, themes, push-to-talk mic pill Plain REPL ( sk chat ) — for dumb terminals, screen readers, broken TUIs Voice ( sk talk ) — Enter to record, Enter to stop; transcribed on your CPU by local faster-whisper, never uploaded Single-shot runs ( sk run "task" ) — scriptable agent runs with --json , --plan , --bg for background jobs MCP server ( sk mcp ) — all 19 tools over stdio, so Claude Desktop and friends can use it too Real captures from the app running headless — slash autocomplete, then a grounded answer with live system data: Sessions, compacting, and review all work across surfaces: Underneath: long-term memory with full-text search, todos, shell history, background daemon with calendar schedules, skill packs in SKILL.md format — and an audit ledger ( sk audit ) that logs every tool run, approval, and network egress so you can prove your code never leaked. That last one is the point most cloud tools structurally can't match: their product is your code; ours never sees it. One technical decision: grounding beats instructions The design bet I'd defend: deterministic grounding injected before the model sees the prompt — your paths, sysinfo, URLs, resolved as code, not described in prose. Small local models routinely ignore system-prompt rules, but they can't argue with facts already in context. Same instinct elsewhere: FTS5 full-text search over vector embeddings (zero dependencies, instant, no embedding server eating RAM on a 4GB box), and capability profiles where known models declare their tool protocol instead of paying a probing round-trip to discover it. Bring your own key when you want frontier models — one guided sk connect flow, a dozen providers plus any OpenAI-compatible endpoint, spend caps per session, keys chmod 600 and masked. Local stays the default; cloud is opt-in per key, never structural. Safety is a feature, not a banner Reads auto-run. Writes, deletes, and shell need approval; shell hard-refuses rm -rf / , mkfs , device writes, and fork bombs even if you approve them. URL fetching blocks localhost and private IPs. Multi-tool turns with destructive actions get one plan review up front instead of nag-per-tool. Plan mode ( /plan , F4 ) blocks writes entirely for research sessions, and /rewind undoes agent file edits. Try it uv tool install sidekick-agent[voice] # global `sk`, STT included sk init # guided first-run: hardware → model → verify sk # fullscreen chat — start here Local path needs Ollama ( ollama serve , pull qwen2.5-coder:7b for smarts or llama3.2:3b for speed). 834 tests pass with no Ollama needed. In Part 2 I'll go inside the grounding pipeline — what gets injected, when, and what broke along the way. Built by the Sidekick community. Repo: https://github.com/Faisal-Fayaz/sidekick

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/irfan_wani/sidekick-part-1-a-terminal-companion-on-your-hardware-330k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
