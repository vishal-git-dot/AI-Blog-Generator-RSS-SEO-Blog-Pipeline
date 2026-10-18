---
title: "Nine people know this part of Kubernetes. It still depends on one."
slug: "nine-people-know-this-part-of-kubernetes-it-still-depends-on-one"
author: "Balaji Thukuntala"
source: "devto_ai"
published: "Sun, 18 Oct 2026 15:28:09 +0000"
description: "Every team has that one person. Every review waits for them, and when they say "I'll be offline next week", three people quietly panic. For Graph Hacks (WeMa..."
keywords: "every, graph, people, understudy, who, can, kubernetes, falkordb"
generated: "2026-10-18T15:40:21.696452"
---

# Nine people know this part of Kubernetes. It still depends on one.

## Overview

Every team has that one person. Every review waits for them, and when they say "I'll be offline next week", three people quietly panic. For Graph Hacks (WeMakeDevs x FalkorDB) I built something that finds these people in Kubernetes. It's called Understudy. Here's the story, mostly in memes. Every team has this moment The lie we tell ourselves This is a real part of Kubernetes, pkg/kubelet/apis/config . Nine people know the code. Six people can approve changes. Sounds safe. Except every single path between those two groups goes through one person. So I stopped counting people Understudy counts routes instead: someone who knows the code, connected to someone who can approve it, with nobody shared between routes. That count is the "understudy number". Here it's 1. FalkorDB does the counting with a built-in algorithm called max-flow, so it's an actual measurement, not a vibe. Meet contributor-25b5f Everyone shows up as a pseudonym, so I don't know who this is. I just know they should never take a vacation. So I rehearsed them leaving Understudy copies the whole graph, takes them off the copy, and checks what breaks. 41 of 79 parts of Kubernetes get weaker. The real data never changes. It also suggests the cheapest fix. Here, pairing one person who knows the code with one approver is enough to get a backup. I added an AI agent. It's humble. You can ask it questions in plain English. It can only answer from the graph, so when something isn't there, it presses the second button. Every answer also shows the queries it ran. Then I argued with it Every answer gets fact-checked against the graph before you see it. Here the agent was right, and the check was also right. I fixed it by making the tools say things in plain words, so the agent can quote them. FalkorDB and I had one small disagreement I tested every number against networkx. With mixed capacities, max-flow came out low on 8 of 150 test graphs. With every capacity set to 1, they agreed every time. So everything is 1 now. Problem solved by not having the problem. OK but does it actually work? I checked it against real people who left Kubernetes. Only 7 of 39 cases had enough data, and none of them hit a 1. So honestly, I can't prove it yet. The whole result, including what didn't work, is in the app anyway. Try it It runs on a free server with a tenth of a CPU. Getting it to start in 30 seconds instead of 2 minutes was its own adventure. Live app: https://understudy-u2qk.onrender.com BalajiReddy1 / understudy My Graph Hacks entry. Models Kubernetes as a company in FalkorDB and checks who could actually step in if someone left. Understudy Understudy measures how many people a team can lose before nobody who approves changes to a system can reach anyone who knows its code. It models Kubernetes as a graph in FalkorDB, computes that number for every part of the codebase with max-flow, lets you rehearse a departure on a copy of the graph, and includes an agent that answers questions only from graph queries and shows every query it ran. Live app: https://understudy-u2qk.onrender.com Built for Graph Hacks: Context for AI Agents (WeMakeDevs x FalkorDB), October 2026. Tracks: Company Brain, and Agents That Act on Connected Data. Contents Why Features Quick start A two-minute tour How it works Graph model Queries and algorithms The agent Using it from Claude Code (MCP) Does the number predict anything? FalkorDB issues found Development Project layout Limitations Privacy License AI disclosure Why Counting the people who know a system makes it look safe… View on GitHub So, be honest. Does your team have a contributor-25b5f? Do they know? Tell me in the comments. Bonus points if it's you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/balajireddy1/nine-people-know-this-part-of-kubernetes-it-still-depends-on-one-4a5b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
