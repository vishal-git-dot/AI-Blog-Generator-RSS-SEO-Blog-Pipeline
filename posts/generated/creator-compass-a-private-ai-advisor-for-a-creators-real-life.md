---
title: "Creator Compass — A Private AI Advisor for a Creator's Real Life"
slug: "creator-compass-a-private-ai-advisor-for-a-creators-real-life"
author: "Ujjwal Gupta"
source: "devto_ai"
published: "Mon, 05 Oct 2026 04:58:00 +0000"
description: "What I Built I built Creator Compass , a personal AI advisor for a friend who recently started her Instagram creator journey while pursuing her PhD at IIT. S..."
keywords: "creator, her, she, what, compass, life, open, model"
generated: "2026-10-05T05:01:22.636458"
---

# Creator Compass — A Private AI Advisor for a Creator's Real Life

## Overview

What I Built I built Creator Compass , a personal AI advisor for a friend who recently started her Instagram creator journey while pursuing her PhD at IIT. She's a talented singer, plays tennis, enjoys spending time with friends, and loves creating reels, carousels, memes, jokes, sarcasm, and self-love content. The problem wasn't that she had no content ideas. The problem was deciding when to create, what to create, and when not to create at all. She wants to grow as a creator, but she also worries about: Whether a post will actually fit her personality and audience Constantly worrying about views and engagement Running out of ideas Spending too much time creating content Whether content creation will interfere with her PhD and research Sharing personal thoughts and daily life with an AI service So instead of building another "AI that generates Instagram captions", I built something closer to a personal creator advisor . She tells Creator Compass: How she's feeling What happened during her day How much time she has Creator Compass then recommends whether she should: 🟢 Create today 🟡 Keep it low-effort 🔴 Don't post today — focus on your actual life When it recommends creating, it suggests a content idea, format, hook, reasoning, and estimated effort. The goal isn't to promise virality. The goal is to help her grow without letting Instagram take over her life. Demo Code GitHub: https://github.com/heyujjwal/creator-compass/ How I Built It Creator Compass is built around local open-source AI . Architecture React ↓ Spring Boot REST API ↓ Ollama ↓ Qwen3 The frontend collects the creator's current context and sends it to a Spring Boot backend. The backend constructs the advisor prompt and sends it to a locally running Qwen3 model through Ollama. The model returns the recommendation, which is displayed in the frontend. For the MVP, I intentionally kept the architecture simple: React for the interface Spring Boot for the backend API Ollama for local model inference Qwen3 as the open-weight AI model No database No Instagram credentials No automatic posting No external AI API This keeps the project small, understandable, and easy to extend. Why Does Open Innovation Matter? This project deals with something that isn't just technical data. The friend I'm building it for may share things about her mood, personal life, PhD work, research, relationships, and daily experiences. Sending all of that to a third-party AI API wasn't something I wanted to make a requirement. Using an open-weight model with local inference changed what I could build. With Ollama, the AI can run locally on the user's machine instead of requiring every personal thought to leave the machine and go to a hosted AI service. It also means the AI isn't a black box that I have to completely depend on. I can: Change the model Modify the system prompt Run the application offline Experiment with different open-weight models Customize the advisor's personality Extend the system without changing the entire architecture That's what open innovation made possible here: I could build an AI around a person's actual life without making a closed AI API the center of the product. What I Learned The biggest thing I learned while building this was that an AI project doesn't need to solve a massive problem. It can solve a very specific problem for one person. Instead of asking: "What AI product can I build?" I started with: "What is something my friend actually struggles with?" That changed the project completely. Creator Compass isn't trying to replace her creativity. It's trying to give her a second opinion — and sometimes tell her that she doesn't need to post anything today.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_gupta_e4460bbf99d9/creator-compass-a-private-ai-advisor-for-a-creators-real-life-2pld

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
