---
title: "keelyard: making AI coding agents prove their work"
slug: "keelyard-making-ai-coding-agents-prove-their-work"
author: "Akobir Tulqinov"
source: "devto_python"
published: "Thu, 29 Oct 2026 04:45:28 +0000"
description: "I'm a solo developer from Uzbekistan. Most of what I ship (Telegram bots and mini apps for small businesses) I build together with AI coding agents. They're ..."
keywords: "keelyard, tests, test, your, they, claude, code, codex"
generated: "2026-10-29T05:13:43.942977"
---

# keelyard: making AI coding agents prove their work

## Overview

I'm a solo developer from Uzbekistan. Most of what I ship (Telegram bots and mini apps for small businesses) I build together with AI coding agents. They're fast, but they have one habit that cost me hours: they say "done" when the work isn't done. Tests still red. Sometimes tests quietly removed. keelyard is my fix. It's a Python CLI plus an MCP server that plugs into Claude Code, Codex and OpenCode. What it does Proof gate. If the agent changed files, it can't finish until the tests pass on the current files. The evidence is labeled: test-verified, command-succeeded or agent-claimed. Deleted tests, new skips and removed assertions keep the gate closed. Rewind. Every edit is snapshotted into .keelyard/shadow.git , separate from your repo. Any step can be undone, and the undo is undoable. Smaller context. Filters for pytest, go test, cargo, jest, ruff, mypy, git and grep keep every error, warning and file:line and collapse the rest. Each filter is tested against real logs in tests/corpus/ . Try it pip install keelyard cd your-project keelyard init --preset lean keelyard doctor Honest limits Proof is only as good as your test suite. Snapshots restore files, not databases or deployed services. The token numbers in BENCHMARKS.md (267,525 -> 52,745 tokens over six tasks, -80%) come from small samples (3-8 runs per setup) on OpenCode only. Savings on Claude Code and Codex aren't measured yet. Claude Code and Codex are checked end to end in CI with the real CLIs and a local scripted model, which proves the wiring, not model quality. CI runs on Linux, macOS and Windows with Python 3.11 to 3.13. It's Apache-2.0, with no telemetry. Repo: https://github.com/akobirjontulqinovfuture/keelyard . Issues labeled "good first issue" are a good place to start, and real logs from your test runners are the most useful thing you can send.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/akobirjontulqinovfuture/keelyard-making-ai-coding-agents-prove-their-work-1j30

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
