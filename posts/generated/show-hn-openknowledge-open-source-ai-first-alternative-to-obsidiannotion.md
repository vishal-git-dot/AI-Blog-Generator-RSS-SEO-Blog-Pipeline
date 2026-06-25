---
title: "Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion"
slug: "show-hn-openknowledge-open-source-ai-first-alternative-to-obsidiannotion"
author: "engomez"
source: "hackernews"
published: "Thu, 25 Jun 2026 16:04:46 +0000"
description: "Hi HN, Nick here. We’re launching OpenKnowledge ( https://openknowledge.ai/ ), a “what you see is what you get” markdown editor that has direct integrations ..."
keywords: "openknowledge, what, you, markdown, open, have, prosemirror, https"
generated: "2026-06-25T20:09:21.017673"
---

# Show HN: OpenKnowledge – open source AI-first alternative to Obsidian/Notion

## Overview

Hi HN, Nick here. We’re launching OpenKnowledge ( https://openknowledge.ai/ ), a “what you see is what you get” markdown editor that has direct integrations with Claude, Codex, and Cursor. Available as MacOS app or CLI. Fully free/local and OSS ( https://github.com/inkeep/open-knowledge ). We built this because we wanted a “Google docs” like experience for writing and sharing markdown files across our team. Obsidian is the best alternative we tried, but found it doesn’t have a true “what you see is what you get” UI and it didn’t integrate well with Claude/Codex outside of community plugins. So we built OpenKnowledge. It takes shape as: 1. A MacOS app with a file navigator, the WYSIWYG editor, and link explorer. 2. Integrations with the Claude, Codex, and Cursor desktop apps. The agents can open an OpenKnowledge editor within their embedded web browsers for a side-by-side experience. 3. Built-in mcps, skills, and RAG for LLM-wiki and “AI Second Brain” scenarios + spec writing 4. An embedded terminal and CLI for TUI-first users OSS stack includes: Tiptap/prosemirror, CodeMirror, yjs (CRDT), Electron (MacOS app), Orama, remark/rehype/micromark/mdast, @pierre/trees On the architecture side, the interesting eng. challenges included: 1. A pipeline to convert ProseMirror to markdown in a bidirectional lossless way. ProseMirror uses ASTs, which are not designed to have byte-fidelity. 2. A dual-observer CRDT to keep the ProseMirror and markdown state in-sync. The CRDT + git also power a collaborative experience that shows what Agents are doing in the markdown, have undo/redo, and version history. The “Share” and cloud-sync functionality are geared for team collaboration. They feel “no-code” but leverage git/GitHub under the hood, which also means data stays fully private. In that spirit, we made OpenKnowledge open source for anybody who’s curious or who’d like to contribute. We’re actively thinking about plugins/extensibility and what’s next. If you have suggestions or feedback, would love to hear it. Comments URL: https://news.ycombinator.com/item?id=48675435 Points: 41 # Comments: 12

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/inkeep/open-knowledge

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
