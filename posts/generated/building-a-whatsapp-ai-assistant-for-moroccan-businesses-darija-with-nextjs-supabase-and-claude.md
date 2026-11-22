---
title: "Building a WhatsApp AI assistant for Moroccan businesses (Darija) with Next.js, Supabase and Claude"
slug: "building-a-whatsapp-ai-assistant-for-moroccan-businesses-darija-with-nextjs-supabase-and-claude"
author: "lamaizi hajar"
source: "devto_ai"
published: "Sun, 22 Nov 2026 19:10:04 +0000"
description: "Most small businesses in Morocco take orders on WhatsApp. The owner reads every message, types the menu again and again, and misses messages at night. I want..."
keywords: "message, whatsapp, hours, token, owner, one, merchants, webhook"
generated: "2026-11-22T19:16:57.017577"
---

# Building a WhatsApp AI assistant for Moroccan businesses (Darija) with Next.js, Supabase and Claude

## Overview

Most small businesses in Morocco take orders on WhatsApp. The owner reads every message, types the menu again and again, and misses messages at night. I wanted to see how far a small, cheap AI assistant could go for them, so I built one that answers in Moroccan Darija, French or Arabic. The problem Customers write in Darija (often in Latin letters), French, or a mix of both. Answers must come only from the business's real menu, prices and hours. No invented dishes. The owner must be alerted when someone orders or asks for a human. One codebase has to serve many merchants without mixing their data. Architecture Routing by phone_number_id. The WhatsApp Cloud API sends every message to one webhook. The webhook finds the merchant (tenant) by the phone number ID of the receiving number. Isolation. Supabase Postgres with Row Level Security. Merchants can only read their own rows. Writes go through server code with the service role. Token security. Each merchant's WhatsApp token is encrypted with AES-256-GCM in a table with no public policy. Webhook safety. HMAC signature check, immediate 200 response, background processing, and a table to ignore duplicate message IDs. Quotas. Monthly conversation limits per plan. Over quota, the customer gets a fixed message and no LLM call is made, so cost is capped. The LLM. Claude Haiku, with a system prompt built from the merchant's catalog, hours and info. Special tags in the reply trigger an order or human-handoff alert to the owner. Things that surprised me The 24-hour rule. WhatsApp only delivers free-form messages within 24 hours of the customer's last message. This also applies to alerts sent to the owner. Outside the window you need an approved template. Token expiry. Meta's test token lasts about 24 hours. A permanent token comes from a System User. I added detection of expired tokens (error 190) so the dashboard tells the merchant what to do. Delivery is asynchronous. The API can accept a message and fail later. The real reason arrives in the webhook statuses events, so log them. Structured editing beats free text. Merchants don't want to write prompts. The dashboard turns product rows, opening hours and delivery info into text for the model, and reads it back without losing anything. What's not covered Subscription payments, Meta's Embedded Signup (one-click onboarding for many merchants), voice-message transcription, and approved message templates for out-of-window alerts. The code I packaged the whole project (Next.js 15, TypeScript, Supabase, Tailwind v4, tests, and install/.env/usage guides) as a paid source-code product, for developers and agencies who want to offer this to their own clients: https://hajarlmz.gumroad.com/l/nlgxr The dashboard and the guides are currently in French. I'm the author. Questions and feedback are welcome in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lamaizi_hajar_b310d8837b4/building-a-whatsapp-ai-assistant-for-moroccan-businesses-darija-with-nextjs-supabase-and-claude-3p7o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
