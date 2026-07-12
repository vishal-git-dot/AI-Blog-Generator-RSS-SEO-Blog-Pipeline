---
title: "Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k"
slug: "claude-code-sends-33k-tokens-before-reading-the-prompt-opencode-sends-7k"
author: "systima"
source: "hackernews"
published: "Sun, 12 Jul 2026 18:25:51 +0000"
description: "This started based off of a hunch. We usually use OpenCode, but were 'forced' to use Claude Code for a while due to issues with Meridian. In that time, we sa..."
keywords: "opencode, claude, code, usage, sends, use, but, much"
generated: "2026-07-12T19:12:47.054997"
---

# Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k

## Overview

This started based off of a hunch. We usually use OpenCode, but were 'forced' to use Claude Code for a while due to issues with Meridian. In that time, we saw the usage meter rise much, much more quickly than when using OpenCode. This was the initial anecdotal evidence, but we undertook this small study to collect empirical data: We added logging between the agentic coding tool (Claude Code and OpenCode) and Anthropic's endpoint, and captured all requests (and the returned usage blocks). With one caveat (toward the end of the post) we found unambiguously that Claude Code was far more inefficient in terms of its cache strategy and its harness token usage than OpenCode. Comments URL: https://news.ycombinator.com/item?id=48883275 Points: 36 # Comments: 11

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://systima.ai/blog/claude-code-vs-opencode-token-overhead

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
