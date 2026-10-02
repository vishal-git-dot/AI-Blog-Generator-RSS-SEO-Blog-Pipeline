---
title: "I built a free SVG animation editor that exports self-contained, callable .svg files — no runtime, no proprietary format"
slug: "i-built-a-free-svg-animation-editor-that-exports-self-contained-callable-svg-files-no-runtime-no-proprietary-format"
author: "saidev ac"
source: "devto_webdev"
published: "Fri, 02 Oct 2026 04:41:30 +0000"
description: "Every vector animation tool makes the same trade: nice editor, but output locked to its runtime. Rive needs .riv , Lottie needs lottie-web . I wanted the opp..."
keywords: "svg, editor, svgmotion, https, workers, callable, export, app"
generated: "2026-10-02T05:02:05.617841"
---

# I built a free SVG animation editor that exports self-contained, callable .svg files — no runtime, no proprietary format

## Overview

Every vector animation tool makes the same trade: nice editor, but output locked to its runtime. Rive needs .riv , Lottie needs lottie-web . I wanted the opposite — an editor whose export is a plain .svg file that renders anywhere, yet stays interactive and callable from code. So I built SVGMotion — a free, local-first, AI-assisted SVG motion studio, split into three editors that build on each other: 🎨 Vector Editor — https://app.svgmotion.workers.dev/vectoreditor The core. Prompt → editable SVG layers → actions, keyframes, state machine. Physics (bounce, roll, tumble, pendulum) is baked into keyframes at export time, so the file ships ~3 KB of markup — not a solver. Every export is callable: js const player = SVGMotionPlayer(mount, scene); player.call('launch'); player.setInput('armed', true); 🤖 Character Studio — https://app.svgmotion.workers.dev/characterstudio Same editor engine, wearing a character hat: skeleton roles, micro-actions, named macros, a multi-entity world stage, and an AI director that composes motion at runtime. Builds directly on the Vector Editor's action/state model. 📱 Asset Studio — https://app.svgmotion.workers.dev/assetstudio The downstream consumer: draw or prompt one SVG, preview it inside real OS masks/safe zones, export ready-made Xcode, Android & PWA bundles. Reuses the same scene format and layer pipeline. Stack: vanilla ES modules, no framework, no build step. AI is BYOK (Ollama/OpenRouter/OpenAI — keys stay in the browser), with an optional WebLLM tier running Llama-3.2-1B in-browser. Cloudflare Workers for hosting. Free, no sign-up, no ads, no watermarks. Gallery of live exports — every item is a real callable .svg: https://app.svgmotion.workers.dev/gallery Source: https://github.com/saidevac/svgmotion

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/saidev_ac_69c0816924a7676/i-built-a-free-svg-animation-editor-that-exports-self-contained-callable-svg-files-no-runtime-2a5i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
