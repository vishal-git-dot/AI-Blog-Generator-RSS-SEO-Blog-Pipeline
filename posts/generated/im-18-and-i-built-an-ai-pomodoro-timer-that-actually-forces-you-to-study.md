---
title: "I'm 18 and I built an AI Pomodoro timer that actually forces you to study"
slug: "im-18-and-i-built-an-ai-pomodoro-timer-that-actually-forces-you-to-study"
author: "Jakub Mužík"
source: "devto_webdev"
published: "Thu, 18 Jun 2026 20:05:34 +0000"
description: "Hey everyone! 👋 I'm an 18-year-old student and solo developer. Like many of you, I struggle with procrastination. I've tried dozens of Pomodoro timers, but t..."
keywords: "you, can, aurora, when, pomodoro, timer, actually, like"
generated: "2026-06-18T20:32:55.631837"
---

# I'm 18 and I built an AI Pomodoro timer that actually forces you to study

## Overview

Hey everyone! 👋 I'm an 18-year-old student and solo developer. Like many of you, I struggle with procrastination. I've tried dozens of Pomodoro timers, but they all have the same fatal flaw: they only track time, not actual focus. You can stare at a wall for 25 minutes, and the app will still congratulate you. That felt broken. So, I spent the last few months designing and building Aurora — a desktop Pomodoro app that uses AI to verify if you were actually working and actively kills your selected running processes on your device. 🧠 How the AI Evaluation Works When you start a focus block in Aurora, you tell it what you are studying (e.g., "Web App Architecture" or "Photosynthesis"). When the timer rings, instead of just taking a break, Aurora uses the Gemini 3.1 Flash-Lite API to generate a quick, personalized quiz about your topic. You only earn XP and level up if you can prove you actually learned something. It turns studying into a game where you can't cheat the system. 🛡️ Hardcore Mode I also added a "Hardcore Mode" for when my ADHD is really bad. When activated: It kills distracting apps (like Discord or Steam). You cannot close the timer or open the blocked apps until the focus time is over. 💻 The Tech Stack Since I wanted this to feel like a premium, native desktop experience rather than just another website, I chose: Electron & Vite React & TailwindCSS Framer Motion Firebase (Auth, Firestore for leaderboards, and saving session history) Google Gemini API (For the AI evaluation) 💡 What I Learned Being completely solo on this forced me to wear every hat: UI designer, frontend dev, backend architect, and now... marketer. Getting the Electron IPC (Inter-Process Communication) to securely handle OAuth and deep linking was probably the hardest technical challenge. Let me know what you think! I just launched Aurora in an alpha release, and I'm super nervous but excited to get feedback from other developers. If you want to check it out or roast my UI design, you can find it here: 👉 [ https://stayaurora.dev ] If you have any questions about the architecture, how I integrated Gemini, or how was my experience with first time using electron, ask away in the comments!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cavalinhoxdd/im-18-and-i-built-an-ai-pomodoro-timer-that-actually-forces-you-to-study-2ipo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
