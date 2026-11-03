---
title: "The Installer Checked Its Own Box"
slug: "the-installer-checked-its-own-box"
author: "Puneet Nanda"
source: "devto_ai"
published: "Tue, 03 Nov 2026 22:49:33 +0000"
description: "A plugin install is a new permission, and the app whose files change has to show the prompt. If the installer can tick the box, you never got a choice. Postm..."
keywords: "app, codex, postman, hook, installer, files, not, config"
generated: "2026-11-03T23:03:46.610314"
---

# The Installer Checked Its Own Box

## Overview

A plugin install is a new permission, and the app whose files change has to show the prompt. If the installer can tick the box, you never got a choice. Postman desktop did this on open. A signed-in user launched the app they already had, and its log recorded auto-existing-upgrade with Codex and Claude Code marked installed. Codex never put up a dialog. The HTTP client had already written the agent's files. The startup hook is a wide new boss, not a tiny helper. It tells the agent to load Postman's skill before non-trivial API work: design, implement, mock, test, monitor, document, deploy. You wanted to send a request. Your coding agent came back with a default coworker and a job description that covers most of software. The installer then tries to approve that hook itself. After install, the Codex integration lists the hook, hashes it, and upserts trusted_hash into Codex config. A comment in that code says it approves only Postman's current hook. Narrow self-approval is still self-approval. The report is careful about one fact: a trust line on disk does not prove which process wrote it. That gap is the lesson. A hash in a config file is not a person clicking Allow. Same pass, the plugin points Codex at https://mcp.postman.com/mcp . Codex logged an auth failure on the way out. The remote tool was in the config before a working login existed. The writeup does not claim collections were uploaded. It claims the integration and the instructions appeared on their own. That is the bug. Boring version, same shape. App A starts and writes App B's marketplace entry, enables the plugin, adds a startup instruction, stores a trust hash, and adds a remote endpoint. App B boots and treats the files as a decision. The decision was a script that can write ~/.codex and ~/.claude . Don't do this: Treat "they launched our app" as permission to edit a different product. Ship an installer that can write the approval for its own hook. Hang a startup instruction on all API work, instead of on an explicit ask. Turn on a remote tool before the host app has an opt-in. Call it an upgrade when the new behavior lives in someone else's config directory. If turning it off means hand-editing two agents, a CLI, and a cache, the feature shipped without an off switch. Takeaway: consent is a prompt in the tool whose files change. Source: https://github.com/postmanlabs/postman-app-support/issues/14370 HN: https://news.ycombinator.com/item?id=50354960 This post was generated automatically from public Hacker News data.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/puneet_nanda_dc25d8b489ad/the-installer-checked-its-own-box-44m2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
