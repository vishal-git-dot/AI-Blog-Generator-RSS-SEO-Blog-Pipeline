---
title: "I built a no-config way to host apps built in AI chats"
slug: "i-built-a-no-config-way-to-host-apps-built-in-ai-chats"
author: "Srujan Ranpise"
source: "devto_webdev"
published: "Wed, 11 Nov 2026 05:24:44 +0000"
description: "Woke up to 310+ installs on the Chrome Web Store, one month after launching Deployinn. Here's the story of why I built it. The problem AI chats are great at ..."
keywords: "code, your, built, mcp, one, deployinn, you, some"
generated: "2026-11-11T05:37:22.170358"
---

# I built a no-config way to host apps built in AI chats

## Overview

Woke up to 310+ installs on the Chrome Web Store, one month after launching Deployinn. Here's the story of why I built it. The problem AI chats are great at building apps. Claude, ChatGPT and Gemini can give you a working frontend, backend or full-stack project in a few minutes. Then you hit the part that isn't fun: Copy the code out of the chat Push it to a repo Pick a host and set up the project Wire up env vars Add a database Fix the build that breaks for some small reason For a personal project, that setup often took longer than writing the app. I got tired of it, so I built my own deployment platform. What Deployinn does Deployinn takes the code your AI builds and puts it live, with no config. There are three ways to use it: 1. Chrome extension. A deploy button appears inside the AI chat. Click it and the code goes live. 2. MCP connector. Add the connector link to your AI app, build something, and type "deploy this". 3. Agent CLI. For hands-free deploys from tools like Claude Code. A few things happen without extra setup: Your code is committed to your own GitHub A Postgres database is connected automatically when your app needs one The server scales up when traffic spikes It currently supports frontend, backend, full-stack and MCP server deploys. What I learned 1. The setup steps were the real problem. I thought the hard part would be hosting. It was actually the manual steps between "the AI wrote the code" and "it's live". 2. Meeting people where they already are matters. A deploy button inside the chat gets used more than a separate dashboard people have to remember to open. 3. Offering several entry points helps. Some people want a one-click button, some want to just ask the AI, and some want a CLI. I started with the extension and added MCP and the CLI later. 4. Early users find the edge cases quickly. The MCP connector and CLI are the newest parts, so they're the least battle-tested. Feedback on failed deploys has been the most useful input so far. Try it There's a free plan. To celebrate the 310+ installs, I'm also giving the Pro plan away for free with the code PROFREE . 👉 deployinn.com I'd love your feedback Where do your AI-built deploys usually fail? Which hosts, platforms or languages would you want next? Does the MCP "just ask" flow feel natural, or would you prefer a button? Let me know in the comments. I read every one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/srujan71/i-built-a-no-config-way-to-host-apps-built-in-ai-chats-3iib

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
