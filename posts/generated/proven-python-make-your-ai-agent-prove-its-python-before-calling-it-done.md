---
title: "proven-python: make your AI agent prove its Python before calling it done"
slug: "proven-python-make-your-ai-agent-prove-its-python-before-calling-it-done"
author: "Shan Wijenayaka"
source: "devto_python"
published: "Sat, 20 Jun 2026 19:03:14 +0000"
description: "The problem Most code an AI agent writes looks right. It compiles, it reads well, it probably works. "Probably" is the problem. The agent stops when the work..."
keywords: "python, proven, agent, code, your, done, skill, not"
generated: "2026-06-20T19:45:32.621674"
---

# proven-python: make your AI agent prove its Python before calling it done

## Overview

The problem Most code an AI agent writes looks right. It compiles, it reads well, it probably works. "Probably" is the problem. The agent stops when the work looks done, and "looks done" is rarely "proven done." You find the gap later, in production, in the case nobody tested. proven-python proven-python is a Claude Code skill that holds an AI coding agent to the way a disciplined engineer actually works on Python: Write the failing test first, then the code that makes it pass. Type every signature and pass mypy --strict, with no unexplained ignores. Keep functions small and honestly named. A bug fix ships with a regression test that fails without the fix. Nothing is "done" until ruff, mypy, and pytest are all green. It is model-invoked: the agent loads it when it is about to write, change, debug, test, or review Python, and follows the procedure instead of producing plausible-looking code nobody ran. It does not get in your way A discipline skill that fights your agent is worse than no skill. proven-python has an "apply with judgment" rule: scale the rigor to the code (a throwaway script earns the spirit, not the full gate), defer to your instructions and the codebase's conventions, and skip the ceremony on a one-line diff. It is built to align with Anthropic's own Claude Code best practices, not override them. How it is built The procedure stays short. Depth (testing, typing, design, docs, review, human-readable output) lives in reference files that load on demand, so it does not bloat context. It ships copy-pasteable pyproject, pre-commit, and CI templates, because a command that fails the build beats a paragraph asking the model to behave. It is agent-agnostic: plain Markdown, so it drops into Codex, Cursor, or any agent that reads a skill or an instructions file. The repo holds its own code to the same bar: the validation script is typed, tested, and gated by CI. Install /plugin marketplace add shanwije/proven-python /plugin install proven-python Or copy skills/proven-python into your project's .claude/skills. Open source MIT licensed, principles distilled from the canonical Python and engineering literature with every source and its license listed in the repo. Feedback and PRs welcome, especially on where it is too strict or gets in the way. https://github.com/shanwije/proven-python

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shan_wijenayaka_ecbe5dc32/proven-python-make-your-ai-agent-prove-its-python-before-calling-it-done-3kj1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
