---
title: "My Claude Code hook silently ate every Korean character, and it took me an hour to figure out why"
slug: "my-claude-code-hook-silently-ate-every-korean-character-and-it-took-me-an-hour-to-figure-out-why"
author: "coding_j"
source: "devto_ai"
published: "Sat, 06 Jun 2026 03:48:06 +0000"
description: "I spent an hour last week debugging a hook that wasn't broken. Here's the setup: I run Claude Code on Windows, and I'd written a little UserPromptSubmit hook..."
keywords: "you, claude, powershell, code, korean, file, bom, hook"
generated: "2026-06-06T04:00:30.109957"
---

# My Claude Code hook silently ate every Korean character, and it took me an hour to figure out why

## Overview

I spent an hour last week debugging a hook that wasn't broken. Here's the setup: I run Claude Code on Windows, and I'd written a little UserPromptSubmit hook in PowerShell — a keyword router that reads my prompt and, if it sees something like mcp 서버 or 코드 리뷰 , injects a hint so Claude pulls up the right skill. Half my prompts are in Korean, so a bunch of the regex patterns had Korean in them. It worked perfectly for the English rules. The Korean ones? Dead. No match, no error, no log line. The script ran, exited 0, and just... did nothing for half my inputs. I did all the dumb things first. Echoed the prompt — looked fine. Tested the regex in a PowerShell console — matched fine. Re-read the JSON parsing five times. Added Write-Host debugging everywhere. Nothing. The actual problem had nothing to do with my code. It was the file encoding . Windows PowerShell 5.1 (the default powershell.exe , not pwsh ) does not assume UTF-8 when it reads a .ps1 file. If there's no byte-order mark, it falls back to the legacy system code page. So my script — saved as plain UTF-8 by my editor — got its Korean bytes reinterpreted as garbage at parse time , before a single line ran. The regex literal that was supposed to be 코드.?리뷰 became mojibake, which of course never matches anything real. And because it's a parse-level reinterpretation, you don't get an error. You get silence. The fix is one line, once you know: function Add-Bom ( $path ) { $text = [ System.IO.File ]:: ReadAllText ( $path ) $enc = New-Object System.Text.UTF8Encoding $true # $true = write the BOM [ System.IO.File ]:: WriteAllText ( $path , $text , $enc ) } Add-Bom " $ env : USERPROFILE \.claude\skill-router.ps1" Re-save with a BOM and everything lights up. Pure-ASCII scripts don't care, which is exactly why every example you find online "works" — almost all of them are bash on macOS, and the handful of PowerShell ones never have a non-ASCII character to trip over. That bug annoyed me enough that I went and cleaned up my whole Claude Code setup so I'd never have to rediscover this stuff. A few things that were worth keeping: A PreToolUse safety hook that stops Claude before it runs rm -rf / , DROP TABLE , git push --force , taskkill , a disk format, etc. It doesn't hard-block — it injects a "show this to the user and confirm first" instruction. Saved me from a --hard reset I didn't mean to approve. The keyword router above, but as a documented template instead of my personal 400-line wall of rules. The value isn't my rules — you'll never have my skills installed — it's the pattern plus the encoding gotchas already solved. A tiny regression test harness for the router, because the day you add one rule above another and quietly break three existing ones is a bad day. It also has the one reliable way I found to pipe non-ASCII JSON into a child PowerShell without mojibake ( chcp 65001 + a temp file + stdin redirect — don't ask how long that took either). A handful of subagent definitions I actually use (reviewer, tester, a couple of stack-specific ones). I put it all up here, MIT, free: https://github.com/coding-jhj/claude-pwsh-kit It's not magic and it won't make Claude smarter. It's plumbing — guardrails, routing, and a setup guide that tells you about the BOM thing on page one so you don't lose the hour I lost. If you're on Windows and your hooks are misbehaving in ways that make no sense, check your encoding before you check your logic. And if you've hit other PowerShell-specific Claude Code papercuts, tell me — I'd rather fix them in the repo than rediscover them at 1am.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/codingjhj/my-claude-code-hook-silently-ate-every-korean-character-and-it-took-me-an-hour-to-figure-out-why-3ii4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
