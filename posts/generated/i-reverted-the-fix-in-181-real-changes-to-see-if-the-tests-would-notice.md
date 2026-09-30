---
title: "I reverted the fix in 181 real changes to see if the tests would notice"
slug: "i-reverted-the-fix-in-181-real-changes-to-see-if-the-tests-would-notice"
author: "syntaxixr"
source: "devto_python"
published: "Wed, 30 Sep 2026 12:05:24 +0000"
description: "I keep running into the same thing with coding agents. The agent fixes a bug, adds a test, CI goes green, and it says "done". But green only means the test p..."
keywords: "test, fix, agent, change, tests, only, code, receipts"
generated: "2026-09-30T12:15:50.056874"
---

# I reverted the fix in 181 real changes to see if the tests would notice

## Overview

I keep running into the same thing with coding agents. The agent fixes a bug, adds a test, CI goes green, and it says "done". But green only means the test passes. It doesn't mean the test would have failed before the fix. And if it wouldn't, it checks nothing about the bug, however green it is. The old-school way to find out is boring: revert the fix and run the test again. So I wrote a tool that does exactly that for every test in a change, and pointed it at the real history of 17 open-source projects. How the check works For each test a change adds or edits, it does two runs. First the test runs with the change. Then only the changed source files go back to the base branch (tests, dependencies and config stay new) and the same test runs again. Fails without the fix, passes with it: PROVEN . This is what you want. Passes both ways: THEATER . It proves nothing about this change. Fails on the old code only because it imports something that didn't exist yet: WEAK . Passes both ways but sits next to a test that does prove the change: GUARD . That's fine, it's the "did I break the neighboring case" test. What I found I took two samples. 81 fix commits from the maintainers of twelve libraries (click, sqlparse, marshmallow, dateutil, more-itertools and others), and 100 pull requests that carry a coding agent's fingerprint, from five repos that are full of agent work: Claude Agent SDK, OpenAI Agents SDK, the MCP Python SDK, fastmcp and simonw/llm. 87 of those 100 were Claude Code. Proven Weak only Maintainer fix commits 90% 0% Agent pull requests 82% 10% Good news first: most tests do their job. These are well-run projects, some of them run by the companies that build the agents. The difference is that WEAK column. In 10% of the agent PRs, every test failed on the old code for the same reason: the test file imports, at the top, a name that the change adds. On the old code that import breaks, the whole file can't load, and every test in it "fails". It looks like proof, but none of those tests ever ran against the old behavior. One example is anthropics/claude-agent-sdk-python#1016 . The test file gets two new imports at the top: from claude_agent_sdk.types import ( TERMINAL_TASK_STATUSES , ... TaskUpdatedMessage , ... ) On the old code neither name exists, so all 10 changed tests die at import, including one that was already there. The fix may well be right. The tests just can't show it. The cheap cure is to import new names inside the tests that need them, so the rest of the file still runs on the old code. No maintainer commit in my sample looked like that. THEATER is rare Only 7 of the 162 changes I could judge were unproven, and every one had a reason. Type-only fixes (runtime tests can't see types). A Windows newline fix tested on Linux, where the bug doesn't exist. A dateutil __repr__ fix whose new output matched what the inherited default already printed. A maintenance commit that happened to mention an issue number. So when the tool says THEATER, there's usually something worth a look. Try it In any git repo, on a branch with a fix and its test: npx github:syntaxixr/receipts check It's deterministic, with no LLM and no API keys, and it runs your own pytest, vitest or jest. There's also a GitHub Action that keeps one comment on the PR, and a skill so the agent checks its own tests before it says it's done: # Claude Code /plugin marketplace add syntaxixr/receipts /plugin install receipts-check@receipts # Codex, Cursor and other agents npx skills add syntaxixr/receipts The fine print The samples are small and not random, so the numbers describe those projects, not the whole ecosystem. "Agent-authored" only means an agent's fingerprint is in the commits, and humans steer those agents. "Judged" means at least one test ran on both sides. The rest failed for environment reasons, since I installed each project once at its current tip. PROVEN means the test notices the change, not that the change is correct. Python and JS/TS only for now. Repo: https://github.com/syntaxixr/receipts . Every change with a link and the method: https://github.com/syntaxixr/receipts/blob/main/docs/study.md . Data: https://huggingface.co/datasets/syntaxixr/receipts-study If it says something wrong about your code, I'd like to hear about it. Heads up: I drafted this post with an AI assistant. The numbers come from the study in the repo, and every change is linked there so you can check them yourself.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/syntaxixr/i-reverted-the-fix-in-181-real-changes-to-see-if-the-tests-would-notice-2e3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
