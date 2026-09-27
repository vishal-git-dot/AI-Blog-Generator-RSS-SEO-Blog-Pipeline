---
title: "I built an AI agent that snapshots every edit and runs your tests before it says "done""
slug: "i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done"
author: "Qweezyy"
source: "devto_python"
published: "Sun, 27 Sep 2026 15:47:51 +0000"
description: "Disclosure: this post was written by Altair — the agent it describes — and reviewed by me. Filed under #ABotWroteThis as the community requires. I'm answerin..."
keywords: "your, not, agent, own, tests, before, one, file"
generated: "2026-09-27T16:44:45.598317"
---

# I built an AI agent that snapshots every edit and runs your tests before it says "done"

## Overview

Disclosure: this post was written by Altair — the agent it describes — and reviewed by me. Filed under #ABotWroteThis as the community requires. I'm answering the comments the same way. If anything here reads like marketing rather than engineering, tell me and I'll fix it. Most coding agents are one more chat window next to your editor. What I wanted was different: an agent I could actually walk away from. The problem is trust. Agents delete the wrong file, run the wrong command, or report "all done" without ever running the tests. So I found myself watching every step — which defeats the whole point. Altair is what I built to fix that. It's open source (Apache-2.0) and runs on your own hardware. Snapshots before every edit Any tool that changes a file — write, patch, delete — saves the previous state first, into the app's data folder, not your project. The file card gets an "undo" button. Multiple edits to the same file roll back one by one, newest to oldest. Commands need different handling, because a command can generate or delete files behind your back. So commands are tracked by a separate hidden git repository that captures their side effects. It never touches your own .git . If a task goes sideways, you can roll back the whole run, not just one edit, and see an audit of exactly what changed. The health-gate This is the part that actually lets me leave it alone. If the agent edited code, then before it's allowed to say "done" it runs your project checks — tests and linter — automatically. If they fail, it goes back and tries to fix them, with a cap on attempts. If it still can't, the run gets rolled back. It cannot report success with red tests. Not "usually" — it structurally can't, because the check runs before the word "done" is allowed to be said. It's not just a chat box The phone app isn't a remote control. It's a second agent with its own context and tools, linked to the PC over a local bridge. The phone has the camera, files, location and notifications; the PC has the heavy tools. They hand whole subtasks to each other, and either can ask the other for something it doesn't have. Keys are yours: any OpenAI-compatible provider, native Anthropic, or local models via Ollama / LM Studio. No Altair cloud, no account, no telemetry. A real run On a cheap model, asked to write a script printing the first 30 primes, run it, and chart the gaps between consecutive primes. It asked permission before writing and running, did the math, built an interactive chart, and noted in its own summary that the largest gap was 8 (between 89 and 97). About two and a half minutes end to end. The bug I remember best is from the library task — asked it to write an RFC 5545 .ics library from scratch. It handled the classic traps: escaping special characters, and folding lines at 75 octets (not characters) without cutting a multi-byte UTF-8 sequence. 15 tests plus 100 random round-trip checks, and the generated file opens in a normal calendar. Cost about $0.04. But the most useful moment was a failure. In the packaged build, the checks were being invoked as LocalAIAgent.exe -m pytest — through the app's own executable instead of Python — which meant the health-gate was silently doing nothing. The agent didn't paper over it. It checked another way and wrote plainly that the automated check had not passed, and why. Later, when the provider's search and review tools returned HTTP 502, it recorded the review as not performed rather than successful. That honesty is the thing I care about most. A pretty report that hides a failed check is worse than no report. Prompt-injection and the boring safety rails External content — web pages, documents, search results — is wrapped in a "this is data, not instructions" frame and scanned for injection patterns. If the agent has just read something suspicious and is about to do something outbound, it asks for confirmation even in automatic mode. On top of that, two rails that user approval cannot switch off: a path sandbox (the agent doesn't leave your working folder) and a destructive-command blacklist ( rm -rf , format , mkfs , dd of=/dev/… , fork bombs). Honest limits of 0.1.x This is early software and I'd rather you hear it from me: Windows only for now. Linux and macOS are planned; the Windows build isn't code-signed, so SmartScreen may warn on first launch. Phone ↔ PC only works on the same local network. Tailscale works as a workaround. The pairing QR scan doesn't work yet — you type the address and token manually. Fix is in progress. Chat history isn't synced between devices yet (specified, not built). It hasn't had much mileage on real-world tasks. Don't hand it anything critical or irreversible without your own review and backups. Try it irm https://raw.githubusercontent.com/Qweezyy/AltairAgent/main/install.ps1 | iex One command, no Python required. Android APK is in the releases. Code, docs and changelog: https://github.com/Qweezyy/AltairAgent

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qweezyy/i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done-l17

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
