---
title: "Amazon Scored 43/100 on a Website Audit: The Pre-Launch Checklist That Catches the Same Misses"
slug: "amazon-scored-43100-on-a-website-audit-the-pre-launch-checklist-that-catches-the-same-misses"
author: "ContentMation"
source: "devto_webdev"
published: "Thu, 08 Oct 2026 22:39:51 +0000"
description: "A free audit tool graded more than 500 well known websites on speed, SEO, accessibility and security. A few of the results: Site Score Grade Fitbit 95 A+ Sep..."
keywords: "page, every, you, one, your, minutes, security, free"
generated: "2026-10-08T23:09:13.584521"
---

# Amazon Scored 43/100 on a Website Audit: The Pre-Launch Checklist That Catches the Same Misses

## Overview

A free audit tool graded more than 500 well known websites on speed, SEO, accessibility and security. A few of the results: Site Score Grade Fitbit 95 A+ Sephora 95 A+ Vercel 94 A+ LinkedIn 75 B YouTube 66 B Stripe 60 C Shopify 55 C Nike 44 D PayPal 44 D Amazon 43 D GitHub 40 D Source: the public score list at nexusbro.com/scores , read on 8 October 2026. Big teams with big budgets still ship pages with missing tags, heavy images and accessibility gaps. If you ship without a QA person, that is good news: the basics are exactly where a small team can win. Here is a checklist you can run in about an hour before any launch. 1. SEO basics (10 minutes) One unique <title> per page, around 60 characters or less. A meta description that reads like an ad, around 150 characters. A canonical tag that points at the page itself. A sitemap.xml that lists every page you want indexed, and a robots.txt that does not block it. One <h1> per page that says what the page is about. Organization structured data (JSON-LD) with your name, logo and contact details. Quick test: open the page source and search for <title> , rel="canonical" and application/ld+json . If one is missing, add it before launch. 2. Speed (15 minutes) Run Lighthouse in Chrome DevTools on your two most important pages, in mobile mode. Aim for Google's "good" Core Web Vitals: LCP at 2.5 seconds or less, CLS at 0.1 or less, INP at 200 ms or less. Compress your hero image, serve WebP or AVIF, and set width and height on every image so the layout does not jump. Defer any third party script that is not needed for the first screen. 3. Mobile (10 minutes) Open the site at 320 px wide. Nothing should scroll sideways. Make buttons and links easy to tap: around 44 to 48 px is a safe target. Use the right input types ( email , tel , number ) so phones open the right keyboard. 4. Accessibility (15 minutes) Alt text on every meaningful image. Body text contrast of at least 4.5:1 (WCAG AA). A visible label on every form field. Every button reachable with the Tab key, with a visible focus ring. 5. Security (10 minutes) HTTPS everywhere, and plain HTTP redirects to HTTPS. No API keys or secrets in client JavaScript. Search your built bundle for sk_ , secret and apiKey . Basic headers: Strict-Transport-Security , Content-Security-Policy , X-Content-Type-Options and Referrer-Policy . 6. Links and forms (10 minutes) Click every link in your header and footer. Submit every form once with real data and once with empty fields. Both should behave. Make sure your 404 page exists and links back home. Automate the first pass Doing all of this by hand for every page gets old fast. Two free tools take the first pass for you: Lighthouse , built into Chrome, for speed and accessibility on one page at a time. nexusbro.com , which runs 125+ checks across SEO, speed, security and mobile on any URL, free with no signup, and hands back one fix prompt you can paste into Cursor, Claude Code, Lovable or Bolt. Fix the top three issues, run it again, then ship. One more check: can people find you? A clean site still needs visitors. The same report card idea works for marketing: the free score at contentmation.com/score rates six channels (SEO, social, content, technical, directory and email) and shows your weakest one. On that list Zapier scores 90 and Stripe 78, and both lose points on the same channel: directory, where a Google Maps or review site link, contact details in structured data and a visible phone number and street address count. None of it needs a budget. Run the checklist, fix the basics, and you will already be ahead of a surprising number of famous sites.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/contentmation/amazon-scored-43100-on-a-website-audit-the-pre-launch-checklist-that-catches-the-same-misses-1a86

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
