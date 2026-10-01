---
title: "Angular, AnalogJS, Spartan and Claude Code: shipping a 6-language comparison site fast"
slug: "angular-analogjs-spartan-and-claude-code-shipping-a-6-language-comparison-site-fast"
author: "Tim"
source: "devto_webdev"
published: "Thu, 01 Oct 2026 12:35:41 +0000"
description: "I built Runometry, a running shoe database and price comparator (841 shoes, 16 brands, 6 locales), mostly with Claude Code and parallel agents. Notes on the ..."
keywords: "angular, code, price, agents, pages, spartan, claude, comparator"
generated: "2026-10-01T12:50:17.623715"
---

# Angular, AnalogJS, Spartan and Claude Code: shipping a 6-language comparison site fast

## Overview

I built Runometry, a running shoe database and price comparator (841 shoes, 16 brands, 6 locales), mostly with Claude Code and parallel agents. Notes on the stack and the workflow. Stack Angular + AnalogJS: static rendering and file-based routing, a good fit for catalog pages generated from data. Signals and standalone components make modern Angular a joy. Spartan (spartan.ng): shadcn-style, accessible UI components for Angular. Consistent design system, fully customizable. Tailwind for styling. Cloudflare for static hosting, with images served as WebP from a CDN. hreflang and localized routes from day one. Page types generated from the catalog Shoe, brand and category pages, A vs B comparator pages restricted to comparable pairs (to avoid thin or nonsensical pages), guides and blog. Workflow with Claude Code Clear conventions up front (structure, naming, component patterns), so agents produce code that fits the project. Parallel agents on independent areas: comparator logic, templates, translations, data validation. Me reviewing diffs, running the build, and checking anything factual. Small, frequent commits so every agent change is easy to review or revert. What I'd do the same way Keep the stack I know best. Agents shine when you can judge their output quickly. What's next Daily price collection as a time series: price history, a price drop radar, alerts. I'm weighing feeds vs APIs vs scraping and would love input. Live: runometry.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/t1m4lc/angular-analogjs-spartan-and-claude-code-shipping-a-6-language-comparison-site-fast-2ec5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
