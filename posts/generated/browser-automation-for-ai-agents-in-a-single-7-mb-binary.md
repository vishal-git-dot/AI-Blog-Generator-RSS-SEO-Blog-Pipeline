---
title: "Browser automation for AI agents, in a single 7 MB binary"
slug: "browser-automation-for-ai-agents-in-a-single-7-mb-binary"
author: "Shubham"
source: "devto_ai"
published: "Mon, 27 Jul 2026 03:29:06 +0000"
description: "Kitewright gives LLM agents a real browser — navigate, screenshot, extract, PDF — without the Node.js and Playwright weight. Written in Rust, installs in one..."
keywords: "kitewright, browser, mcp, agents, node, one, binary, tools"
generated: "2026-07-27T03:38:46.279703"
---

# Browser automation for AI agents, in a single 7 MB binary

## Overview

Kitewright gives LLM agents a real browser — navigate, screenshot, extract, PDF — without the Node.js and Playwright weight. Written in Rust, installs in one line. AI agents are getting good at using tools, and "drive a real browser" is one of the most useful tools you can give them: log into a dashboard, pull a number, fill a form, turn a page into a PDF.The problem is what it costs to set up. Almost every option drags in the full Node.js + Playwright stack — a runtime to install and 100+ MB of memory sitting idle before the agent does anything. Kitewright is a lighter answer. It's an MCP server — the standard way agents call tools — that gives an LLM a real Chromium browser through a single ~7 MB static binary written in Rust. No Node runtime, no heavyweight install. One line and it's running: npx @kitewright/mcp ## Small and fast, measured I care about honest numbers, so here they are, head to head against the Node/Playwright equivalent on the same machine and the same Chromium: Cold start to listening: 75 ms vs ~350 ms Idle memory: ~8 MB vs 100–125 MB Distribution: one 6.9 MB binary vs an 18 MB package plus a Node runtime The browser is reaped when idle and pre-warmed again on the next session, so idle cost stays near zero And the honest caveat, because trust matters: once a page is actually loading, navigation latency is a tie — everyone is speaking the same protocol to the same browser, and the network is the network. The wins are startup, memory, and shipping as one binary. That's exactly what matters when you're running a browser next to a local model, in a container, or across a fleet. ## Built for agents, not just scripts An LLM driving a browser fails differently than a human does, so the reliability model is different too. Clicks and typing don't fire blindly — Kitewright waits for the target element to be present, visible, enabled, un-covered, and settled, then either acts or returns a specific reason it couldn't: not found, not visible, disabled, covered, or unstable. No silent misclicks, and the agent gets an error it can actually reason about. There are 23 tools in total: navigate, screenshot, extract and extract-to-markdown, accessibility snapshots, form filling, clicks and typing, key presses, network and console inspection, HTML→PDF, and save/restore of session state so a login survives across runs. It speaks both stdio and Streamable HTTP, and it's in the official MCP registry. Try it Kitewright is MIT-licensed and open source. npx @kitewright/mcp or add it to an MCP client directly: claude mcp add kitewright -- npx -y @kitewright/mcp Repo, benchmarks, and a demo GIF: https://github.com/kitewright/kitewright If you're building anything where an agent needs to touch the web, I'd love your feedback — especially on the tool surface.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shubham_f98d63c2451d6e035/browser-automation-for-ai-agents-in-a-single-7-mb-binary-1pmm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
