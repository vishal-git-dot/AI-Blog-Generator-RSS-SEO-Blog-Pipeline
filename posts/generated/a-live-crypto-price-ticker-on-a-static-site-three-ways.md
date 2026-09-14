---
title: "A live crypto price ticker on a static site, three ways"
slug: "a-live-crypto-price-ticker-on-a-static-site-three-ways"
author: "Ethan Cole"
source: "devto_webdev"
published: "Mon, 14 Sep 2026 03:57:43 +0000"
description: "I run a small static site on Netlify and wanted a scrolling price ticker across the top. No build step, no server, and ideally no signup. Here is what I trie..."
keywords: "you, one, cache, price, script, widget, marquee, crypto"
generated: "2026-09-14T04:21:00.974360"
---

# A live crypto price ticker on a static site, three ways

## Overview

I run a small static site on Netlify and wanted a scrolling price ticker across the top. No build step, no server, and ideally no signup. Here is what I tried and where each one hurt. 1. Fetch a public API in the browser The shortest path is a plain fetch against a public endpoint. CoinGecko still answers without a key on the simple price route: const url = " https://api.coingecko.com/api/v3/simple/price " + " ?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true " ; const res = await fetch ( url ); const data = await res . json (); // { bitcoin: { usd: 77642, usd_24h_change: 0.58 }, ... } Rate limiting bit me first. The free tier counts calls per IP, and since each visitor brings their own IP, the ceiling is effectively per visitor. That holds until a dozen people behind one office network open a page that polls every five seconds. Poll once a minute at most, and stash the last response in sessionStorage so a reload does not spend a call. Then there is the id mapping. The route wants CoinGecko ids rather than symbols, and solana only works because the two happen to match. MATIC is matic-network . UNI is uniswap . I ended up with a hardcoded lookup table, the sort of thing that quietly rots the day a project renames itself. Cost: roughly 40 lines with the rendering, plus a table to maintain. 2. Proxy it through a function If you need a key, or you want one cache shared by every visitor, put a function in front: // netlify/functions/prices.js let cache = { at : 0 , body : null }; export default async () => { if ( Date . now () - cache . at < 60 _000 ) { return new Response ( cache . body , { headers : { " content-type " : " application/json " } }); } const r = await fetch ( " https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd " ); cache = { at : Date . now (), body : await r . text () }; return new Response ( cache . body , { headers : { " content-type " : " application/json " } }); }; For a real app this is the answer. One upstream call a minute regardless of traffic, the key never reaches the browser, and you get to reshape the payload on the way out. What tripped me up is that the in-memory cache only lives as long as the instance stays warm. A cold start pays the upstream call again, and several concurrent instances each keep their own copy, so the real rate is a multiple of what the code suggests. Move the cache into a KV store if that number has to be exact. Cost: a function, a deploy target that runs one, and a cold start on the first request of the day. 3. Drop in a hosted widget On a marketing page I stopped trying to own the data. A hosted ticker is one element and one script: <div id= "crypto-marquee" data-theme= "dark" data-count= "10" ></div> <script src= "https://www.thecoinanalysis.com/widgets/crypto-marquee-widget.js" ></script> I settled on the marquee from The Coin Analysis , which asks for no key and no account. It weighs about 16 KB, takes its settings from data attributes, and renders a credit link back to the source. That last part is the deal you accept with any free widget. Pasting someone else's script in took me less time than the three checks around it. Content Security Policy. The tag fails silently when your policy leaves the host out of script-src . The widget also calls its own price endpoint, so connect-src needs the host too. If it injects styles, add style-src . If it loads token logos, add img-src . Layout shift. The ticker renders once the script has loaded, and everything below it jumps down. Reserve the height yourself: #crypto-marquee { min-height : 44px ; } Measure the rendered height once in devtools and hardcode it. On a page like that, it is the single biggest Cumulative Layout Shift win available. Motion. A scrolling marquee is a vestibular trigger for some readers. Whatever you embed, wrap it: @media ( prefers-reduced-motion : reduce ) { #crypto-marquee * { animation : none ; } } That rule is the only lever you have from the outside, so check that the widget renders into ordinary DOM rather than a closed shadow root before you commit to it. What I would pick again On a side project where the prices are decoration, the hosted widget wins on time and has never woken me up. When the number is the product, fetch it yourself and keep a function in front, because the day a free tier changes you want that failure landing in your logs instead of inside a script you do not control. One habit carried across all three: render the stale value with a timestamp instead of a spinner. A price from four minutes ago still tells the reader something. A spinner only tells them the site is broken.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ethancole26/a-live-crypto-price-ticker-on-a-static-site-three-ways-12ie

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
