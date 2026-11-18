---
title: "Give Claude Code a Memory: claude-mem Remembers Between Sessions"
slug: "give-claude-code-a-memory-claude-mem-remembers-between-sessions"
author: "oVu X"
source: "devto_ai"
published: "Wed, 18 Nov 2026 15:17:46 +0000"
description: "What it is claude-mem is a free, open-source tool that gives your coding agent a memory across sessions. A coding agent is a program that writes and edits co..."
keywords: "you, your, claude, mem, memory, agent, session, project"
generated: "2026-11-18T15:25:47.042450"
---

# Give Claude Code a Memory: claude-mem Remembers Between Sessions

## Overview

What it is claude-mem is a free, open-source tool that gives your coding agent a memory across sessions. A coding agent is a program that writes and edits code for you from plain prompts. Each new session starts blank. The agent re-reads the same files, re-asks the same questions, and repeats mistakes you already fixed. claude-mem records what happens in each session, and it hands the key facts to the next session. The project lives at thedotmack/claude-mem on GitHub. It holds more than 118,000 stars, and it uses the Apache-2.0 license. The current release is version 16.0.0, published 18 November 2026. How it works claude-mem hooks into your coding agent. A hook is a small step that runs when a set event starts or ends. The hooks watch SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, and SessionEnd. Each event sends the tool activity to a small local worker on your machine. A second agent, called the observer, turns that activity into short notes. When a session ends, the observer writes a summary. The next session opens with a short index of past notes. It pulls full details only when it needs them. Your memory lives in a folder named .claude-mem in your home folder. The notes sit in a local database file, and a search index helps the agent find old work fast. The agent can also search your history in three steps: find an index entry, view the timeline around it, and fetch the full note. You can also run /learn-codebase to front-load a whole repo, which takes about five minutes on a typical repo. How to start Run one command in your terminal: npx claude-mem install. The installer finds the coding agents on your machine, and it asks which ones to set up. Then restart Claude Code. Your second session in a project opens with memory from the first. To test it, do real work in one session, close it, and open a new session in the same project. Ask the agent what you decided last time. If it recalls the choice, the memory works. You need Node.js 20.19 or later, or Node.js 22.12 or later. The installer adds Bun and uv itself when they are missing. Do not use npm install -g claude-mem. That command installs the library only. It does not set up the hooks or start the worker. Honest limits claude-mem is free, but its memory needs a model to write the notes. The installer asks you to sign in through your browser with a magic link. No card is needed to sign in. If you pick the claude-mem observer, it starts a 30-day free trial, and the checkout page asks for a payment method. After the trial ends, memory falls back to your Anthropic plan unless you subscribe. You can skip sign-in with a provider flag, or use your own OpenRouter or Gemini key. The project says the observer runs off-plan, so you get up to 100 percent more use from your plan. Treat that number as the project claim, not a test result. Anonymous use data is on by default, and you can turn it off with npx claude-mem telemetry disable. Tool screenshots stay on your machine by default, and they upload only when cloud sync is on. Your memory stays local unless you turn cloud sync on. Wrap text in tags to keep it out of memory. One caution from the project history: in late October 2026, a user report said the installer sent 30 days of prompts to the project server. The report said this happened without asking first. That report is now closed, and the current installer asks you to choose each option. Read the setup screens with care before you accept them. Verdict claude-mem solves a real pain: every coding session starts blank, and re-teaching the agent costs time. One command sets it up, and the memory stays on your machine unless you choose cloud sync. The trial asks for a payment method, so set a reminder before day 30 if you do not plan to pay. The privacy history shows why you should read each setup screen. If you use Claude Code each day, try it on one project first. Watch the second session. If the agent recalls your last choice, keep it. Follow along I test AI tools and build in public: GitHub: https://github.com/ovu-lab YouTube: https://youtube.com/@oVuCyber

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ovulab/give-claude-code-a-memory-claude-mem-remembers-between-sessions-20e7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
