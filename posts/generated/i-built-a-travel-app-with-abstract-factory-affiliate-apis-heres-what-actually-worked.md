---
title: "I built a travel app with Abstract Factory + affiliate APIs — here's what actually worked"
slug: "i-built-a-travel-app-with-abstract-factory-affiliate-apis-heres-what-actually-worked"
author: "Sivaraman Ramaswami"
source: "devto_webdev"
published: "Thu, 12 Nov 2026 14:54:41 +0000"
description: "I've been building packedNbooked ( https://packednbooked.com ) — a trip planner that starts with your budget instead of a destination. You enter $2,000, JFK,..."
keywords: "affiliate, com, booking, live, hotel, prices, factory, you"
generated: "2026-11-12T14:55:17.818634"
---

# I built a travel app with Abstract Factory + affiliate APIs — here's what actually worked

## Overview

I've been building packedNbooked ( https://packednbooked.com ) — a trip planner that starts with your budget instead of a destination. You enter $2,000, JFK, 7 days → it fans out to flight/hotel/car/activity APIs in parallel and returns ranked complete trip packages. This post is about the architecture decisions that held up and the ones that didn't. The pattern: Abstract Factory Every travel category (flights, hotels, cars, attractions) gets its own factory. Each factory spawns provider agents. The orchestrator never touches provider logic directly. class FlightProviderFactory(BaseFactory): def create_agent(self) -> BaseAgent: return TravelpayoutsAgent() class HotelProviderFactory(BaseFactory): def create_agent(self) -> BaseAgent: return BookingAgent() This paid off when I swapped hotel providers mid-project (Hotellook → Booking.com via CJ affiliate). Zero changes to the orchestrator — I just swapped the agent behind the factory. Same when Ticketmaster went live: new factory, new agent, plug it in. The fan-out itself runs async — all four factories fire in parallel, results get budget-pruned, then an LLM (Groq + gpt-oss-120b) ranks the combos by value. The hotel API nightmare This is the part nobody writes about. My original plan was real-time hotel pricing. Here's what I found: Amadeus — decommissioned their free tier in July 2025 Travelpayouts hotel endpoints — all 404 Booking.com, Agoda, Expedia, HotelBeds — all require commercial contracts Booking.com via CJ affiliate — Demand API is restricted to "strategic partners," no application path I spent three weeks on this before accepting the ceiling: mock prices + live Booking.com deep-links is the permanent setup. The links go to Booking.com search results where users see real availability. It's honest — I label prices as estimates and the Show HN caveat was upfront about it. The lesson: travel pricing APIs are a moat. If you're not paying enterprise rates, you're not getting real-time hotel data. Build around it, not through it. The affiliate setup (actual numbers) Revenue model is affiliate commissions — no ads, no paywall: Partner Integration Notes Travelpayouts/Aviasales Live prices via Data API marker 326901 Booking.com via CJ Deep-links, mock prices publisher 101876939 Viator Live affiliate links ID P00319033 DiscoverCars Affiliate link ~$20/booking, 365-day cookie Booking.com's CJ approval took about a week. Viator was instant. DiscoverCars was the fastest approval and best cookie window. Realistic projection: $0–20/mo now, $200–430/mo at 20k monthly visitors. It's a long game — the affiliate revenue only matters if the SEO compounds. What's actually live FastAPI backend on Railway ($5/mo), React/Vite frontend on Render (free static) Flights: real cached prices from Travelpayouts /v2/prices/latest Hotels: estimated prices, live Booking.com deep-links Attractions: Viator (live) + Ticketmaster Discovery API (real events by city/date) AI ranking: falls back to cost-sort if Groq key is missing 115 tests passing What I'd do differently Start with the affiliate approvals. I wired affiliate links at the end and retroactively got approvals. Should have done it week one — some take a week+, and you don't want to build around a partner that rejects you. Don't fight the hotel API wall. I lost three weeks trying to find real-time hotel pricing. The correct answer was always "mock prices + live booking link." Abstract Factory was the right call. The pattern felt like over-engineering for a solo project at first. It wasn't — I swapped providers three times without touching orchestration logic. App is live at https://packednbooked.com . Code isn't public yet but happy to answer questions about the architecture or affiliate setup. What travel pricing APIs have you found that actually work at the free/indie tier?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sivaraman_ramaswami_e7cc2/i-built-a-travel-app-with-abstract-factory-affiliate-apis-heres-what-actually-worked-41g3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
