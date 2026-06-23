---
title: "Meet Chatrove: a 100% local, open-source vault for your AI chats"
slug: "meet-chatrove-a-100-local-open-source-vault-for-your-ai-chats"
author: "vuhuutam459-max"
source: "devto_webdev"
published: "Tue, 23 Jun 2026 09:51:18 +0000"
description: "Meet Chatrove: a 100% local, open-source vault for your AI chats If you followed my earlier posts about Gemini Vault — this is the same project, grown up and..."
keywords: "your, you, chatrove, local, gemini, search, source, vault"
generated: "2026-06-23T09:53:37.258160"
---

# Meet Chatrove: a 100% local, open-source vault for your AI chats

## Overview

Meet Chatrove: a 100% local, open-source vault for your AI chats If you followed my earlier posts about Gemini Vault — this is the same project, grown up and renamed. Here's the full story and what it does today. We don't actually own our AI memories Every day we pour our best ideas, code and drafts into Gemini, ChatGPT and Claude. But we don't truly own any of it. Accounts get suspended (I lost access to an AI account myself — that's what kicked all of this off). Services go down. APIs change. And the official "Export your data" buttons? They hand you an unreadable JSON dump you can't search or even read. I got tired of renting my own digital memory from the cloud. I wanted my chats stored safely on my disk, available completely offline, with instant search. So I built a tool to take them back. Why the rename: Gemini Vault → Chatrove I originally called it Gemini Vault, but the project outgrew the name. It no longer backs up only Gemini — it merges Gemini, ChatGPT and Claude into one archive — and tying a product to a single provider's trademark was a bad idea long-term. So it's now Chatrove: a chat + trove, a treasure chest for your conversations. Vendor-neutral, and it's still the same MIT-licensed project. (The old repo link redirects to the new one.) What Chatrove is A fully local backup tool and offline viewer for your AI conversations. You import the official export once, and you get a fast, private, searchable archive that lives entirely on your machine. Repo: https://github.com/vuhuutam459-max/chatrove How it works under the hood I wanted this to be as lightweight and independent as possible: Zero-dependency core. The processor runs on the pure Python 3.10+ standard library. No heavy frameworks to install. Millisecond search. I used SQLite with FTS5 (full-text search), so you can search across thousands of chats instantly, including non-Latin scripts. Source-agnostic core. An adapter layer normalizes the official JSON exports from Gemini, ChatGPT and Claude into one unified database — adding a new source doesn't touch the core logic. Offline viewer. A single-page dashboard that works completely offline. It renders LaTeX (KaTeX) for math, syntax highlighting for code, Canvas, and handles broken/missing images gracefully. Safe re-imports. SHA256 dedup means re-importing a newer export only adds what changed — no duplicates. Bilingual UI (English / Russian). The "Smart Librarian" — optional local AI This is the part I'm most excited about, and it's completely optional. If you have Ollama running locally (e.g. gemma3:4b), Chatrove can: automatically scan your old chats, generate summaries, and assign topical tags; power "Ask the archive" — ask a question in plain language, and it does retrieval over your local database and returns an answer with clickable citations straight to the exact chat it came from. The crucial part: every byte stays on your machine. The LLM endpoint is just an OpenAI-compatible base_url, so you can point it at whatever local model you like. And if you don't run Ollama at all, the archive, search and viewer work exactly the same. Privacy is the whole point No server. No accounts. No API keys. No telemetry. Your database, logs and personal exports are git-ignored by design and never leave your device. Chatrove is built for your own trusted data, by you, on your hardware. How to run it There's no build step. On Windows, you double-click a launcher and the viewer opens in your browser. On macOS/Linux, you run it with Python. Pick what you need: just the offline viewer, or add the local-AI tools. It's open-source — and I'd love your feedback Chatrove is MIT-licensed. If you value your data and want to keep your AI brainstorming safe, give it a try, and I warmly welcome any stars, forks, issues or PRs. ⭐ Repo: https://github.com/vuhuutam459-max/chatrove One genuine question I keep asking people: how do you currently keep the "good" prompts and important snippets your AI generates? Do you just leave them in the browser history, or copy them into Notion / Obsidian? I'd love to hear your workflow in the comments. Let's own our data. 🚀 — Max

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vuhuutam459max/meet-chatrove-a-100-local-open-source-vault-for-your-ai-chats-1no4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
