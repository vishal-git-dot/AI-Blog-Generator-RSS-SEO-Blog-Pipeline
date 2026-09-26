---
title: "I spent months building a markdown notes app and finally shipped it — here's the whole story"
slug: "i-spent-months-building-a-markdown-notes-app-and-finally-shipped-it-heres-the-whole-story"
author: "Parimal Mahindrakar"
source: "devto_python"
published: "Sat, 26 Sep 2026 04:01:32 +0000"
description: "So I've been sitting on this project for a while now and I think it's finally time to talk about it. I wanted a place to write. Not just dump text somewhere ..."
keywords: "you, just, your, notes, can, write, one, markdown"
generated: "2026-09-26T04:26:44.937394"
---

# I spent months building a markdown notes app and finally shipped it — here's the whole story

## Overview

So I've been sitting on this project for a while now and I think it's finally time to talk about it. I wanted a place to write. Not just dump text somewhere — actually write , in markdown, with my notes organized the way my brain works. Folders inside folders, tags, links between notes. And then when I write something worth sharing, I want to just... share it. Without copying it into some other platform, without reformatting it, without fighting a WYSIWYG editor. So I built it myself. It's called MarkdownStack and it's been the most fun and most frustrating side project I've ever worked on. What it actually does At its core it's a markdown vault. You sign up, you get a private workspace. You write notes. You organize them into folders. You can link notes to each other with [[wikilinks]] , tag things with #hashtags , and search everything with a quick switcher (double-tap P anywhere — stole that idea from every IDE I've ever used). The editor has a live preview mode where the rendered output is clickable — click anywhere in the preview and it jumps your cursor to that exact spot in the source. That one feature alone took me way longer than I'm comfortable admitting. Then there's the publishing side. Hit one button and your note is live at a public URL. Anyone can read it, no account needed. They can leave comments, upvote it. You can even publish a whole folder — every note inside it gets its own page with a navigation sidebar so readers can move between them. Oh and there's an AI chat thing now. Hit C C , ask it to write a note on whatever topic, and it generates proper markdown and saves it straight to your vault. You bring your own API key so I'm not paying for your GPT-4 habit. The stack, since everyone always asks Frontend: React 18, Vite, Tailwind. No Redux or Zustand or anything like that — just React Context per feature. Kept it simple and honestly didn't miss a state library once. Backend: FastAPI with async SQLAlchemy on PostgreSQL. Full-text search is just tsvector — no Elasticsearch, no Algolia, just Postgres doing its thing. JWT auth, email verification through Mailgun, Alembic for migrations. Infra: AWS EC2 behind nginx, Docker Compose, GitHub Actions for deployments. Nothing fancy. There's also an MCP server so Claude and other AI assistants can interact with your vault directly as a tool. That one was a rabbit hole I did not expect to go down but here we are. Things that nearly broke me The markdown renderer. I'm using remark + rehype + highlight.js for syntax highlighting. Running that whole pipeline on every single keystroke was absolutely destroying performance on any note longer than a few hundred lines. The fix was splitting the content into discrete blocks and memoizing each one individually — so when you edit a paragraph, only that paragraph re-renders, not the entire note. Obvious in hindsight, painful to arrive at. Async SQLAlchemy. If you've used it you know. If you haven't — there's this error called MissingGreenlet that happens when you try to access a relationship that wasn't eagerly loaded. It doesn't give you a great error message, it just explodes at runtime. The rule I eventually internalized: always use selectinload() on every query that touches a relationship, no exceptions. Theming. I spent a week going back and forth on how to handle dark/light mode before landing on CSS custom properties for everything. --bg , --text , --accent , every color is a variable. Switching themes is one data-theme attribute on the root element. Should've done this from day one instead of trying to use Tailwind's dark variant. The thing I'm most proud of Honestly? The published folder experience. You publish a folder, you get a URL, anyone can open it and read all your notes with a proper sidebar navigation. It feels like a mini documentation site that required zero setup. I use it myself to share notes with people and it just works the way I always wanted sharing to work. Just for your reference : https://mdstack.in/p/s/llmevaluations Go try it mdstack.in — free to sign up, free to use. Write something, publish it, drop the link in the comments here. I want to see what people actually use it for. And if something's broken or you have a feature idea, tell me. I read everything.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/parimalmahindrakar/i-spent-months-building-a-markdown-notes-app-and-finally-shipped-it-heres-the-whole-story-3boe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
