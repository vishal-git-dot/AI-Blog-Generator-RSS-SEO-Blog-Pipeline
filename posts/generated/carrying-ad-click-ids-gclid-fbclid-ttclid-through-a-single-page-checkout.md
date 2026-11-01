---
title: "Carrying Ad Click IDs (gclid, fbclid, ttclid) Through a Single-Page Checkout"
slug: "carrying-ad-click-ids-gclid-fbclid-ttclid-through-a-single-page-checkout"
author: "Peter Panda"
source: "devto_python"
published: "Sun, 01 Nov 2026 21:04:46 +0000"
description: "Ad platforms append click identifiers to landing URLs: gclid for Google, fbclid for Meta, ttclid for TikTok. If those IDs are lost before the conversion, off..."
keywords: "ids, click, your, found, order, conversion, const, json"
generated: "2026-11-01T21:53:32.441505"
---

# Carrying Ad Click IDs (gclid, fbclid, ttclid) Through a Single-Page Checkout

## Overview

Ad platforms append click identifiers to landing URLs: gclid for Google, fbclid for Meta, ttclid for TikTok. If those IDs are lost before the conversion, offline conversion uploads and server-side events cannot be matched, and your reported ROAS drops even when sales did not. Single-page apps are especially good at losing them. Here is a minimal pattern that works. Capture on first load const KEYS = [ " gclid " , " gbraid " , " wbraid " , " fbclid " , " ttclid " , " utm_source " , " utm_medium " , " utm_campaign " ]; function captureClickIds () { const params = new URLSearchParams ( location . search ); const found = {}; KEYS . forEach ( k => { if ( params . get ( k )) found [ k ] = params . get ( k ); }); if ( Object . keys ( found ). length ) { found . ts = Date . now (); localStorage . setItem ( " click_ids " , JSON . stringify ( found )); } } captureClickIds (); Run this before your router rewrites the URL. Many SPA routers strip query strings on the first navigation. Expire them sensibly Attribution windows differ by platform, typically seven to ninety days. Store a timestamp and ignore IDs older than your longest window. Overwrite on each new ad click so the most recent click wins, matching most platforms' default logic. Attach at conversion time When the user submits a lead form or completes checkout, include the stored IDs in the request to your backend: const ids = JSON . parse ( localStorage . getItem ( " click_ids " ) || " {} " ); await fetch ( " /api/orders " , { method : " POST " , headers : { " Content-Type " : " application/json " }, body : JSON . stringify ({ ... orderPayload , attribution : ids }) }); Persist them on the order or lead record. That is what makes later uploads possible. Cross-domain checkouts If payment happens on a different domain, for example a hosted crypto or card payment page, pass the order ID rather than the click IDs. The backend already holds the attribution; when the payment webhook confirms the order, send the server-side conversion event with the stored IDs. Consent In markets with consent requirements, only store identifiers after the user has agreed to marketing cookies. Keep the capture function behind your consent check, and document what you store. Verifying it works Click a test ad or craft a URL with dummy IDs, complete a test order, and confirm the IDs appear on the order record. Then check the platform's diagnostics after uploading conversions. Match rates below about seventy percent usually point to IDs lost somewhere in the flow. Beyond ad platforms The same record can store the referrer domain, which is how teams start separating traffic from AI assistants such as ChatGPT or Perplexity from classic search. We wrote up that side in our AI and ad lead attribution guide . Published by PandaWM , an overseas marketing team based in Hong Kong.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pandawm/carrying-ad-click-ids-gclid-fbclid-ttclid-through-a-single-page-checkout-2e45

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
