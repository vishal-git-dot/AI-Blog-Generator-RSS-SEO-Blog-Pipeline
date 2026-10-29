---
title: "I read ~150 public Razorpay webhook handlers. At least 9 would process the same payment twice."
slug: "i-read-150-public-razorpay-webhook-handlers-at-least-9-would-process-the-same-payment-twice"
author: "Pritom Mazumdar"
source: "devto_python"
published: "Thu, 29 Oct 2026 12:24:29 +0000"
description: "Razorpay delivers webhooks "at least once". Its own docs say the same event can arrive more than once and tell you to dedupe on x-razorpay-event-id . I wante..."
keywords: "razorpay, event, payment, webhook, same, handler, side, req"
generated: "2026-10-29T12:39:59.114631"
---

# I read ~150 public Razorpay webhook handlers. At least 9 would process the same payment twice.

## Overview

Razorpay delivers webhooks "at least once". Its own docs say the same event can arrive more than once and tell you to dedupe on x-razorpay-event-id . I wanted to see how often real code actually does that. Method. I pulled 247 public Python / JS / TS files on GitHub that reference Razorpay webhook events. A keyword scan flagged 48 candidates, and each one was then reviewed line by line. About 148 files contain a real webhook handler; the rest are helpers, schemas or client-side "verify payment" endpoints. I only counted a handler if delivering the same event twice would demonstrably run a non-idempotent side effect twice. Where idempotency could come from a database constraint I couldn't see, I marked it unclear rather than broken. (I'm being strict here because my first keyword-only pass said "1 in 5". When I read the code, most of those were false alarms, e.g. a wallet field that just stores the payment method.) What I found At least 9 of ~148 handlers (6%) run a side effect again when the same webhook is redelivered. Another 7 are unclear. (Only the 48 flagged files were checked for this, so the real number can only be higher.) 5 of those 9 change money-like values: user.wallet = (user.wallet || 0) + 100 on every payment.captured . Razorpay retries, and the user gets 200 coins. invoice.amount_paid_paise += amount and a customer "total recovered" counter, both incremented on every delivery. A WorkerPayout row created on every payment.captured . That's a duplicate payout record, and this handler doesn't verify signatures either. 9 handlers (6%) never verify the webhook signature at all. Anyone who finds the URL can POST a fake payment.captured . Several more verify only when the header or secret is present, so leaving the secret unset silently disables the check. A common, subtler pattern: computing the HMAC over JSON.stringify(req.body) instead of the raw request body. It works until something re-serializes the JSON differently, and then valid webhooks start failing. 6% doesn't sound like much until you remember these are the people who publish their payment code. And it only takes one retry storm to double-pay every affected user. Why tests don't catch it. Everyone tests the happy path once in Razorpay test mode. Nobody fires the same event three times, or sends events out of order. What I built. carbon-layer is an open-source CLI that fires realistic, correctly signed Razorpay, Stripe, Cashfree, Juspay and Hyperswitch webhooks at your local endpoint, including retries with the same X-Razorpay-Event-Id , out-of-order delivery, and bad signatures. A non-idempotent handler still answers 200, so it also checks the side effect itself: give it any command that counts what your handler does, and it compares before and after. pip install -U carbon-layer carbon run dispute-spike --provider razorpay \ --webhook-url http://localhost:8000/webhooks --webhook-secret $SECRET \ --webhook-repeat 3 --webhook-order random \ --verify-cmd "psql -tAc 'select count(*) from wallet_credits'" Against a handler written like the wallet one above: FAIL: duplicate processing: payment.captured: 200 unique events caused 600 side effects; handler is not idempotent The same handler with an event-id check gives PASS: each event processed exactly once . No gateway account needed. Repo: github.com/Pritom14/carbon-layer The fix most of these handlers need: record x-razorpay-event-id in a table with a UNIQUE constraint, in the same transaction as the side effect. If the event is already there, return 200 and do nothing: create table processed_webhooks ( event_id text primary key , received_at timestamptz default now ()); app . post ( ' /webhooks/razorpay ' , express . raw ({ type : ' application/json ' }), async ( req , res ) => { if ( ! Razorpay . validateWebhookSignature ( req . body . toString (), req . get ( ' x-razorpay-signature ' ), SECRET )) return res . sendStatus ( 400 ); // verify the RAW body, not JSON.stringify(req.body) const eventId = req . get ( ' x-razorpay-event-id ' ); const event = JSON . parse ( req . body ); await db . tx ( async ( t ) => { const { rowCount } = await t . query ( ' insert into processed_webhooks (event_id) values ($1) on conflict do nothing ' , [ eventId ]); if ( rowCount === 0 ) return ; // duplicate delivery: already handled if ( event . event === ' payment.captured ' ) await creditWallet ( t , event . payload . payment . entity ); }); res . sendStatus ( 200 ); }); Doing the insert and the side effect in one transaction matters: if the credit fails, the event id rolls back too, and Razorpay's retry gets processed properly. (Repo names are deliberately left out. If you want to know whether yours was in the scan, DM me and I'll send you the specific finding privately.)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pritom14/i-read-150-public-razorpay-webhook-handlers-at-least-9-would-process-the-same-payment-twice-1bnb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
