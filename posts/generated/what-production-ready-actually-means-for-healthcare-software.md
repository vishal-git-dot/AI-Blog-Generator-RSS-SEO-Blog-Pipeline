---
title: "What "production-ready" actually means for healthcare software"
slug: "what-production-ready-actually-means-for-healthcare-software"
author: "Nazmul Huda"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 04:40:44 +0000"
description: "In most apps, a small bug is an inconvenience. In healthcare software, the same bug can mean a wrong dose, a missed warning, or a bill that's silently off. S..."
keywords: "day, early, not, same, what, healthcare, software, most"
generated: "2026-06-15T05:01:58.097610"
---

# What "production-ready" actually means for healthcare software

## Overview

In most apps, a small bug is an inconvenience. In healthcare software, the same bug can mean a wrong dose, a missed warning, or a bill that's silently off. So before we let BioMedixAI — an AI-native healthcare platform — anywhere near a launch, we spent a full day doing nothing but trying to break it. Here's what that day actually looked like, and the bugs that taught us the most. 1. Vital-sign thresholds, re-aligned to NEWS2 Early on, our "normal vs abnormal" vital-sign bands were reasonable but not standard . In clinical software, "reasonable" isn't good enough. We re-aligned every threshold to NEWS2 (National Early Warning Score) — the scoring system hospitals use worldwide to catch a deteriorating patient early. Pulse, blood pressure, respiratory rate, SpO₂, temperature: each now sits in the exact band that produces the correct early-warning flag. Lesson: in a regulated domain, don't invent your own constants. Find the published standard and match it exactly — then write tests that assert the boundaries ( spo2 === 91 should escalate, 92 should not). 2. Timezones will betray you at midnight Several of our "per day" features (bed-day billing accrual, daily reports, sequence-number year prefixes) were quietly bucketing by UTC . For a facility in UTC+6, that means a day "closes" six hours early — and a bill can land on the wrong calendar day. We moved everything to roll over at each facility's local midnight, DST included. The fix isn't hard; noticing it is. The only reliable way we found to catch these is to run the logic with the clock pinned to an awkward time (23:30 local, last day of the month) and watch what bucket the row lands in. 3. Concurrency: the database is your last line of defense Two requests admitting the same patient to the same bed at the same millisecond shouldn't both succeed. App-level checks ( SELECT then INSERT ) lose this race. The fix is a partial unique index that lets the DB reject the second write: one bed → at most one ACTIVE admission, enforced in Postgres, not in Node. Application guards are for friendly error messages. The database is for truth. 4. Access control is correctness, not a feature Part of the audit was purely adversarial: log in as role X, try to read role Y's data, and confirm we get a hard stop. A few endpoints were returning data they shouldn't have. We also standardized on returning 404, not 403 , for cross-tenant IDs — a 403 quietly confirms the record exists , which is its own small leak. Takeaway None of this makes a good screenshot. There's no "we did the security and correctness properly" demo. But this is the work that earns a system the right to stand next to someone's health data. We'd rather be slow and correct than fast and sorry. Building BioMedixAI in public. More notes as we go.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nazmulhd10/what-production-ready-actually-means-for-healthcare-software-2ei3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
