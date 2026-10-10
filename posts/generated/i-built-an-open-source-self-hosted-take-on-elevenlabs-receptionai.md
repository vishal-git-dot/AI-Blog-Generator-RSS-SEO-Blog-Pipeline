---
title: "I built an open-source, self-hosted take on ElevenLabs' Reception.ai"
slug: "i-built-an-open-source-self-hosted-take-on-elevenlabs-receptionai"
author: "Gurnoor Singh Saini"
source: "devto_webdev"
published: "Sat, 10 Oct 2026 11:54:28 +0000"
description: "The phone rings at a dental clinic while everyone's hands are busy. Nobody picks up. The caller books somewhere else. Frontdesk.ai is an open-source AI recep..."
keywords: "voice, your, call, business, you, open, frontdesk, own"
generated: "2026-10-10T12:13:29.604916"
---

# I built an open-source, self-hosted take on ElevenLabs' Reception.ai

## Overview

The phone rings at a dental clinic while everyone's hands are busy. Nobody picks up. The caller books somewhere else. Frontdesk.ai is an open-source AI receptionist that picks up instead. It answers the call, books the appointment against a real calendar, answers questions from the business's own website, and leaves a transcript, a recording and a summary behind. Code: github.com/Sainigurnoor511/frontdesk-ai (Apache-2.0) Where the idea came from Frontdesk.ai is inspired by Reception.ai from ElevenLabs. I liked the product and wanted to build an open-source, self-hosted version of it: one you can read, change and run yourself. It is written from scratch, and it is an independent project that is not affiliated with ElevenLabs. It runs on your own system. One docker compose up on your laptop or your server. Your calls, clients and recordings live in your own Supabase project. There is no subscription to ElevenLabs, and no platform fee to me either. You bring your own API keys for speech and the LLM and pay those providers directly for what you use. Every part is swappable. Change the voice, the model, the prompts or the whole voice engine. What it does Answers calls in a natural voice, in the browser, from a dashboard or a public booking page Books appointments by checking real availability: business hours, staff hours, time off and existing bookings Answers questions from the business's website, uploaded files and FAQs Writes it all down : transcript, recording, summary and outcome for every call Sets itself up : paste a website URL and it fills in the business profile and services How a call works A live call is real-time audio over WebRTC, with no job queue in the middle: Browser ⇄ LiveKit room (WebRTC audio) │ voice worker joins the room speech-to-text → LLM with tools → text-to-speech │ on hangup: transcript, recording, summary saved The browser asks the server for a room and a token, then connects. A voice worker joins the same room and runs Groq Whisper for speech-to-text, a Groq-hosted LLM for the conversation, and Fish Audio for the voice. The agent has three tools: check_availability , book_appointment and search_knowledge . Two rules apply to every tool call: Arguments are validated with Zod before anything is written. Model output never flows straight into the database. The business is resolved on the server , never from an ID the client sends. If you would rather not run a voice worker, each receptionist can switch to a managed voice agent API with one setting. The tools are written once and both engines use them. The stack Layer Choice App Next.js 16 (App Router, Server Actions), React 19 Data and auth Supabase: Postgres, row-level security, storage Live voice LiveKit (WebRTC) + Groq + Fish Audio Background jobs BullMQ on Redis: website scans, knowledge indexing, webhooks UI Tailwind CSS v4, shadcn/ui on Base UI It is multi-tenant: every business only ever sees its own calls, clients and calendar. What is not done yet No inbound phone calls yet. Calls happen in the browser today. Real phone numbers are the top item on the roadmap. Cancel and reschedule are not voice tools yet. Callers can do both on the booking page. Try it git clone https://github.com/Sainigurnoor511/frontdesk-ai.git cd frontdesk-ai cp .env.example .env.local # add your keys npx supabase db push docker compose --env-file .env.local up --build Open http://localhost , paste a website, and call your receptionist. It is open to contributions. If you try it, tell me what broke and what you would want it to handle next.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sainigurnoor511/i-built-an-open-source-self-hosted-take-on-elevenlabs-receptionai-4mjm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
