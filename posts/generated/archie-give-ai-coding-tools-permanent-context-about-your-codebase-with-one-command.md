---
title: "Archie – Give AI coding tools permanent context about your codebase with one command"
slug: "archie-give-ai-coding-tools-permanent-context-about-your-codebase-with-one-command"
author: "Abhishek"
source: "devto_webdev"
published: "Tue, 30 Jun 2026 19:51:20 +0000"
description: "Hi everyone, this is my first post on dev.to and I wanted to share a project I've been building. Here's the problem I kept running into with Cursor and Claud..."
keywords: "archie, context, every, files, you, codebase, project, decisions"
generated: "2026-06-30T20:05:30.546719"
---

# Archie – Give AI coding tools permanent context about your codebase with one command

## Overview

Hi everyone, this is my first post on dev.to and I wanted to share a project I've been building. Here's the problem I kept running into with Cursor and Claude Code: the AI has no idea why decisions were made in a codebase. It suggests refactors that break existing architecture. It recommends libraries I'd already evaluated and rejected. It doesn't know my constraints. I ended up re-explaining the same context in every new chat session, and when a new developer joins the project, their AI starts from zero again too. I built Archie to fix this. One command: npx archie init It reads your codebase and git history, uses Gemini to generate a structured ARCHITECTURE.md , and keeps that doc updated automatically via a git post-commit hook. No manual upkeep required. The doc captures: what the project actually does why each technology was chosen how core flows work, traced through real files key decisions and the alternatives you rejected (and why) known limitations End result is that every developer and every AI tool that opens the project gets the same context the original developer had. The AI stops re-suggesting things you already ruled out. Technical decisions worth discussing Context window I went with Gemini specifically for the huge context window Incremental updates Archie builds a dependency graph from static import analysis. When files change, it finds their direct imports and importers (basically their neighbors), and only sends those to Gemini — not the whole codebase. Keeps updates fast and cheap per commit. State management .git/archie/state.json tracks lastProcessedCommit . The hook grabs ALL commits between the last processed one and HEAD, not just the latest — so it catches changes even if you've made a bunch of commits offline. Surgical update prompting There's a Generate mode (first run) and an Update mode (every run after). The update prompt explicitly tells Gemini to only touch the sections affected by the changed files, so anything you've manually written stays untouched. Significance detection This is what stops Archie from burning API calls on every tiny commit. It only fires on things like package.json changes, schema/migration files, new directories, or commits touching 5+ files. Smaller commits still move the state pointer forward, just without triggering a regeneration. Known limitations (being upfront here) Import analysis is regex-based, so it misses dynamic imports and re-exports No monorepo support yet Prompt quality varies on non-TypeScript codebases It's still early — about 250 npm downloads since launch a few days ago — so I'm still figuring out what's actually useful to people. GitHub: https://github.com/abhishek-sonje/archie Landing page: https://archie.abhishekdev.tech Try it: npm i archie-ai I'd genuinely like to hear what you think, whether it's the core premise, the architecture doc format, or any of the technical decisions above. Happy to discuss any of it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abhishek_208a88756e55d3c3/archie-give-ai-coding-tools-permanent-context-about-your-codebase-with-one-command-42l7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
