---
title: "I spent a day building the button that lets people cancel and leave me"
slug: "i-spent-a-day-building-the-button-that-lets-people-cancel-and-leave-me"
author: "shaojie gong"
source: "devto_webdev"
published: "Tue, 04 Aug 2026 14:05:25 +0000"
description: "I spent a full day building the one button that makes it easy for people to stop paying me. On purpose. Here's why that's not as dumb as it sounds. NotebookB..."
keywords: "stripe, cancel, one, customer, you, they, portal, button"
generated: "2026-08-04T14:28:10.957346"
---

# I spent a day building the button that lets people cancel and leave me

## Overview

I spent a full day building the one button that makes it easy for people to stop paying me. On purpose. Here's why that's not as dumb as it sounds. NotebookBloom, my NotebookLM extension, has a Pro tier. Payment goes through a Stripe Payment Link — you click, you pay, you're Pro. Clean. Done in an afternoon. And for a while I thought that was the whole billing story. It isn't. A Payment Link is a one-way door. It's great at letting money in. It does nothing about letting people out. There was no cancel screen anywhere in my product. If you subscribed and then wanted to stop, your options were: email me and wait, or... call your bank. That second option is the one that should scare every solo founder. When a customer can't find how to cancel, they don't shrug and keep paying. They dispute the charge — a chargeback. And chargebacks don't just cost you that one payment plus a fee. Stripe watches your chargeback rate like a hawk. Cross a threshold and they can freeze or close your account. One angry user who couldn't find a cancel button is an annoyance. A pattern of them is an existential threat to the thing collecting all your revenue. So the cancel button isn't a courtesy to users. It's insurance on my own business. The clean way to do it is Stripe's Customer Portal — a hosted page where a customer can cancel, change their card, or download invoices, none of which I have to build. I just have to send the right customer to the right portal session. That "right customer" part is where the actual work was. The portal link has to be generated per-customer, server-side, and I had to make sure user A can't open user B's billing portal. My flow: the extension sends the user's Google token to my Cloudflare Worker. The worker verifies that token with Google to get the real email — the client never just says "I'm bob@gmail" and gets believed, because that's how you'd let anyone cancel anyone's subscription. With the verified email, the worker looks up the Stripe customer id, asks Stripe for a one-time portal session, and hands the URL back. The extension opens it in a new tab. One "Manage subscription" button in settings, and everything else is Stripe's problem. The loop closes on its own: user cancels in the portal, Stripe fires a subscription.deleted webhook, my worker flips their record to inactive, and the next time the extension revalidates, they're back to free. I don't touch anything. There was one detail I got wrong at first, mentally. I assumed "cancel" meant "Pro turns off now." It doesn't — Stripe defaults to canceling at the end of the paid period. Which is correct! They paid for the month, they get the month. So a canceled-but-still-active subscription is a real state I had to handle: the extension now shows "Pro access until [date] — won't renew" instead of just yanking it. Small thing, but it's the difference between feeling respected and feeling robbed. The reframe I'm keeping: the exit is part of the product. I spent the first afternoon on the part that takes money and thought I was done. The part that lets people leave gracefully turned out to matter more — to my Stripe account's health, and to whether anyone trusts me enough to subscribe in the first place. Did anyone else find out the hard way that "accept payments" and "handle subscriptions" are two completely different amounts of work? — building NotebookBloom in public, #14

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shaojie/i-spent-a-day-building-the-button-that-lets-people-cancel-and-leave-me-562c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
