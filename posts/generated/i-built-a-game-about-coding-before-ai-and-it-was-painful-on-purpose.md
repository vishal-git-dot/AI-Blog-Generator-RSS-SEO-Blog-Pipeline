---
title: "I built a game about coding before AI (and it was painful on purpose)"
slug: "i-built-a-game-about-coding-before-ai-and-it-was-painful-on-purpose"
author: "Before AI"
source: "devto_webdev"
published: "Wed, 04 Nov 2026 23:09:15 +0000"
description: "It's 2019. There is no AI. You get a ticket: "Center the signup modal. It must work in IE11." You have a search engine, a Q&A site called StackUnderflow, and..."
keywords: "copy, game, you, your, paste, every, build, minutes"
generated: "2026-11-04T23:27:35.557497"
---

# I built a game about coding before AI (and it was painful on purpose)

## Overview

It's 2019. There is no AI. You get a ticket: "Center the signup modal. It must work in IE11." You have a search engine, a Q&A site called StackUnderflow, and copy-paste. Every search, every tab, and every build costs in-game minutes. Your coworkers ping you. Your lead calls a standup. How long does your shift take? That's beforeai.dev, a small browser game I shipped this week. It's free, needs no signup, and takes about 5 minutes to play. 🎮 How it plays Search: Tappable query chips (or type directly on desktop). Open answers: Some are closed as duplicate. Some are from 2011. One suggests a jQuery plugin. Copy, then "Paste + build": Builds take ~4 minutes. Wrong answers fail with very specific 2019 pain: place-items isn't supported in IE11, the cookie disappears because of Access-Control-Allow-Origin: *, or this is undefined in a class component. Chat pings: "can u review my PR? it's small (2,400 lines)". Help now and lose 15 minutes, or hit "after lunch". Nobody gets stuck: After 2 failed builds, a senior dev DMs you the right link. A shift is 3 tickets. At the end, you get your total time, a rank ("Junior Tab Hoarder", "Senior Copy-Paste Engineer"), and a share card. 🛠️ How it's built Next.js static export: The game is entirely client-side—a fake browser, a fake editor, and a ticket panel. No heavy game engine, just React and a small Zustand store. Levels are plain TypeScript data files, so adding a new ticket is just creating a new file. Cloudflare Workers: Serves the static files. A tiny Hono worker handles two routes: /r (a share page with Open Graph tags for social cards) and /api/event (anonymous daily counters in D1: starts, finishes, shares). No cookies, no IPs stored. Pre-rendered share images: Generated at build time with satori + resvg (one per rank), so the worker never has to render images on the fly. Automated testing (Vitest): Checks that every level is actually solvable—verifying no dead links, that rescue links lead to passing answers, that the rescue triggers after at most 2 fails, and that no real brand names snuck into the copy. Hosting cost so far: $0 on free tiers. 💡 Lessons learned Mobile-first matters even for desktop-feeling UI: A long line of code inside a CSS grid column initially pushed the entire page wider than mobile screens, hiding key action buttons. Fixing it required proper grid constraints: minmax(0, 1fr) and min-w-0. Minimize friction on mobile: Nobody wants to manually highlight and copy code on a phone. "Copy" opens a sheet with a single primary button: "Paste + build". Parody names only: StackUnderflow, Searchly, "the AI". It keeps the tone humorous while avoiding copyright headaches. 🔮 What's next Frontend is the only playable role right now. Fullstack, Backend, and DevOps are listed as "coming soon" (and tapping one logs a vote). (And yes, DevOps players: there will be YAML.) Give it a run and let me know your final time and rank: beforeai.dev

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/before_ai/i-built-a-game-about-coding-before-ai-and-it-was-painful-on-purpose-372g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
