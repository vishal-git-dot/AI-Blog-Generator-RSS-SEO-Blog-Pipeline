---
title: "I tested whether a code health score actually predicts bugs. Here's the benchmark"
slug: "i-tested-whether-a-code-health-score-actually-predicts-bugs-heres-the-benchmark"
author: "Raghav Chamadiya"
source: "devto_python"
published: "Sat, 06 Jun 2026 07:57:41 +0000"
description: "Most code health scores are vibes. A number goes up, a number goes down, and nobody checks whether the files it flags are the files that actually break later..."
keywords: "repowise, health, files, same, score, code, defect, file"
generated: "2026-06-06T08:41:07.450205"
---

# I tested whether a code health score actually predicts bugs. Here's the benchmark

## Overview

Most code health scores are vibes. A number goes up, a number goes down, and nobody checks whether the files it flags are the files that actually break later. I wanted to know if the score I built does better than that, so I ran it against a defect corpus and put it head to head with the leading commercial code-health tool. On the same 2,770 files across 9 languages, scored at the same leakage-free commit against the same defect labels, the score surfaces 2.3x the defects under a fixed review budget. This post is how that works, and the four other layers sitting next to it in repowise . What the score is Every file gets a 1 to 10 score from 25 deterministic biomarkers. McCabe complexity, deep nesting, brain methods, class cohesion (LCOM4), god classes, native Rabin-Karp clone detection, untested hotspots, function-level churn, code-age volatility, ownership dispersion, change entropy, co-change scatter, prior-defect history, test-quality smells, and more. No LLM calls. No cloud. No new runtime dependency. It is pure Python over tree-sitter and git data, and it finishes in under 30 seconds on a 3,000-file repo. repowise health # KPIs + lowest-scoring files repowise health --coverage cov.lcov # ingest LCOV/Cobertura/Clover repowise health --refactoring-targets # ranked by impact / effort repowise health --trend # snapshots + declining alerts The biomarker weights are calibrated against a real defect corpus instead of hand-tuned. Only the learned constants ship. The runtime itself stays fully deterministic, so the same file produces the same score every time. Does the score find bugs The validation setup avoids the usual leakage trap. Health scores are collected at a historical commit (call it T0). Bug-fixing commits are counted over the following 6 months. Then the two get correlated. The score never sees the future it is being graded on. Across 21 open-source repositories spanning all 9 Full-tier languages: Cross-project mean ROC AUC of 0.74 [95% CI 0.68 to 0.79] at identifying files that go on to receive bug fixes. Up to 0.90 on individual repos. It survives controlling for file size (partial Spearman rho = -0.16). It is not just flagging the big files. It out-discriminates recent churn by +0.10 AUC and prior-defect history by +0.12 AUC, DeLong p < 1e-9. It holds on an external published dataset it has never seen (PROMISE/jEdit CK-metrics: AUC 0.76 to 0.78, within about 0.03 of that dataset's own tuned model). Head to head Same files, same commit, same labels, paired tests against the leading commercial code-health tool: Axis repowise Commercial tool Recall @ 20%-of-lines budget 0.173 0.074 Effort-aware ranking (Popt) 0.607 0.462 Defect density, size-normalized (Alert:Healthy) 2.18x 0.56x Discrimination (ROC AUC) 0.731 0.705 Ranking files by repowise health surfaces 2.3x the defects under a fixed review budget. Popt delta +0.144, recall delta +0.098, density delta p = 0.003, all paired and significant. Full methodology and CIs . The four other layers Code health is one of five. The point of the other four is that your AI coding agent reads files but knows nothing about how the codebase got there. Graph. A real tree-sitter dependency graph across 15 languages. File and symbol nodes, 3-tier call resolution, Leiden communities, PageRank, framework-aware route-to-handler edges. Git. Behavioral signals static analysis cannot see. Hotspots (churn times complexity), ownership percentages, co-change pairs that expose hidden coupling, bus factor, reviewer suggestions. Docs. An LLM-generated wiki per module and file, rebuilt incrementally on every commit with freshness and confidence scoring, searchable via hybrid RAG (full-text plus vector through reciprocal rank fusion). Decisions. Architectural decisions mined from 8 sources, evidence-backed, linked to graph nodes, connected by supersedes / refines / conflicts_with edges. This is the layer most tools capture nowhere. The agent angle All five layers expose through nine MCP tools shaped around tasks, not data entities. You pass multiple files or symbols in one call and get complete context back, instead of chaining 30 greps and reads. Paired SWE-QA runs on real repos, same model and harness, with and without the MCP tools: 70% fewer tool calls 89% fewer file reads 36% lower cost per query answer quality at parity Feeding an agent a commit through get_context costs 2,391 tokens versus 64,039 for the raw changed files. About 27x fewer. There is also repowise distill , which compresses noisy command output before the agent reads it, errors first, every omission reversible: Command Raw to distilled tokens Saved pytest -q (11 failures) 3,374 to 1,317 61% git log -50 3,064 to 331 89% git diff (30 commits) 62,833 to 8,635 86% Try it pip install repowise cd your-project repowise init # builds all five layers repowise serve # MCP server + local dashboard The graph, git, dead-code, and health layers build in minutes with zero LLM calls. Run repowise init --index-only for a queryable index almost immediately. After that, every commit-triggered update takes under 30 seconds and only regenerates the pages your change touched. 100% local, bring your own API key, AGPL-3.0. Repo, benchmarks, and live demo: github.com/repowise-dev/repowise and repowise.dev . If you run the health-defect benchmark on your own repos, I want to see the numbers. The whole harness is public so you can reproduce or break it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/raghav_builds/i-tested-whether-a-code-health-score-actually-predicts-bugs-heres-the-benchmark-10dl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
