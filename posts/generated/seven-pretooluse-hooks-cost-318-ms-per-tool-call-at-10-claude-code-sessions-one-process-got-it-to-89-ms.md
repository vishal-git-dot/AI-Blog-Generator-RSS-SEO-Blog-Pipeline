---
title: "Seven PreToolUse hooks cost 318 ms per tool call at 10 Claude Code sessions. One process got it to 89 ms."
slug: "seven-pretooluse-hooks-cost-318-ms-per-tool-call-at-10-claude-code-sessions-one-process-got-it-to-89-ms"
author: "Myeongseok Kang"
source: "devto_ai"
published: "Wed, 11 Nov 2026 13:47:17 +0000"
description: "I run many Claude Code sessions on one machine at the same time, often ten or more. Each of them makes a shell call every few seconds, and every shell call g..."
keywords: "guard, one, bulkhead, process, code, sessions, call, claude"
generated: "2026-11-11T13:54:26.915133"
---

# Seven PreToolUse hooks cost 318 ms per tool call at 10 Claude Code sessions. One process got it to 89 ms.

## Overview

I run many Claude Code sessions on one machine at the same time, often ten or more. Each of them makes a shell call every few seconds, and every shell call goes through the PreToolUse hooks of claude-bulkhead , the plugin I wrote to stop those sessions from killing each other's dev servers, taking each other's ports and committing each other's half-finished edits. This post is about what those hooks cost, why the cost grew with the number of sessions, and how version 0.3.0 changed it. Where the time went Up to version 0.2, bulkhead registered seven separate Bash hooks: kill-guard, wait-guard, memory-guard, port-guard, checkout-guard, disk-guard and basics. Claude Code runs every matching hook for a tool call side by side, each as its own process with the payload on stdin. On an idle machine that looks cheap. The guards run in parallel, most of them only look at the command text, and one call took 47 ms on my MacBook Pro (M5 Pro, Node 24). The number that mattered was a different one. Starting Node alone takes 32 ms on that machine, so every guard paid most of its cost before reading a single byte of input. Seven guards meant seven Node processes per shell call. When ten sessions make a tool call at the same moment, which happens all the time when several agents are running test suites and builds, that is seventy Node processes starting at once and competing for the same cores. Each session then waited 318 ms for its hooks. With twenty sessions it was 611 ms. One process, cheapest checks first In 0.3.0 Claude Code starts a single hook for Bash and PowerShell, src/bash-guards.js , and that process runs the guards one after another. The order is deliberate. The guards that only parse the command text go first. The ones that may read git, the memory state, the process table or a port go last, and they only do that work after the text matched something: port-guard tries a TCP connection to the port before it reads any process list, checkout-guard runs git only when another session is alive, and basics runs git status only for git reset --hard and git clean . The process stops at the first block, so a blocked command never pays for the guards after it. The benchmark ships with the repository, so you can run it on your own machine: node scripts/bench-hooks.js 9 --sessions 10 On my machine it measured this: one process per guard (0.2) one process (0.3) one tool call, allowed 47 ms 76 ms 10 sessions at once 318 ms 89 ms 20 sessions at once 611 ms 109 ms The first row went the wrong way, and that is expected. Running the guards in a row is slower than running them side by side when nothing else is happening. I kept the change because nobody runs bulkhead for a single idle session. It exists for the case in the second and third rows, and there one process per call instead of seven is what keeps the hooks out of the way. Writing a block to the event log added no measurable time in either layout. What else is in 0.3.0 Merging the hooks also made two features easy that needed one place to see every guard's verdict. bulkhead explain -- <command> runs a command through every guard against the sessions, processes, ports and git tree on the machine right now, and prints what each one would say and why, without executing anything. Every block message now ends with a short code, and the user can run bulkhead allow <code> in their own terminal to let that exact command through once within ten minutes. A rule in basics blocks the agent from running bulkhead allow itself, so the approval stays with the person. kill-guard now also knows which session owns a process. kill <pid> and pkill -f <pattern> pass when they reach only your own session's processes and are blocked when they reach another live session's tree, and broad kills such as pkill -u , kill -1 , docker system prune and adb kill-server are blocked while another session is alive. The same guards can be registered for Codex, Gemini CLI, Copilot CLI, Cursor, Windsurf and five other agents with bulkhead setup <agent> --write . The full list is in the changelog . Trying it bulkhead has no dependencies and sends nothing off the machine. You can see what it would have done on your own history before turning anything on, because scan only reads your past transcripts: npx claude-bulkhead scan 30d To install it as a Claude Code plugin: /plugin marketplace add dooly6276/claude-bulkhead /plugin install bulkhead@bulkhead The code, the benchmark and the 18-second recording of a real session are on GitHub . Claude Code wrote most of the code and the tests with me, and I reviewed and measured every change described here.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dooly6276/seven-pretooluse-hooks-cost-318-ms-per-tool-call-at-10-claude-code-sessions-one-process-got-it-to-4mp2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
