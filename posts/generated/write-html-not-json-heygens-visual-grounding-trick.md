---
title: "Write HTML, Not JSON: HeyGen's Visual-Grounding Trick"
slug: "write-html-not-json-heygens-visual-grounding-trick"
author: "Max Quimby"
source: "devto_webdev"
published: "Tue, 23 Jun 2026 03:56:14 +0000"
description: "Read the full version with screenshots and embedded sources on AgentConn → agentconn.com/blog/heygen-hyperframes-html-visual-grounding-video-ui-agents-2026 E..."
keywords: "json, html, agent, visual, hyperframes, video, grounding, heygen"
generated: "2026-06-23T04:02:13.419358"
---

# Write HTML, Not JSON: HeyGen's Visual-Grounding Trick

## Overview

Read the full version with screenshots and embedded sources on AgentConn → agentconn.com/blog/heygen-hyperframes-html-visual-grounding-video-ui-agents-2026 Every agent framework in 2026 tells you to return structured JSON. Schema-validated, type-safe, parseable. And for most tasks, that's correct — structured output gives agents 95–99% action success rates versus 70–85% for unstructured text. But here's the problem nobody talks about: JSON has no visual semantics. An agent can produce a perfectly valid JSON config describing a video timeline — correct schema, valid keyframes, legal property values — and the rendered output looks like garbage. The agent wrote "correct" instructions for something it can't see. HeyGen figured this out. Their open-source framework HyperFrames doesn't use JSON configs. It uses HTML. The Visual-Grounding Problem When an agent generates a JSON video config, it's working blind. A perfectly valid JSON scene description — correct schema, right keyframes — can render as visual garbage because the agent can't reason about spatial layout in a non-visual format. The SeeAct-V research confirms what practitioners already know: visual grounding is a fundamental capability gap for language models working in non-visual formats. HyperFrames: HTML as the Agent's Canvas HyperFrames launched April 17, 2026, and hit 30,100 stars in two months. Instead of JSON configs, agents write standard HTML with CSS and data-* attributes for timing: <div data-scene= "intro" data-duration= "3s" > <h1 style= "font-size: 48px; text-align: center; margin-top: 20vh;" > Hello World </h1> </div> The agent can reason about this . It knows what text-align: center looks like. It knows margin-top: 20vh pushes the heading down. It understands CSS layout. The architecture: headless Chrome (Puppeteer) for deterministic frame capture, FFmpeg for encoding. Supports GSAP 3, Lottie, Three.js, Anime.js, and WebGL shaders — any animation library that runs in a browser works without adapters. Why HTML Wins Over JSON The HN discussion put it plainly: "It's just a superset of HTML, and agents know how to write HTML + GSAP by default." LLMs are trained on billions of web pages. They know what display: flex looks like, that border-radius: 50% makes a circle, that font-size: 72px is large. This visual intuition doesn't exist for arbitrary JSON coordinate systems. The Agent Skill Architecture HyperFrames includes dedicated skills for Claude Code, Cursor, Gemini CLI, and Codex. HeyGen's own launch video was made 100% with Claude Code + HyperFrames. Nous Research's Hermes agent has an official HyperFrames skill — the first major agent framework to integrate video production natively. The Pattern Beyond Video The insight is general: match the output format to the model's strongest reasoning modality. Domain Low-Grounding High-Grounding Video JSON config HTML + CSS + data-* Diagrams DOT/Graphviz SVG Dashboards Chart.js JSON HTML grid + components Presentations Slide JSON HTML slides + CSS HeyGen bet that agents think better in HTML than in JSON. Thirty thousand stars in two months suggests they were right. Originally published at AgentConn

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/max_quimby/write-html-not-json-heygens-visual-grounding-trick-49ff

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
