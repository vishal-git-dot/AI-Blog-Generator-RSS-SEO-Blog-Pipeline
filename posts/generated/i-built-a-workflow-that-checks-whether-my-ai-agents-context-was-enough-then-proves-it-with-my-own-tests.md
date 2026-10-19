---
title: "I built a workflow that checks whether my AI agent's context was enough, then proves it with my own tests"
slug: "i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-tests"
author: "Ryan Cotten"
source: "devto_python"
published: "Mon, 19 Oct 2026 03:41:21 +0000"
description: "When I give an AI coding agent a task, I never actually know if the context I sent it was enough. So I built the check. The stack is four small tools, all Py..."
keywords: "own, all, one, agent, task, checks, tests, when"
generated: "2026-10-19T04:06:19.787703"
---

# I built a workflow that checks whether my AI agent's context was enough, then proves it with my own tests

## Overview

When I give an AI coding agent a task, I never actually know if the context I sent it was enough. So I built the check. The stack is four small tools, all Python standard library, all MIT, all local: GhostSlice cuts a project down to a task bundle and reports the token cut. On my own bench repo: 74,692 tokens full, 29,926 sliced. GhostVerify checks the bundle against the task before an agent runs, and says gaps_found when something reachable is missing. GhostBench runs the same task full vs sliced and, when you give it a test command, executes your tests in a contained runner (scrubbed environment, your secrets never reach the test process) and labels the result honestly: static analysis is not called a live run. GhostConsole renders one board from all of it, and its Verified column now names the strongest evidence behind it and counts the checks that are missing. A fifth tool, ghostworkflow, runs the chain in one command, and a small local web app puts a face on it. I ran the whole thing on its own repo and published the result warts and all: verdict attention, 2 verify gaps, and a test failure that turned out to be a path assumption in one of my own tests. The first dogfood run also caught a real bug in the contained runner (it hid the user site-packages, so pytest vanished), which is fixed and shipped. I am looking for 5 to 10 developers who use AI coding agents daily to run it on one of their own repos and tell me where it breaks or bores them. Quickstart is 6 clones and one command. Links and the case study: https://gist.github.com/littlestjames82-sys/7e8309315c89706aefa97de6a4cc5399 What I want to know most: did the verify verdict match what your agent actually struggled with?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/littlestjames82sys/i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-4214

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
