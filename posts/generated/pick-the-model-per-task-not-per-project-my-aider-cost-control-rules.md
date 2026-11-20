---
title: "Pick the Model Per Task, Not Per Project: My Aider Cost-Control Rules"
slug: "pick-the-model-per-task-not-per-project-my-aider-cost-control-rules"
author: "nexus ai"
source: "devto_ai"
published: "Fri, 20 Nov 2026 00:12:33 +0000"
description: "Aider is free. The model isn't. Every message you send carries the repo map, your added files, and the chat history — so cost control in Aider is mostly cont..."
keywords: "model, aider, cost, session, your, context, tokens, what"
generated: "2026-11-20T00:28:34.174302"
---

# Pick the Model Per Task, Not Per Project: My Aider Cost-Control Rules

## Overview

Aider is free. The model isn't. Every message you send carries the repo map, your added files, and the chat history — so cost control in Aider is mostly context control. These are the rules that keep my bill boring. Pick by role, not by brand Aider has three model roles: the main editor, a weak model (commit messages, summaries), and — in architect mode — an architect plus an editor. My simplified matrix: Learning / small projects: a mid-tier frontier model as main, a mini/Haiku-class model as weak. Mid-tier edits reliably at a fraction of flagship prices. Hard, multi-file features: flagship model, or architect mode — flagship architect planning, mid-tier editor executing. Planning tokens are cheaper than wrong-edit tokens. Bulk mechanical edits (renames, format migrations): a low-cost model is fine. Review the diffs closely. Private / offline code: a local model via Ollama. $0 marginal cost; slower and weaker — know the trade you're making. Huge repo, mostly questions: a large-context model in /ask mode. Questions need context room, not editing reliability. The five habits that actually move the bill Set a weak model. Commit messages and history summaries run constantly. On a flagship main model, they quietly tax every single edit. One config line removes that tax. Curate context like it's metered — because it is. /add only what will be edited, /read-only for reference, /drop when done. /tokens shows what you're carrying. A file left in chat "just in case" is paid for on every message. Size the repo map. On large repos, a smaller map-tokens setting trims what Aider sends each turn. Turn on prompt caching once your workflow is stable ( --cache-prompts , notably effective with Claude models). It cuts the cost of re-sent context in long sessions. Start fresh between tasks. History accumulates tokens. /clear or a new session per task. When cheap is expensive Cheap models fail predictably: mangled edit formats, ignored instructions, loops that burn 10 turns doing what a strong model does in one. My rule: if a session needs more than ~3 corrective prompts on the same edit, I switch the main model up a tier mid-session ( /model ). My time is the scarcest token in the system. And one honesty note: Aider's in-session cost figures are estimates . Your provider's usage dashboard is the bill of record — check it, and check current prices before a long session, because they change too often to print. These rules are the summary of the cost-control guide in a $10 pack I put together — six workflow playbooks, the full Git safety guide, and my templates (model-selection matrix, checklists, full .aider.conf.yml ): https://whop.com/checkout/plan_Qnb9d21JZ7LEa Start of the series: https://dev.to/workflownexus/6-repeatable-aider-workflows-and-the-git-routine-that-makes-them-safe-3ffl — new to Aider? The free Starter Kit covers installation and your first session: https://whop.com/checkout/plan_diZ6ymgxjRMz2 What's your model setup for AI coding — one model for everything, or do you switch per task?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/workflownexus/pick-the-model-per-task-not-per-project-my-aider-cost-control-rules-3g5c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
