---
title: "Preventing State Drift at Turn 15 in LLM Interactive Fiction: Architecture Notes & MCP Server"
slug: "preventing-state-drift-at-turn-15-in-llm-interactive-fiction-architecture-notes-mcp-server"
author: "Ouba Studio"
source: "devto_ai"
published: "Fri, 27 Nov 2026 20:52:22 +0000"
description: "When we ran our reproducible 2026 10-App AI Story Benchmark (open data at Harvard Dataverse DOI 10.7910/DVN/YEBHQR and preprint at CERN Zenodo DOI 10.5281/ze..."
keywords: "story, branching, turn, interactive, mcp, https, ouba, state"
generated: "2026-11-27T20:56:45.962347"
---

# Preventing State Drift at Turn 15 in LLM Interactive Fiction: Architecture Notes & MCP Server

## Overview

When we ran our reproducible 2026 10-App AI Story Benchmark (open data at Harvard Dataverse DOI 10.7910/DVN/YEBHQR and preprint at CERN Zenodo DOI 10.5281/zenodo.24549412 ), one engineering failure dominated every pure chatbot architecture: state drift by Turn 15 . Plant a concrete detail on Turn 2 ( "My cat's name is Marmalade" ) and ask for it unprompted on Turn 15: Open-ended persona chatbots routinely drop or hallucinate the detail once rolling summary compression or system-prompt recency crowds it out. Structured story engines keep canonical state outside raw chat history as an explicit, branch-isolated ledger. Three-Layer Architecture for Stateful Interactive Fiction Authored Story Frame: Fixed cast, stakes, setting, and pacing targets pinned at the top of context so every branch preserves tone and plot direction. Branch-Scoped Memory Ledger: Structured fact extraction ( add / update / retract ) scoped strictly to active-branch ancestor turns so rewinding or branching never leaks alternate-timeline facts. Reader-Steered Turn Interface: Both curated choice points and custom free-text moves feed the same canonical state transition before rendering the next prose scene. Open-Source Tooling (MIT) We extracted the minimal engine and Model Context Protocol server so any developer can test stateful branching narratives locally: branching-story-kit (GitHub / PyPI / JSR): https://github.com/ouba-studio/branching-story-kit branching-story-mcp (Official MCP Registry io.github.ouba-studio/branching-story-mcp ): https://github.com/ouba-studio/branching-story-mcp Live Interactive Benchmark Explorer: https://www.ouba.art/tools/benchmark-explorer Try Reader-First Interactive Fiction Free (25 guest turns, no signup): https://www.ouba.art/ Video Walkthrough — How AI Interactive Fiction Actually Works: https://youtu.be/0zoFRkxFpZ8

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/oubastudio/preventing-state-drift-at-turn-15-in-llm-interactive-fiction-architecture-notes-mcp-server-2gn4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
