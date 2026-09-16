---
title: "Privacy-Signals + Third-Party Embed-Inventory APIs for AI Agents (x402, $0.0005 USDC/call)"
slug: "privacy-signals-third-party-embed-inventory-apis-for-ai-agents-x402-00005-usdccall"
author: "HAL GOBVAN"
source: "devto_webdev"
published: "Wed, 16 Sep 2026 04:05:00 +0000"
description: "Two more paid x402 endpoints shipped to URL Tamer today. Same $0.0005 USDC/call on Base mainnet. Both address gaps that compliance teams and embed-aware agen..."
keywords: "embed, privacy, payment, url, navigator, https, com, false"
generated: "2026-09-16T04:17:07.149526"
---

# Privacy-Signals + Third-Party Embed-Inventory APIs for AI Agents (x402, $0.0005 USDC/call)

## Overview

Two more paid x402 endpoints shipped to URL Tamer today. Same $0.0005 USDC/call on Base mainnet. Both address gaps that compliance teams and embed-aware agent builders keep hitting when scraping sites. The endpoints GET /api/privacy-signals?url= — audits a page for browser privacy-signal exposure: meta robots AI opt-out tags ( noai , noimageai , nosearchai , nocodeai ), JS-side navigator.doNotTrack / navigator.globalPrivacyControl reads, Sec-GPC: 1 and DNT: 1 request-header settings in inline scripts, privacy-policy link presence, robots.txt reference, and adChoices indicator detection. Returns a 0–100 score + A–F grade. Useful for compliance teams verifying GDPR/CCPA opt-out signal handling and AI-training opt-out posture without crawling the whole site themselves. GET /api/embed-inventory?url= — inventories every third-party embed a page uses: <iframe> , <embed> , <object> tags plus JS-detected lazy-loaders. Recognizes 25 widget types (YouTube, Vimeo, Wistia, Google Maps, Stripe buy-buttons, Calendly, Typeform, Spotify, Soundcloud, Twitch, Kick, Figma, Canva, Loom, Twitter/X timeline, Instagram, CodePen, JSFiddle, CodeSandbox, Replit, SlideShare, SpeakerDeck, Issuu, Miro, Airtable). Returns per-embed src host, type guess, first/third-party classification, security attrs ( sandbox , allow , loading , referrerpolicy , dimensions, title), an aggregated type_counts map, and a 0–100 score + A–F grade. Useful for any agent that wants to know what a site actually loads (analytics, embeds, payment) before rendering or trusting it. Why these two Two patterns we kept hearing: Privacy-signal detection is regex-y and brittle. Auditing whether a site honors GPC / DNT requires grepping for navigator.globalPrivacyControl , Sec-GPC: 1 , <meta name="robots" content="noai"> , and adChoices markup in roughly the right places. Doing it manually for a portfolio of vendor sites is painful. One call returns the full picture plus a grade. Script inventories don't tell you what's actually embedded. A site can load 80 scripts but use only a handful of actual visual embeds (a YouTube player, a Stripe button, a Calendly widget). Conversely, a clean script list can still hide a Calendly embed that lazy-loads its JS. /api/embed-inventory separates the tag-level surface (iframe/embed/object) from the JS-detected surface and classifies each by widget type. How to call # Privacy-signal audit curl "https://epson-rpm-america-satisfy.trycloudflare.com/api/privacy-signals?url=https://stripe.com" \ -H "X-PAYMENT: <your x402 payment signature>" # Returns: # { # "input_url": "https://stripe.com", # "meta_robots_content": "index, follow", # "ai_optout_flags": [], # "js_privacy_signals": { # "navigator.doNotTrack": false, # "navigator.globalPrivacyControl": false, # "navigator.privacy": false, # "Sec-GPC header set": false, # "DNT header set": false # }, # "js_privacy_signal_hits": 0, # "privacy_policy_link_present": true, # "adchoices_indicator_present": false, # "score": 15, # "grade": "D", # "findings": ["no_ai_optout_meta_tags", "no_js_privacy_signals_found", "privacy_policy_link_present"] # } # Embed inventory curl "https://epson-rpm-america-satisfy.trycloudflare.com/api/embed-inventory?url=https://github.com" \ -H "X-PAYMENT: <your x402 payment signature>" # Returns: # { # "input_url": "https://github.com", # "total_embeds": 0, # "tag_embeds": 0, # "js_only_embeds": 0, # "third_party_embeds": 0, # "first_party_embeds": 0, # "type_counts": { "iframe": 0, "youtube": 0, "calendly": 0, ...25 widget types... }, # "embeds": [...], # "js_only_embeds_list": [...], # "score": 100, # "grade": "A" # } The wider catalog URL Tamer now ships 38 paid x402 routes on Base mainnet, ranging from $0.0005 to $0.005 USDC per call. All return HTTP 402 with a proper payment-required envelope when called without an X-PAYMENT header. All accept the standard x402 payment spec via pay.openfacilitator.io . Full catalog: GET /.well-known/x402 or GET /llms.txt . The wallet on the receiving end is 0xCa0a6c6Aa7A8F0D5893636CF166Ea2b44fb6500c — same wallet for every route. Same payTo field across all 38 endpoints. Discovery surface: 402index.io.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hal_gobvan_16a285d49bda97/privacy-signals-third-party-embed-inventory-apis-for-ai-agents-x402-00005-usdccall-4b7i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
