---
title: "I got tired of rewriting the same Indian utilities. So I built bharatutils."
slug: "i-got-tired-of-rewriting-the-same-indian-utilities-so-i-built-bharatutils"
author: "Ansuman Jaiswal"
source: "devto_python"
published: "Mon, 15 Jun 2026 04:58:36 +0000"
description: "Every project. Same story. Format salary as ₹15 L instead of 1,500,000. Validate a GSTIN. Parse "Flat 302, Nr. SBI ATM, MG Road, Pune - 411001" into somethin..."
keywords: "bharatutils, every, nan, not, one, indian, number, import"
generated: "2026-06-15T05:01:58.093114"
---

# I got tired of rewriting the same Indian utilities. So I built bharatutils.

## Overview

Every project. Same story. Format salary as ₹15 L instead of 1,500,000. Validate a GSTIN. Parse "Flat 302, Nr. SBI ATM, MG Road, Pune - 411001" into something a database can understand. Check if today is a public holiday. Every Indian developer has written these functions. Most of us have written them five times across five projects-slightly differently each time, untested, quietly breaking on the first NaN in a pandas column. I got tired of it. So I built bharatutils . What it does pip install bharatutils 💰 Indian number formatting from bharatutils import format_inr , indian_commas format_inr ( 1500000 ) # '₹15.0 L' format_inr ( 50000000 ) # '₹5.0 Cr' format_inr ( " 15,00,000 " ) # handles messy strings format_inr ( float ( " nan " )) # 'N/A' - never crashes on pandas NaN indian_commas ( 15000000 ) # '1,50,00,000' - banker's style 🧾 GST validation with a real checksum Most validators only check the format pattern. bharatutils implements the official mod-36 check-digit algorithm - meaning a single wrong character in a GSTIN fails validation, exactly as it should. from bharatutils import validate_gstin_strict , parse_gstin validate_gstin_strict ( " 27AAAPZ2318J1ZI " ) # True validate_gstin_strict ( " 27AAAPZ2319J1ZI " ) # False - one typo, caught parse_gstin ( " 27AAAPZ2318J1ZI " ) # {'state': 'Maharashtra', 'pan': 'AAAPZ2318J', 'entity_number': '1'} 🪪 PAN validation + holder type from bharatutils import parse_pan parse_pan ( " AAAPZ2318J " ) # {'holder_type': 'Individual', 'name_initial': 'Z', 'is_individual': True} The 4th character of every PAN encodes who owns it: P = person, C = company, T = trust, G = government. Decoded for you. 📍 Indian address parsing from bharatutils import parse_address parse_address ( " Flat 302, Nr. SBI ATM, MG Road, Pune - 411001 " ) # {'pincode': '411001', 'state': 'Maharashtra', 'city': 'Pune'} It handles space-broken pincodes ( 700 016 ), ignores phone numbers sitting next to addresses, and always returns a dict - never crashes, safe for pandas pipelines. 🪔 One calendar for all of Bharat from bharatutils import next_festival , days_until , get_festivals next_festival () # {'name': 'Muharram', 'date': date(2026, 6, 26)} days_until ( " Diwali " ) # 150 len ( get_festivals ( 2026 )) # 19 festivals Holi and Eid. Christmas and Guru Nanak Jayanti. Buddha Purnima and Diwali. One calendar, every celebration - verified against official Government of India holiday lists, 2023–2027. What I learned building this 1. NaN is not None. My first pandas test printed ₹nan . Turns out float('nan') is not None - and the only clean way to catch NaN is number != number , because NaN is the only value in Python not equal to itself. Spent 20 minutes on this, will never forget it. 2. PyPI versions are immutable. I shipped a broken v0.1.0 on day one - an IndentationError in __init__.py from a copy-paste mistake. Discovered you cannot re-upload the same version number, ever. Fixed it as v0.1.1. Both versions live in the release history forever - a permanent record of the mistake. Strangely, that felt right. 3. Data needs verification, not memory. The festival calendar started with dates from memory. A verification pass against official government holiday lists caught a one-day error in Eid ul-Fitr before it shipped. Every data library should have this step - checking a primary source before publishing is just engineering diligence. 4. Checksum algorithms are beautiful. GSTIN's mod-36 check digit isn't just validation - it's a mathematical fingerprint baked into every tax identification number in India. I verified my implementation by generating a valid GSTIN from the algorithm itself and confirming a single-character corruption fails. Self-verification under uncertainty feels very satisfying. 5. The hardest part isn't the code. It's packaging, licensing, README, pyproject.toml, PyPI tokens, version bumps, and doing all of it correctly while a friend's advice is echoing: "shipping is 50% of the value." The code took 5 days. Getting it properly live took 2 more. Why it exists The global Python ecosystem was built for other conventions. Millions, not lakhs. Social Security numbers, not GSTINs. Thanksgiving, not Diwali. Nothing wrong with that - they built tools for their problems. The strange part is us. Millions of Indian developers, and we've collectively accepted our own conventions as edge cases in someone else's world. These problems are too small for Google to care about. Fine. They're ours to solve. bharatutils is MIT licensed - it's not mine, it's ours. Fork it, break it, fix it. This is step one. The goal: every "how do I do X in Python for India" question should eventually have one answer. Pincode-exact lookups, IFSC validation, regional festival calendars by state - that's the road ahead. Links GitHub: github.com/iam-ansuman/bharatutils PyPI: pypi.org/project/bharatutils What's the utility you keep rewriting in every project? That's the v0.2 roadmap.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/iam-ansuman/i-got-tired-of-rewriting-the-same-indian-utilities-so-i-built-bharatutils-40bn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
