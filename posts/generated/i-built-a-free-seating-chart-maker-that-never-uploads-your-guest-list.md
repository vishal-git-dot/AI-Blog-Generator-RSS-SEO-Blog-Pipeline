---
title: "I built a free seating chart maker that never uploads your guest list"
slug: "i-built-a-free-seating-chart-maker-that-never-uploads-your-guest-list"
author: "Dejan Stajic"
source: "devto_webdev"
published: "Sun, 22 Nov 2026 19:08:29 +0000"
description: "I'm Dejan. I built a free seating chart maker and I want to be upfront about that. This post is about why I kept the guest list in the browser, and how the t..."
keywords: "list, table, chart, you, can, seating, guest, name"
generated: "2026-11-22T19:16:57.017285"
---

# I built a free seating chart maker that never uploads your guest list

## Overview

I'm Dejan. I built a free seating chart maker and I want to be upfront about that. This post is about why I kept the guest list in the browser, and how the tool actually works. Wedding and event seating is a messy puzzle: couples who should stay together, relatives who should not sit at the same table, meal counts for the caterer, and a floor plan you can print. Most tools I looked at want an account, or they upload the list to a server. I didn't want a guest list leaving the device at all. The tool is here: https://dejoski.github.io/seating-chart-maker/ It runs in the browser. There is no sign-up, no ads, and no guest limit. The list is stored only in the browser's local storage on that device and is never uploaded. If you need the chart on another device, use Backup (.json) and Restore. How I use it: Paste people in, one name per line, or paste columns from a spreadsheet (Name, Group, Meal, Notes). Write couples as "Alex & Sam Lee" and plus-ones as "Jordan Park +1" so they stay linked. Set up tables. There are quick layouts (rounds of 8 or 10, long tables, a head table, classroom rows, pairs, pods, and U-shape), or you can add tables one at a time with 1–20 seats. Drag a table by its name bar to move it around the room. Add rules. Keep two people together or apart, and lock anyone whose seat is already decided. Auto-arrange, then fine-tune. Auto-arrange fills tables while respecting every rule it can, keeps couples together, and puts people from the same group near each other. Drag names to adjust. On a phone, tap a name, then tap a table. Export a PDF (floor plan, a by-table list, and an A–Z "find your seat" list), a PNG, or a caterer CSV with meals by table. If the rules can't all be met, the tool keeps the arrangement with the fewest broken rules and lists each conflict in red, so you can add a table, change seat counts, or loosen a rule. Wedding, classroom, and event modes each keep their own chart, so switching modes doesn't overwrite anything. For more charts in the same mode, save a backup file for each one. That's the whole product: a free, no-account chart you can paste, arrange, and print, with the list staying on your machine. If you try it and something is awkward, I'd like to hear it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dejan_stajic_28050c35cb79/i-built-a-free-seating-chart-maker-that-never-uploads-your-guest-list-5gee

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
