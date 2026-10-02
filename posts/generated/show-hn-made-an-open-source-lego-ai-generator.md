---
title: "Show HN: Made an open-source Lego AI generator"
slug: "show-hn-made-an-open-source-lego-ai-generator"
author: "antelocnova"
source: "hackernews"
published: "Fri, 02 Oct 2026 20:00:15 +0000"
description: "Hi there :-) New on HN, first time posting. Past year, around December, I started experimenting with making ChatGPT and Claude generate source code in LDraw ..."
keywords: "lego, ldraw, source, models, one, claude, generate, language"
generated: "2026-10-02T22:01:18.329215"
---

# Show HN: Made an open-source Lego AI generator

## Overview

Hi there :-) New on HN, first time posting. Past year, around December, I started experimenting with making ChatGPT and Claude generate source code in LDraw language. This LDraw is literally an "assembly" language, a low-level programming language that describes how to assemble LEGO pieces together into models, one placement instruction at a time. When executed by specific tools, like e.g. LDView, LeoCAD, Studio... these instructions become LEGO CAD models, that can be interacted with, modified, etc. Or, in other words: one LDraw source file in .mpd or .ldr format is equivalent to one LEGO CAD model. So, the idea I had was: if I manage for maybe ChatGPT or Claude to generate high-quality LDraw source files... then, they would actually be generating high-quality LEGO CAD models, right? Then, after months of iterations and trying one thing after the other... it worked!!! Long story short: using GPT-6 Astra and Opus 5.5, I've managed to create a python toolset, instructions, and docs for agents in general. Now, these can be used by them to generate LDraw models. I've packed it all as a dockerized web app for others to try and experiment, with several providers (and agents) to choose from: OpenAI, Claude and OpenRouter. I'd really appreciate feedback and comments, let's see where this goes =) Comments URL: https://news.ycombinator.com/item?id=49937916 Points: 39 # Comments: 25

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/anteloc/ldraw-nova

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
