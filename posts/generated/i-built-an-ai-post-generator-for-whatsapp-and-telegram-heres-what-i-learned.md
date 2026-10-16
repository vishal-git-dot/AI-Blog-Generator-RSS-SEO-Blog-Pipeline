---
title: "I Built an AI Post Generator for WhatsApp and Telegram - Here's What I Learned"
slug: "i-built-an-ai-post-generator-for-whatsapp-and-telegram-heres-what-i-learned"
author: "Waleed Shamhan"
source: "devto_ai"
published: "Fri, 16 Oct 2026 16:21:37 +0000"
description: "I'm an IT student, and I also work as a media coordinator. That means I live in two worlds: writing code, and writing content. One day I got tired of staring..."
keywords: "post, tool, you, api, writing, templates, content, python"
generated: "2026-10-16T16:24:14.489219"
---

# I Built an AI Post Generator for WhatsApp and Telegram - Here's What I Learned

## Overview

I'm an IT student, and I also work as a media coordinator. That means I live in two worlds: writing code, and writing content. One day I got tired of staring at a blank screen every time I needed a post for a WhatsApp or Telegram channel, so I built a small tool to solve my own problem: AI-Post-Generator . It's a Python command-line tool that generates professional posts for WhatsApp and Telegram channels using AI. You can find it here: https://github.com/waleedshamhan2050-sys/AI-Post-Generator The problem Running a channel means publishing constantly: announcements, tips, motivational posts, interactive questions. Writing all of that by hand is slow, and the tone drifts from post to post. I wanted something that could produce good drafts fast, in a consistent voice, and in Arabic. How it works The flow is deliberately simple: You pick a topic and a template from the command line. The tool loads a JSON template for that post type (announcement, tip, motivation, interactive question) with guiding examples. It sends the prompt to the OpenAI API (using gpt-4.1-mini ) and gets back a generated post. The generated post is saved automatically in an examples/ folder, so you can reuse or review it later. The tech stack is small: Python 3.x , the OpenAI API , python-dotenv for managing the API key safely in a .env file, and JSON for the templates. Design decisions I am proud of Templates instead of free-form prompts. Every post type has a JSON template with examples. This keeps the output consistent and lets me steer the AI toward a specific kind of post instead of hoping for a good result. Arabic-first. The tool generates posts in Modern Standard Arabic with appropriate emojis, because that is the audience I write for. Most AI writing tools I tried defaulted to English, so this mattered to me. Keep the secrets out of the code. The API key lives in a .env file, never in the source. It is a small thing, but it is the kind of habit I want to keep for every project. What I learned Building this taught me more than the tool itself: Python CLI apps: structuring a command-line program and keeping the code clean and documented. Working with AI APIs: how to call the OpenAI API, shape prompts through templates, and handle the response. Structured data: using JSON to store and manage templates in an organized way. Environment management: keeping sensitive data like API keys secure with .env files. Prompt design: writing templates that guide the AI toward a specific post type is a skill of its own. Content automation: how the whole loop of creating content for social channels can be automated. What is next I want to add direct publishing to channels, more template types, and support for scheduling posts. The goal is the same as when I started: less time staring at a blank screen, more time on the ideas that matter. If you run a channel or create content regularly, I would love to hear how you handle the blank-page problem. And if you try the tool, feedback is welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/waleedshamhan2050sys/i-built-an-ai-post-generator-for-whatsapp-and-telegram-heres-what-i-learned-3glg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
