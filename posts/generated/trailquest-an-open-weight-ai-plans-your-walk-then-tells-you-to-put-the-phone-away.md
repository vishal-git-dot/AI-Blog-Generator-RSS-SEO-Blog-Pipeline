---
title: ""TrailQuest: an open-weight AI plans your walk, then tells you to put the phone away""
slug: "trailquest-an-open-weight-ai-plans-your-walk-then-tells-you-to-put-the-phone-away"
author: "Noor Ul Huda"
source: "devto_ai"
published: "Sun, 11 Oct 2026 04:52:28 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass What I Built Most fitness apps want your attention. TrailQuest wants ..."
keywords: "quest, you, your, model, open, then, demo, gemma"
generated: "2026-10-11T05:08:30.397336"
---

# "TrailQuest: an open-weight AI plans your walk, then tells you to put the phone away"

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 1: Touch Grass What I Built Most fitness apps want your attention. TrailQuest wants the opposite. You tell it how you feel today: your energy, your mood, how many minutes you have, indoors or outdoors, and a goal like 8,000 steps. It builds you a short quest : a warm-up, a brisk walk with faster intervals, a nature challenge (like "spot something with three colors"), and a cooldown. Then you press Start , and the screen turns into a plain timer that says Phone away. Go enjoy it. You walk. When you come back, you log your steps and earn XP and a Touch Grass streak . The streak counts any finished quest, even an easy recovery walk. It rewards showing up, not pushing harder. It's for people who want to move more but burn out on apps that demand attention, and for tired days when a gentle 10-minute quest beats skipping. Demo ▶ Watch the 50-second demo video In the demo, I create an account with an email code and set a 10-minute outdoor quest. I press Start and the phone-away timer runs. Then I log 3,200 steps and get 82 XP and a 1-day streak. I also open the dashboard, the daily journal, the trail map and the badges, and switch to dark mode with the Ocean theme and miles. Code GitHub repo: github.com/noorulhuda07/trailquest To run it: docker compose up --build , open http://localhost:8080 , and click Try the demo . How I Built It Stack: React and Vite for the frontend, FastAPI for the backend, Gemma through Ollama for quest generation, SQLite for accounts, and Docker Compose to run it all. User → FastAPI → Gemma (via Ollama) → Validator → Quest ↓ fails or unavailable Rules-based fallback → Quest My main rule is AI suggests, code validates. Gemma never talks to the user directly. Its answer must pass these checks first: Is it valid JSON with all the required fields? Does the intensity match the energy the user chose? Do the step durations add up to the time they have? Does any step contain unsafe wording? Is it an indoor quest? Then there are no nature challenges. If a check fails, or Gemma isn't available, a small rules engine builds a safe quest instead. Every quest carries a badge that says which one wrote it: Gemma (gemma3), self-hosted, code-validated or Backup rules engine . The server sets the badge, not the model, so the model can't claim credit it didn't earn. I also kept free text out of the prompt. Energy, mood and target are fixed options, and the workout type comes from a fixed list, so a user can't smuggle instructions into the model. Around the AI, I built sign-up with email or phone codes, Google sign-in, a one-click demo mode, and light and dark modes with four color themes. I tested the app with 42 backend tests and 5 frontend tests. The backend tests cover forged login tokens, SQL injection strings, code guessing, rate limits, and malformed or unsafe model output. GitHub Actions runs the tests and security scans on every push. What I Saw When I Ran It In my recorded demo, the quest came from the backup rules engine, not from Gemma, and the badge on screen says so. I'd rather show that than hide it. It's the point of the design: a missing or bad AI answer never reaches the user, and the app always gives a safe quest. Why Does Open Innovation Matter? Your mood stays yours. A quest request contains your energy, mood and schedule. With an open-weight model running on your own machine, that data doesn't need to leave it. I can swap the model with one setting. GEMMA_MODEL=gemma3:1b for a laptop with little memory, or a bigger one if you have the hardware. Fine-tuning for coaching styles is possible later. No bill per quest. Running it costs electricity, not API fees. I control the guardrails. Because I run the model, I choose the output format and what happens when it misbehaves. The trade-offs: the first run downloads about 3 GB, and a small model on a CPU is slower and less reliable than a large hosted one. That is exactly why the validator and fallback exist. My Agent Session I built TrailQuest with help from an AI coding assistant, then ran and tested the result myself. What's Next Weather and location tools so a rainy day gives an indoor quest, then friends, group quests and challenges. Real step tracking comes with a phone app. Built by noorulhuda07.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/noor_ulhuda_67fbcf3d4b66/trailquest-an-open-weight-ai-plans-your-walk-then-tells-you-to-put-the-phone-away-172f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
