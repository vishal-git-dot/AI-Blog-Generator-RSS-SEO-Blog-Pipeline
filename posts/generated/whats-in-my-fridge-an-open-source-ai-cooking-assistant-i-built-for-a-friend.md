---
title: "What's in My Fridge? — An Open-Source AI Cooking Assistant I Built for a Friend"
slug: "whats-in-my-fridge-an-open-source-ai-cooking-assistant-i-built-for-a-friend"
author: "fatik07"
source: "devto_webdev"
published: "Mon, 05 Oct 2026 04:59:31 +0000"
description: "The problem A friend of mine has a habit: they open the fridge, stare at a handful of random ingredients — some eggs, half a chicken, a bag of rice — and jus..."
keywords: "what, model, you, openrouter, not, open, friend, tanstack"
generated: "2026-10-05T05:01:22.635495"
---

# What's in My Fridge? — An Open-Source AI Cooking Assistant I Built for a Friend

## Overview

The problem A friend of mine has a habit: they open the fridge, stare at a handful of random ingredients — some eggs, half a chicken, a bag of rice — and just... close it again. Not because there's nothing to cook, but because turning "what I have" into "what I could make" takes a kind of mental effort that's easy to skip when you're tired. So for this weekend's Hacktoberfest challenge — Build for a Friend — I built them exactly that: What's in My Fridge? Tell me what you have. I'll tell you what you can cook. You add the ingredients sitting in your kitchen, optionally tell it something like "no spicy food" or "only 15 minutes," hit one button, and get back a handful of realistic meal ideas — each one clearly split into what you already have and what you'd still need to buy. No chat window. No meal-planning dashboard. Just: ingredients in, meal ideas out. Demo & code Code: github.com/fatik07/my-frigde Live demo: not deployed yet — this was built and tested locally during the challenge window. The README has full setup instructions if you want to run it yourself. Why open matters here The AI model is the core feature of this app — not a bolt-on. It runs through OpenRouter , defaulting to openrouter/free , OpenRouter's router that automatically picks a free, open model for each request. Why that choice specifically, and not a single proprietary model locked behind one vendor's API: It costs nothing to run. A friend using this shouldn't need me to keep a paid API key topped up. openrouter/free means the running cost is zero. It isn't locked to one model. The entire AI call is isolated behind one small module ( src/server/ai/adapter.ts ). Swapping to a different open model — or a different provider entirely — is a one-line change, not a rewrite. The rest of the app doesn't know or care which model answered. Everything downstream just sees validated, typed JSON. To be precise about what "open" means in this build: inference doesn't run locally on my friend's laptop — it still happens on OpenRouter's infrastructure. What open buys here is choice and cost , not offline/local inference. I think that's a legitimate and underrated version of "open matters": it's the difference between a project my friend can actually keep running for free, versus one that quietly stops working the day my API credits run out. How it works Stack: TanStack Start , TypeScript, TanStack Router , TanStack Query , TanStack AI ( @tanstack/ai + @tanstack/ai-openrouter ), Supabase (Postgres), OpenRouter , Tailwind CSS. The flow is deliberately boring and linear: Ingredients (Supabase) → AI call (server-only) → OpenRouter → structured JSON → reconciled against pantry → rendered meal cards A few pieces worth calling out: 1. The AI call never touches the browser. It's a TanStack Start server function, and the OpenRouter key only ever lives in process.env on the server: export function getMealSuggestionAdapter (): OpenRouterTextAdapter < any > { const apiKey = process . env . OPENROUTER_API_KEY if ( ! apiKey ) throw new Error ( ' OPENROUTER_API_KEY is not configured ' ) const model = process . env . AI_MODEL || ' openrouter/free ' return createOpenRouterText ( model as any , apiKey ) } 2. The response is schema-validated, not trusted prose. chat() takes a Zod outputSchema , so the model either returns a typed object or the call fails loudly — with a plain-JSON fallback for models that don't support strict structured output: const result = await chat ({ adapter , messages : [{ role : ' user ' , content : prompt }], outputSchema : AiSuggestionsResponseSchema , stream : false , }) 3. The model's claims get fact-checked against the real pantry. This was the part I cared about most: an AI that says "uses: chicken" when you don't actually have chicken is worse than useless. So every suggestion gets reconciled server-side — anything the model claims as "used" that isn't genuinely in your pantry gets demoted to "missing" before it's ever rendered: export function reconcileWithPantry ( suggestion : MealSuggestion , pantryNames : string []) { // anything claimed as "used" that isn't actually in the pantry // gets moved to "missing" instead — the model can't fake what you have ... } Standard stuff rounds it out: empty-pantry state, a loading state ("Thinking of something delicious…"), and a retry-able error state that never leaks a raw API error to the UI. What I'd do differently Given more time, the next step is exactly what the theme asks for: hand it to my friend and see what breaks. Right now it's been built and exercised locally, but not yet used by the person it's actually for — that's the real test, and I'll be reporting back on what they said. AI disclosure This project and this post were built with heavy assistance from an AI coding agent (Claude Code) — architecture, implementation, debugging version mismatches in the TanStack Start/Router packages, and writing this post. I reviewed and verified the code and claims above myself. Built solo for the Hacktoberfest Weekend Challenge: Build for a Friend ( #hf26challenge ).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fatik07/whats-in-my-fridge-an-open-source-ai-cooking-assistant-i-built-for-a-friend-12ge

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
