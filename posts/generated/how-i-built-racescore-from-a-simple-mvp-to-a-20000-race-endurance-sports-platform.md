---
title: "How I built RaceScore: From a simple MVP to a 20,000-race endurance sports platform"
slug: "how-i-built-racescore-from-a-simple-mvp-to-a-20000-race-endurance-sports-platform"
author: "Ugo"
source: "devto_webdev"
published: "Thu, 23 Jul 2026 08:30:09 +0000"
description: "Hey Dev.to community! 👋 A year ago, I posted here presenting the early MVP of RaceScore—a side project I started to solve a simple frustration: trail runners..."
keywords: "racescore, race, what, security, platform, here, level, performance"
generated: "2026-07-23T08:38:07.283730"
---

# How I built RaceScore: From a simple MVP to a 20,000-race endurance sports platform

## Overview

Hey Dev.to community! 👋 A year ago, I posted here presenting the early MVP of RaceScore—a side project I started to solve a simple frustration: trail runners had universal indices like Betrail or ITRA to evaluate their level, but road runners and multi-sport athletes had nothing similar. Fast forward to today, and RaceScore has evolved from a small prototype into a full-fledged endurance sports platform with over 20,000+ races, a dynamic performance scoring algorithm, and B2B tools for race directors. Here is a look at what changed, the tech stack behind it, and what I learned along the way! 🏃‍♂️💨 🚀 What RaceScore Does Today Universal Dynamic Performance Score: Instead of just looking at raw finish times or rankings, RaceScore calculates a relative score based on race difficulty, field depth, and conditions. Interactive Event Discovery: Powered by Mapbox GL JS, athletes can explore over 20,000+ running, trail, and triathlon events with elevation profiles and GPX tracks. Ecosystem Sync & Features: Strava OAuth integration for auto-syncing race activities, an HMAC-signed ICS calendar feed, and a peer-to-peer secondhand bib marketplace. B2B Organizer Suite: Turnkey race management including Stripe online registrations, waiting list management, and QR-code bib scanning on race day for volunteers. 🛠️ The Tech Stack Here is what powers racescore.fr under the hood: Frontend: React 19 + Vite + TypeScript UI & Styling: Tailwind CSS v4 + shadcn/ui (Radix UI) Routing & Data Fetching: React Router v7 + TanStack React Query Backend & Database: Supabase (PostgreSQL, Auth, Row Level Security) Serverless API: Vercel Serverless Functions (Node/TypeScript) Mapping & Data Vis: Mapbox GL JS + Recharts Third-Party Services: Stripe (Payments), Strava API (OAuth), Nodemailer/Brevo (Transactional Emails), hCaptcha 🔐 Key Technical Learnings & Security Highlights Building a platform with thousands of public race pages and personal athletic data brought some fun engineering challenges: Securing Calendar Subscriptions: To prevent IDOR vulnerabilities on user ICS calendar exports, feed URLs are signed using HMAC tokens. OAuth Cookie Security: Strava authentication tokens are sealed strictly inside httpOnly cookies, keeping them inaccessible to client-side JavaScript. Constant-Time Timing Protection: Internal webhooks and CRON triggers use constant-time comparison (crypto.timingSafeEqual) to mitigate timing attacks. Granular Database Access: Leveraging Supabase's Row Level Security (RLS) paired with strict role checks on administrative endpoints (/api/admin). 👀 Check it out! The app is live and fully accessible: 🔗 Website: racescore.fr I'd love to hear your thoughts, feedback on the performance scoring concept, or any technical critiques regarding the stack. Happy running & coding! 🏃‍♂️⚡

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/racescore/how-i-built-racescore-from-a-simple-mvp-to-a-20000-race-endurance-sports-platform-4a3g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
