---
title: "I built an open-source platform where AI agents work like governed employees, and now they can use desktop apps"
slug: "i-built-an-open-source-platform-where-ai-agents-work-like-governed-employees-and-now-they-can-use-desktop-apps"
author: "Valter Eduardo"
source: "devto_python"
published: "Thu, 05 Nov 2026 05:49:54 +0000"
description: "Most "AI agent" demos stop at the moment it gets interesting for a company: who's allowed to let the agent pay an invoice, send an email or change a record, ..."
keywords: "agent, hangar, them, desktop, agents, use, end, where"
generated: "2026-11-05T06:01:18.140139"
---

# I built an open-source platform where AI agents work like governed employees, and now they can use desktop apps

## Overview

Most "AI agent" demos stop at the moment it gets interesting for a company: who's allowed to let the agent pay an invoice, send an email or change a record, and how do you know what it did? That's the problem I've been working on with Agent Hangar , an open-source (Apache-2.0), self-hosted platform where agents work as digital employees . It covers the whole range: from a simple chat agent, to agents built in other frameworks, all the way to a Digital employee with a harness (Claude Code, Codex) that works in your IDE with its own role, budget and authority. GitHub: https://github.com/valteresj2/agent-hangar valteresj2 / agent-hangar One home for every AI agent. Build, test and ship agents once, then use them from Claude, ChatGPT, Codex, Cursor, VS Code or Slack (MCP, OpenAI-compatible, A2A, ACP). Self-hosted, with teams, approvals, audit, memory and multi-agent composition. Docker or Kubernetes. ⌂ Agent Hangar One home for every AI agent your company builds, whatever tool built it. People create agents where they already work: Claude, ChatGPT, Cursor, VS Code, Codex, OpenCode. Agent Hangar brings them all to one place, runs each one in its own container, and makes them usable from any platform over OpenAI-compatible, MCP, A2A and ACP , and inside your own app over AG-UI . Everyone can find them, talk to them, and combine them into new agents. Interactive demo · Desktop app · Computer use · Example · Install · Features · How it works · Website · Docs · Roadmap · Português The user portal, recorded on a local install · MP4 version Watch: Agent Hangar end to end agent-hangar-end-to-end.mp4 2 min 45 s, with captions: what Agent Hangar is, how to install it, build, test and ship agents, use them over every protocol (inside your… View on GitHub The idea: an agent is an employee, not a script Each Digital employee has: a role and a team , and a person it reports to; a monthly budget in tokens and money; a list of allowed tools (connectors, MCP servers, platform tools); an authority level : anything above it waits for a person's approval. Every task has a timeline with each step, the decisions taken and who approved them. New: governed computer use A lot of real work still lives in desktop applications with no API: a legacy ERP, a spreadsheet, an installed system. In the latest release, a Digital employee can operate them the way a person does, by looking at the screen . How it stays safe: It runs in an isolated Linux desktop (built on Cua ) with no internet access, and the agent can open only the apps allowed for it. Each action returns the window's screenshot plus its accessible elements, numbered. Apps with no accessibility info are operated by position on the screenshot. Clicks that save, post, send or pay go through the authority check. The approval request carries the screenshot, and the click happens exactly where the person approved. Passwords stay in the vault. The agent types secret://name ; the model and the timeline never see the value. I tested it end to end with a real model (DeepSeek through OpenRouter) on 8 cases: logging in with a vault password, a date typed in another format, a nonexistent invoice, a confirmation dialog, menus with scrolling, saving a spreadsheet with "Save as", reading a CSV, and two payments in one task without duplicates. 8 of 8 passed. The test also caught a real bug (tool events showing twice on the timeline), fixed in 0.58.4. There's an 80-second video of the run in the README. Turning it on docker compose --profile desktop up -d desktop Then list the allowed apps in the employee's settings. Two sample apps come with it (Gnumeric and a Tk "legacy ERP"); you add your own in the desktop's Dockerfile. What else is in there Any LLM per agent: OpenAI, Anthropic, Gemini, OpenRouter, a corporate gateway, Ollama, any OpenAI-compatible endpoint Agent memory as a graph on PostgreSQL with Apache AGE Warnings before a model an agent uses is deprecated An MCP endpoint, SSO/SCIM, Helm and Terraform installs, a desktop app Feedback welcome I'd love to hear what you'd need to trust an agent with real work, and where the safety boundaries for computer use should be. Issues and PRs are open on GitHub: https://github.com/valteresj2/agent-hangar

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/valteresj/i-built-an-open-source-platform-where-ai-agents-work-like-governed-employees-and-now-they-can-use-1e0g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
