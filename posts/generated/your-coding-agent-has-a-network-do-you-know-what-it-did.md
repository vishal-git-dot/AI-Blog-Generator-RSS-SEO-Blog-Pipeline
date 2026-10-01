---
title: "Your Coding Agent Has a Network. Do You Know What It Did?"
slug: "your-coding-agent-has-a-network-do-you-know-what-it-did"
author: "Rishi G"
source: "devto_ai"
published: "Thu, 01 Oct 2026 22:19:15 +0000"
description: "First off, thanks to everyone who read and commented on my last post! Your coding agent tells you all tests pass. Sometimes that's not true. The discussion a..."
keywords: "what, you, agent, did, network, coding, actually, another"
generated: "2026-10-01T22:31:42.471152"
---

# Your Coding Agent Has a Network. Do You Know What It Did?

## Overview

First off, thanks to everyone who read and commented on my last post! Your coding agent tells you all tests pass. Sometimes that's not true. The discussion around that post got me thinking about another dimension of the same problem. As I have been developing Rashomon, I have been focused on one question: what did the agent actually do? Rashomon keeps an independent record of agent execution and compares it against what the agent claims happened. Did the command actually run? Did it fail? Did the expected test execute? Did a subagent do something that never made it into the final summary? But there is another layer of agent behavior that execution records alone do not capture: What happened on the network? A command doesn't tell you everything. Take something simple like: npm install You can verify that the command ran. But you do not necessarily know everything that happened as a result. The process may have contacted package registries, downloaded files, reached Git hosts, or communicated with other external services. Or imagine an agent says: "I verified the API and deployed the fix." You might be able to verify that it ran the relevant commands. But did it actually reach the API it claimed to reach? What other destinations did it contact? Did a subprocess or subagent make network requests that were not mentioned? These are questions about what the agent communicated with, rather than simply what it executed. Why this matters more with autonomous agents? Coding agents are increasingly capable of operating without someone watching every command. They can install dependencies, call APIs, interact with cloud services, spawn subagents, and run hundreds of commands during a single session. The agent transcript gives you one account of what happened. Execution evidence gives you another. Network activity can give you another. The interesting question is what happens when you start putting those pieces together. If an agent says it deployed a change, for example, you could potentially look at both the deployment command it executed and the network activity associated with it. That doesn't prove intent by itself, but it gives you more independent evidence to compare against the agent's claims. This has gotten me interested in exploring how network-level visibility could complement what we are building with Rashomon. Rashomon is focused on what actually ran. Network visibility could provide another piece of the picture: what those processes actually communicated with. I think combining those perspectives could help answer much more interesting questions about autonomous coding sessions. The broader idea is the same one behind Rashomon: As coding agents become more autonomous, we should have independent evidence of what they actually did, rather than relying entirely on their own summary. I'm curious what other developers think. If you could see both what your coding agent executed and what it communicated with, what would you want to know?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rishi_g_25/your-coding-agent-has-a-network-do-you-know-what-it-did-1bdg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
