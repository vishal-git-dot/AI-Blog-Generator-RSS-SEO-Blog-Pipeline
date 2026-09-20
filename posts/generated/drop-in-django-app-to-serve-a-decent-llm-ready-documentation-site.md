---
title: "Drop-in Django app to serve a decent LLM-ready documentation site"
slug: "drop-in-django-app-to-serve-a-decent-llm-ready-documentation-site"
author: "Corstiaan"
source: "devto_python"
published: "Sun, 20 Sep 2026 15:42:00 +0000"
description: "Hi all, I'm working on a bigger Python project that I'll release soon, and as part of it I found myself needing a documentation site. Most doc sites are serv..."
keywords: "docs, mdjango, site, your, django, some, side, you"
generated: "2026-09-20T15:50:36.610374"
---

# Drop-in Django app to serve a decent LLM-ready documentation site

## Overview

Hi all, I'm working on a bigger Python project that I'll release soon, and as part of it I found myself needing a documentation site. Most doc sites are served statically, but every time I fall for the siren song of a static site I end up regretting it the moment I want some dynamic behaviour. So I figured I'd use my go-to, Django, and serve a proper docs site with that. As we say in Dutch: "Zo gezegd, zo gedaan"; roughly, "no sooner said than done". So I took a small side quest from the larger project and built a decent docs engine for Django, called mdjango. Some notable features: Markdown based. Point it at a directory of .md files and mdjango handles the rest. Sensible default design. There are a few knobs for fonts, base colors and the like, but customization is deliberately limited. mdjango shouldn't have you tweaking endlessly. Set it up, adjust just enough to fit your style, and get on with your work. MiniSearch.js out of the box. Fast, client-side, typo-tolerant fuzzy search across your docs. LLM ready. llms.txt and llms-full.txt are generated automatically, so agents can consume your docs without any extra work. The mdjango docs are themselves built with mdjango, so they double as a demo: docs · source · PyPI Hope you find my little side quest useful. Try it out and let me know what you think. It's v0.1.0 so expect some rough edges. AI disclosure: mdjango was developed AI-assisted, supervised by me as a professional software engineer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/corstiaan84/drop-in-django-app-to-serve-a-decent-llm-ready-documentation-site-3p3o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
