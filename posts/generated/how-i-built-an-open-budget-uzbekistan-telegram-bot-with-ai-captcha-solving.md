---
title: "How I built an Open Budget Uzbekistan Telegram bot with AI captcha solving"
slug: "how-i-built-an-open-budget-uzbekistan-telegram-bot-with-ai-captcha-solving"
author: "Jahongir Tajiboyev"
source: "devto_python"
published: "Wed, 19 Aug 2026 06:38:34 +0000"
description: "Open Budget Uzbekistan is a government platform where citizens vote for public initiative projects (parks, roads, lighting, etc.) in their districts. Each ye..."
keywords: "bot, api, open, budget, captcha, async, gemini, railway"
generated: "2026-08-19T06:52:53.079382"
---

# How I built an Open Budget Uzbekistan Telegram bot with AI captcha solving

## Overview

Open Budget Uzbekistan is a government platform where citizens vote for public initiative projects (parks, roads, lighting, etc.) in their districts. Each year, thousands of projects compete for budget funding based on public votes. I built a Telegram bot that automates the voting process and rewards participants with UZS (Uzbek Som) for each vote they submit. The Problem The Open Budget portal requires: SMS verification for every vote CAPTCHA solving on each submission Manual interaction with the website This makes bulk or assisted voting extremely tedious. Our bot solves all of this automatically. Tech Stack Python 3.11 Aiogram 3.x — async Telegram bot framework aiosqlite — async SQLite with WAL mode aiohttp — async HTTP client for API calls User → Telegram Bot → Our API Gateway → Open Budget API ↓ Gemini AI (CAPTCHA) ↓ SQLite DB (rewards) Key Features 1. AI-Powered CAPTCHA Solving We use Google Gemini Vision API to automatically read and solve image CAPTCHAs from the Open Budget portal: python async def solve_captcha(image_bytes: bytes) -> str: model = genai.GenerativeModel("gemini-1.5-flash") response = await model.generate_content_async([ "Read the CAPTCHA text from this image. " "Return only the text, nothing else.", {"mime_type": "image/png", "data": image_bytes} ]) return response.text.strip() 2. Reward System Every user who votes receives UZS rewards directly to their Uzcard/Humo bank cards. Admins configure reward amounts via the built-in admin panel. 3. Admin Panel Bot owners get a full control panel via /admin: Connect API key Set target project ID Configure reward per vote Approve/reject withdrawal requests Broadcast messages to all users Download TXT reports 4. Persistent Storage on Railway One challenge was Railway's ephemeral filesystem. We solved it with Railway Volumes and an environment variable: python DB_PATH = os.getenv("DATABASE_PATH", "client_bot.db") async def get_db_conn(): db_dir = os.path.dirname(DB_PATH) if db_dir: os.makedirs(db_dir, exist_ok=True) return await aiosqlite.connect(DB_PATH) Set DATABASE_PATH=/data/client_bot.db and mount a Volume — data persists across deployments! Open Source The full source code is available on GitHub: openbudget-uz-bot Includes: Complete bot source code INSTALL.md — step-by-step setup guide API.md — API endpoint documentation .env.example — configuration template MIT License Demo Bot: @Budjetuz2026_bot API Keys: @Budjetuz2026_Bot Lessons Learned Gemini timeouts — ISP throttling in Uzbekistan causes slow responses. Set timeout to 8+ seconds. Railway volumes — Always mount a volume for SQLite, otherwise data resets on every deploy. Async SQLite — Use aiosqlite with WAL mode for concurrent reads without blocking. - **Google Gemini AI** — for automatic CAPTCHA solving - **Railway.app** — cloud deployment with persistent volumes ## Architecture Overview

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jahongir_tajiboyev_b806d0/how-i-built-an-open-budget-uzbekistan-telegram-bot-with-ai-captcha-solving-4l3m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
