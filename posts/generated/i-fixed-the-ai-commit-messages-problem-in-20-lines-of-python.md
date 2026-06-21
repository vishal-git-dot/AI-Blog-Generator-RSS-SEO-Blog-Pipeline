---
title: "I Fixed the "AI Commit Messages" Problem in 20 Lines of Python"
slug: "i-fixed-the-ai-commit-messages-problem-in-20-lines-of-python"
author: "Enjoy Kumawat"
source: "devto_python"
published: "Sun, 21 Jun 2026 09:14:30 +0000"
description: "You've probably seen that trending post — "I Asked AI to Write My Commit Messages and It Was Embarrassing." Same. But instead of accepting embarrassing outpu..."
keywords: "git, diff, commit, you, claude, message, system, api"
generated: "2026-06-21T09:58:05.290632"
---

# I Fixed the "AI Commit Messages" Problem in 20 Lines of Python

## Overview

You've probably seen that trending post — "I Asked AI to Write My Commit Messages and It Was Embarrassing." Same. But instead of accepting embarrassing output, I fixed it. Here's the thing: the problem isn't AI writing commit messages. The problem is how you ask it. One clear system prompt + the actual diff = surprisingly good results. The Setup No new packages. No API key. If you have Claude Code , you're already set. #!/usr/bin/env python3 import subprocess SYSTEM = ( " You are a git commit message generator. " " Output ONLY the commit message — no explanation, no markdown, no quotes. " " Follow Conventional Commits: type(scope): subject. " " Types: feat, fix, docs, style, refactor, test, chore. " " Subject: imperative, lowercase, max 72 chars. " ) diff = subprocess . check_output ([ " git " , " diff " , " --staged " ], text = True ) if not diff . strip (): print ( " Nothing staged. Run `git add` first. " ) raise SystemExit ( 1 ) msg = subprocess . check_output ( [ " claude " , " -p " , SYSTEM + " \n\n " + diff ], text = True , ). strip () print ( msg ) That's it. 20 lines. Uses the claude CLI under the hood — no API key, no config, just your existing Claude Code OAuth session. Why It Works The system prompt does the heavy lifting. Three constraints: Output ONLY the commit message — no preamble, no explanation Follow Conventional Commits — feat , fix , chore , etc. max 72 chars — keeps it readable in git log The diff is the context. You're not asking "write a commit message". You're asking "given these exact changes, what happened?" That's a much more answerable question. Usage # No setup needed if you have Claude Code. Just: git add . python /path/to/git_commit.py # → feat(server): add AI commit message generator via Claude CLI Or wire it into a git alias: git config --global alias.ai '!python /path/to/git_commit.py' # git ai The Results Before: update stuff fix bug WIP added the thing After: feat(api): add generate_commit_message tool to MCP server fix(auth): handle expired token on refresh refactor(db): extract query builder into separate module As an MCP Tool Too I also wrapped it as an MCP tool so Claude Code can call it directly from any conversation: @mcp.tool () def generate_commit_message ( diff : str ) -> str : """ Generate a Conventional Commits message from a git diff string. """ full = SYSTEM + " \n\n " + diff return subprocess . check_output ([ " claude " , " -p " , full ], text = True ). strip () Full project: github.com/enjoy-kumawat/my-git-manager 20 lines. No new dependencies. No API key. Conventional Commits every time. The embarrassing part was waiting this long to build it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/enjoy_kumawat/i-fixed-the-ai-commit-messages-problem-in-50-lines-of-python-3a5a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
