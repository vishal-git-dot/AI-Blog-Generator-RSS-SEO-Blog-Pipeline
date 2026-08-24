---
title: "Day 6/70 | Testing PyForge & Making It Actually Installable| 10 Weeks Challenge"
slug: "day-670-testing-pyforge-making-it-actually-installable-10-weeks-challenge"
author: "Nattar Kani Murugan"
source: "devto_python"
published: "Mon, 24 Aug 2026 18:14:44 +0000"
description: "Okay, Nattar. Day 6. Today wasn't about adding another big feature. It was about making yesterday's PyForge CLI a little more real. The goal was simple: Writ..."
keywords: "pyforge, install, project, day, testing, actually, today, work"
generated: "2026-08-24T18:48:28.651044"
---

# Day 6/70 | Testing PyForge & Making It Actually Installable| 10 Weeks Challenge

## Overview

Okay, Nattar. Day 6. Today wasn't about adding another big feature. It was about making yesterday's PyForge CLI a little more real. The goal was simple: Write a pytest suite with 70%+ coverage, make pip install -e . work, and create a README with setup steps and a usage GIF. I added a pytest test suite for PyForge and worked towards getting the project above 70% test coverage . This made me think differently about the code I wrote yesterday. Writing: "It works." is one thing. Writing tests that prove: "This actually works." is another. I also got more comfortable with running tests, checking failures, and fixing issues instead of just manually testing everything from the CLI. I also wanted PyForge to behave like an actual Python package. So I worked on the package configuration until this worked: pip install -e . The -e option was something I wanted to understand better. It allows me to install the project in editable mode , so I can keep developing the source code without repeatedly reinstalling the package. That felt like an important step from: "I have some Python files." to: "I have a Python project." Finally, I cleaned up the README. I added: Setup instructions Installation steps Basic usage A usage GIF The goal was simple: Someone should be able to clone the project, follow the README, and actually get it running. That's something I hadn't paid enough attention to in my earlier projects. 🌱 Today's takeaway Today reminded me that building software isn't just about writing features. It's also about: Testing → Packaging → Documentation → Usability The code might work on my machine. But if someone else can't install it, understand it, or use it... there's still work to do. Day 6 — done. ✅ View PyForge on GitHub 🚀 Keep going, Nattar.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nattarkani/day-670-testing-pyforge-making-it-actually-installable-10-weeks-challenge-23b0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
