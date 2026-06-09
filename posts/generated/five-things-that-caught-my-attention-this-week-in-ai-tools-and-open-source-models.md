---
title: "Five things that caught my attention this week in AI tools and open-source models"
slug: "five-things-that-caught-my-attention-this-week-in-ai-tools-and-open-source-models"
author: "MORINAGA"
source: "devto_ai"
published: "Tue, 09 Jun 2026 03:53:19 +0000"
description: "A lighter week for me operationally — content refreshes, a YouTube analytics update, some Bluesky queue maintenance. Which meant more time to actually read t..."
keywords: "code, claude, you, mcp, agent, here, servicenow, tools"
generated: "2026-06-09T04:03:32.531595"
---

# Five things that caught my attention this week in AI tools and open-source models

## Overview

A lighter week for me operationally — content refreshes, a YouTube analytics update, some Bluesky queue maintenance. Which meant more time to actually read things. Here are five items that stuck. 1. Claude Code Agent View changes the mental model Anthropic shipped Agent View inside Claude Code on May 11. It's a unified dashboard for managing multiple parallel Claude Code sessions: start a session, send it to the background, check results when you want to. The interface treats individual sessions the way a CI dashboard treats builds. I've been running Claude Code by opening multiple terminals with different working directories. It works, but the overhead of context-switching between tabs adds up fast. A UI that surfaces what each agent is doing without requiring a terminal switch is more than quality-of-life — it shifts Claude Code from "smart terminal" to "orchestration layer." That's the direction I think AI coding tools are heading. The question isn't whether you can have a useful conversation with an AI about code. It's whether you can queue up a batch of distinct tasks, step away, and come back to something actionable. Agent View is an early answer to that question. 2. ZAYA1-8B trained on AMD hardware is a supply chain signal Zyphra released ZAYA1-8B under Apache 2.0 around May 6-7. It's a mixture-of-experts architecture: ~8B total parameters, ~760M active per token. Standard MoE efficiency math. What's not standard: the entire training run used AMD Instinct hardware. The serious open-weights training runs are almost universally done on NVIDIA H100s or A100s. Zyphra shipping a competitive reasoning model that's clean Apache license and trained end-to-end on AMD is a concrete counter-example to "you need NVIDIA to train anything worth using." That doesn't mean AMD is catching up fast enough to matter at scale yet, or that my next fine-tune would go faster on Instinct hardware. It means the GPU monoculture in open-source training has a verifiable crack in it. I'm watching whether other small labs follow. 3. The Harness productivity report has a buried lede Harness released The State of Engineering Excellence 2026 on May 13. The headline: 89% of engineering leaders report improved developer productivity; 88% report improved satisfaction since adopting AI coding tools. The headline is predictable. Every vendor survey about AI tools says the same thing. The part worth reading is the buried finding: AI has outpaced the measurement frameworks organizations use to track productivity. Existing DORA metrics — deployment frequency, change failure rate, MTTR, lead time — weren't designed for workflows where a human is reviewing and steering AI-generated output rather than writing from scratch. If you're building dev tooling and trying to sell to engineering leaders right now, "AI made us faster" is table stakes. "Here's what to measure instead, and here's how we surface it for your team" is the actual product bet worth making. 4. ServiceNow Build Agent went GA inside Claude Code and Cursor ServiceNow announced on May 13 that Build Agent is generally available in ServiceNow Studio and extended its core skills into Claude Code, Cursor, Windsurf, and GitHub Copilot — with governance defaults on. Developers can build with ServiceNow APIs from their own editors without leaving their environment. The governance-by-default choice is the interesting design decision here. Most IDE integrations hand full control to the developer and assume IT will configure guardrails separately. ServiceNow's bet is that enterprise buyers want the platform's access controls and audit trails to travel with the tool automatically. Harder to sell on a feature list; better moat if the bet holds. 5. I removed MCP servers from my pipeline and reliability went up This one is personal. I dropped several MCP server connections from my content pipeline this week (the commit message is "i-removed-mcp-servers-and-my-pipeline-got-more-reliable," which about covers it). MCP servers add real capabilities. They also add failure surfaces: network timeouts, schema drift when a remote API changes without warning, authentication tokens that expire silently at 3 AM. My ETL runs unattended on a cron schedule. When a remote MCP call hangs, the whole job hangs. I didn't always know until I checked results the next morning. The lesson I'm taking: MCP integrations are excellent for interactive sessions where a human is watching and can handle a failure gracefully. For scheduled, unattended workflows, each external dependency is a reliability tax you pay whether or not you're awake to collect it. I'm keeping MCP for interactive use and building local fallback paths for anything production-critical. Part of an ongoing 6-month experiment running three AI-curated directory sites. The technical claims here are real; this article was AI-assisted.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/morinaga/five-things-that-caught-my-attention-this-week-in-ai-tools-and-open-source-models-3hb2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
