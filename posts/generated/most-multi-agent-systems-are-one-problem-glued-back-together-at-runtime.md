---
title: "Most multi-agent systems are one problem, glued back together at runtime"
slug: "most-multi-agent-systems-are-one-problem-glued-back-together-at-runtime"
author: "Omar Baruzzo"
source: "devto_ai"
published: "Thu, 17 Sep 2026 11:09:59 +0000"
description: "Multi-agent is the default reach right now, and most of the time it's the wrong one. Splitting a task across agents doesn't add capability — it moves the har..."
keywords: "agent, more, one, agents, most, multi, default, glue"
generated: "2026-09-17T11:22:03.944865"
---

# Most multi-agent systems are one problem, glued back together at runtime

## Overview

Multi-agent is the default reach right now, and most of the time it's the wrong one. Splitting a task across agents doesn't add capability — it moves the hard part from inside the agents to the glue between them. What the glue costs you: Every handoff drops or distorts context. Each agent owns its control flow, so nondeterminism multiplies instead of adding. Errors compound: five agents in a chain pass mistakes downstream as facts. No stack trace for "they misunderstood each other". More prompts to maintain, more surfaces to evaluate, more cost per run. When it's actually justified: genuinely independent, parallelizable subtasks, or parts that need different tools, permissions, or trust boundaries. That's a design reason. "More agentic" isn't. Default to one capable agent with good tools and a fixed workflow around it. It's cheaper, testable, and you can reason about what it did. Full version: https://www.omarbaruzzo.it/en/blog/meno-agenti-di-quanti-pensi

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/omarbaruzzo/most-multi-agent-systems-are-one-problem-glued-back-together-at-runtime-1g42

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
