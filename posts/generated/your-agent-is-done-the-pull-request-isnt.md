---
title: "Your agent is done. The pull request isn't."
slug: "your-agent-is-done-the-pull-request-isnt"
author: "Little Pan"
source: "devto_ai"
published: "Sat, 24 Oct 2026 03:55:10 +0000"
description: "Claude Code fixed the bug in four minutes and opened a pull request. Then I spent the next forty refreshing it. E2E tests still running. Refresh. Still runni..."
keywords: "agent, when, merge, what, you, code, running, row"
generated: "2026-10-24T04:04:22.635560"
---

# Your agent is done. The pull request isn't.

## Overview

Claude Code fixed the bug in four minutes and opened a pull request. Then I spent the next forty refreshing it. E2E tests still running. Refresh. Still running. Refresh. Review bot waiting for checks. Refresh. Red. The agent was done. The pull request wasn't. PonyMux 0.14 moves that wait into the app. Every PR in the Inspector now shows where it stands: checks running, passed, or failing, merge conflicts, and what the review bots said. When it's ready, merge it from the same row. And a new Servers section lists the dev servers your agent started in the Terminal, so the one from an hour ago stops holding port 5173. Why am I still waiting after the agent finished? Writing the code got fast. Everything after it didn't. CI runs, then the review bots run, and CodeRabbit by default waits for GitHub Checks to finish before it reviews. With two or three agents going, that's two or three PRs, each in a different state, each behind a browser tab. It isn't just me. A Harvard working paper by Fiona Chen and James Stratton, using data from 718 companies, found that coding agents raised code output by about 30%, while the time from opening a pull request to merging it went up 49% ( summary ). It's not peer reviewed yet, and the data come from an analytics vendor. Still, it matches the afternoon above. On Hacker News someone described fixing CI on a "5-minute-delay loop" as hell, and the reply was a skill that spins up a subagent just to poll the PR. I wanted the poll without the tab. Is CI done yet? Did the review pass? Open the Inspector next to a Terminal running Claude Code, Codex, or Grok. Each row under Pull Requests now carries its status. A pulsing ring while checks run, a green check when they pass, a red cross with the number failing. A triangle when the branch has conflicts. A badge on the PR icon for the review bots: Codex, CodeRabbit, GitHub Copilot, Gemini Code Assist, Claude, and Cursor Bugbot. Hover the row and you get each bot's verdict in words. Status updates on its own while the row is on screen, and again when you come back to the app. It's read with your gh login, so private repositories work. If gh isn't installed or signed in, the ⓘ next to the section turns yellow and tells you the command. Don't want it? Turn it off in Settings → General. You find out it's red when it turns red, not on the fourth refresh. Can I merge without opening GitHub? Yes. Open the row's ⋯ menu and choose Merge . The menu already knows the repository's merge method, and when a merge can't go it says why: a draft, conflicts, branch protection, or a branch behind its base. Merging asks first. The dialog reads the PR from GitHub again, so you're confirming what's true now, not what was true when the row last updated. Pick a merge commit, squash, or rebase from what the repository allows, and tick a box to delete the branch. If branch protection is still waiting on checks, it offers auto-merge instead. The dialog stays until GitHub answers, so you see the result instead of guessing. Close and reopen work the same way. Which server did my agent leave running? This one is quieter. The agent runs npm run dev & to check a page, says it looks good, and moves on. The server doesn't. An hour later Vite tells you port 5173 is in use and quietly moves to 5174. People find these the hard way. In one Claude Code issue , a wrangler dev started this way kept running for two days at 89% CPU and 2.5 GB of memory. In another , a stuck process used 16 GB for over two hours, and it turned up only in ps aux . Servers lists every port a process started from this Terminal is listening on. Hover a row to see when and where it started, what started it ( claude › npm › node ), and the command. Click the trash button to stop it. PonyMux asks it to quit, forces it after 3 seconds, and leaves your shell and the agent alone. When the agent exits, Servers moves up near the top, where a forgotten one is hard to miss. The agent forgets what it started. The Inspector doesn't. What else changed? PRs and files created by subagents now show up in Pull Requests and Outputs, for Claude Code, Codex, and Grok. An agent you have installed but never ran shows a Connect button, with up-to-date install links. The working indicator stays on while a background subagent is still busy. Moving a Terminal to the Trash or Archive stops what's running in it, servers included. Quit and crash dialogs follow your light or dark theme. The status badge on Terminal rows no longer sits on a backing circle. Status, merging, and Servers are covered in Workspace and Navigation . For the full list, see the changelog . PonyMux is free for macOS: download it here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/heylittlepan/your-agent-is-done-the-pull-request-isnt-1877

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
