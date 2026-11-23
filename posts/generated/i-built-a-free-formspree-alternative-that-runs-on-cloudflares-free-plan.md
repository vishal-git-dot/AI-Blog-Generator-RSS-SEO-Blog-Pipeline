---
title: "I built a free Formspree alternative that runs on Cloudflare's free plan"
slug: "i-built-a-free-formspree-alternative-that-runs-on-cloudflares-free-plan"
author: "Jacob Alcock"
source: "devto_webdev"
published: "Mon, 23 Nov 2026 23:29:23 +0000"
description: "I got annoyed with form backends. Every static site needs a contact form, and the usual services give you 50 submissions a month before asking for money. So ..."
keywords: "form, spam, you, free, email, own, cloudflare, your"
generated: "2026-11-23T23:39:37.004137"
---

# I built a free Formspree alternative that runs on Cloudflare's free plan

## Overview

I got annoyed with form backends. Every static site needs a contact form, and the usual services give you 50 submissions a month before asking for money. So I built my own, called it sendm8, and made it free. It's been live since mid-September. The whole thing runs on one Cloudflare Worker on the free plan: Hono for routing, D1 for the database, R2 for file uploads and Workers AI for spam. The only thing I pay for is email (Resend). It's open source (AGPL), so you can also run your own copy: https://github.com/m8team/sendmate The one-line version You don't need an account to use it. Put your email address in the form's action: <form action = "https://sendm8.com/f/you@example.com" method = "POST" > <input type = "email" name = "email" required > <textarea name = "message" required ></textarea> <input type = "text" name = "_gotcha" style = "display:none" tabindex = "-1" autocomplete = "off" > <button> Send </button> </form> The first submission sends you a confirmation link. Click it and everything after that lands in your inbox. If you sign in later with the same address, the form moves into your account with every submission so far, and you get a dashboard, CSV export, and delivery to Discord, Slack, Telegram or a webhook. The field names match Formspree's ( _replyto , _subject , _next , _gotcha ), so moving over is usually just changing the URL. Fitting inside the free plan The free plan has hard limits, and most of the interesting decisions came from those: 10 ms of CPU per request. Sign-in is OAuth only (Google or GitHub), because hashing passwords would blow the budget. Request bodies are capped, and anything slow (email, webhooks, the AI spam check) runs after the response has gone back. 50 database queries per invocation. The cron jobs work in small batches and stop before they hit the cap, then pick up where they left off on the next run. 100,000 D1 writes a day. A submission costs about three writes. An hourly job checks usage, and if it gets past 90% it stops storing spam and pauses new no-account endpoints until the next day. Email. Each account gets a number of instant emails a day, then the rest arrive together in a daily digest, so a busy day turns into one email rather than a bill. All the limits live in one file, and the marketing site reads the same numbers the Worker enforces, so the pricing page can't drift from reality. Spam Spam was harder than I expected. There's a honeypot and some simple rules (link counts, markup links, throwaway email domains, keyboard mash), and then Workers AI scores what's left. A Llama model gives each submission a 0–100 spam score, and only a confident score bins it on its own. The model gets things wrong in fairly predictable ways, so there are a few exceptions: It scored ordinary Persian and Chinese enquiries as spam, so for text that's mostly in a non-Latin script it can flag but can't bin. It scored raffle entries (name, phone, ticket count) as spam because there's no free text to judge, so short structured submissions get let off. Someone testing their own form ("is this thing on?") reads like junk too, so a clean submission from the form's own owner is never binned. Then one day Cloudflare retired the model I was using, and the AI check silently stopped for most of a day. I now test candidate models against a few hundred real past submissions before switching, rather than guessing. What people actually use it for This is the bit I like most. About 50 people have a form on it now, submissions have come in from 36 countries, and almost none of the uses are what I pictured: A bar uses it to collect end-of-shift reports from the bartenders. A company in Jordan collects job applications through it, CVs and all. A Colombian business ran a raffle on it and got 100 entries in a few days. Someone built a checkout on it, and order details arrive as form submissions. No marketing so far. I honestly don't know how most of them found it yet, which is half the reason for this post. Running your own If you'd rather not depend on me, the repo deploys to your own Cloudflare account, and there's a Dockerfile for running it anywhere else (minus the AI spam check, which only runs on Cloudflare). The defaults fit inside Cloudflare's and Resend's free plans. Feedback welcome, especially if you try to break the spam filter. https://sendm8.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jacobdavidalcock/i-built-a-free-formspree-alternative-that-runs-on-cloudflares-free-plan-4mjh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
