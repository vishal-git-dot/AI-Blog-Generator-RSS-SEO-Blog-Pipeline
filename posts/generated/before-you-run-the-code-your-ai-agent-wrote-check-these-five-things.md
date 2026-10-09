---
title: "Before you run the code your AI agent wrote, check these five things"
slug: "before-you-run-the-code-your-ai-agent-wrote-check-these-five-things"
author: "Isaac Bell"
source: "devto_ai"
published: "Fri, 09 Oct 2026 12:43:00 +0000"
description: "Coding agents are good enough that it's tempting to accept the diff, run npm install , and start the dev server. Most of the time that's fine. The problem is..."
keywords: "code, agent, you, run, your, semgrep, check, server"
generated: "2026-10-09T12:55:31.305390"
---

# Before you run the code your AI agent wrote, check these five things

## Overview

Coding agents are good enough that it's tempting to accept the diff, run npm install , and start the dev server. Most of the time that's fine. The problem is the time it isn't, because an agent has your permissions and reads text you never saw. These are the five places I look before running anything an agent produced. 1. Dependencies you didn't ask for Assistants sometimes suggest package names that don't exist, or that are one letter off a real one. Attackers register those names. For every new entry in package.json or requirements.txt , check that it's the package you meant and that it has a real history. Advisory scanners ( npm audit , OSV-Scanner) are still worth running, but they only know about reported problems. A brand-new malicious package has no advisory yet. 2. Setup commands copied from somewhere curl ... | sh , a new postinstall script, an editor task. An agent that browses can repeat whatever an untrusted page told it to run. Read every script entry the agent added or changed. 3. Config that runs programs Agent hooks, MCP server definitions, .claude/settings.json , .mcp.json , .vscode/tasks.json , *.config.js . All of these start processes, and none of them look like "code" in a diff review. 4. Insecure model-calling code Hardcoded API keys. Model output passed to exec or eval . User input concatenated into a system prompt. No max_tokens . Agents write this code readily because it's all over their training data. 5. Server code that fetches URLs If the agent wrote a link preview, a webhook, or an "import from URL" feature, check whether it validates where the URL points. Otherwise someone can aim your server at 169.254.169.254 and read your cloud credentials. That's SSRF. Automating the first pass I maintain two open-source tools for this. Both run with npx and need no account. am-i-hacked reads the project for signs of malicious code: auto-run editor tasks, install scripts that download or decode things, obfuscated payloads, executables disguised as assets, capture code paired with an exfiltration endpoint, and the project's own AI-tool config. npx am-i-hacked Put it in front of your dev server so it runs every time: { "scripts" : { "dev" : "am-i-hacked && next dev" } secure-semgrep runs Semgrep with bundled rules for AI-agent code: hardcoded provider keys, model output to exec, user input in system prompts, MCP command injection and tool poisoning, risky agent hooks, prompt injection in SKILL.md files. It also adds Semgrep's own security packs for your stack. It needs semgrep installed. npx secure-semgrep -L ts -L node . npx secure-semgrep -L ssrf . # opt-in SSRF rules Both exit 1 on findings, so they drop into CI. What they don't do Neither tool knows what you asked the agent to do. A scan finds known patterns; it doesn't prove the code is correct or safe. Neither scans installed node_modules . Neither is antivirus. They're a first pass that tells you where to look, and reading the diff is still the check that matters. The full guide, including a table of what the AI rules cover, is here: Is AI-generated code safe to run? How to check it first . Everything is MIT licensed: github.com/IsaacBell/secure-devtools .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ikeisahacker/before-you-run-the-code-your-ai-agent-wrote-check-these-five-things-4g8g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
