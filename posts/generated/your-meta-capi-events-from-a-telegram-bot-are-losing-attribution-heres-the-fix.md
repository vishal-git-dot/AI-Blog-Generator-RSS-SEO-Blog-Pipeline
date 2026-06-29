---
title: "Your Meta CAPI events from a Telegram bot are losing attribution. Here's the fix."
slug: "your-meta-capi-events-from-a-telegram-bot-are-losing-attribution-heres-the-fix"
author: "Boris Kl"
source: "devto_webdev"
published: "Mon, 29 Jun 2026 19:37:36 +0000"
description: "A funnel I see all the time: a Meta ad sends people to a landing page, the page says "message us on Telegram," and a bot takes it from there — qualifies the ..."
keywords: "click, bot, token, fbclid, you, meta, start, telegram"
generated: "2026-06-29T20:06:45.989064"
---

# Your Meta CAPI events from a Telegram bot are losing attribution. Here's the fix.

## Overview

A funnel I see all the time: a Meta ad sends people to a landing page, the page says "message us on Telegram," and a bot takes it from there — qualifies the lead, takes the order, whatever. The conversion happens inside the bot , server-side, so you fire it to Meta with the Conversions API instead of the Pixel. Makes sense. Except attribution quietly falls apart, and it took me a while to see why. The click ID is the whole game Meta matches a server event back to the ad click using fbc . The format is fixed: fb.1.<timestamp>.<fbclid> That <fbclid> comes off the landing URL as ?fbclid=... when someone arrives from the ad. No fbc , and your CAPI event still lands — but match quality drops and Meta can't tie the conversion to the click. Which is the one thing you actually wanted. So the job is: capture fbclid on the landing page, carry it into the bot, rebuild fbc there, send it with the event. "Carry it into the bot" is where it breaks. Telegram's deep link won't hold it You move someone from web into a bot with a deep link: https://t.me/your_bot?start=<payload> The bot gets <payload> as the argument to /start . Perfect place to stash the click ID, right? No. Telegram caps that start payload at 64 characters , and only allows A-Z a-z 0-9 _ - . A real fbclid runs way past that — the ones I've measured sit around 170+ characters. It does not fit. Truncate it and it's no longer a valid click ID. URL-encode it and it gets longer . There's no squeezing the real value through that gate. This is the part nobody warns you about. The naive build looks fine in testing with a short fake fbclid, then drops attribution in production with real ones. The fix: hand over a token, not the value Don't pass the click ID. Pass a short token that points to it. On the landing page, when the visitor taps through to Telegram: Generate a short random token (a dozen URL-safe chars is plenty). Store { fbclid, click timestamp, utm params } against that token server-side — Redis, a KV store, a tiny table. Build the deep link with the token: https://t.me/your_bot?start=ab12cd34ef . In the bot, on /start : bot . start ( async ( ctx ) => { const token = ctx . startPayload ; // "ab12cd34ef" const click = await store . get ( token ); // { fbclid, ts, utm } if ( click ) { const fbc = `fb.1. ${ click . ts } . ${ click . fbclid } ` ; await sendCapiEvent ({ event_name : " Lead " , action_source : " chat " , // it happened in a messaging app, not a website user_data : { fbc /* + whatever else you have */ }, // event_id if you also fire a Pixel, so Meta dedups }); } // no token? organic /start. Fine — just lower match quality, no fbc. }); The token is short, so it sails through the 64-char limit. The real fbclid never has to travel through Telegram at all. Two details that bite Use the click timestamp, not the bot-open time. Store ts when they hit the landing page. People tap an ad now and open the bot tomorrow — if you stamp fbc with the moment /start fired, the window's off. Carry the original click time with the token. action_source should tell the truth. A bot conversion isn't a website event — it happened in a messaging app, so the value is chat . ( business_messaging is Meta's own channels like WhatsApp, not Telegram — don't borrow it.) Meta accepts non-website sources; misreporting it just muddies your own data later. And give tokens a TTL. A click that never opens the bot leaves a dangling entry — expire them after a day or two. None of this is exotic. It's one indirection — a token standing in for a value that's too big to move. But the failure is silent: events keep arriving, dashboards look populated, and attribution is just... soft, with no error to tell you why. If you're running paid traffic into a chat funnel, check whether your click IDs are actually surviving the handoff. I build these bot funnels and the tracking behind them — if yours is leaking attribution somewhere, happy to take a look.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lamas51/your-meta-capi-events-from-a-telegram-bot-are-losing-attribution-heres-the-fix-5c07

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
