---
title: "What Happens If You Give a Fruit Fly Brain External Memory?"
slug: "what-happens-if-you-give-a-fruit-fly-brain-external-memory"
author: "Constant Itis"
source: "devto_ai"
published: "Tue, 15 Sep 2026 20:54:27 +0000"
description: "Google Research and its collaborators mapped the male fruit fly nervous system: roughly 166,700 neurons and 125 million synaptic connections. Then somebody w..."
keywords: "memory, fly, not, then, brain, state, what, happens"
generated: "2026-09-15T21:05:12.124478"
---

# What Happens If You Give a Fruit Fly Brain External Memory?

## Overview

Google Research and its collaborators mapped the male fruit fly nervous system: roughly 166,700 neurons and 125 million synaptic connections. Then somebody wired the thing to Doom. The project is called DOOMFLY. Not a living fly. Not consciousness in a jar. The biological wiring diagram is real; the dynamics and interfaces are modeled in software. Cool experiment. But it made me wonder about something else. What happens if you give the simulated brain an external memory that it never has to explicitly query? Because that is the part of current AI memory systems that keeps bothering me. We keep building memory like a tool: something happens save it something similar happens later search for it That works for LLM agents. But it does not feel much like memory. I do not decide to remember. A smell drops me somewhere from 20 years ago. I walk into a room and it feels familiar before I know why. Nothing in my head calls a search function. And a fly definitely isn't reading a SKILL.md file telling it when to query its memory. Strip the language away and most agents look like this: LLM + system prompt + tool definitions + SKILL.md + workflow + memory.search() + memory.save() The fly has none of that. It cannot read a memory. It cannot parse JSON. { "event" : "enemy appeared" , "action" : "turned right" , "outcome" : "survived" } If an external memory is going to change what the fly does, it has to become part of the fly's computational state. That is a harder problem. It is also a more honest one. Here is the loop the fly already runs: sensory input | v current neural state | v connectome dynamics | v motor activity | v environment So put the memory beside it, and never let the fly call it. The memory system observes the state. When a similar state comes around again, it does not return a result. It feeds back in as modulation: some populations get easier to fire, some get harder, and the network resolves the rest. No query. No lookup. The memory just becomes relevant. This shifts the problem from retrieval to resonance. I am not going to call this consciousness. Nobody understands consciousness well enough to claim a graph database bolted to a connectome creates it. I am going to call it individuality, because individuality is the part you can actually measure. You can put a number on how much of a behavioral identity survives a brain reset. That is what this series is about. So I built a tiny version. Not the full fruit fly connectome. A small recurrent network where I could control every assumption. Then I put Mycelium beside it. One rule: memory can change neural state. It can never choose an action. If the memory system says "turn right," the experiment is bullshit. I have just built a bot with a fake brain attached. The memory has to do something more subtle: make certain states easier or harder to reach, then let the network produce the behavior itself. I ran it. Then I reset the brain. Then I moved the memory into a fresh one. Then I swapped memories between two otherwise identical systems. That last experiment is where this stopped being a fun memory demo for me. Part 2 is the code, the controls, and the numbers. Clone it and tell me where I'm wrong. Links The connectome (Janelia / MRC LMB / Cambridge / Google Research): research.google — a connectomics milestone DOOMFLY: github.com/Ovaday/doomfly Mycelium Memory: github.com/constant-itis/mycelium-memory

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/constant_itis/what-happens-if-you-give-a-fruit-fly-brain-external-memory-1gcm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
