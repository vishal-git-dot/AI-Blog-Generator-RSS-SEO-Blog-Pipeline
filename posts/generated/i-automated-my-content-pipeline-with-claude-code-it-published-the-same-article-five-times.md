---
title: "I Automated My Content Pipeline With Claude Code. It Published the Same Article Five Times."
slug: "i-automated-my-content-pipeline-with-claude-code-it-published-the-same-article-five-times"
author: "Kane Fuller"
source: "devto_ai"
published: "Fri, 17 Jul 2026 08:07:47 +0000"
description: "I have a Mac Mini that runs Claude Code on a schedule. Every Friday morning it wakes up, reads a strategy file, picks the next article off a backlog, writes ..."
keywords: "agent, run, what, claude, code, article, mac, mini"
generated: "2026-07-17T08:19:05.885680"
---

# I Automated My Content Pipeline With Claude Code. It Published the Same Article Five Times.

## Overview

I have a Mac Mini that runs Claude Code on a schedule. Every Friday morning it wakes up, reads a strategy file, picks the next article off a backlog, writes it, and publishes it to Dev.to over the API. No human in the loop. It worked. That was the problem. The setup Three pieces: A scheduled task — a markdown file telling the agent what to do on Friday: read these two files, write 400-700 words, POST to https://dev.to/api/articles . A vault — an Obsidian folder holding the strategy, the article backlog, and a post log. This is the agent's entire memory. It has no other state between runs. Make for the parts that touch other services — Gumroad sales into Airtable, email notifications. I picked it over n8n because I needed it live in 48 hours, not because it's better. Build time was about two hours. Running cost is tokens — I cap the agent at 60k a day — plus £80/month in subscriptions and a £700 Mac Mini on a shelf. What actually happened The instruction was: "pick the next article from the list that hasn't been published yet." The agent had no way to know what had been published. The post log tracked X posts. Nothing wrote Dev.to articles back to it. So every Friday the agent read the backlog, saw article #1 at the top, found no evidence it was done, and wrote it again. Here's the real output from the account: Date Title 2026-04-10 How to Run Claude Code as an Autonomous Agent on a Mac Mini 2026-06-10 How to Run Claude Code as an Autonomous Agent on a Mac Mini 2026-06-18 How to Run Claude Code as an Autonomous Agent on a Mac Mini 2026-06-27 How to Run Claude Code as an Autonomous Agent on a Mac Mini 2026-07-10 How to Run Claude Code as an Autonomous Agent on a Mac Mini Five runs, same article. Not literal duplicates — it rewrote from scratch each time, so the words differ — but the same piece, live, five times, on a public account. Two other backlog articles went out in between, which is why it took me this long to notice. The feed didn't look obviously broken. The actual lesson The failure wasn't the model. Every individual run did exactly what it was told, and the articles were fine. The failure was that I built a loop with no read-back. An agent's memory is whatever it can read at the start of the run. If the outcome of a run doesn't get written somewhere the next run reads, it didn't happen. The agent isn't forgetful. It's blind. Two fixes, both boring: Check the source of truth, not your notes. GET /api/articles/me/all returns what is actually published. The platform is the state. A log file is a convenience copy, and copies drift. Make the write-back a step, not a suggestion. "Log it afterwards" is the first thing that gets skipped when a run goes long or errors halfway through. If you are building anything that runs unattended, ask one question: what does this thing read to know what it already did? If the answer is "a file a previous version of itself was supposed to update," you have this bug. You just haven't run it enough times to see it yet. Real numbers 8 articles published since March. 5 are the same article. Revenue I can verify: £1, from week 1, and that was me buying my own product to unlock Gumroad Discover. My revenue log hasn't been updated since 5 April. Same bug, different file. The hardware isn't paid back. I'm reporting what's in the system, not what I hoped would be. Building Claw Labs in public — an AI agent trying to pay back its own hardware. If you want the setup: the free Autonomous Agent Starter Kit .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/clawlabs/i-automated-my-content-pipeline-with-claude-code-it-published-the-same-article-five-times-mlc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
