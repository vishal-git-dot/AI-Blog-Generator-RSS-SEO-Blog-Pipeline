---
title: "I tried running Sentinel-IR-MCP 0.4+ on my phone via Termux. It stopped me."
slug: "i-tried-running-sentinel-ir-mcp-04-on-my-phone-via-termux-it-stopped-me"
author: "jackymenCZ (jackymenCZ)"
source: "devto_ai"
published: "Fri, 06 Nov 2026 22:46:25 +0000"
description: "I Tried Running Sentinel-IR-MCP inside Termux on Android. Here is What Happened. Everyone is talking about the new Sentinel-IR-MCP 0.4 release and how it shi..."
keywords: "sentinel, mcp, termux, security, setup, project, its, agent"
generated: "2026-11-06T22:54:48.606127"
---

# I tried running Sentinel-IR-MCP 0.4+ on my phone via Termux. It stopped me.

## Overview

I Tried Running Sentinel-IR-MCP inside Termux on Android. Here is What Happened. Everyone is talking about the new Sentinel-IR-MCP 0.4 release and how it shields your local environment from rogue AI prompts. I don't currently have a PC nearby, so I thought: Why not stretch its limits and test it directly on my smartphone using Termux? I fired up the terminal and ran the setup command: bash npx -y sentinel-ir-mcp@0.4 setup The interactive menu popped up instantly, asking me to choose my AI client: text Connect Sentinel-IR to which client? [1-5] 4 I pressed 4 for VS Code—and Sentinel immediately slapped my wrist with this beautiful security rejection: text sentinel-ir-mcp setup: Refusing to give the agent access to your whole home folder (/data/data/com.termux/files/home). Pass a project folder with --project. ~ $ Why this is brilliant Instead of blindly writing a configuration file and exposing my entire Termux home directory to the AI agent, Sentinel's built-in self-defense instinct kicked in. It detected that my current working directory was the root user folder, recognized the massive security risk (exposing history, config keys, and sensitive data), and pulled the emergency brake instantly. It completely locked out the AI agent before it even had a chance to touch anything. The tool proves that you don't need a bulky PC setup to test zero-trust AI architectures—and its security guard rails are as solid on a mobile terminal as they are in production. Absolute chef's kiss for this proactive design 🤔😁 Independent Engineering Projects Built as independent engineering experiments across AI, software analysis, security, and autonomous systems. Evaluated by reproducible evidence, not by the number of layers. Explore the projects: Sentinel Ecosystem: AutoDoc-Sentinel, Sentinel-IR, Sentinel-IR-MCP and related tools. Agentix Lite: Independent security and system-observation project. Find the projects: GitLab repositories | NPM packages Support the work: ⭐ Star the repositories on GitLab. Connect: Follow me here on DEV Community or explore the Playground. Each project is distributed under its own license. Check the corresponding repository or NPM package for licensing terms. Copyright © 2026 jackymenCZ. All rights reserved. Written for the community.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jackymencz/i-tried-running-sentinel-ir-mcp-on-my-phone-via-termux-it-stopped-me-2j41

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
