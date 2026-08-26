---
title: "I Built a Terminal AI Assistant That Never Freezes — Here's the Architecture"
slug: "i-built-a-terminal-ai-assistant-that-never-freezes-heres-the-architecture"
author: "Devesh tiwari"
source: "devto_python"
published: "Wed, 26 Aug 2026 06:32:18 +0000"
description: "I'm an AI Engineering student, and I got tired of alt-tabbing to a browser every time I needed to ask an LLM something mid-coding session. So I built term-ai..."
keywords: "free, model, openrouter, terminal, not, pricing, models, what"
generated: "2026-08-26T06:57:10.995214"
---

# I Built a Terminal AI Assistant That Never Freezes — Here's the Architecture

## Overview

I'm an AI Engineering student, and I got tired of alt-tabbing to a browser every time I needed to ask an LLM something mid-coding session. So I built term-ai — a fully async, terminal-native AI assistant that runs as a real installed CLI tool, not a janky script. Here's what I built, why I made specific architectural decisions, and what broke along the way. What It Does Type ai-agent in any terminal. Get a clean, keyboard-driven chat interface that renders AI responses as live Markdown — code blocks, headings, lists — right in your shell. Switch between multiple free AI models mid-conversation without losing context. That's the whole pitch. The Stack Textual — for the async TUI LangChain — for conversation memory and orchestration OpenRouter API — for routing prompts to free LLM models pyproject.toml — packaged as a real CLI tool Architecture: Three Layers, One Rule The one rule: nothing blocks the UI thread. Presentation Layer — Textual Every network call runs inside a Textual @work worker task. This is the entire reason the UI never freezes — even on a slow model response, you can keep scrolling, typing, or switching models while generation runs in the background. Responses render as live Markdown. This matters more than it sounds — getting back a wall of **bold** and code asterisks in a terminal is genuinely painful. Orchestration Layer — LangChain LangChain manages in-memory conversation state. The key design decision here: memory is not tied to a single model . You can start a task with one model, switch to another mid-conversation, and the full context carries over. Same thread, different brain, zero friction. Routing Layer — OpenRouter OpenRouter gives you a single API endpoint that routes to 400+ models. For this project I'm routing exclusively to free-tier models. The Problem That Almost Broke Everything I had a hardcoded AVAILABLE_MODELS list: AVAILABLE_MODELS = [ ( " Gemini 2.5 Pro " , " google/gemini-2.5-pro:free " ), ( " DeepSeek R1 " , " deepseek/deepseek-r1:free " ), ( " Llama 4 Maverick " , " meta-llama/llama-4-maverick:free " ), # ... ] One day, every single model started throwing: The entire top tier had quietly gone paid. The :free suffix in the model id doesn't mean anything once a provider pulls the model from the free tier — OpenRouter just updates the pricing fields in their API. The id string stays the same. The Permanent Fix I wrote openrouter_models.py — a self-healing module that fetches OpenRouter's live model catalog on startup and filters by actual pricing data, not by the id string: def _is_free ( model : dict ) -> bool : pricing = model . get ( " pricing " ) or {} prompt_price = pricing . get ( " prompt " ) completion_price = pricing . get ( " completion " ) # Pricing is the source of truth — not the :free suffix. # A model can keep a :free-looking id after going paid. if prompt_price is not None and completion_price is not None : return prompt_price in ( " 0 " , 0 ) and completion_price in ( " 0 " , 0 ) return str ( model . get ( " id " , "" )). endswith ( " :free " ) This runs once on startup, caches for 6 hours locally, and falls back gracefully if OpenRouter is unreachable. The AVAILABLE_MODELS list now rebuilds itself every time the cache expires — I will never manually patch a model slug again. Installation (The Actual Modern Way) This is packaged via pyproject.toml , not a shell script: git clone https://github.com/your-username/ai-terminal-app cd ai-terminal-app python -m venv venv && source venv/bin/activate cp .env.example .env # add your OpenRouter key pip install -e . Then from anywhere: ai-agent For a true global install outside any venv: pipx install . Keybindings Key Action Enter Submit prompt Ctrl+L Clear memory Ctrl+C Quit Mouse Scroll, click to navigate What's Next 🎙️ Voice Engine — local Whisper STT + TTS, fully offline 💾 Persistent Memory — SQLite + LangChain so context survives between sessions Links GitHub: [your repo link here] OpenRouter free model catalog: https://openrouter.ai/collections/free-models If you're building terminal tools or working with OpenRouter's free tier, I'd genuinely like to hear what you're running into — drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/deveshtiw/i-built-a-terminal-ai-assistant-that-never-freezes-heres-the-architecture-5dnd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
