---
title: "5 JSON Schemas That Stop AI Coding Agents From Shipping Garbage"
slug: "5-json-schemas-that-stop-ai-coding-agents-from-shipping-garbage"
author: "Ryan Cole"
source: "devto_python"
published: "Sun, 04 Oct 2026 05:03:02 +0000"
description: "Your agent said "done". Production disagreed. If you run autonomous coding agents (Cursor, Claude Code, Windsurf, custom loops), you have met the silent fail..."
keywords: "agent, schemas, code, not, every, agents, claude, pipeline"
generated: "2026-10-04T05:17:20.174154"
---

# 5 JSON Schemas That Stop AI Coding Agents From Shipping Garbage

## Overview

Your agent said "done". Production disagreed. If you run autonomous coding agents (Cursor, Claude Code, Windsurf, custom loops), you have met the silent failure mode: the agent returns plausible output, the pipeline accepts it, and the breakage surfaces three steps downstream. The fix is not a smarter model. It is deterministic contracts at every handoff. Below are the 5 JSON Schemas I now require in every agent pipeline. 1. Task Handoff Schema Every task between agents carries: id , goal , inputs[] , acceptance_criteria[] , max_turns . If an agent cannot produce acceptance_criteria , it is not allowed to start. 2. Tool-Call Envelope Wrap every tool call as {tool, args, expected_shape, on_failure} . expected_shape is validated before the result re-enters the agent context, so a malformed API response never poisons reasoning. 3. Code-Evaluation Result {status: pass|fail, tests_run, tests_passed, error_excerpt} . No free-text "looks good". A pipeline that cannot count tests cannot trust a claim. 4. Review Verdict {verdict: approve|request_changes, blocking_issues[], nits[]} . Splitting blocking from non-blocking stops the classic loop where an agent blocks a PR over a typo. 5. Artifact Manifest {files[], hash, produced_by, verified_by} . Determinism lives here: if the hash is not in the manifest, it did not ship. Why this works Schemas move failure detection left — from a 2 a.m. incident to a validation error at the boundary. They are boring, versionable, and model-agnostic: swap GPT for Claude and the contracts still hold. I packaged these 5 schemas (plus a Pydantic V2 validation CLI and cross-platform configs for Cursor/Windsurf/Claude Code) into a drop-in vault: -> Universal Agent Skills & Production Prompt Vault 2026 — 50% OFF with code LAUNCH50 https://ancuboy.gumroad.com/l/universal-agent-skills-vault/LAUNCH50 Deploy contracts that hold. Stop fixing broken agent runs by hand. Built by a solo engineer shipping deterministic automation tools.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/housharenet/5-json-schemas-that-stop-ai-coding-agents-from-shipping-garbage-25b4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
