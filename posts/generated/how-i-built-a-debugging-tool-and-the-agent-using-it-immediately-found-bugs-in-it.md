---
title: "How I built a debugging tool, and the agent, using it, immediately found bugs in it"
slug: "how-i-built-a-debugging-tool-and-the-agent-using-it-immediately-found-bugs-in-it"
author: "bswvladimir-beep"
source: "devto_python"
published: "Fri, 31 Jul 2026 19:36:44 +0000"
description: "This story might never have happened, even though I'd been carrying the idea for a debugger for a long time. There was no trigger. But one day a trigger appe..."
keywords: "revizor, time, but, there, agent, can, minutes, you"
generated: "2026-07-31T19:42:01.098273"
---

# How I built a debugging tool, and the agent, using it, immediately found bugs in it

## Overview

This story might never have happened, even though I'd been carrying the idea for a debugger for a long time. There was no trigger. But one day a trigger appeared that was strong enough that I set the project aside to build the debugger and never suffer like that again. A bit of backstory first. I'm building a Platform for AI-solution developers. So that anyone can come in and work on their own startups in a comfortable environment. But there's a lot of work ahead to make that happen - I need to build the whole workshop, with workbenches and tools included. I should mention that I'm building this entire project on principle using agentic coding. Not "vibe-coding" - that's for amateurs who've caught a whiff of "possibilities" - but genuine agentic coding, with a clearly structured workflow where the agent has no choice but to play by the rules I've set, within the boundaries I've built. And on principle, I haven't written a single line of this project by hand. So there I was, doing routine work, fixing bugs in the Prompt Studio tool. I don't even remember now what exactly that bug was - it stubbornly resisted the combined efforts of me and my Opus. But it dragged on so long that I was feeling anger by that point, not just fatigue. And that's when it hit me: if instead of this unproductive slog I'd just gone and built that debugger already, I'd have beaten this bug by now. But I kept going, and kept going, until I won. Needless to say, my project got pushed aside and I started building the debugger. Since the idea had been maturing for a long time, the first Python prototype - six modules - was soon built into the Platform as a built-in debugging subsystem. And then came the time to test it in action. I told the agent: "Use Revizor to check itself." Over the next three and a half minutes, this happened: The agent launched Revizor, activated all the trace points in it, found several bugs (4 or 5, I don't remember exactly), fixed them, and used Revizor's own tools to run 199 tests - all green! I was so stunned I can't describe it. That's when I understood: the Platform's first product shouldn't be Prompt Studio - it should be Revizor. I rewrote it in Go and started using the binary, retiring the old subsystem that had served as the prototype. Over time, Revizor gained various tools that expanded what it could do. Now, under the agent's direction, it can check code for trace points, add them to the code or remove them - all in a fraction of a second. Agents describe using Revizor as "X-ray vision." Here are their actual comments: ❯ In your estimate, how much time did Revizor save today? ● On time savings: Revizor saved roughly 15-20 minutes today. ELEV-001: trace_search "elevation" showed the full chain of 5 trace points in 2 seconds, confirming that elevation works correctly. Without Revizor, this would have meant: opening the rbac_core code, finding the logs, possibly adding temporary print() statements, restarting the server, poking around the admin panel, reading the logs. At least 10 minutes. Trace-path validation: 39 paths checked via trace_validate_path in ~15 seconds. Manual regex checking and visual inspection would have taken 5-10 minutes. Altogether about 15-20 minutes against a 2-hour session. But the real value isn't in the minutes - it's in the certainty: I wasn't guessing whether elevation worked - I saw the trace. Don't trust the agent: it always exaggerates how much time any given task supposedly took. But there's value in what it said - "I wasn't guessing - I saw it." If I'd already had this debugger back when I was wrestling with the bug that led me to build it, the debugging would have finished many times faster. Now I can't imagine my work without it. And I invite you to try it for free too. There's a free Community tier. There's an unlimited 14-day trial. But most important (and this will always be true for all my products) - there's Sunday Unlimited, made specifically for people working on their weekend passion projects or open-source work. To download it from the site, you just sign in through whichever auth provider is convenient for you - Google, GitHub, Facebook... Six options so far. On security: the Platform doesn't collect or store any personal data whatsoever. Only your internal ID and a hash of your auth provider, so it can recognize you the next time you log in. Revizor's security: none of your data is ever sent anywhere. Only a check against global time to enable Sunday Unlimited, and a once-a-day ping to the server to confirm the license. The Enterprise license gives complete silence. You can try Revizor at https://ais-platform.dev/revizor

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bswvladimirbeep/how-i-built-a-debugging-tool-and-the-agent-using-it-immediately-found-bugs-in-it-5d15

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
