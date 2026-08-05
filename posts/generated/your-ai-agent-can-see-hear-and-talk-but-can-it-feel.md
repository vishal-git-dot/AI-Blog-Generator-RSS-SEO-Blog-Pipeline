---
title: "Your AI Agent Can See, Hear, and Talk. But Can It Feel?"
slug: "your-ai-agent-can-see-hear-and-talk-but-can-it-feel"
author: "liesliy"
source: "devto_ai"
published: "Wed, 05 Aug 2026 02:39:23 +0000"
description: "Three years ago, I couldn't have imagined building software for something you can't see, hear, or photograph. Today, I spend my days thinking about how robot..."
keywords: "data, you, tactile, how, what, tlabel, can, but"
generated: "2026-08-05T02:54:38.759211"
---

# Your AI Agent Can See, Hear, and Talk. But Can It Feel?

## Overview

Three years ago, I couldn't have imagined building software for something you can't see, hear, or photograph. Today, I spend my days thinking about how robots feel — and more specifically, how we make sense of the data their skin produces. If you've been following the AI agent space lately (and honestly, who hasn't), you've probably noticed a pattern: everyone's building agents that can see (vision), hear (audio), and talk (LLM outputs). But almost nobody's asking: what about touch? The "Babel Problem" Nobody Talks About Here's what I found when I started working on embodied AI data: Every robotics lab on the planet stores tactile data differently. Different column names. Different units. Different sampling rates. Different everything. Lab A records force in Newtons, columns named fx, fy, fz Lab B uses raw ADC counts, columns named ch_0, ch_1... Lab C has its own JSON schema with nested objects Robot D has a completely different coordinate system Try to train a model across these datasets. Try to benchmark. Try to share data with a collaborator at another university. Good luck. I call this the Babel Problem. Everyone's speaking their own language, and nobody can understand each other. "But We Have MCP Now, Right?" Great question. MCP standardized how LLMs call tools. A2A handles agent-to-agent communication. OpenTelemetry covers observability. None of these touch tactile perception. There is no standard for what a "tactile reading" actually means. Not its semantics. Not its structure. Not its units. Not how you describe contact geometry, pressure distribution, slip events, or texture features. Think of it this way: if someone published a recipe using inches, Fahrenheit, and a custom unit called "glugs," you couldn't reproduce it — no matter how brilliant the cooking was. That's where tactile data is right now. Why This Matters Now Embodied AI is having its moment. Foundation models are being trained on robot demonstrations. Dexterous manipulation is no longer sci-fi. But the data pipeline underneath all of this is held together with tape. Without a standard: Cross-dataset training is basically impossible (you spend more time normalizing than modeling) Hardware swaps break every downstream pipeline Reproducibility is a joke (good luck replicating someone's tactile benchmark) Data sharing between labs requires a custom converter... per dataset What We Built After months of frustration, I started building TLabel — an open standard for tactile data. The core idea is simple: define a universal schema that describes what tactile data means, regardless of which sensor produced it. TLabel defines 14 semantic dimensions, including: Contact Geometry — where and how the contact happens Normal / Shear Force — force direction and magnitude Pressure Distribution — spatial pressure map Texture — surface micro-features Temperature — thermal perception Slip — detection of movement at contact ...and 8 more (full spec in the design doc) Each data file carries a Compliance Level (L1–L4), so consumers know exactly what's available — even if some sensors only provide basic readings. The key design principle: TLabel doesn't tell you how to process tactile data. It tells you how to describe it. The processing is up to you. Show Me The Code Load a tactile file — same API regardless of which sensor produced it: from tlabel import TLabelFile data = TLabelFile ( " sample.tlabel " ) Access standardized dimensions: forces = data . get_forces () # Newtons, always contacts = data . get_contact_geom () # Consistent coordinate frame textures = data . get_texture_features () Check what's available and inspect sensor metadata: print ( data . compliance_level ) # L1 = basic, L4 = full spec print ( data . sensor_info ) # Original hardware metadata preserved No matter whether the original data came from a GelSight, a BioTac, a custom capacitive array, or a future sensor nobody's invented yet — the interface is the same. The Python package is at v0.18.2 on PyPI, and we're actively building exporter plugins for popular formats. The open-source embodied AI ecosystem is moving fast — LeRobot, Forge, various simulators and hardware platforms. But if these systems can't share and understand tactile data, we're building a tower with no common language. I don't think TLabel is the final answer. But the conversation needs to happen, and the standard needs to be open — not owned by one company or one lab. The project is here if you're curious: github.com/liesliy/tlabel

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/liesliy/your-ai-agent-can-see-hear-and-talk-but-can-it-feel-3pjk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
