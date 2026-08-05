---
title: "Why Storing a TRACES Establishment Code as a Static Field Is a Data Modelling Bug"
slug: "why-storing-a-traces-establishment-code-as-a-static-field-is-a-data-modelling-bug"
author: "Kristi Hampson"
source: "devto_ai"
published: "Wed, 05 Aug 2026 08:39:25 +0000"
description: "The bug Most ERP setups treat a TRACES establishment code the way they treat a VAT number. One field on the supplier record, entered once, trusted forever. T..."
keywords: "code, traces, establishment, field, one, string, timestamp, shipment"
generated: "2026-08-05T08:43:39.000072"
---

# Why Storing a TRACES Establishment Code as a Static Field Is a Data Modelling Bug

## Overview

The bug Most ERP setups treat a TRACES establishment code the way they treat a VAT number. One field on the supplier record, entered once, trusted forever. That model is wrong, because the value is not the fact. The code is an identifier. The fact you actually depend on is the approval status of that identifier on a given date, for a given activity category. Those are different objects, and collapsing them into one field guarantees stale data. What the code represents A TRACES establishment code is the approval number the EU assigns to a facility authorised to produce or handle animal-origin products. National competent authorities propose the facility, DG SANTE reviews it, and the European Commission publishes the listing through TRACES NT. A useful primer on what a TRACES establishment code is sets out that chain and where the public lists sit. A better shape supplier establishment_code (string) establishment_check code (string) activity_category (enum) checked_at (timestamp) listed (boolean) matched_name (string) consignment_id (fk) Now status is an event with a timestamp, not an attribute. You can answer "was this listed on the ship date" without guessing. Why the timestamp matters Establishments get suspended after audits and delisted after disease outbreaks, with no notification to the trader. A code valid in one month can be refused the next. Without checked_at, a checked shipment and an unchecked shipment look identical in your database. Where to put the check Pre-shipment, inside the workflow, ideally through an API call from the ERP or TMS rather than a human opening a portal tab. Watch a demo

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kristi-hampson/why-storing-a-traces-establishment-code-as-a-static-field-is-a-data-modelling-bug-1dd1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
