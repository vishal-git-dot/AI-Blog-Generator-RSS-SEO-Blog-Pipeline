---
title: "From Rust CLI bug-hunting to a massive Portfolio overhaul"
slug: "from-rust-cli-bug-hunting-to-a-massive-portfolio-overhaul"
author: "Yash Kumar Saini"
source: "devto_python"
published: "Sat, 06 Jun 2026 08:34:48 +0000"
description: "23 commits, 3 PRs, and a 7-day streak. This week was a balance of deep-diving into Rust CLI logic, refining my Neovim setup, and a massive +4,500 line overha..."
keywords: "week, portfolio, rust, logic, but, you, cli, commits"
generated: "2026-06-06T08:41:07.448865"
---

# From Rust CLI bug-hunting to a massive Portfolio overhaul

## Overview

23 commits, 3 PRs, and a 7-day streak. This week was a balance of deep-diving into Rust CLI logic, refining my Neovim setup, and a massive +4,500 line overhaul of my portfolio. TL;DR It’s been a while since I’ve had a "perfect week," but I finally hit that 7-day commit streak. 23 commits, 3 PRs, and 1 closed issue across 4 different repos—this week was the definition of a polyglot grind. I spent my time bouncing between surgical Rust fixes in a CLI tool, deep-diving into Python backend logic, and completely ripping apart my portfolio for a modern redesign. WHAT I BUILT The week was split between high-level visual work and low-level logic. I managed to touch four different repositories, each serving a very different purpose in my workflow. DeepRead I spent a good chunk of the week in DeepRead . With 8 commits, this was my most active repo in terms of frequency. It’s a Python-heavy project, and I was focused on refining the core processing logic. Python is usually my go-to for anything involving heavy data or AI-adjacent backend work, and this week was no exception. I didn't open a PR here yet, but the 8 commits represent a lot of iterative testing and refining of the internal modules. nvim You know it’s a productive week when you’re also tweaking your tools. I pushed 7 commits to my nvim config. Most of this was Lua-based (obviously), and I was mainly focused on tightening up my LSP settings and UI. There’s something incredibly satisfying about spending 20 minutes fixing a minor annoyance in your editor and then seeing it pay off for the rest of the week. If my environment isn't perfect, I can't get into that deep flow state. GitBanner I’ve been working on GitBanner , a TypeScript tool for generating GitHub profile banners. I pushed 6 commits and opened a new feature PR: feat: add ignore-languages input to filter generated/vendored files . The goal here was to give users more control over what shows up in their stats. Nobody wants their "top languages" to be skewed by a massive vendored library or a bunch of generated CSS files. It’s a small DX improvement, but those are the ones that make a tool actually usable. trx Finally, I did some surgical work on trx , a Rust-based CLI tool. This was a classic "scratch your own itch" situation. I noticed a bug where the tool would repeatedly prompt for an update even after I’d already upgraded. I opened an issue for it— bug: TRX repeatedly prompts for update even after successfully updating —and then immediately went in to fix it. Rust is great for this kind of thing because once you get the logic right and the compiler is happy, you know it’s solid. PULL REQUESTS I opened three PRs this week, and they tell the story of where my head was at. The most significant one in terms of sheer volume was for my portfolio . The PR, feat: portfolio modern redesign + scrolling GitHub PR sidebar , clocked in at a massive +4,509 lines. I decided it was time to move away from my old layout and go for something much more modern. The highlight of this redesign is a new scrolling sidebar that pulls in my latest GitHub PRs. It’s a bit meta—building a tool to show the tools I’m building—but I love how it looks. It’s still open as I’m fine-tuning some of the CSS transitions, but the bulk of the work is done. On the Rust side, I got fix: stop re-prompting update after user skips or upgrades merged into trx . This was the fix for the bug I mentioned earlier. It involved tightening up the version check logic to ensure the CLI respects the user's choice to skip an update or correctly identifies when the local version matches the remote. I also have the GitBanner PR open, which adds the ignore-languages input. This was a fun bit of TypeScript logic, essentially filtering the language data before it hits the rendering engine. ISSUES & DISCUSSIONS I only opened one issue this week, but it was a productive one. I reported the update prompt bug in trx and then closed it myself with the PR I mentioned above. I’m a big believer in documenting bugs even if you’re the one fixing them five minutes later. It creates a paper trail for anyone else who might run into the same weird behavior. TECH STACK This was a true polyglot week. My language breakdown is all over the place: Python for the heavy lifting in DeepRead. TypeScript for the GitBanner logic and the massive Portfolio redesign. Rust for the CLI stability in trx. Lua for the Neovim configuration. The numbers tell an interesting story: +4,614 additions and -1,081 deletions. That’s a huge net positive, mostly driven by the portfolio redesign. Usually, I like to see more deletions (refactoring is a gift), but when you’re shipping a whole new UI, the additions are going to win every time. And of course, the 7-day streak. It wasn't a forced grind; I just happened to be in a really good rhythm where I had something I wanted to ship every single day. WHAT'S NEXT Next week is all about landing those open PRs. I want to get the portfolio redesign merged and live—there are still a few responsive design bugs I need to squash in that new scrolling sidebar. I also want to see the GitBanner feature through to completion. Beyond that, I’m planning to dive back into the Python side of things with DeepRead. There’s some performance optimization I’ve been putting off, and now that my environment is dialed in and my portfolio is looking fresh, I’ve got no excuses left. Catch you all next week! python #typescript #rust #frontend #dx #consistency · 4 min read · Generated 2026-05-24 by DevNotion

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yashksaini/from-rust-cli-bug-hunting-to-a-massive-portfolio-overhaul-7nn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
