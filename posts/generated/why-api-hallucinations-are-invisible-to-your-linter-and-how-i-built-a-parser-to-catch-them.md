---
title: "Why API Hallucinations Are Invisible to Your Linter (And How I Built a Parser to Catch Them."
slug: "why-api-hallucinations-are-invisible-to-your-linter-and-how-i-built-a-parser-to-catch-them"
author: "Carlos Luque Zayas Bazan"
source: "devto_python"
published: "Mon, 26 Oct 2026 21:31:01 +0000"
description: "When an AI coding assistant writes requests.get_json() instead of response.json(), the code compiles. Tests pass. Type checkers don't complain. SAST tools do..."
keywords: "api, code, because, real, you, hallucinations, how, catch"
generated: "2026-10-26T22:30:36.501184"
---

# Why API Hallucinations Are Invisible to Your Linter (And How I Built a Parser to Catch Them.

## Overview

When an AI coding assistant writes requests.get_json() instead of response.json(), the code compiles. Tests pass. Type checkers don't complain. SAST tools don't flag it. And yet the method doesn't exist. This is an API hallucination. It's a specific failure mode of AI-generated code that most static analysis tools miss because they're looking for known vulnerabilities or suspicious patterns, not for calls to functions that were never real to begin with. I've been building a CLI in Go that parses Python code and checks whether the functions and methods it calls actually exist in the library. The core idea is simple: if you know the valid API surface of requests, json, and os, you can flag requests.get_json() because get_json isn't in that surface. The parsing is done with gotreesitter, a pure-Go implementation of tree-sitter. I chose it over the CGO binding because I needed to compile on Windows without MinGW. The tradeoff is performance (the pure-Go version is slower), but for a CLI that analyzes individual files, the difference is milliseconds. The hard part isn't the parser. It's the registry of valid APIs. For the first version, I hardcoded the valid methods for three libraries. That's enough to demonstrate the concept, but it doesn't scale. Expanding it to pandas, numpy, or django requires either manual curation or extracting method names from type stubs. What I've learned so far: API hallucinations are predictable. They follow patterns — plausible-sounding method names, slight variations on real APIs, invented functions that "should" exist. A deterministic checker can catch them if it knows what's real. The question is how to build that "what's real" database without drowning in maintenance. The code isn't public yet, but I'm sharing the approach because I think the problem is worth solving. If you've seen API hallucinations in your own AI-generated code, I'd like to hear how you catch them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/carlos_luquezayasbazan_/why-api-hallucinations-are-invisible-to-your-linter-and-how-i-built-a-parser-to-catch-them-1185

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
