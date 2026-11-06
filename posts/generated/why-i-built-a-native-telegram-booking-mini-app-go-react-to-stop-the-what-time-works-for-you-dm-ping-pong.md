---
title: "Why I Built a Native Telegram Booking Mini App (Go + React) to Stop the "What Time Works for You?" DM Ping-Pong"
slug: "why-i-built-a-native-telegram-booking-mini-app-go-react-to-stop-the-what-time-works-for-you-dm-ping-pong"
author: "SerjIan"
source: "devto_webdev"
published: "Fri, 06 Nov 2026 22:28:11 +0000"
description: "For solo specialists who work 1-on-1 with clients — language tutors, therapists, coaches, personal trainers, tattoo artists, and beauty/barber pros — almost ..."
keywords: "telegram, your, you, clients, every, time, client, booking"
generated: "2026-11-06T22:54:48.604750"
---

# Why I Built a Native Telegram Booking Mini App (Go + React) to Stop the "What Time Works for You?" DM Ping-Pong

## Overview

For solo specialists who work 1-on-1 with clients — language tutors, therapists, coaches, personal trainers, tattoo artists, and beauty/barber pros — almost all client communication already happens inside Telegram. That’s where homework gets shared, sessions get rescheduled, and clients ask when they can come in next. Yet the moment someone wants to book a time, it turns into a 20-minute ping-pong match in DMs: "Are you free Tuesday at 18:00?" "Tuesday is full — how about Thursday at 16:30?" "Wait, is that my timezone or yours?" "Sorry, I forgot I need a 15-minute break between back-to-back calls..." Sending a client out of a warm chat to an external website, asking them to fill out long forms, or relying on email confirmations that sit unread in a spam folder breaks the flow for both sides. And keeping track of reschedules, cross-border timezones, and manual "Just a reminder, we meet tomorrow at 15:00" messages quickly turns into a second job. I wanted the schedule to live in the exact same place where the conversation happens — right inside Telegram, one tap away. That’s why I built VisitKit ( @visitkit_bot ). The Core Idea: Everything at Your Fingertips Without Leaving Telegram Instead of a separate website with logins and passwords, VisitKit opens as a native Telegram Mini App right inside the messenger: Clients book in 3 taps without leaving the chat. You drop your booking link in a DM or pin a "Book a time" button in your Telegram channel. The client taps it, sees only your open slots, picks a time, and confirms. Their name is pulled from Telegram automatically. Morning schedule digest & automated bot reminders. Every morning, the bot sends you a clean summary of your appointments for the day. And it automatically reminds each client 24 hours and 2 hours before their session — cutting last-minute no-shows to near zero. Automatic timezone conversion. If you’re an online tutor, therapist, or coach living in Belgrade, Lisbon, or Tbilisi while your students or clients are in London, Berlin, or New York, nobody has to do timezone math in their head. You manage your hours in your timezone; clients see free slots in theirs. Weekly recurring slots for regular clients (1–12 weeks). When a student takes lessons every Tuesday at 17:00 or a therapy client books every Wednesday at 12:00, you don’t have to recreate the slot every week — just pick 4× or 8× weekly repeat in one tap. 2-tap rescheduling & automatic buffer time between sessions. Need to move a session an hour later? Tap Reschedule inside the booking card and the bot immediately notifies the client with the updated time. You can also set a 5, 10, 15, or 30-minute break after every booking so back-to-back sessions never overlap. Browser fallback link & 1-tap calendar sync. Have clients who message you from WhatsApp, Instagram, or SMS and don’t use Telegram? Every specialist also gets a clean browser booking page ( visit.dailykit.top/b/... ) that works in 20 languages, plus .ics calendar export for Apple, Google, and Outlook Calendars. Under the Hood (Go + React + PostgreSQL) To keep the Mini App instant even on slow mobile connections: Backend: Go ( chi + pgx + PostgreSQL) handling timezone-aware slot generation, recurring series conflict detection, .ics calendar feeds, and Telegram webhook/reminder workers in a single binary. Frontend: React + TypeScript + Tailwind CSS compiled into a lightweight bundle that adapts to Telegram’s native light/dark theme variables ( --tg-theme-* ) and supports 20 languages out of the box (including RTL for Arabic and Persian). Try It Live Setting up a page takes about two minutes inside Telegram — add your services (or session lengths) and pick your working hours using a weekly template or specific open dates. Every new page starts with 2 months of full Pro features as a gift , and the base tier remains free. Open in Telegram: https://t.me/visitkit_bot Step-by-step How-To guide with screenshots: https://dailykit.top/visitkit/how-to/getting-started/ Product overview & interactive demo: https://dailykit.top/visitkit/ If you manage clients, students, or consultations through Telegram (or build Telegram Mini Apps yourself), I’d love to hear your feedback — what scheduling edge cases matter most in your daily workflow?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/serj_serj_830e7254a86d7ea/why-i-built-a-native-telegram-booking-mini-app-go-react-to-stop-the-what-time-works-for-you-1khb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
