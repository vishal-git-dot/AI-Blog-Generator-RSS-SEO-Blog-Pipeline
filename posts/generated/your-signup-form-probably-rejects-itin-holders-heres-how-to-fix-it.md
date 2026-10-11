---
title: "Your Signup Form Probably Rejects ITIN Holders. Here's How to Fix It"
slug: "your-signup-form-probably-rejects-itin-holders-heres-how-to-fix-it"
author: "ITIN Dev Notes"
source: "devto_webdev"
published: "Sun, 11 Oct 2026 21:39:16 +0000"
description: "If your product asks for a U.S. tax ID (payroll, lending, banking, tax prep, marketplaces paying out sellers), there is a good chance your form quietly rejec..."
keywords: "itin, ssn, your, number, return, group, area, you"
generated: "2026-10-11T21:42:13.760136"
---

# Your Signup Form Probably Rejects ITIN Holders. Here's How to Fix It

## Overview

If your product asks for a U.S. tax ID (payroll, lending, banking, tax prep, marketplaces paying out sellers), there is a good chance your form quietly rejects a whole group of real customers: people who file taxes with an ITIN instead of a Social Security Number. An ITIN (Individual Taxpayer Identification Number) is issued by the IRS to people who must file U.S. taxes but can't get an SSN. It looks exactly like an SSN, which is precisely why so many validators get it wrong. This post is a checklist of the bugs I see most often, with code you can drop in. 1. Your SSN validator is rejecting every ITIN ITINs are nine digits, formatted like an SSN ( 9XX-XX-XXXX ), and always start with 9 . SSNs, on the other hand, are never issued with an area number from 900 to 999. So the classic SSN rule "reject anything starting with 9" is correct for SSNs and fatal for ITINs. The fix is to validate a taxpayer ID , not an SSN, and to classify it: import re TIN = re . compile ( r " ^(\d{3})-?(\d{2})-?(\d{4})$ " ) ITIN_GROUPS = [ range ( 50 , 66 ), range ( 70 , 89 ), range ( 90 , 93 ), range ( 94 , 100 )] def classify_tin ( value : str ) -> str | None : """ Return " SSN " , " ITIN " , or None if the number cannot be valid. """ match = TIN . match ( value . strip ()) if not match : return None area , group , serial = match . groups () if area . startswith ( " 9 " ): return " ITIN " if any ( int ( group ) in r for r in ITIN_GROUPS ) else None if area in ( " 000 " , " 666 " ) or group == " 00 " or serial == " 0000 " : return None return " SSN " The ITIN check uses the 4th and 5th digits: the IRS issues ITINs with those digits in the ranges 50 to 65, 70 to 88, 90 to 92, and 94 to 99. Keep that list in one place so it is easy to update if the IRS expands it again. The same logic on the client, so people get instant feedback: const ITIN_GROUPS = [[ 50 , 65 ], [ 70 , 88 ], [ 90 , 92 ], [ 94 , 99 ]]; export function classifyTin ( value ) { const m = value . trim (). match ( /^ (\d{3}) - ?(\d{2}) - ?(\d{4}) $/ ); if ( ! m ) return null ; const [, area , group , serial ] = m ; if ( area . startsWith ( " 9 " )) { const g = Number ( group ); return ITIN_GROUPS . some (([ lo , hi ]) => g >= lo && g <= hi ) ? " ITIN " : null ; } if ( area === " 000 " || area === " 666 " || group === " 00 " || serial === " 0000 " ) return null ; return " SSN " ; } Always repeat the check on the server. Client-side validation is a convenience, not a control. Test the edges A handful of unit tests catches most regressions. Make sure your suite covers at least: A number starting with 9 whose 4th and 5th digits are in an ITIN range is accepted as an ITIN A number starting with 9 whose 4th and 5th digits are outside those ranges (for example 49 or 93) is rejected 000 , 666 , a 00 group and a 0000 serial are rejected as SSNs The same number is accepted with and without dashes, and with surrounding spaces 2. Your label tells people they don't belong A field labeled "Social Security Number" tells an ITIN holder to leave. Even if your backend accepts ITINs, many people will abandon the form at that label. Label the field "SSN or ITIN" or "Taxpayer ID (SSN or ITIN)" Add one line of help text: "We accept either a Social Security Number or an ITIN." Don't make people pick the ID type from a dropdown if you can detect it from the number Use inputmode="numeric" and autocomplete="off" , and accept the number with or without dashes 3. Your name and address fields assume one culture Many ITIN holders have names that break naive validation: two surnames, accents, apostrophes, or a single name. Store names as Unicode and never strip accents ("María José García López" is one valid name) Prefer a single full name field plus an optional "what should we call you?" field Don't require a "last name" or reject hyphens and apostrophes If you need a mailing address, allow non-U.S. addresses and don't force a U.S. state 4. Your business logic treats an ITIN like an SSN They look the same, but they are not interchangeable, and the differences matter for your product rules: An ITIN is not work authorization. Don't use it for I-9 or employment eligibility checks. ITINs expire. An ITIN that isn't used on a federal tax return at least once in three consecutive years expires and has to be renewed. If your product depends on a valid ITIN, plan a friendly "you may need to renew" path instead of a hard failure. Some financial products accept ITINs, some don't. Make that a product decision made explicitly, not an accident of your validator. 5. You store it like a username An ITIN is as sensitive as an SSN. Treat it that way: Encrypt it at rest, separately from the rest of the user record Show only the last four digits after it is saved ( ***-**-1234 ) Keep it out of logs, analytics events, URLs, and error trackers Restrict who and what can read the full value, and audit those reads The short checklist Validate a taxpayer ID , and classify it as SSN or ITIN instead of rejecting numbers that start with 9 Label the field "SSN or ITIN" Accept real-world names and non-U.S. addresses Model ITIN-specific rules (no work authorization, expiration) explicitly Protect it like an SSN None of this is hard, and it opens your product to millions of taxpayers that a one-line regex was turning away. If you have hit other ITIN edge cases in production, share them in the comments. I'll fold the good ones into this checklist.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/itin_dev_notes_5f7d/your-signup-form-probably-rejects-itin-holders-heres-how-to-fix-it-98

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
