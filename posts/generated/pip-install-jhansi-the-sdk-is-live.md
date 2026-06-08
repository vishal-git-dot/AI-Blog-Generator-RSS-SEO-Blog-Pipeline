---
title: "pip install jhansi — the SDK is live"
slug: "pip-install-jhansi-the-sdk-is-live"
author: "Arun Raghunath"
source: "devto_python"
published: "Mon, 08 Jun 2026 19:49:30 +0000"
description: "Six weeks ago, running code on jhansi.io meant curl + sandbox IDs + manual cleanup. Today it looks like this: from jhansi import Sandbox with Sandbox ( langu..."
keywords: "docker, petri, jhansi, sandbox, code, you, python, containers"
generated: "2026-06-08T20:25:42.487195"
---

# pip install jhansi — the SDK is live

## Overview

Six weeks ago, running code on jhansi.io meant curl + sandbox IDs + manual cleanup. Today it looks like this: from jhansi import Sandbox with Sandbox ( language = " python " ) as sb : sb . upload_file ( " main.py " ) result = sb . exec ( " python main.py " ) print ( result [ " output " ]) That's the milestone. The SDK is live. Why this matters The API was always there. Petri — the execution engine underneath — has been running code in isolated Docker containers since v0.1. But you had to understand HTTP, manage container lifecycle, and remember to delete sandboxes or you'd leak resources. The SDK removes all of that. You write Python. jhansi.io handles the rest. The context manager was non-negotiable If you create a sandbox and forget to delete it, you leak containers and workspace storage. That's not acceptable — especially when AI agents are creating sandboxes programmatically. The context manager makes cleanup automatic: with Sandbox ( language = " python " ) as sb : # sandbox created here sb . upload_file ( " main.py " ) result = sb . exec ( " python main.py " ) # sandbox deleted here — even if exec raised an exception No leaked containers. No cleanup code. No surprises. The Docker-in-Docker problem Self-hosting Petri via docker compose up uncovered something we hadn't anticipated. Petri runs inside a Docker container. But Petri's job is to spin up Docker containers to run your code. So Petri needs access to Docker — from inside Docker. Fix one: mount the Docker socket. volumes : - /var/run/docker.sock:/var/run/docker.sock Fix two: shared workspace path. Petri creates workspace folders inside its container. When it mounts those into sandbox containers, Docker looks for the path on the host — not inside Petri. The path doesn't exist. volumes : - /var/run/docker.sock:/var/run/docker.sock - /tmp/petri-workspaces:/tmp/petri-workspaces environment : - PETRI_WORKSPACE_ROOT=/tmp/petri-workspaces Same path both sides. Docker finds it. Problem solved. Getting started # Start Petri git clone https://github.com/jhansi-io/petri.git cd petri docker compose up # Install the SDK pip install jhansi Full docs at docs.jhansi.io . What's next v0.6 — persistent registry so sandboxes survive Petri restarts v0.7 — streaming exec, real-time output as your code runs MCP server — Cursor and Claude Code use Petri directly instead of their own cloud. The MCP server is the one I'm most excited about. More on that soon. Star the repo if you're following the build. ⭐ github.com/jhansi-io/jhansi

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/thearun85/pip-install-jhansi-the-sdk-is-live-1l03

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
