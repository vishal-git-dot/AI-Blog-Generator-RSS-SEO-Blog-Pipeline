---
title: "Selling event tickets on WooCommerce without the per-ticket tax"
slug: "selling-event-tickets-on-woocommerce-without-the-per-ticket-tax"
author: "Rebel Studios"
source: "devto_webdev"
published: "Tue, 15 Sep 2026 11:19:28 +0000"
description: "If you run events and a WordPress site, the ticketing math is quietly brutal. Eventbrite takes roughly $1.79 + 3.7% per ticket . Sell 300 tickets at $40 and ..."
keywords: "ticket, you, woocommerce, ticketing, own, tickets, your, already"
generated: "2026-09-15T11:28:03.174942"
---

# Selling event tickets on WooCommerce without the per-ticket tax

## Overview

If you run events and a WordPress site, the ticketing math is quietly brutal. Eventbrite takes roughly $1.79 + 3.7% per ticket . Sell 300 tickets at $40 and you've handed over ~$500 before your own payment processor takes its cut. And the "free" WordPress ticketing plugins mostly aren't — the common pattern is a free RSVP tier with the actual paid-ticket feature locked behind a $75+ upgrade, sometimes just to turn on Stripe. Here's the thing: if you already run WooCommerce, you don't need any of that. Why WooCommerce-native ticketing avoids the fees WooCommerce already has your payment gateway configured — Stripe, PayPal, whatever you use. It already handles tax, currency, receipts, and refunds. A ticket is just a product. So "event ticketing" doesn't need to be a separate platform with its own cut; it can be a thin layer on top of the checkout you already run. That changes the fee structure completely: No per-ticket platform fee. You pay your normal payment-processor rate (~2.9% 30¢) and nothing else. On 300 tickets at $40 that's the difference between keeping ~$11,600 vs ~$11,100 — and none of it routed through a third party. The money lands in your own account , same as every other WooCommerce order — not held by a ticketing company on their payout schedule. No forced paywall on payments. Taking money should not itself be the premium feature. What "good enough" ticketing actually needs For the vast majority of organizers — a workshop, a supper club, a meetup, a class series — the real requirements are small: Put a price on an event and take payment through your existing checkout. Issue a QR-coded ticket by email , automatically, once the order is paid (not when someone abandons checkout — that should never issue a ticket or eat a seat). Scan the QR at the door to check people in — no separate hardware, no app. Optionally, multiple ticket types — General / VIP / Early bird — each with its own price and its own capacity that sells out independently. An attendee list and CSV export. That's it. Seat maps and reserved seating are a genuinely bigger problem, but most organizers don't need them and shouldn't pay for a platform that assumes they do. The build/buy version I build small WordPress tools, and I made exactly this so I'd stop recommending Eventbrite to people who already had WooCommerce: Event Tickets & Registration . The free plugin does unlimited RSVP events with QR tickets and door check-in; the Pro add-on adds paid tickets through your own WooCommerce checkout and multiple ticket types — one-time price, no per-ticket cut, ever . It's a separate download and not required; the free tier stands on its own. But the real point stands whether you use it or not: if you're on WooCommerce, you're already paying for the infrastructure ticketing platforms resell back to you. Stop paying the per-ticket tax on top.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rebel_studios/selling-event-tickets-on-woocommerce-without-the-per-ticket-tax-33ek

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
