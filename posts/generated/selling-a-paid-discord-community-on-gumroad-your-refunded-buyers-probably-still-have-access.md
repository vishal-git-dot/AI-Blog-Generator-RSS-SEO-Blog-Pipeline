---
title: "Selling a paid Discord community on Gumroad? Your refunded buyers probably still have access"
slug: "selling-a-paid-discord-community-on-gumroad-your-refunded-buyers-probably-still-have-access"
author: "Pau Drudis"
source: "devto_webdev"
published: "Tue, 20 Oct 2026 04:07:05 +0000"
description: "A paid Discord is one of the easiest things to sell on Gumroad: a course community, a trading channel, a mod-support server. The usual setup goes like this: ..."
keywords: "gumroad, bot, ping, url, sale, discord, key, role"
generated: "2026-10-20T04:19:10.500025"
---

# Selling a paid Discord community on Gumroad? Your refunded buyers probably still have access

## Overview

A paid Discord is one of the easiest things to sell on Gumroad: a course community, a trading channel, a mod-support server. The usual setup goes like this: buyer pays, buyer pastes their license key into a bot, and the bot gives them a role. There are two quiet bugs in almost every version of that setup. Bug 1: success: true doesn't mean "paid" Gumroad's POST /v2/licenses/verify returns success: true for a key even after the purchase was refunded or charged back . You have to check the purchase flags yourself: function isActive ( p ) { if ( p . refunded || p . chargebacked || p . disputed ) return false ; if ( p . subscription_ended_at || p . subscription_cancelled_at || p . subscription_failed_at ) return false ; return true ; } If your bot only checks success , a buyer can pay, get the role, refund, and stay in your server indefinitely. Bug 2: Gumroad pings aren't signed To remove roles on refund, you'll use Gumroad's Ping (Settings → Advanced). But the ping is a plain form POST with no signature. Anyone who learns the URL can send sale_id=... and pretend. The fix is simple: treat the ping only as a "something changed" signal . Pull the sale ID out of it and re-fetch the real record: const r = await fetch ( `https://api.gumroad.com/v2/sales/ ${ saleId } ` , { headers : { Authorization : `Bearer ${ process . env . GUMROAD_ACCESS_TOKEN } ` } }); const { sale } = await r . json (); if ( isActive ( sale )) grantRole (); else revokeRole (); Also put a long random secret in the ping URL, and compare it with crypto.timingSafeEqual . Adding and removing the role With a bot that has Manage Roles , and whose own role sits above the roles it grants: const url = `https://discord.com/api/v10/guilds/ ${ GUILD } /members/ ${ userId } /roles/ ${ roleId } ` ; await fetch ( url , { method : ' PUT ' , headers : { Authorization : `Bot ${ BOT_TOKEN } ` } }); // grant await fetch ( url , { method : ' DELETE ' , headers : { Authorization : `Bot ${ BOT_TOKEN } ` } }); // revoke Two more things people miss Key sharing. Store sale_id → discord_id and refuse to link the same sale to a second account. Missed pings. Hosts restart, and pings get dropped. Run a nightly job that re-checks every linked sale and revokes anything inactive. Free check, or the full thing The refund-aware license check on its own is free and MIT licensed: gumroad-license-check . If you'd rather not wire up the rest yourself, the Gumroad → Discord Access Kit packages all of it: the ping endpoint, the linking form, one-key-per-account, the nightly reconcile and 12 tests, with zero dependencies.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pau_drudis_6182de07fdc9f0/selling-a-paid-discord-community-on-gumroad-your-refunded-buyers-probably-still-have-access-5mh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
