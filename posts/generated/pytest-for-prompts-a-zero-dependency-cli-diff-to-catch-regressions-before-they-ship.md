---
title: "pytest for prompts: a zero-dependency CLI diff to catch regressions before they ship"
slug: "pytest-for-prompts-a-zero-dependency-cli-diff-to-catch-regressions-before-they-ship"
author: "rene"
source: "devto_ai"
published: "Sat, 24 Oct 2026 20:21:47 +0000"
description: "You edit a system prompt or switch models, and other cases quietly break. prompt-diff runs a small prompt suite against a baseline (A) and a candidate (B). I..."
keywords: "diff, you, prompt, zero, cli, suite, side, pass"
generated: "2026-10-24T20:31:17.912364"
---

# pytest for prompts: a zero-dependency CLI diff to catch regressions before they ship

## Overview

You edit a system prompt or switch models, and other cases quietly break. prompt-diff runs a small prompt suite against a baseline (A) and a candidate (B). It writes a side-by-side line diff and a pass/fail report in Markdown and JSON. If B fails a case that A passed, it exits with code 1, so you can gate CI on it. What you get: prompt-diff.mjs: a single-file Node 18+ CLI with zero dependencies Checks: contains, notContains, regex, minChars/maxChars, valid JSON Two variant sources: recorded outputs (.jsonl, offline) or any OpenAI-compatible endpoint Statuses: PASS, FAIL, REGRESSION, FIXED A working example suite with A/B outputs A README with a GitHub Actions snippet Pay what you want: minimum $1, suggested $5. MIT license. Get it here: https://renevibe76.gumroad.com/l/tywvdr

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/renev3408/pytest-for-prompts-a-zero-dependency-cli-diff-to-catch-regressions-before-they-ship-2la7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
