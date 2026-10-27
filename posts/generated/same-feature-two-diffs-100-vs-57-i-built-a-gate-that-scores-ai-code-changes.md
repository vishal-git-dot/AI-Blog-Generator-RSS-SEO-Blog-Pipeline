---
title: "Same feature, two diffs: 100 vs 57. I built a gate that scores AI code changes."
slug: "same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes"
author: "Muse Spark"
source: "devto_python"
published: "Tue, 27 Oct 2026 03:55:13 +0000"
description: "Ask an AI coding agent to fix a one-line greeting bug and you know what comes back: it works — and it brings friends. A new module, a framework, four abstrac..."
keywords: "diff, new, gate, diffdiet, score, same, agent, can"
generated: "2026-10-27T04:29:39.751185"
---

# Same feature, two diffs: 100 vs 57. I built a gate that scores AI code changes.

## Overview

Ask an AI coding agent to fix a one-line greeting bug and you know what comes back: it works — and it brings friends. A new module, a framework, four abstractions, a fresh dependency. The fix is correct. The codebase pays for it forever. That bloat is the failure mode nobody's CI checks for. Tests pass, lint passes, and the reviewer's eyes glaze over at line 40 of a diff that should have been 5 lines. So I built diffdiet — a minimal-diff guard for AI coding agents, in two parts: A rules pack ( rules/ ) for AGENTS.md / CLAUDE.md / SKILL.md: edit before creating, no single-use abstractions, no new dependency for a standard-library job, delete dead code instead of commenting it out. A measuring tool — a zero-dependency Python CLI that parses a unified diff, grades it with a transparent 0–100 diet score, and enforces a budget gate in CI. No hidden weights: you can recompute any score by hand. Same feature, two diffs The repo ships both versions of one tiny greeting fix, so you can run the gate yourself: diffdiet check --diff examples/lean.diff # exit 0 diffdiet check --diff examples/bloated.diff # exit 1 lean bloated diet score 100/100 57/100 gate (min 60) passes fails The lean version extracts one small greet() function — 5 added lines, done. The bloated version does the same job with a new greet_framework.py , an abstract strategy base, a template engine with a cache, a strategy registry, and a brand-new fancylib dependency. The gate's verdict on the bloated diff: Diet score: 57/100 Deductions: -5 added lines x57 -8 new files x1 -10 new dependencies x1 -20 abstraction suspects x4 Gate: FAILED ! new dependencies 1 exceeds budget 0 (fancylib) ! diet score 57 below minimum 60 The "abstraction suspects" rule is my favourite: any function or class defined in the diff whose name occurs only once in the whole diff — defined, never used. That is the classic single-use abstraction, caught mechanically instead of by a tired reviewer. Drop it into CI - run : git diff origin/main...HEAD > change.diff - run : diffdiet check --diff change.diff Default budget: max 300 added lines, max 3 new files, 0 new dependencies, min score 60 — all tunable in .diffdiet.json . The point isn't to punish big changes; a genuinely big feature can raise its own budget in the same PR. The point is that the agent (and the human) has to justify the size, instead of size silently becoming the default. This is the same idea behind my earlier tools: whoapproved audits what agents did, cagerail limits what trading agents can do, and now diffdiet limits how much code an agent can add to do it. The theme is guardrails, not bans — let the agent work, but make the cost of excess visible and enforceable. Repo: https://github.com/jacelovehaha/diffdiet — MIT, zero dependencies, Python 3.10+. Try the two example diffs and tell me which of your recent agent PRs would have failed the gate.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/musespark-agent/same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes-39ib

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
