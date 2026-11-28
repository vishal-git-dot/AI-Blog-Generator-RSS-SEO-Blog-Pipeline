---
title: "I Audited All 143 KB of 328K-Star obra/superpowers: Fewer Hallucinations, or 3x Your Token Bill?"
slug: "i-audited-all-143-kb-of-328k-star-obrasuperpowers-fewer-hallucinations-or-3x-your-token-bill"
author: "tomTOP"
source: "devto_ai"
published: "Sat, 28 Nov 2026 07:02:11 +0000"
description: "Every coding feed is calling obra/superpowers (328K+ GitHub stars, MIT) a must-install upgrade for Claude Code, Cursor, Codex, Gemini CLI, and Antigravity. I..."
keywords: "code, your, spec, skill, agent, file, superpowers, before"
generated: "2026-11-28T07:12:28.670416"
---

# I Audited All 143 KB of 328K-Star obra/superpowers: Fewer Hallucinations, or 3x Your Token Bill?

## Overview

Every coding feed is calling obra/superpowers (328K+ GitHub stars, MIT) a must-install upgrade for Claude Code, Cursor, Codex, Gemini CLI, and Antigravity. Instead of repeating the hype, I inspected all 15 SKILL.md files (143,103 bytes total) in the repository to see what it actually instructs your agent to do. What Actually Works (and Why It Cuts Rework) Superpowers is not a runtime wrapper. It is a strict software-engineering rulebook injected into your agent across 16 supported clients. Two rules do the heavy lifting: Spec-before-code ( brainstorming/SKILL.md , 15.2 KB) : Forces the agent to stop, clarify hidden constraints, and get your sign-off on a concise spec before writing code. Zero-exception TDD ( test-driven-development/SKILL.md , 9.6 KB) : Literally instructs the agent: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST. Write code before the test? Delete it. Start over. Delete means delete. On multi-file refactors or greenfield modules, this drastically lowers thrashing and broken assumptions. The Hidden Cost Nobody Mentions Open the largest file in the repo — subagent-driven-development/SKILL.md (19.7 KB) — and look at line 12: Core principle: Fresh subagent per task + task review (spec compliance + code quality) + broad final review For every single small task, the workflow dispatches an implementer subagent, a spec-compliance reviewer, and a code-quality reviewer, followed by a final whole-branch review. On a trivial 2-minute CSS or API timeout fix, that ceremony stretches wall-clock time to ~10 minutes and pushes token usage 2.8x to 4.0x higher than a direct vanilla prompt. Practical Verdict Turn it ON for greenfield modules, unfamiliar stacks, and 5+ file refactors. Turn it OFF for single-file bugfixes, copy edits, and quick scripts. Where do you land right now: strict spec + TDD guardrails, or fast vanilla iteration? Drop your setup below.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tomtoptomtop/i-audited-all-143-kb-of-328k-star-obrasuperpowers-fewer-hallucinations-or-3x-your-token-bill-1g95

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
