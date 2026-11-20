---
title: "Stripe trials and Meta: how a trial-to-paid sale reaches your ads"
slug: "stripe-trials-and-meta-how-a-trial-to-paid-sale-reaches-your-ads"
author: "FloorSync"
source: "devto_webdev"
published: "Fri, 20 Nov 2026 15:02:17 +0000"
description: "Disclosure: I work on FloorSync, a small tool that sends Stripe sales and renewals to Meta and GA4. This guide works with or without it. You run a Stripe bus..."
keywords: "meta, stripe, paid, you, invoice, trial, event, send"
generated: "2026-11-20T15:10:11.461313"
---

# Stripe trials and Meta: how a trial-to-paid sale reaches your ads

## Overview

Disclosure: I work on FloorSync, a small tool that sends Stripe sales and renewals to Meta and GA4. This guide works with or without it. You run a Stripe business with a free trial and Meta ads. The ad gets a click, the person starts a trial, and a week later Stripe charges them. Meta often shows the ad as a failure, even though the sale was real. Here is how to make the trial-to-paid sale reach Meta, step by step. 1. Know which Stripe event is which A trial has two moments: checkout.session.completed fires when the person starts the trial. The amount is usually 0. In Meta this is a Lead or a StartTrial, not a Purchase. invoice.paid fires when the first real charge succeeds, after the trial. This is the money. It is also the event for every renewal after. If you send only checkout.session.completed as a Purchase, Meta sees a zero-value sale. If you send nothing for invoice.paid , Meta never sees the paid conversion. Send both, with different event names. 2. Save fbc and fbp at checkout Meta matches a server event to an ad click with the fbc cookie (from the fbclid in the URL) and fbp . The paid invoice happens days later, when the browser is gone. So save them when the person is still on your page: const session = await stripe . checkout . sessions . create ( { mode : 'subscription' , subscription_data : { trial_period_days : 7 , metadata : { fbc , fbp } } , metadata : { fbc , fbp } , // ... } ) ; Put them on the subscription metadata, not only on the session. Later invoices point to the subscription, so you can read them back when invoice.paid arrives. Also send a hashed email if you have one. 3. Send the right event time and value For the trial start, use the session's created time. For the paid invoice, use the invoice's status_transitions.paid_at , and amount_paid as the value with the invoice currency. Meta's Conversions API accepts events up to 7 days old, so send within hours, not weeks. 4. Dedupe on Stripe IDs Stripe retries webhooks. If you send twice, Meta may count twice. Use the Stripe event id ( evt_... ) or the invoice id ( in_... ) as the event_id you send. For GA4, use the invoice id as transaction_id . Keep a small table of ids you have already sent and skip repeats. 5. Expect a gap, and know why Even when it all works, Meta will not match Stripe exactly: Meta attributes a purchase to an ad only inside its click window (7 days by default). A trial that converts on day 7 or later after the click can fall outside it. Some people have no fbc , so Meta can only match by email, and not always. Some paid invoices come from people who never came from an ad. A gap is normal. A gap that is huge, or a Meta count of zero, means events are missing. 6. Check a closed month Once a month is over: In Stripe, list invoices with status paid for the month. Total the count and the amount. In Meta Events Manager, count Purchase events (or your renewal event) for the same dates, and the value. Compare. Look at which invoice ids are missing in Meta. Those are the ones to fix, usually missing fbc , a wrong event name or a webhook that failed. Do this once a month and you will catch a broken sync early. Try it without building it If you want to see what Meta and GA4 would get from your own Stripe event, the free dry run needs no sign-up: https://floorsync.towers.app/?from=devto2 More how-tos on Stripe sales and renewals missing in Meta and GA4: https://floorsync.towers.app/guides/?from=devto2

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/floorsync/stripe-trials-and-meta-how-a-trial-to-paid-sale-reaches-your-ads-5921

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
