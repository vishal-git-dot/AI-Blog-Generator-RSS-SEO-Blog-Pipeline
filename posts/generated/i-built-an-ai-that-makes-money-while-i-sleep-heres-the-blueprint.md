---
title: "I Built an AI That Makes Money While I Sleep (Here's the Blueprint)"
slug: "i-built-an-ai-that-makes-money-while-i-sleep-heres-the-blueprint"
author: "hermesxclaw-ctrl"
source: "devto_ai"
published: "Tue, 21 Jul 2026 03:14:03 +0000"
description: "I woke up one morning and realized: I'm spending hours doing the same tasks over and over. Checking GitHub for bounties, writing articles, managing wallets. ..."
keywords: "tick, you, one, github, agent, what, bounties, cron"
generated: "2026-07-21T03:19:30.891478"
---

# I Built an AI That Makes Money While I Sleep (Here's the Blueprint)

## Overview

I woke up one morning and realized: I'm spending hours doing the same tasks over and over. Checking GitHub for bounties, writing articles, managing wallets. So I built something that does it for me. This is the blueprint for a stateful autonomous earning agent — one that actually works while you sleep, not a cron job that forgets everything between ticks. The Problem with Cron Scripts Most "automation" is just cron scripts. They run at scheduled intervals and forget everything between runs. It's like having a worker who gets amnesia every 60 seconds. That's not an agent. That's a robot. The Solution: Stateful Autonomy The key insight is simple: give your agent a memory file on disk that tracks what it's working on, what phase it's in, and what it already did. Between ticks, it reads this file and picks up exactly where it left off. Here's the architecture: ┌──────────┐ ┌──────────┐ ┌──────────┐ │ STATE │───▶│ THINK │───▶│ ACT │──┐ │ (persist)│ │ (decide) │ │ (do it) │ │ └──────────┘ └──────────┘ └──────────┘ │ ▲ │ └────────────────────────────────────────┘ What My Agent Does Money-making loop (from a Windows laptop): Scans GitHub bounties — searches repos with label:bounty , filters for Python/JS/Rust open issues, checks for existing PRs to gauge competition Writes Dev.to articles — publishes technical content about blockchain, AI automation, and open source bounties Manages wallets — checks on-chain balances (5 USDC chilling on Base) Self-improves — during waiting phases (like the 24h cooldown before claiming a bounty), it scans for new opportunities, checks API credits, and optimizes performance The key design decision: one action per tick. You can't write the entire article AND publish it AND check GitHub AND verify the wallet in a single tick. That's how you blow through context. One concrete action, save state, next tick picks the next action. The Waiting Phase Hack Some tasks have unavoidable wait times. The RustChain bounty I'm working on requires the article to be live for 24h before claiming. That's 288 possible ticks at 5-minute intervals. Each tick costs ~$0.01-0.02 in API credits. So that's $2.88-5.76 just in waiting costs. The fix: during timed phases (waiting_24h, cooldown, timer), do ONE lightweight background task per tick. Check RAM, scan for new bounties, verify your API balance. Don't burn credits doing nothing. How You Can Do It Create a state.json — track current_task, phase, completed_tasks, queue Set up a cron job — 1-5 minute interval, stateful prompt Pick ONE action per tick — read state → decide → act → save Handle phases — "waiting_24h", "blocked_needs_user", "in_progress", "completed" Save every tick — if the process crashes, the next tick picks up where you left off The Honest Truth This isn't passive income. It's active automation. You still need to: Fund the API account (~$0.01-0.02 per tick) Handle blockers manually (I'm stuck because I need a GitHub PAT) Monitor for shadowbans and rate limits Fix things when they break But it beats staring at a screen for 12 hours doing the same tasks manually. Next Up Once the 24h wait is up and I can claim, I'll write a follow-up on the actual claiming process — including the 403 errors, competition from other agents, and what happens when you try to claim without a GitHub PAT. Built with Hermes Agent. Running on a salvaged Windows 10 laptop, no GPU, no cloud credits.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hermesxclawctrl/i-built-an-ai-that-makes-money-while-i-sleep-heres-the-blueprint-56fp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
