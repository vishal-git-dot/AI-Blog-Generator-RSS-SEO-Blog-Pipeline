---
title: "The npm package your AI just suggested doesn't exist. Someone already registered it. published: false"
slug: "the-npm-package-your-ai-just-suggested-doesnt-exist-someone-already-registered-it-published-false"
author: "Maria"
source: "devto_ai"
published: "Wed, 08 Jul 2026 08:31:02 +0000"
description: "Nearly 1 in 5 packages, an AI coding assistant suggests, are pure invention. Attackers know this, and they're registering those hallucinated names with malwa..."
keywords: "signature, package, your, packages, malware, malicious, npm, already"
generated: "2026-07-08T08:37:13.653138"
---

# The npm package your AI just suggested doesn't exist. Someone already registered it. published: false

## Overview

Nearly 1 in 5 packages, an AI coding assistant suggests, are pure invention. Attackers know this, and they're registering those hallucinated names with malware, waiting for the next pip install or npm install . We're running a live webinar on July 22nd @ 10:30 CEST to show how this works and how to catch it before a signature even exists. Details at the bottom 👇 The problem: slopsquatting Ask an AI assistant for code, and there's a ~19.7% chance it recommends a package that doesn't exist (source: USENIX Security 2025). That alone isn't the scary part; LLMs hallucinate; that's known. What's scary is that the same fake name keeps coming back across prompts and models. Attackers noticed this pattern, and now they register those exact names on npm, PyPI, and other registries, ship malware inside, and wait. This now has a name: slopsquatting. It's not theoretical: A single hallucinated package, planted as a benign test, pulled in 30,000+ downloads in three months Confirmed malicious packages exploiting this pattern are already live in public registries With tools like GitHub Copilot generating ~46% of a developer's code on average, this attack surface grows every single day Why signature-based scanning isn't enough Over 450,000 new malicious packages were published in 2025 alone (~75% YoY growth). Traditional scanners wait for a known signature before flagging something as malicious. Against a threat this fast-moving, "wait for the signature" is already too late. What we're showing live We're doing a working session (not a slide deck) with two parts: See everything — using AI Inventory + AI BOM to surface every AI component in a real codebase: models, agents, MCP connections, AI-introduced dependencies. You can't defend what you can't see. Block the malware — showing Xygeni Shield (powered by MEW — Malware Early Warning) detecting and blocking malicious packages before a signature exists for them. Bring your toughest question — this is a demo, not a pitch. Details 📅 July 22nd ⏰ 10:30 CEST Save your seat here Curious if others have run into hallucinated-package suggestions from Copilot/ChatGPT/etc. in the wild — drop your experience in the comments 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mariaxyg/the-npm-package-your-ai-just-suggested-doesnt-exist-someone-already-registered-it-published-472d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
