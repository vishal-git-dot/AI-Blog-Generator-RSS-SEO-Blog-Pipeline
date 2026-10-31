---
title: "I built a prize wheel for our perfume shops that only spins once you actually follow us on Instagram"
slug: "i-built-a-prize-wheel-for-our-perfume-shops-that-only-spins-once-you-actually-follow-us-on-instagram"
author: "Brahim"
source: "devto_python"
published: "Sat, 31 Oct 2026 20:21:36 +0000"
description: "Result first: customers in our perfume shops scan a QR code on a flyer, follow our Instagram account, type the first letters of their username, tap their own..."
keywords: "you, follow, instagram, account, customer, our, their, username"
generated: "2026-10-31T21:15:20.726049"
---

# I built a prize wheel for our perfume shops that only spins once you actually follow us on Instagram

## Overview

Result first: customers in our perfume shops scan a QR code on a flyer, follow our Instagram account, type the first letters of their username, tap their own profile picture, and the prize wheel unlocks. The follow check is automatic and takes about 2–3 seconds, even for private accounts that followed a few seconds earlier. The question I was trying to answer: can a small shop check "did this person really follow us?" without asking the cashier to look at the customer's phone, and without the customer logging in with Instagram? What didn't work I was skeptical. The official Graph API doesn't tell you who follows you. So I went through the usual list: Instagram DMs: technically possible, but way too much friction for someone standing at the counter. Logging in with my own account and cookies: fragile, and a good way to get the account flagged. A couple of RapidAPI scrapers: rate-limited (429s), or they return followers in a random cached order, so someone who followed 10 seconds ago isn't in the list. An Apify actor that advertised a query parameter: it returned the same first page whatever I searched for. A SaaS wheel tool: it doesn't verify the follow at all, it just trusts the customer. What worked What finally worked is a "search inside followers" endpoint. I used HikerAPI . You give it the account's user id and a partial username, and it returns the matching followers with their profile pictures. That fits the UX perfectly: the customer types 3–4 letters, sees up to 5 profile pictures, and taps their own. import requests headers = { " x-access-key " : " YOUR_KEY " } r = requests . get ( " https://api.hikerapi.com/v1/user/search/followers " , params = { " user_id " : " OUR_ACCOUNT_ID " , " query " : " brah " }, headers = headers , ) for u in r . json (): print ( u [ " username " ], u [ " profile_pic_url " ]) Setup: a WordPress plugin on our existing site. The call happens server-side only, so the key never reaches the browser, and results are cached for 60 seconds so a customer typing letter by letter doesn't burn a request on every keystroke. In practice it's 2–4 requests per player, at about $0.001 each. Honest limitations The search is partial, so I match the tapped profile exactly on the server. Otherwise someone could type "a" and pick a stranger. It proves the account follows you now . Nothing stops someone from unfollowing afterwards. For a one-shot prize that's acceptable. It relies on a third-party API. If it's down, the game falls back to "show your phone to the seller", which is what shops were doing before anyway. I wouldn't use this to collect data. We only store the username and the result of the check. Curious whether others have solved "verify a social action" for in-store promos differently, especially without Instagram login. Did anyone find something lighter than this?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/brahim_gacem_03454acc8cdc/i-built-a-prize-wheel-for-our-perfume-shops-that-only-spins-once-you-actually-follow-us-on-instagram-11hh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
