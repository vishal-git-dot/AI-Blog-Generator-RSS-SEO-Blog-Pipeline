---
title: "ChatGPT writes you a clean doc. Your Mac shows raw text with ## everywhere. Here's the fix"
slug: "chatgpt-writes-you-a-clean-doc-your-mac-shows-raw-text-with-everywhere-heres-the-fix"
author: "Arthur"
source: "devto_ai"
published: "Fri, 05 Jun 2026 10:11:09 +0000"
description: "Short version: if ChatGPT, Claude, or Cursor handed you a file that opens as a wall of # , * , and backticks on your Mac, that file is Markdown and nothing o..."
keywords: "you, file, free, your, yes, markdown, want, text"
generated: "2026-06-05T10:13:51.910463"
---

# ChatGPT writes you a clean doc. Your Mac shows raw text with ## everywhere. Here's the fix

## Overview

Short version: if ChatGPT, Claude, or Cursor handed you a file that opens as a wall of # , * , and backticks on your Mac, that file is Markdown and nothing on your Mac is rendering it. Install a small app that adds a Finder preview for it, then hit Space on the file and it shows up formatted. Free options exist and they are covered below. If reading AI output is part of your daily work and you want the formatted view to refresh on its own each time an agent rewrites the file, that is the specific frustration I built MacMD Viewer to solve. Why does my Mac show the file as raw text instead of a clean document? Because the file is Markdown, and macOS has no built-in renderer for it. Markdown is a plain-text format where # Heading , **bold** , and - item are shorthand instructions for formatting. The model emits those symbols, your editor or chat window interprets them and shows you the pretty result, but the symbols themselves are all that gets saved to the .md file. There is no formatting baked in, only instructions waiting to be read. The reason it looks fine in the chat and broken on disk comes down to who is doing the rendering. Inside ChatGPT or Claude, the web interface reads the Markdown and paints it for you in real time. The moment you download the file, you leave that renderer behind. Now it is just text. Double-click the .md and TextEdit shows the raw symbols, because it treats the file as plain text with nothing to interpret. Press Space in Finder and Quick Look shows the same raw text, because Apple ships Quick Look generators for PDFs, images, and .txt , but not for .md . This was a niche annoyance for years, mostly hitting developers. Now that millions of people receive plans, specs, meeting notes, and drafts back from AI as .md files, it has become a daily papercut, and most people do not even know the file format has a name they can search for. How do I fix it on macOS? Pick the lightest tool that matches how often you actually hit this. There is no single right answer: a one-off problem and a daily workflow deserve different solutions, and overspending on a paper cut is its own mistake. If it happens rarely. Do not install anything. Send the file's contents back into the chat that produced it and ask for it formatted, then read it right there in the browser. Or open one of the many free browser-based Markdown viewers and paste it in. VS Code also has a built-in preview if you already have it: open the file, then press Shift+Cmd+V. All free, slightly fiddly, perfectly fine for something you do twice a month. If you want it to just work in Finder. Install a small Mac app that registers a Quick Look extension for .md . Once it is installed, pressing Space on any Markdown file shows it formatted in place: headings, bold, lists, links, code blocks, tables, and Mermaid diagrams too. You never open a separate app, you just preview like you would a photo. Readdown is a free app that does exactly this and does it well, and it even refreshes on its own when the file changes. QuickMD is another free option that renders Markdown and Mermaid, though it does not add a Finder Quick Look preview or refresh when the file is overwritten. If your needs stop at "I want Space to show me a clean doc," start with Readdown before paying for anything. If you live in AI output all day. When you run Claude Code, Cursor, or any agent that writes files on your behalf, the same .md gets overwritten again and again as the model works. You want a window that stays open and repaints itself the instant the file changes. Readdown, the free option above, actually does this well, and if you just want the lightest free reader it is a genuinely great pick. I built MacMD Viewer for people who want a fuller, actively maintained and supported tool around that same live-reload idea. It is on Setapp and Homebrew (Readdown is a direct-download, no-account hobby project), it adds a Library window and 7 themes, and its live-reload is debounced at around 50ms so it keeps up cleanly with an agent overwriting the file in rapid bursts. Like the free tools it handles Mermaid and syntax-highlighted code, installs the Finder Quick Look extension, and is read-only by design (it never touches your files). It costs a one-time 19.99 dollars, no subscription. If you only need the occasional clean render, the free options above genuinely cover it. Quick comparison Tool Price Quick Look in Finder Live reload Mermaid Paste back into the chat free no no no Readdown free yes yes yes QuickMD free no no yes MacMD Viewer 19.99 once yes yes yes Typora (this is an editor) 14.99 no n/a yes Marked 2 (this is an editor companion) 13.99 no yes no What if I want to edit the file, not just read it? Then you want an editor, which is a different category of tool. Everything above is tuned for reading AI output cleanly. If you plan to write Markdown yourself, Typora formats your text live as you type, and Obsidian is the better pick if you are assembling a connected notes system. But you do not need either one just to look at what the model handed you, and paying for an editor to solve a viewing problem is the long way around. Full disclosure: MacMD Viewer is my own product, so weigh my praise for it accordingly. I have made a point of calling out exactly where the free tools are the smarter choice, since for plenty of readers that is the honest answer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/crackx17/chatgpt-writes-you-a-clean-doc-your-mac-shows-raw-text-with-everywhere-heres-the-fix-1m15

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
