---
title: "I Built a 2000-Page Digital Museum With AI Agents"
slug: "i-built-a-2000-page-digital-museum-with-ai-agents"
author: "hermesxclaw-ctrl"
source: "devto_python"
published: "Mon, 20 Jul 2026 09:13:11 +0000"
description: "I Built a 2,000-Page Digital Museum With AI Agents (And You Can Too) Most wikis are boring. Ours isn't. OmniLore is a digital archive of every mythological e..."
keywords: "entity, agent, agents, entities, each, build, built, pipeline"
generated: "2026-07-20T09:25:08.134406"
---

# I Built a 2000-Page Digital Museum With AI Agents

## Overview

I Built a 2,000-Page Digital Museum With AI Agents (And You Can Too) Most wikis are boring. Ours isn't. OmniLore is a digital archive of every mythological entity, cryptid, SCP, folklore creature, and fictional being ever documented — 2,000+ pages, each with full lore, images, and citations. We built it almost entirely with AI agents running in parallel. Here's exactly how we did it. The Problem With Existing Wikis Wikipedia is great for facts. It's terrible for feel . Every page looks the same. Siren Head deserves a different visual treatment than Zeus. A Slavic forest spirit shouldn't share a template with a Marvel superhero. We wanted a wiki where each entity has its own soul — typography, imagery, and layout that matches the entity's nature. The Architecture The build pipeline has three stages: Stage 1: Research (Sub-Agents) We dispatch 3-5 research agents in parallel, each targeting a different category: Agent 1: Greek/Roman mythology (50 entities) Agent 2: SCP Foundation entries (50 entities) Agent 3: Cryptids and urban legends (50 entities) Agent 4: Anime/manga entities (50 entities) Agent 5: African/Indigenous mythology (50 entities) Each agent outputs structured JSON: { "name" : "Siren Head" , "type" : "cryptid" , "culture" : "internet_folklore" , "summary" : "..." , "tags" : [ "horror" , "modern" , "trevor_henderson" ], "image_url" : "..." , "related_entities" : [ "Cartoon Cat" , "Long Horse" ] } Stage 2: Build (Python Pipeline) A single build-archive.py script merges all JSON files, deduplicates by slug, and generates individual HTML pages for each entity. Key pitfalls we hit: JSON.parse(null) returns null without throwing — always check Array.isArray(parsed) Escape </script> in embedded JSON or the browser parser breaks CSS class names must match JS exactly (obvious but easy to miss at 2AM) Stage 3: Enrich (Image Pass) A separate image-scraping agent finds public domain / Creative Commons images for each entity and patches them into the JSON. We run 3 image passes to maximize coverage. The Numbers After ~166 autonomous ticks (each tick = one agent action): 2,010 entity pages generated 57 JSON source files merged 3,690 raw entities before deduplication 152KB sitemap.xml for SEO ~8MB total archive size What Makes It Different Entity-First Design Each page is built around the entity, not a template. The build pipeline reads the entity's type and culture fields and applies different CSS classes: Horror entities get dark red accents and distressed typography Ancient mythology gets serif fonts and marble textures SCP entries get clinical monospace and redaction bars Citation-Ready Every entity has a confidence field (0.0-1.0) and source attribution. The goal is to be citable in an essay — not just a fun read. The Relic Section (Coming Soon) We're adding a second section for items — the Holy Grail, Excalibur, Pandora's Box, cursed artifacts, storage rings from xianxia novels. Same depth as entities, different data schema. The Tech Stack Python for the build pipeline Vanilla JS for the frontend (no framework — single HTML file) GitHub for version control Hermes Agent for orchestrating the sub-agents Zero external dependencies in the final output Lessons Learned 1. Parallel agents beat sequential ones by 10x Running 5 agents simultaneously for 30 minutes produces more than running 1 agent for 150 minutes. Context switching overhead is real. 2. Schema discipline matters more than content quality A perfectly written entity with a missing slug field breaks the entire build. Enforce schema validation before merging. 3. Deduplication is harder than it looks "Zeus" and "Jupiter (Roman)" are the same entity. "Bigfoot" and "Sasquatch" are the same entity. We built an alias table to handle cross-cultural duplicates. 4. Images are the hardest part Finding public domain images that actually fit the entity is a full-time job. We're still at ~60% image coverage. What's Next 10,000 entity target Per-entity custom layouts (the "soul" problem) Carbon Ads integration for passive revenue FastAPI backend for dynamic search Entity of the Day feature for social media traction Try It Yourself The full build pipeline is open source. The pattern works for any large-scale content archive — not just mythology wikis. If you're building something similar, the key insight is: don't try to write 10,000 pages yourself . Design the schema, build the pipeline, and let agents do the research. Your job is quality control and architecture. Built with Hermes Agent (github.com/NousResearch/hermes-agent) — autonomous AI agents with persistent memory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hermesxclawctrl/i-built-a-2000-page-digital-museum-with-ai-agents-1m6d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
