---
title: "Claude Code Tops JetBrains' New Kotlin Benchmark with 85.7% Resolution"
slug: "claude-code-tops-jetbrains-new-kotlin-benchmark-with-857-resolution"
author: "gentic news"
source: "devto_ai"
published: "Thu, 09 Jul 2026 03:38:23 +0000"
description: "Claude Code with Opus 4.7 xhigh tops JetBrains' Kotlin Benchmark at 85.7%. Configure your CLAUDE.md with Kotlin conventions and use --model opus-4.7-xhigh to..."
keywords: "kotlin, claude, benchmark, code, xhigh, model, your, jetbrains"
generated: "2026-07-09T03:49:54.087583"
---

# Claude Code Tops JetBrains' New Kotlin Benchmark with 85.7% Resolution

## Overview

Claude Code with Opus 4.7 xhigh tops JetBrains' Kotlin Benchmark at 85.7%. Configure your CLAUDE.md with Kotlin conventions and use --model opus-4.7-xhigh to match this performance. Key Takeaways Claude Code with Opus 4.7 xhigh tops JetBrains' Kotlin Benchmark at 85.7%. Configure your CLAUDE.md with Kotlin conventions and use --model opus-4.7-xhigh to match this performance. What Changed — JetBrains Just Released a Kotlin-Specific AI Benchmark On July 8, 2026, JetBrains launched the Kotlin Benchmark — the first public benchmark specifically designed to evaluate AI coding agents on real-world Kotlin software engineering tasks. Unlike existing Kotlin evaluations like Kotlin_HumanEval (which test syntax and core concepts), this benchmark measures end-to-end task completion: reading an issue, navigating a repository, and generating a validated patch. The dataset includes 105 tasks sourced from active open-source Kotlin repositories. Each task is verified in a containerized environment — a solution only counts if it passes all tests. What It Means For You — Claude Code Dominates, But The Real Signal Is Configuration The first leaderboard results are telling: Rank Agent Model Config Score 1 Claude Code Opus 4.7 xhigh 85.71% 2 JetBrains Junie Opus 4.7 max 81.9% 3 Codex GPT 5.5 xhigh 81.9% Claude Code with Opus 4.7 xhigh resolved 90 of 105 tasks — a 4-point lead over the next best setup. But here's what matters for your daily workflow: the benchmark reveals that model choice and configuration directly impact Kotlin task resolution . The same model (Opus 4.7) in different configurations (xhigh vs. max) produced different results. Try It Now — Replicate the Winning Setup If you work with Kotlin, here's how to match the benchmark-winning configuration: 1. Use the xhigh model variant claude --model opus-4.7-xhigh The "xhigh" variant provides extended context and reasoning capacity, which is critical for navigating large Kotlin codebases with complex type hierarchies. 2. Optimize your CLAUDE.md for Kotlin Based on the benchmark's task structure, your CLAUDE.md should include: # Kotlin Project Context - Build system: Gradle (Kotlin DSL) - Testing framework: Kotest / JUnit 5 - Code style: Official Kotlin style guide - Coroutines: kotlinx.coroutines (structured concurrency) - Serialization: kotlinx.serialization # Task Execution Rules 1. Read the full issue description before modifying code 2. Navigate the repository to understand existing patterns 3. Generate patches that pass existing tests 4. Do not introduce new dependencies unless specified 3. Enable file-level context awareness Claude Code's advantage came from its ability to interpret issue descriptions and navigate project context. Make sure you're using the full file context mode: claude --context full Why This Benchmark Matters for Your Workflow This isn't just another leaderboard. The Kotlin Benchmark is the first to measure agentic task completion specifically for Kotlin — which means the results directly translate to how well these setups will perform on your Kotlin projects. Key takeaways: Model quality matters more than agent brand : Claude Code and Junie both use Opus 4.7, but configuration differences produced a 4-point gap. The agent framework matters, but the model is the foundation. Task interpretation is the bottleneck : The benchmark tests whether an agent can read an issue, understand the repository, and produce a correct patch. This is exactly what you ask Claude Code to do daily. Containerized verification is your QA : The benchmark's strict pass/fail based on test verification mirrors what you should be doing: always run tests after an AI-generated patch. The Bottom Line JetBrains' Kotlin Benchmark confirms what many Claude Code users already know: with the right model configuration and project context, Claude Code handles real-world Kotlin tasks at an 85%+ success rate. Start by adding model selection to your workflow ( --model opus-4.7-xhigh ) and investing in your CLAUDE.md to describe Kotlin conventions and build setup. The benchmark is open-source on GitHub . You can even run it against your own codebase to see how your setup compares. Source: blog.jetbrains.com [Updated 09 Jul via github_changelog] GitHub launched Codex as a new agent provider in public preview for JetBrains IDEs on July 7, 2026, one day before JetBrains released its Kotlin Benchmark [per GitHub Blog]. The integration adds Hooks support, richer MCP server management, and custom model configuration. While Codex placed third on the benchmark (81.9% with GPT 5.5 xhigh), this update means developers can now run Codex directly inside JetBrains without switching to a terminal — potentially narrowing the gap with Claude Code by improving workflow integration. Originally published on gentic.news

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gentic_news/claude-code-tops-jetbrains-new-kotlin-benchmark-with-857-resolution-5cf5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
