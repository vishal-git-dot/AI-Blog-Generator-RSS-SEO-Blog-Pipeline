---
title: "Compaction turns your agent's decisions into folklore — here's the fix"
slug: "compaction-turns-your-agents-decisions-into-folklore-heres-the-fix"
author: "Linford Reyes"
source: "devto_python"
published: "Wed, 12 Aug 2026 18:41:37 +0000"
description: "Compaction turns your agent's decisions into folklore — here's the fix Last week I posted about context compaction silently destroying agent memory. The resp..."
keywords: "recovery, your, memory, decision, provenance, compaction, agent, decisions"
generated: "2026-08-12T19:08:00.188617"
---

# Compaction turns your agent's decisions into folklore — here's the fix

## Overview

Compaction turns your agent's decisions into folklore — here's the fix Last week I posted about context compaction silently destroying agent memory. The response that stuck with me came from a reader working on ranking and Maps workflows: "A decision like 'location visibility dropped' is weak unless the summary keeps the grid, query set, timestamp, competitor set, and changed GBP fields. Without that provenance, compaction turns an observation into folklore." Folklore. That's the word. A decision without its source isn't weaker information — it becomes unquestionable. There's nothing left to challenge it with. That comment landed as a feature within hours (v0.3.1: decisions carry source + evidence, and the audit tool grades them). But the reader's follow-up made me look at the other half of the pipeline, and I found something embarrassing: the audit could detect lost provenance, but the recovery side never restored it. The verdict would say "decision lost provenance", then the recovery block would re-inject the decision without the source anyway. Half a fix. So this week: Wrote a recover-side drill that checks every expected item — rules, todos, decisions with source and evidence , progress — verbatim inside the recovery block, per category, with an exit-code gate. Ran it against a manifest with provenance: decisions recovered at 50% before the fix, 100% after. Fixed the recovery block to re-inject source/evidence alongside each decision (empty fields are skipped, so existing manifests are unaffected). 37 tests pass. The pipeline is now symmetric: preserve side: compaction_drill measures what your compressor destroys audit side: cam judge classifies every tracked item verbatim / paraphrased / lost recover side: recover_drill verifies the recovery block re-anchors everything — provenance included Why provenance is the part that matters most: a compressed memory that keeps "we decided X" but drops "because file Y behaved this way on date Z" will steer future code while being impossible to challenge. The next agent run inherits the conclusion without the evidence. That's how bugs become traditions. The fix is one line in the recovery block per decision — but the test is the real deliverable. recover_drill.py runs against your own manifest and the summary your compressor actually produced, and fails the exit code with a per-category report if anything is missing. No more trusting the recovery path. If you run long agent sessions and have ever wondered whether the compressed memory is still the same memory — run the drill. It takes a minute, and the first run usually surprises you. repo: https://github.com/44334433/memory-anchor (v0.3.2) first post: https://dev.to/linfordr/context-compaction-is-silently-destroying-your-llm-agents-memory-2pg2

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/linfordr/compaction-turns-your-agents-decisions-into-folklore-heres-the-fix-4pn1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
