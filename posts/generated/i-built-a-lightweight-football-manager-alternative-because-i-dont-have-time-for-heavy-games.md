---
title: "I built a lightweight Football Manager alternative because I don't have time for heavy games"
slug: "i-built-a-lightweight-football-manager-alternative-because-i-dont-have-time-for-heavy-games"
author: "Chen Tao"
source: "devto_webdev"
published: "Tue, 07 Jul 2026 03:35:36 +0000"
description: "Hi guys, I am a web developer from China. Today I want to show you my side project: 38-0 League . It is a football (soccer) simulation game on web. I used to..."
keywords: "you, have, because, don, play, football, time, want"
generated: "2026-07-07T03:56:09.937941"
---

# I built a lightweight Football Manager alternative because I don't have time for heavy games

## Overview

Hi guys, I am a web developer from China. Today I want to show you my side project: 38-0 League . It is a football (soccer) simulation game on web. I used to play a lot of Football Manager. But now I have a full-time job, I don't have time to play 5 hours just for half season. Sometimes I just have a stupid idea in my head: "What if Arsenal play in La Liga?" or "What if Haaland play in League 2?". So I write this game. You can custom teams, players, and just click one button. It will simulate 38 matches very fast. Here is some technical problems I met and how I fix them. Maybe it can help you if you build similar things. 1. Heavy Calculation in Browser Because I have no money to buy strong backend server, all match simulation runs in user's browser. Simulating 380 matches (20 teams play each other 2 times) is actually very fast in JS. The slow part is React rendering. At first, when I click "Simulate Season", the page freeze for 2 seconds. This is because I try to put all match logs and events into DOM state at same time. Solution: I separate the logic and UI. The simulation function just return a big JSON object in memory. React only render the final League Table. The match details are lazy loaded. If you don't click the specific match, it never renders. 2. Cheap Leaderboard using Cloudflare D1 I want a leaderboard so players can compete. But Redis or AWS RDS is too expensive for a free game. I try Cloudflare D1. It is serverless SQLite on edge. It is amazing! I write a Cloudflare Worker to receive high score from client, check a simple secret token, and save to D1 database. The latency is very low because the worker runs near the user. And the free tier gives me 100,000 writes per day. Very enough for me. 3. SEO for SPA (Multi-language) This is my biggest headache. I use Vite + React. Google crawler don't like it. I want people from Spain or Brazil to find my game, so I need /es and /pt routes. I didn't use Next.js because I don't want to rewrite all my code. So I write a post-build Node script. After npm run build , the script copy index.html into many folders, and replace the <title> and <meta> tags with correct language text statically. It's a bit dirty hack, but Google Search Console finally start to index my pages! 4. Ads vs PageSpeed To pay the domain name, I put some Adsterra banners. But these ad scripts destroy my Core Web Vitals. My LCP and TBT become red in Lighthouse. How I fix: I delay the ad script. I use a simple event listener. Only when user scroll or move mouse, I append the ad <script> to document body. So Lighthouse sees a clean page, and real users still see the ads. Win-win. If you like football, please try it here: 38-0.one You can try the Sandbox mode to make your own crazy league. Let me know if you find bugs or have ideas! Thanks!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cksmct/i-built-a-lightweight-football-manager-alternative-because-i-dont-have-time-for-heavy-games-1jd4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
