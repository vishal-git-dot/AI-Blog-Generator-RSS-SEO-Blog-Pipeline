---
title: "I built an entire agency management platform by myself. Here's what actually happened."
slug: "i-built-an-entire-agency-management-platform-by-myself-heres-what-actually-happened"
author: "Alok Barai"
source: "devto_webdev"
published: "Sat, 04 Jul 2026 03:18:54 +0000"
description: "I used to deliver food on Zepto. 14-15 hours a day. Sun, rain, didn't matter. I saved up, bought a laptop, and started doing video editing for clients. That'..."
keywords: "you, one, every, your, actually, client, not, day"
generated: "2026-07-04T03:39:49.959257"
---

# I built an entire agency management platform by myself. Here's what actually happened.

## Overview

I used to deliver food on Zepto. 14-15 hours a day. Sun, rain, didn't matter. I saved up, bought a laptop, and started doing video editing for clients. That's when things got messy. I was managing clients on WhatsApp. Tracking who paid me in Google Sheets. Sending invoices as PDF attachments that nobody opened. Every new client meant another chat group, another row in my spreadsheet, another folder I'd forget about. I went looking for one tool that could handle all of this. CRM, invoicing, projects, client communication — in one place. Everything was either $200+/month (when you add up all the separate tools) or missing basic stuff like a client portal. So I started building my own. That was a month ago. What I actually built Arpixa. One dashboard for agencies and freelancers. CRM, invoicing, project boards, AI assistant, file manager, scheduling, analytics, and a client portal where your clients can view projects, pay invoices, and message you. Every agency gets a branded subdomain — youragency.arpixa.io. Your clients see your brand, not mine. I'm not going to dump the whole feature list here. You can check arpixa.io if you're curious. The hard parts nobody warns you about Subdomains are a nightmare. Giving every user their own subdomain sounds simple until you realize auth doesn't work across subdomains by default. I had to build a token handoff system where you log in on one domain and the session gets securely passed to your workspace subdomain. It took longer than I expected going in — auth is the part everyone assumes is solved and nobody explains. Two payment gateways, because one isn't enough. I integrated both Stripe and Razorpay. Stripe for international users, Razorpay for India (UPI is how everyone pays here). The app auto-detects your country and shows the right payment flow. Sounds fancy — mostly it was just a lot of logic and twice the amount of webhook handling. Security rules will humble you. I wrote database-level security rules for every single collection — not API middleware, the actual database rejects unauthorized reads and writes. It took weeks longer than I budgeted. Multi-tenant isolation looks simple on a whiteboard and stops looking simple the first time you actually try to prove one workspace can never see another's data, in every possible query path. AI that's actually useful is hard. I didn't want a "chat with GPT" button slapped on the dashboard. The AI assistant knows about your clients and projects, so when you ask it to manage my client, it actually knows context. Things I got wrong I built too much before launching. 12 modules shipped. In hindsight I should have launched with 4 — CRM, invoicing, project management, client portal — and built the rest based on what people actually asked for. Instead I kept thinking "just one more feature" for months, and every one of those months was time I wasn't hearing from real users. I should have talked to users on day 1. I spent almost a 6 months building in isolation. Every day without user feedback is a day you might be building the wrong thing. I underestimated marketing. I'm an introvert. I'd rather debug a payment webhook for 8 hours than send one cold email. But nobody's going to find your product by accident. I'm forcing myself to post, reach out, talk to people. It's uncomfortable. I'm doing it anyway. What I'd tell you if you're building something solo Stop reading articles about the perfect tech stack. Pick tools you already know, build the thing, and ship it. The stack doesn't matter if nobody uses your product. I went from 14-hour delivery shifts with no technical background to shipping a 12-module SaaS product alone, in a year, by working on it every day whether I felt ready or not. That's the actual takeaway, not a slogan — showing up daily with no formal path is a strategy, not a consolation prize. Arpixa is live at arpixa.io. Free tier, no credit card. Happy to answer questions in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alok_barai/i-built-an-entire-agency-management-platform-by-myself-heres-what-actually-happened-3agf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
