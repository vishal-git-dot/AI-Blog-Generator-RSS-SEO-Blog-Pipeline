---
title: "A CVSS 10.0 in Your AI Coding Agent Is Just TOCTOU Wearing a Hoodie"
slug: "a-cvss-100-in-your-ai-coding-agent-is-just-toctou-wearing-a-hoodie"
author: "Cor E"
source: "devto_ai"
published: "Mon, 10 Aug 2026 13:11:08 +0000"
description: "A GitHub issue can now potentially exfiltrate your CI secrets, and the tool that let it happen is the same one your team is using to "move faster." That's th..."
keywords: "your, agent, same, you, github, one, bug, file"
generated: "2026-08-10T13:20:58.525973"
---

# A CVSS 10.0 in Your AI Coding Agent Is Just TOCTOU Wearing a Hoodie

## Overview

A GitHub issue can now potentially exfiltrate your CI secrets, and the tool that let it happen is the same one your team is using to "move faster." That's the story, and it deserves more than zero comments. Context This isn't new math, it's an old bug class wearing a new jacket. Time-of-check-to-time-of-use flaws have been around since multi-user Unix systems first had race conditions in file permissions. What's new is the attack surface: coding agents that read GitHub issues, .env files, or an AGENTS.md config as "context," decide that context is safe in one pass, then act on it with full privileges in a later pass. Swap "file descriptor" for "LLM prompt" and you've basically got the same bug your professor warned you about, except now it's got a CVE and a marketing problem. Three vendors, three implementations, the same architectural flaw. That's the part worth sitting with. When Claude Code, Gemini CLI, and OpenAI Codex all have a harness-level validation gap, that's not a coincidence, that's convergent evolution. Everyone building these agent harnesses is solving the same problem (let the model act autonomously on external input) with the same shortcut (validate once, trust forever). Hype Check Here's what's getting overstated: the "no in-the-wild exploitation confirmed" line is going to get read by some people as "so it's fine." It's not fine, it just means nobody's publicly bragged about it yet, or nobody's noticed. A CVSS 10.0 in a tool that runs on CI infrastructure with secrets attached is about as close to a worst-case scenario as this bug class gets. The absence of a confirmed breach isn't evidence of safety, it's evidence that researchers got there first this time. What's being understated: the trust boundary problem here isn't a bug you patch once. A GitHub issue title, a .env file, a config file the agent reads for "instructions" — these are all untrusted input by definition, and yet the entire pitch of these tools is "let the agent read your repo and just handle things." Every one of those ingestion points is a potential injection vector. Patching this specific CVE doesn't close the category, it closes one door in a house that was built with a lot of doors. Who benefits from the current narrative? Honestly, the vendors get a pretty clean story here: found, patched, moving on, no incidents. That's the standard "responsible disclosure worked" arc, and to be fair, it did work this time. But it also quietly reframes a fundamental architecture problem (validate-then-trust across a privilege boundary) as a one-off bug that's been "fixed," when the actual lesson is that the harness design pattern itself needs scrutiny across every agent product doing this. Implications If you've wired any of these tools into CI, this is your reminder that "AI coding assistant" and "process with access to your secrets" are the same sentence now. Treat the agent's action surface the same way you'd treat a third-party GitHub Action: least privilege, scoped tokens, no blanket repo or write-all scopes because it's convenient. If your agent doesn't need to see the .env file to do its job, it shouldn't have a path to read it. For security teams, the useful move isn't just patching, it's asking your own AI tooling vendors a pointed question: where exactly does your validation happen relative to where the model gets to act? "We validate the input" is not an answer. "Validation happens in the same trust boundary as execution, with no re-check between context ingestion and tool invocation" is an answer, and if a vendor can't give you that level of detail, that's useful information too. For the broader industry: this is going to keep happening until agent harnesses get boring, standardized, and boxed in the same way sandboxing and permission models got boring for browsers and mobile OSes. We're early. The zero HN engagement on this story is honestly more telling than the CVE itself, this stuff is still flying under the radar for a lot of people who are deploying these tools into production pipelines right now without a second thought. Open Question When your CI pipeline's job is to run untrusted code fast, and your AI agent's job is to read untrusted input and act autonomously, at what point does "agentic" stop being a feature and start being the vulnerability class itself? — Cor, Skyblue Soft Sources Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/coridev/a-cvss-100-in-your-ai-coding-agent-is-just-toctou-wearing-a-hoodie-31jj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
