---
title: ""Label Created" is not a location: modeling the pre-transit gap in shipment tracking"
slug: "label-created-is-not-a-location-modeling-the-pre-transit-gap-in-shipment-tracking"
author: "24hTrack"
source: "devto_webdev"
published: "Mon, 21 Sep 2026 04:12:57 +0000"
description: "If you build anything that shows shipment status to end users — an order page, a Slack alert, a support dashboard — the single most common complaint you will..."
keywords: "carrier, days, received, label, has, created, first, not"
generated: "2026-09-21T04:21:01.282510"
---

# "Label Created" is not a location: modeling the pre-transit gap in shipment tracking

## Overview

If you build anything that shows shipment status to end users — an order page, a Slack alert, a support dashboard — the single most common complaint you will get is some version of: "It has said Label Created for three days. Is it lost?" The answer is almost always no. But the way most tracking UIs model that first state makes the question inevitable. Here is how to model it better. What "Label Created" / "Info Received" actually is Every carrier has a status for "we received the shipment's data". The wording varies: USPS: Shipping Label Created, USPS Awaiting Item UPS: Shipper created a label, UPS has not received the package yet Royal Mail: We're expecting it Cross-border carriers: Electronic information received , Pre-shipment They all mean the same thing: the carrier has an electronic manifest record, not a parcel. No person or machine has touched the box. The first physical scan (acceptance, pickup, hub arrival) is a different event, and it can come hours or days later. The mistake is treating that first event like any other point on a timeline. It isn't. It carries no location and no evidence of movement. How long is the gap, really? We measured it on parcels tracked on the 24hTrack platform over the last 60 days: the time from the label/info event to the next real scan. Carrier Median 80% within Longer than 7 days USPS ~1 day ~3 days ~6% Yanwen Express (cross-border) ~3 days ~5 days ~15% Two practical consequences: A 24–48h gap is the median case, not an anomaly. Don't alert anyone at hour 24. The threshold must depend on the carrier. A cross-border consolidator that ships in batches has a legitimately longer gap than a domestic postal service. Modeling it in code Treat the pre-transit state as its own bucket, separate from "In Transit", and give it a carrier-aware staleness threshold: const PRE_TRANSIT = /label created|information received|info received|pre- ? shipment|awaiting item|expecting it/i ; function staleness ( events , carrier ) { const last = events [ 0 ]; // newest first const hours = ( Date . now () - Date . parse ( last . time )) / 36 e5 ; const preTransit = PRE_TRANSIT . test ( last . description ); // domestic ~7 days, cross-border ~10 days before a human should chase it const limit = preTransit ? ( isCrossBorder ( carrier ) ? 240 : 168 ) : 240 ; return { preTransit , hours , shouldChase : hours > limit }; } And in the UI, say what the state means instead of repeating the carrier's words: Info Received — the shop has sent the parcel's details. The carrier doesn't have the box yet. Most parcels get their first scan within a few days. That one sentence removes most "is it lost?" tickets. Two more traps "Info Received" with a local courier's name does not mean the parcel is in the country. A cross-border parcel can be manifested to its final-mile courier while it is still in a warehouse abroad. Location only starts at the first physical scan. The chase goes to the sender, not the carrier. Before acceptance the carrier literally has nothing. The merchant holds the contract and knows whether it was handed over. If you don't want to build the normalizer yourself 24hTrack (24htrack.com) is a free package tracker for 3,200+ carriers — paste any tracking number, the carrier is detected automatically, no sign-up. It groups every carrier's wording into one status list (Info Received, In Transit, Out for Delivery, Delivered, Alert) and exposes the same thing through a REST API and an MCP server for AI assistants. The carrier's original wording stays in the timeline, so you can show both. A plain-English guide to every status: https://www.24htrack.com/blog/tracking-status-meanings — and why tracking stops updating . FAQ Is "Label Created" a sign of a scam? No. It is the normal first step for nearly every parcel. Can the carrier speed it up? No — it doesn't have the parcel yet. Ask the sender whether it was handed over. When should a buyer worry? About 7 days with no new scan domestically, about 10 days cross-border. I work on 24hTrack. This post was written with AI assistance and edited by our team.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/support24htrack/label-created-is-not-a-location-modeling-the-pre-transit-gap-in-shipment-tracking-4gl4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
