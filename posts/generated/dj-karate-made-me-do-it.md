---
title: "Dōjō 道場 — karate made me do it."
slug: "dj-karate-made-me-do-it"
author: "C W"
source: "devto_ai"
published: "Sat, 11 Jul 2026 07:46:00 +0000"
description: "This is a submission for Weekend Challenge: Passion Edition What I Built Dōjō (道場) is a Shito-Ryu based karate kata training companion, built around the Pass..."
keywords: "voice, sensei, counts, built, flame, kata, fire, streak"
generated: "2026-07-11T08:04:04.875251"
---

# Dōjō 道場 — karate made me do it.

## Overview

This is a submission for Weekend Challenge: Passion Edition What I Built Dōjō (道場) is a Shito-Ryu based karate kata training companion, built around the Passion Edition prompt taken literally, to say that passion is the fire that drives us. The home screen is a living flame that grows with your training, fed by both your streak and the effort you put in each day. If you show up consistently, it builds and feeds the flame; if you put in a hard session, it flares up that same day. It's a real canvas particle fire and not a static graphic. The core is a count-along kata drill with a live sensei voice. Pick a kata, set the tempo, and a sensei counts you through it in Japanese — ichi, ni, san… — on the beat, with a kiai shout on the traditional counts and an optional metronome. Pause/resume mid-drill, and every kata's counts are editable, since those conventions vary by branch. Finishing a drill logs the session and feeds the flame. Rounding it out: a kata hall grouped by their respective lineage (Pinan, Shuri-te, Naha-te), with a belt-and-history view, and a one-tap Kiai button to test the chosen voice. I have been practicing karate for 30 years and my goal was to build something that feels like stepping into a dōjō, not opening a fitness dashboard — and to make the voice feel like a real sensei counting beside you. Demo Code chantleyw / dojo Dōjō · 道場 A Shito-Ryu (糸東流) training companion with a live sensei voice. Dōjō is a karate practice app built around a single emotional idea: passion is the fire that drives us . The home screen shows a flame that grows with your training streak — a cold ember at zero, a roaring fire past 30 days. Pick a kata and a sensei voice counts you through it in Japanese, on the beat — ichi, ni, san… — with a kiai shout on the traditional counts and an optional metronome tick. Built for the DEV.to Weekend Challenge (Passion Edition). ✨ Highlights A flame that grows with your streak. Layered SVG plume with a Framer Motion flicker, driven by fire = min(1, streak / 30) . Reduced-motion holds it still. A live count-along drill. Choose a kata; the sensei counts in Japanese on the beat, kiai-ing on the traditional counts. Tempo… View on GitHub How I Built It The stack is Vite + React + TypeScript + Tailwind, with Framer Motion, Zustand for state, the Web Audio API for the metronome, and Netlify Functions for the backend. State persists per-device in localStorage — so no accounts are required. The sensei voice (ElevenLabs) This is the core of the app, and getting it to feel live drove most of the interesting decisions. A custom voice, built in Voice Design. The sensei is a purpose-built deep, gravelly grand-master voice created in ElevenLabs Voice Design — the kind of voice that could bark a battle command. The app pulls every voice on the account into a picker, but defaults to the sensei. Authentic Japanese counting. Numerals are generated programmatically as hiragana (いち, に, さん…, composing じゅういち for 11, and so on) and spoken with Turbo v2.5 using language_code: "ja". That language flag was the unlock because without it, an English-leaning accented voice pronounces さん like the English word "san"; with it, you get a proper sahn pronunciation. Making it land on the beat. A count drill can't afford a network round-trip per number. So on "Begin," the app pre-generates one clip per unique word, caches them as object URLs keyed by text, then plays the cached audio on each metronome beat. The count and the kiai are also given separate expressiveness profiles — the counts stay crisp and consistent, while the kiai runs at low stability / high style for a raw, shouted delivery. Keeping the key safe. The link is public, so the ElevenLabs key can never touches the browser. A tiny Netlify Function proxies /api/tts and /api/voices, holding the key in an env var and forwarding requests server-side. The client only ever talks to my own domain. Never hard-failing. If the proxy returns a non-200 — a quota cap, a rate limit — the app falls back to the browser's built-in speech synthesis (preferring a Japanese voice) and keeps counting. I actually hit this live during testing when a capped key ran dry, and the drill kept running on the fallback voice without a hiccup. Generation is also concurrency-limited with retries so the free tier's request limits don't drop individual clips. The flame is a canvas particle system — rising flame particles, floating embers, and an additive glow, all scaling with a single fire value from 0 to 1. Rather than tie that purely to the streak, I compute it from both consistency and effort: fire = 0.7 × (streak / 30) + 0.4 × (today's minutes / 45), capped at 1. A long streak carries a strong baseline, a hard session flares it up the same day, and a single huge day can't max it out alone. Reduced-motion users get a still flame instead. Prize Categories Best Use of ElevenLabs. The sensei voice is the core of the app: a custom generated Voice Design grand-master voice, spoken with Turbo v2.5 and language_code: "ja" for authentic Japanese counting, pre-generated and cached per word so it lands on the beat, with separate expressiveness profiles for the counts and the kiai which are all served through a serverless proxy that keeps the API key off of the client, with a seamless fallback to the browser voice so a public link never hard-fails.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/moersebene/dojo-dao-chang-karate-made-me-do-it-1abj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
