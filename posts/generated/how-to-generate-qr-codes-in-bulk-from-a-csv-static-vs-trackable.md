---
title: "How to Generate QR Codes in Bulk from a CSV (Static vs. Trackable)"
slug: "how-to-generate-qr-codes-in-bulk-from-a-csv-static-vs-trackable"
author: "Ryan Bame"
source: "devto_python"
published: "Wed, 14 Oct 2026 21:12:44 +0000"
description: "How to Generate QR Codes in Bulk from a CSV (Static vs. Trackable) You have a spreadsheet. Maybe it's 50 product SKUs, 500 rental units, or 5,000 asset tags...."
keywords: "you, codes, code, url, csv, bulk, static, row"
generated: "2026-10-14T21:28:09.485800"
---

# How to Generate QR Codes in Bulk from a CSV (Static vs. Trackable)

## Overview

How to Generate QR Codes in Bulk from a CSV (Static vs. Trackable) You have a spreadsheet. Maybe it's 50 product SKUs, 500 rental units, or 5,000 asset tags. Each row needs its own QR code. Generating them one at a time in a web form is a non-starter, so the question becomes: how do you turn a column of URLs into a folder of QR codes without doing it by hand? There are two real answers, and which one you pick matters more than the tooling. Option 1: Static codes, generated locally (Python) If the codes are truly fixed — the URL behind each one will never change and you don't need scan data — you can generate them yourself in a few lines. Here's the whole thing with the qrcode library: import csv import qrcode # input.csv: # name,url # unit-101,https://example.com/units/101 # unit-102,https://example.com/units/102 with open ( " input.csv " , newline = "" ) as f : for row in csv . DictReader ( f ): img = qrcode . make ( row [ " url " ]) img . save ( f " out/ { row [ ' name ' ] } .png " ) Run it, and out/ fills with one PNG per row. Want SVG for print? Swap in the qrcode.image.svg factory: import qrcode.image.svg img = qrcode . make ( row [ " url " ], image_factory = qrcode . image . svg . SvgImage ) img . save ( f " out/ { row [ ' name ' ] } .svg " ) This is genuinely fine for a lot of jobs. It's free, it runs offline, and the codes work forever. If that's your use case, stop here — you don't need a platform. But read the next paragraph before you print 5,000 of them. The problem with static bulk codes A static QR code encodes the destination URL directly into the pixels . That has two consequences that only show up after the codes are in the wild: You can't change where they point. The day a URL changes — a domain migration, a restructured path, a campaign that moved — every printed code pointing at the old URL is dead. On a batch of 5,000, that's 5,000 reprints. You get zero data. A static code is a dumb pointer. You will never know how many were scanned, when, where, or on what device. For asset tags that might be acceptable; for anything marketing- or operations-facing, flying blind at scale is expensive. The batch loop above can't fix either problem, because the limitation is in the format, not the code. Option 2: Dynamic codes, generated in bulk from the same CSV A dynamic QR code encodes a short redirect URL instead of the final destination. The pixels point at something like qrch.am/a1b2c3 , which 301s to wherever you want — and you can repoint it later without touching the printed code. Every scan is logged on the way through. The bulk workflow is the same shape as the Python script — CSV in, codes out — except the output is a set of trackable, editable codes instead of flat images. Two ways to drive it: Upload the CSV in the dashboard. Drop your spreadsheet into the bulk QR code generator , map the URL column, and it mints one dynamic code per row and hands you a ZIP of print-ready PNG/SVG files. This is the fastest path for a one-off batch. Or hit the API for a repeatable pipeline. If the batch is part of a system — a nightly job tagging new inventory, a per-tenant onboarding step — generate them programmatically: curl -X POST https://api.qrchameleon.com/v1/qr/bulk \ -H "Authorization: Bearer qrc_your_api_key" \ -H "Content-Type: application/json" \ -d '{ "items": [ { "name": "unit-101", "url": "https://example.com/units/101" }, { "name": "unit-102", "url": "https://example.com/units/102" } ] }' Each returned code is dynamic, so a later PATCH to its destination updates where the physical code points — no reprint. (Exact request/response schema and rate limits are in the API docs — treat the snippet above as the shape, not the spec.) Which should you use? Static (local script) Dynamic (bulk upload / API) Cost Free Free tier, paid at volume Works offline Yes No (needs the redirect) Editable after printing No Yes Scan analytics None Per-code Best for Fixed, fire-and-forget codes Anything you'll track or change Rule of thumb: if the batch is permanent and you don't care about data , the 10-line Python script is the right tool and you should use it. If the codes represent anything you might reprint, repoint, or measure — products, properties, campaigns, assets in a system of record — generate them as dynamic codes so a URL change is a one-line edit instead of a reprint run. The spreadsheet-to-codes step is easy either way. The decision that actually costs money is static vs. dynamic — make that one on purpose. Generating a batch right now? The bulk QR code generator takes a CSV and returns print-ready dynamic codes with scan tracking built in — free to start, no credit card.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ryan_bame_84/how-to-generate-qr-codes-in-bulk-from-a-csv-static-vs-trackable-15lm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
