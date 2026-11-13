---
title: "I stopped letting Opus write my code (and my weekly quota survived)"
slug: "i-stopped-letting-opus-write-my-code-and-my-weekly-quota-survived"
author: "Yiğit Güldal"
source: "devto_ai"
published: "Fri, 13 Nov 2026 14:22:12 +0000"
description: "one day claude ate 62% of my weekly quota in a single day. i was letting opus write every line. so i changed one rule: claude plans and reviews, cheaper mode..."
keywords: "one, write, claude, code, lead, diff, worker, file"
generated: "2026-11-13T14:27:37.207680"
---

# I stopped letting Opus write my code (and my weekly quota survived)

## Overview

one day claude ate 62% of my weekly quota in a single day. i was letting opus write every line. so i changed one rule: claude plans and reviews, cheaper models write the code. the split lead (claude): reads the task, splits it into small pieces with the exact files and an acceptance check, then reviews the diff workers (codex, opencode, free models): write the code for one piece each lead again: runs the tests itself, reads the real diff, sends it back if its off the trick is the spec. a worker that gets "fix the login bug" burns tokens wandering around the repo. a worker that gets "edit src/auth.ts lines 40-80, expected behaviour X, run npm test auth , short report" finishes fast and cheap. what broke when i did it by hand 5 terminals, copy pasting context between them forgetting which agent was on which file two agents editing the same file a long build dying at the 5 hour limit in the middle of a task what fixed it one git worktree per agent, so they never share a checkout one memory file in the repo, so the next session doesnt start from zero the lead always looks at the real diff, never trusts the worker's report you can do all of this with plain terminals and a CLAUDE.md. i ended up building a desktop app for it, foxpit , but the split works without it too.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yiit_gldal_755ea0157bad/i-stopped-letting-opus-write-my-code-and-my-weekly-quota-survived-26ka

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
