---
title: "I added a $1.30 invoice generator to my Telegram bot — here's the parser that never throws"
slug: "i-added-a-130-invoice-generator-to-my-telegram-bot-heres-the-parser-that-never-throws"
author: "member_fb93637b"
source: "devto_python"
published: "Tue, 20 Oct 2026 21:13:11 +0000"
description: "A few weeks ago I wrote about running a Telegram Stars payment bot on GitHub Actions for $0/month . That bot only sold one fixed product. This week I added a..."
keywords: "same, invoice, bot, line, buyer, notes, item, not"
generated: "2026-10-20T21:26:05.881197"
---

# I added a $1.30 invoice generator to my Telegram bot — here's the parser that never throws

## Overview

A few weeks ago I wrote about running a Telegram Stars payment bot on GitHub Actions for $0/month . That bot only sold one fixed product. This week I added a second, much cheaper product to the same bot: a buyer sends a plain-text list of line items in chat, gets a priced preview and a payment link, pays 100 Stars (~$1.30), and the bot sends back a polished HTML invoice. The interesting part isn't the payment flow — that's the same pre_checkout_query / successful_payment plumbing as before. It's the parser that turns a Telegram message into invoice data, because unlike a web form, a chat message has no input validation before it reaches your code. The format /invoice from: Your Name to: Client Name invoice_number: INV-001 date: 2026-10-20 due_date: 2026-11-20 tax_rate: 0 notes: Thanks for your business item: Website redesign | 10 | 50 item: Logo design | 1 | 200 Line-based key: value , with repeated item: lines split on | for description/qty/rate. No JSON, no quoting rules, nothing a non-technical buyer has to get exactly right syntactically — just colons and pipes. The rule that shaped the whole function: never raise parse_invoice_text() runs directly on untrusted user input with no validation layer in front of it (there's no form, no client-side JS — a Telegram message is just a string). So the function's contract is (data, None) on success or (None, error_message) on failure, and it is not allowed to raise: def parse_invoice_text ( text ): lines = [ ln for ln in text . splitlines () if ln . strip ()] ... for ln in lines : if " : " not in ln : return None , f " Couldn ' t parse this line (missing ' : ' ): { ln !r} \n\n { USAGE } " key , _ , value = ln . partition ( " : " ) ... if key == " item " : parts = [ p . strip () for p in value . split ( " | " )] if len ( parts ) != 3 : return None , f " Item line needs exactly 3 parts separated by ' | ' ... " try : qty = float ( qty_s ) rate = float ( rate_s ) except ValueError : return None , f " qty and rate must be numbers, got: { ln !r} \n\n { USAGE } " Every failure path returns the exact same usage text that would've gotten the message right in the first place, inlined after the specific complaint. A buyer who gets qty and rate must be numbers, got: 'item: Logo design | one | 200' immediately sees both what they did and what's expected, in the same message, with no need to scroll up. 26 tests cover this (valid messages, missing fields, malformed item lines, non-numeric qty/rate, bare /invoice with no body) — the whole point of this function is that it has no code path that reaches an uncaught exception, and the tests exist to keep that true across edits, not just to hit a coverage number. The forgiving part: unknown keys are silently ignored elif key in ( " from " , " to " , " invoice_number " , " date " , " due_date " , " notes " ): data [ key ] = value # unknown keys are silently ignored rather than rejected — keeps the # format forgiving of e.g. a stray colon in a copy-pasted notes line If I made unknown keys an error, a buyer who pastes a notes: line containing its own colon ( notes: Paid via wire, ref: 4471 ) wouldn't actually break anything, since partition(":") only splits on the first colon and notes is matched as a known key before this branch could ever trigger — but the design leaves room for a buyer typo'ing a field name ( not: instead of notes: ) to fail silently rather than loudly. That's a real tradeoff, not a free win: silent data loss is worse than a loud rejection in some products. For a $1.30 one-shot invoice I chose forgiving over strict, because the buyer sees a full preview before paying — a dropped field shows up as a visibly blank line in the preview, not as corrupted output after money has changed hands. Reusing the renderer, not importing it The HTML the bot sends back is byte-for-byte the same template as my free, zero-dependency freelance-invoice-cli — same fonts, same table layout, same print stylesheet. I vendored the render function into this repo instead of importing it across repos at runtime, specifically so a buyer who later wants to self-serve with the free CLI isn't surprised by a different-looking invoice, and so this bot has no runtime dependency on another repo's availability. The tradeoff is the usual one for vendoring: if the CLI's renderer changes, I have to remember to port the change by hand. For a ~30-line pure function that's a cost I'm fine carrying. Where it stands Live now: send /invoice to @freelancerkitbot with the format above. More detail + a worked example . No new hosting, no new bot, no new Telegram app — same $0/month Actions-hosted responder from the earlier post, same bot token, new code path. Code (MIT): https://github.com/kleogeos/telegram-stars-checkout

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/member_fb93637b/i-added-a-130-invoice-generator-to-my-telegram-bot-heres-the-parser-that-never-throws-2bhb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
