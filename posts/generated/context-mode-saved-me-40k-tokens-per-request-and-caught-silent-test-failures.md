---
title: "Context Mode Saved Me 40K Tokens Per Request (And Caught Silent Test Failures)"
slug: "context-mode-saved-me-40k-tokens-per-request-and-caught-silent-test-failures"
author: "Marcus Reed"
source: "devto_ai"
published: "Fri, 13 Nov 2026 23:21:32 +0000"
description: "The Problem Nobody Talks About Last month I spent two hours debugging why Cursor kept suggesting a deprecated API—one I'd removed three commits ago. The file..."
keywords: "context, test, mode, cursor, file, files, token, what"
generated: "2026-11-13T23:25:16.993349"
---

# Context Mode Saved Me 40K Tokens Per Request (And Caught Silent Test Failures)

## Overview

The Problem Nobody Talks About Last month I spent two hours debugging why Cursor kept suggesting a deprecated API—one I'd removed three commits ago. The file was gone. Git history was clean. Yet the AI insisted the old implementation was still valid. Turns out? Context window compression had silently dropped my recent changes. The model was working with a 6-hour-old snapshot of the codebase. Why Context Compression Breaks Silently Cursor (and most AI coding tools) aggressively compress context to fit models' token limits. When your codebase crosses that threshold: Recent file changes get deprioritized Test files disappear from context entirely The AI hallucinates based on stale architecture The worst part? No warnings. You just get confident, wrong answers. Enter Context Mode I found mksglu/context-mode after the third time I shipped a bug because Cursor's context and my actual codebase had diverged. It's a dead-simple VSCode extension that shows you exactly what files are in your AI's context window —in real time, with token counts. What It Actually Does # Install code --install-extension mksglu.context-mode # Then open Command Palette (Cmd+Shift+P) # Search: "Context Mode: Show Active Context" You get a live panel showing: Which files are currently loaded (by priority) Token count per file What got dropped due to limits Real-World Impact Before Context Mode: Me: "Why is the login test failing?" Cursor: "The test passes locally for me." [30 min of confusion] Turns out: test file wasn't in context After Context Mode: Context panel shows : auth . test . ts ( excluded - token limit ) Me : [ adds . cursorrules to prioritize test files ] Cursor : [ actually sees the failing assertion ] My .cursorrules Setup I now force-include critical files that Cursor's auto-prioritization misses: # .cursorrules context : always_include : - "**/*.test.ts" - "**/*.spec.ts" - "vitest.config.ts" - "tsconfig.json" exclude : - "node_modules/**" - "dist/**" - "*.log" This cut my context size from 52K → 12K tokens while keeping test coverage visible. The Verification Script I added this to my pre-commit hook: #!/bin/bash # .git/hooks/pre-commit # Check if critical files are in Cursor's context context_check ( ) { local file = $1 if ! cursor-context-cli contains "$file" ; then echo "⚠️ $file missing from AI context" exit 1 fi } context_check "vitest.config.ts" context_check "src/**/*.test.ts" (Note: cursor-context-cli is a hypothetical wrapper—Context Mode doesn't ship a CLI yet, but the VSCode API makes this trivial to build.) What I Learned AI coding tools lie by omission. If a file isn't in context, the model will confidently work around its absence. Token budgets are not fungible. Dropping test files to fit more source code is almost always the wrong tradeoff. Verification is cheaper than debugging. Spending 5 seconds checking Context Mode beats spending 20 minutes chasing phantom bugs. The Dilemma I'm Still Solving Context Mode solved visibility, but I'm still wrestling with prioritization: If I force-include all tests, I hit token limits on large PRs If I let Cursor auto-prioritize, it drops the exact test that would've caught my bug Manual context curation per task feels like fighting the tool How do you decide what belongs in context when everything feels critical?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/marcus_reed/context-mode-saved-me-40k-tokens-per-request-and-caught-silent-test-failures-2mni

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
