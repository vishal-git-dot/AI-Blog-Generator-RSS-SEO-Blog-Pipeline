---
title: "What If AI Coding Agents Could Predict a Bad Code Change Before Making It?"
slug: "what-if-ai-coding-agents-could-predict-a-bad-code-change-before-making-it"
author: "Vignesh P A"
source: "devto_ai"
published: "Sun, 18 Oct 2026 10:39:32 +0000"
description: "AI coding agents usually follow this loop: Make a change → Run tests → Fix errors → Try again. But what if the first change was a bad idea from the start? Th..."
keywords: "preflight, change, graph, could, function, what, agents, code"
generated: "2026-10-18T10:43:33.400264"
---

# What If AI Coding Agents Could Predict a Bad Code Change Before Making It?

## Overview

AI coding agents usually follow this loop: Make a change → Run tests → Fix errors → Try again. But what if the first change was a bad idea from the start? The agent may spend minutes or hours editing files and fixing errors, only to discover that another approach would have been much safer. I wanted to help AI agents predict the impact of a code change before they start editing. That is why I built Preflight . GitHub: https://github.com/VigneshPA-30/preflight The idea behind Preflight Imagine an AI agent wants to rename a function used across 50 files. Instead of making the change immediately, what if it could first ask: Which functions and files could be affected? Which tests might fail? Can some failures go unnoticed because of mocks? Is there a safer way to make this change? Preflight builds a graph of the codebase and simulates different refactoring plans on separate copies of that graph. It predicts the impact of each plan, identifies risky paths and ranks the options. The agent can then reject a bad approach before touching the actual source code . Why FalkorDB? The codebase is represented as a graph of functions, calls, imports, mocks and test relationships. FalkorDB makes it possible to follow these connections across multiple levels. Its GRAPH.COPY feature lets Preflight create an isolated graph for each proposed change. Each plan can be simulated separately without modifying the real graph. This is not just about finding where a function is used. It is about understanding what could happen if we change it. Finding the problems tests may miss One interesting case came from my analysis of the open-source project invoke . Changing a function's parameters broke 59 call sites. Tests were expected to catch 58 of them. One could remain hidden because its test mocked the function. Preflight identifies this as a masked breakage, helping the agent avoid trusting a path that looks safe but is not. Does it work? I tested Preflight against five real changes in the open-source project cookiecutter , comparing its predictions with the actual test failures. The results: 0.96 precision 0.99 recall These are early results from one project, not a guarantee for every codebase. Preflight currently supports Python function renames and parameter changes, and static analysis has known limits. The bigger idea I believe the next step for AI coding agents is not just writing code faster. It is knowing which path is worth trying before spending time on it . Preflight is my attempt to make that possible: predict the impact, compare the options, abandon risky paths early, and only then make the change. Simulate first. Choose wisely. Then edit. Project: https://github.com/VigneshPA-30/preflight

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vigneshpa_/what-if-ai-coding-agents-could-predict-a-bad-code-change-before-making-it-13ae

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
