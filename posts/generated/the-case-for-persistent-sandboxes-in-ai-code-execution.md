---
title: "The case for persistent sandboxes in AI code execution"
slug: "the-case-for-persistent-sandboxes-in-ai-code-execution"
author: "Arun Raghunath"
source: "devto_python"
published: "Fri, 05 Jun 2026 09:56:53 +0000"
description: "Every AI coding tool generates code. None of them solve what happens next. Cursor writes your Python. Claude Code refactors your script. Windsurf ships your ..."
keywords: "code, file, sandboxes, post, workspace, every, run, exec"
generated: "2026-06-05T10:10:12.596245"
---

# The case for persistent sandboxes in AI code execution

## Overview

Every AI coding tool generates code. None of them solve what happens next. Cursor writes your Python. Claude Code refactors your script. Windsurf ships your feature. But running that code safely, in isolation, with audit trails, without exposing your secrets, is still an unsolved problem. That's what Jhansi.io is built for. The mistake we made in v0.1 Our first execution model was simple. Send code as a string, run it in an isolated container, return the output. POST /v1/sandboxes/{id}/exec body: { "code": "print('hello world')" } It worked. But it had three fundamental problems. Problem Why it breaks Single file only No multi-file projects, no shared modules, no dependencies. Not how production code works. Full payload on every run Even if nothing changed, you resent everything. Wasted bandwidth, added latency. No foundation for delta sync If you're sending everything every time, there's nothing to diff against. The insight A sandbox should be a workspace, not a disposable container. Give every sandbox a dedicated folder on disk. Files live there between runs. Execution just says "run this file" — no payload, no resend, no waste. This is the architecture shift in Jhansi.io v0.2. What changed Workspace per sandbox. Every sandbox gets a dedicated folder on disk at creation time. Zero config locally, overridable in production via PETRI_WORKSPACE_ROOT . File upload API. Upload once. Upload only when something changes. POST /v1/sandboxes/{id}/files Files land in the sandbox workspace and persist between runs. Exec by filename. No code in the request body. Just a filename. POST /v1/sandboxes/{id}/exec body: { "filename": "main.py" } Jhansi.io mounts the workspace into a fresh isolated container and runs the named file. The container dies. The workspace survives. The flow # Create once curl -X POST /v1/sandboxes -d '{"language": "python"}' # Upload when files change curl -X POST /v1/sandboxes/ { id } /files -F "file=@main.py" # Exec as many times as you need curl -X POST /v1/sandboxes/ { id } /exec -d '{"filename": "main.py"}' What this unlocks The persistent workspace is the foundation for everything coming next: Delta sync — detect file changes, upload only diffs Auto dependency detection — parse imports, install packages invisibly Multi-file projects — real codebases, not toy scripts If you're building AI agents that generate and run code, we want you in our design partner program. Early access at jhansiio.featurebase.app Jhansi.io — Build it. Run it. Ship it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/thearun85/the-case-for-persistent-sandboxes-in-ai-code-execution-3158

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
