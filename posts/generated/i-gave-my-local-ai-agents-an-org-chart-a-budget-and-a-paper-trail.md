---
title: "I gave my local AI agents an org chart, a budget, and a paper trail"
slug: "i-gave-my-local-ai-agents-an-org-chart-a-budget-and-a-paper-trail"
author: "Nathan C."
source: "devto_ai"
published: "Tue, 06 Oct 2026 05:45:02 +0000"
description: "Most AI agents die when you close the chat. Mine don't. They're called sparks , and they live in Flash , my open source agent shell for Ollama . Each one get..."
keywords: "you, sparks, one, can, agent, spark, new, they"
generated: "2026-10-06T05:48:43.501847"
---

# I gave my local AI agents an org chart, a budget, and a paper trail

## Overview

Most AI agents die when you close the chat. Mine don't. They're called sparks , and they live in Flash , my open source agent shell for Ollama . Each one gets a name, a goal, a schedule, and lines it must never cross. Then it works on its own, on your machine, and reports back. Make a spark that checks my repo every morning for new issues and tells me which ones look like bugs. Never comment on anything. Two sparks were fine. Six were six interns who had never met. So today they got a company. Teams and an org chart Any spark can report to a lead . Its reports roll up to the lead, and the lead tells you what matters, so you read one report instead of six. Each team is drawn as a live org chart, with reports flying up the lines as comets. /sparks teams add Dev Team Built-in templates (Dev Team, Personal Desk) start paused , so nothing burns your GPU before you've looked. Hiring needs your yes A spark can propose hiring a new spark, or letting one go, with a reason. It waits as a card until you approve or decline. Budgets Off by default. Turn one on and a spark gets tokens per hour, day, week or month. When it runs out, it pauses. /sparks budget scout 50k/day Local tokens still cost you: they're GPU time, and a loop at 3am is still a loop. An audit log you can't quietly edit Every shift, tool call, approval and change goes into an append-only log. Each entry carries the hash of the one before it: hashlib . sha256 (( previous + body ). encode ( " utf-8 " )). hexdigest () Edit a line by hand and verification points at it. Pause all, Stop all Pause all stops new shifts and lets running ones finish. Stop all is the big red button. Real DevTools for the agent The agent can already drive a web page. Now devtools gives it the network log, full requests, the console, a JS console, and computed styles. A screenshot can't show a 404. This can. Notifications, on your terms notify_user pops up a toast in the web UI, a browser notification in a background tab, or a desktop notification. It's rate limited, and you set the limit: /notify 8 per 30m The rest Default model for new sparks. If you ollama rm it, sparks fall back to another model and say so instead of crashing. Images the agent sends now show inline in the chat. Click one to open it in the side panel. 10 features in one day, 1,916 tests passing, 0 API keys. Try it curl -fsSL https://raw.githubusercontent.com/Natuworkguy/Flash/main/install.sh | bash flash Then type /sparks new . Stars on GitHub help a lot. What job would you give an agent that works for you around the clock? The best answer becomes a template.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/natuworkguy/i-gave-my-local-ai-agents-an-org-chart-a-budget-and-a-paper-trail-4ff8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
