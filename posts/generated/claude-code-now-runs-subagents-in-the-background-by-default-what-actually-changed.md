---
title: "Claude Code Now Runs Subagents in the Background by Default — What Actually Changed"
slug: "claude-code-now-runs-subagents-in-the-background-by-default-what-actually-changed"
author: "Alvarito1983"
source: "devto_ai"
published: "Fri, 07 Aug 2026 07:15:58 +0000"
description: "Original article in Spanish on El Rack: Claude Code ya no espera a que le mires: subagentes en segundo plano por defecto I run Claude Code daily as my main d..."
keywords: "claude, code, subagents, default, run, sessions, opus, context"
generated: "2026-08-07T07:23:56.538034"
---

# Claude Code Now Runs Subagents in the Background by Default — What Actually Changed

## Overview

Original article in Spanish on El Rack: Claude Code ya no espera a que le mires: subagentes en segundo plano por defecto I run Claude Code daily as my main dev agent, both locally and over SSH against a VPS running a handful of production sites. A change that landed over the last few weeks quietly rewired how I work with it: subagents now run in the background by default. Before, when Code delegated a task to a subagent, the conversation blocked until that subagent finished. Since July 1, it keeps working on other things while the subagent runs, and notifies you when it's done. For anyone running long sessions with --dangerously-skip-permissions and checking back hours later, that's the difference between a tool that waits and one that actually works unattended. What changes day to day My workflow has always been the same: approve the initial plan, then let Code proceed without confirmation on every step, stopping only on real errors. With background subagents, that autonomy compounds. I can now ask it to audit a site, generate new content, and review config files at the same time — each running as an independent subagent instead of queuing one after another. Two limits matter here: a default cap of 20 concurrent subagents, and nesting now allowed up to 3 levels deep (up from 1). Both exist for a reason — it's easy for a large task to branch further than you expect if nothing constrains it. Sonnet 5 and Opus 5: 1M context is no longer the exception Claude Sonnet 5 became the default model in late June, with a native 1M-token context window. Claude Opus 5 replaced it as the default Opus model on July 24, also with 1M context. In long sessions — the kind you get during a full editorial rebuild of a site — I used to watch /context and run /compact mid-task to avoid losing thread. Now I run noticeably longer sessions without touching either. It's not magic: auto-compaction still kicks in, and cost on very long Opus sessions is worth watching, but the practical ceiling moved. The security fix that actually matters As someone who manages production infrastructure, this is the line item I care about most: in August, a fix landed for worktree-isolated sessions (and their subagents) that could run destructive git commands against the main checkout. When you're launching subagents with broad permissions against something that matters, broken isolation like that is exactly the failure mode you don't want. That it got closed quickly is a good sign — but also a reminder that "autonomous" and "unsupervised" aren't the same thing. I still review the final report of every session rather than assuming no visible errors means everything went well. Where I still draw lines With this much autonomy, the temptation is to hand off increasingly ambitious tasks and walk away. I don't do that on anything touching client-facing production servers — those sessions stay interactive, with explicit confirmation on sensitive steps. Where I do give it full rein is on my own infrastructure, where the cost of a mistake is low and recoverable. That distinction, more than any config flag, is what actually determines how much autonomy a session gets. Bottom line Background-by-default subagents are the change that's altered my day-to-day with Claude Code the most in months — not because it's flashy, but because it fits how I was already using it: approve the plan, let it run. The 1M context on Sonnet 5 and Opus 5 supports that well. The worktree isolation fix is the reminder that more autonomy means reviewing final output more carefully, not less. Original (Spanish, full version with pros/cons and more context): https://elrack.es/herramientas-ia/claude-code-subagentes-segundo-plano-opus-5-2026/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alvarito1983/claude-code-now-runs-subagents-in-the-background-by-default-what-actually-changed-54kb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
