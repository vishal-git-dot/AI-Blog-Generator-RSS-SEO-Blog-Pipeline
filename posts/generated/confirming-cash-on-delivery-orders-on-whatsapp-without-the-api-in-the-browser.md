---
title: "Confirming cash-on-delivery orders on WhatsApp without the API, in the browser"
slug: "confirming-cash-on-delivery-orders-on-whatsapp-without-the-api-in-the-browser"
author: "Low Key Builds"
source: "devto_webdev"
published: "Tue, 20 Oct 2026 16:32:15 +0000"
description: "Most online orders in Pakistan are cash on delivery. Sellers who run ads get a steady stream of fake or careless orders, and every refused parcel costs two-w..."
keywords: "orders, whatsapp, order, number, message, urdu, sellers, one"
generated: "2026-10-20T16:39:11.048083"
---

# Confirming cash-on-delivery orders on WhatsApp without the API, in the browser

## Overview

Most online orders in Pakistan are cash on delivery. Sellers who run ads get a steady stream of fake or careless orders, and every refused parcel costs two-way courier charges. So most small stores do one manual step before booking the courier: they message each customer on WhatsApp and ask them to confirm. The paid fix is a Shopify app on the WhatsApp Business API (there are several, from about $3 to $10 a month plus Meta's per-message fees). I wanted to see how far a free, static, browser-only tool could go for the sellers who do not have Shopify or do not want the API: WooCommerce stores, and Instagram and Facebook sellers who keep orders in a Google Sheet. The result is ConfirmKaro , which I built. Here is what was interesting to build. 1. wa.me links do the sending WhatsApp has a public click-to-chat URL: https://wa.me/<number>?text=<urlencoded message> . On a phone it opens the chat in the WhatsApp app with the message typed; on desktop it opens WhatsApp Web. The seller presses send. No API, no number registration, no template approval, and the message comes from the shop's normal WhatsApp, which customers already recognise. The cost is one tap per order, which is fine up to a few dozen orders a day. 2. Pakistani phone numbers in the wild wa.me wants the international format with no + , no spaces and no leading zero: 923001234567 . Order exports contain everything else: 0300 1234567 -> 923001234567 +92 321 7654321 -> 923217654321 0333-5556667 -> 923335556667 3001234567 -> 923001234567 (leading zero lost by Excel) 00923001234567 -> 923001234567 03451234 -> invalid (too short) function normPhone ( raw ) { const s = String ( raw || '' ). trim (); const plus = s . startsWith ( ' + ' ); let d = s . replace ( / \D /g , '' ); if ( d . startsWith ( ' 0092 ' )) d = d . slice ( 2 ); if ( d . length === 11 && d . startsWith ( ' 03 ' )) d = ' 92 ' + d . slice ( 1 ); else if ( d . length === 10 && d . startsWith ( ' 3 ' )) d = ' 92 ' + d ; if ( d . length === 12 && d . startsWith ( ' 923 ' )) return { ok : true , wa : d , pk : true }; if ( plus && d . length >= 10 && d . length <= 15 ) return { ok : true , wa : d , pk : false }; return { ok : false , wa : d }; } The Excel case matters more than it looks: when a sheet stores the number as a number, the leading zero disappears, so a 10-digit value starting with 3 is almost certainly a Pakistani mobile. 3. Shopify exports one row per line item Shopify's orders CSV repeats the order Name ( #1041 ) on one row per item, and only the first row has the total and shipping details. Merging by order number and appending item rows gives one message per order. WooCommerce export plugins use different headers ( Billing Phone , Order Total Amount ), so columns are matched by a ranked list of header tests, and the user can override any column. 4. Fake-order flags without any server All local heuristics: invalid number, the same number on several orders in the batch, an address under 12 characters ("abc"), a name with digits or fewer than three letters, and a total over four times the batch median. None of these prove fraud; they decide who gets confirmed most carefully. 5. Urdu in Nastaliq, and Roman Urdu Most sellers write to customers in Roman Urdu ("Order confirm karne ke liye 1 likh kar bhejein"), some in Urdu script, some in English. The templates come in all three. The page self-hosts Noto Nastaliq Urdu (SIL OFL) as a 160 KB woff2 converted with fontTools, sets lang="ur" dir="rtl" , and needs a line height above 2 because Nastaliq stacks vertically. WhatsApp renders the Urdu text itself with the phone's font, so the font only matters on the page. 6. Nothing leaves the browser The CSV is read with FileReader , statuses (pending, confirmed, no reply, cancelled) live in localStorage , and the confirmed orders download as a CSV for courier bulk booking. Customer names and phone numbers never touch a server, which is the main reason a seller can trust a tool from someone they do not know. What I would like to know If you build stores for Pakistani (or Indian, Bangladeshi, Egyptian, Moroccan) COD sellers: how do your clients confirm orders today, and what format does their courier's bulk booking want? Replies at confirmkaro@appin60.com or in the comments shape what gets added next. Disclosure: I built ConfirmKaro. It is free and has no paid tier.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lowkeybuilds/confirming-cash-on-delivery-orders-on-whatsapp-without-the-api-in-the-browser-3bb7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
