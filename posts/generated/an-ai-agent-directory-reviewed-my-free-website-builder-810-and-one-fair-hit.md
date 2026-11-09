---
title: "An AI agent directory reviewed my free website builder: 8/10, and one fair hit"
slug: "an-ai-agent-directory-reviewed-my-free-website-builder-810-and-one-fair-hit"
author: "TimofeUS"
source: "devto_webdev"
published: "Mon, 09 Nov 2026 15:37:55 +0000"
description: "TapToAgent , a directory of free AI agents, just listed openconstructor , my free, open-source AI interface builder, and gave it 8/10 . What I like about the..."
keywords: "free, one, you, page, directory, open, account, can"
generated: "2026-11-09T15:46:00.539809"
---

# An AI agent directory reviewed my free website builder: 8/10, and one fair hit

## Overview

TapToAgent , a directory of free AI agents, just listed openconstructor , my free, open-source AI interface builder, and gave it 8/10 . What I like about their directory is one simple rule: if a tool makes you create an account before you can use it, it doesn't get listed. That's exactly the wall I tore down a week ago. My first launch got hundreds of visitors and two accounts, because the free AI was hidden behind a sign-in form. Now you open the site and type a request, no email, no key. Getting listed by a directory that requires that felt like confirmation it was the right call. What they tested The reviewer went in signed out and asked for a coffee shop landing page: ~36 seconds to a full page: hero, menu with prices, opening hours; ~25 seconds for a follow-up edit: change one price. They also called it the only interface builder in the directory, which I'll happily take. The fair criticism Style can drift between generations. They asked to change one price , and the page came back with prices and hours intact, but a noticeably different look. That's a real bug in how I prompted edits: the model was told to "return the complete updated element", and small free models read that as "redesign it while you're at it". Fixed the same day. Edits now come with an explicit rule: an update is an edit, not a redesign. Copy the current code, change only the lines the request is about, and keep the class names, colors, fonts, spacing and photos everywhere else. Asked to change one price? You get the same page with one different number. The other notes are trade-offs I chose on purpose: 3 free generations a day without an account (20 with a free one). It runs on free open models on Cloudflare, and that cap is what keeps it free for everyone. Other models need your own key. If you have one, there's no cap at all. Saving to the cloud and publishing need a free account. Building and exporting don't. Since the review: it can browse the web One more thing that shipped this week: the AI can now look things up. Ask about something current, or paste a link ("make a landing page in the style of https://…"), and it searches or reads the page before building. You watch it happen in the chat as exploring internet . Try it without an account: openconstructor.pw . The full review is on TapToAgent . The whole project is free and open source. If you like it, a ⭐ on GitHub helps a lot: it's how other people find the project, and it keeps me shipping. Thanks!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/timofeus_248d45d3902a91a3/an-ai-agent-directory-reviewed-my-free-website-builder-810-and-one-fair-hit-572b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
