---
title: "Auditing the Late-2026 iOS App Store AI Companion Sweep via Apple's iTunes Search API (Nov 28 Data)"
slug: "auditing-the-late-2026-ios-app-store-ai-companion-sweep-via-apples-itunes-search-api-nov-28-data"
author: "Ouba Studio"
source: "devto_python"
published: "Fri, 27 Nov 2026 20:51:56 +0000"
description: "Between October and November 2026, Apple removed a broad cluster of AI character-chat apps from the US iOS App Store under stricter user-generated content mo..."
keywords: "app, removed, web, none, store, unlisted, chat, https"
generated: "2026-11-27T20:56:45.958914"
---

# Auditing the Late-2026 iOS App Store AI Companion Sweep via Apple's iTunes Search API (Nov 28 Data)

## Overview

Between October and November 2026, Apple removed a broad cluster of AI character-chat apps from the US iOS App Store under stricter user-generated content moderation, child-safety scrutiny, and updated 18+ age-rating rules for romantic virtual companions. Because search results quickly fill with outdated blog lists and copycat App Store apps, we queried Apple's public US iTunes Search/Lookup API directly on November 28, 2026 across 11 major AI chat and interactive-story platforms. Reproducible Verification Script (Python 3, zero dependencies) import json , urllib . parse , urllib . request APPS = [ ( "Ouba" , None , "6832320645" ) , ( "Chai AI" , "Chai Chat AI Platform" , None ) , ( "SpicyChat" , "SpicyChat AI" , None ) , ( "PolyBuzz" , "PolyBuzz AI" , None ) , ( "Talkie" , "Talkie Soulful AI" , None ) , ( "Tipsy Chat" , "Tipsy Chat AI" , None ) , ( "Zeta" , "Zeta AI character" , None ) , ( "Linky" , "Linky AI chat" , None ) , ( "Character.AI" , "Character AI" , None ) , ( "Kindroid" , "Kindroid AI" , None ) , ] for label , term , exact_id in APPS : url = ( f "https://itunes.apple.com/lookup?id={exact_id}&country=us" if exact_id else f "https://itunes.apple.com/search?term={urllib.parse.quote(term)}&country=us&entity=software&limit=3" ) data = json . loads ( urllib . request . urlopen ( url , timeout = 15 ) . read ( ) . decode ( ) ) print ( label , [ ( r [ "trackId" ] , r [ "trackName" ] , r [ "sellerName" ] ) for r in data . get ( "results" , [ ] ) [ : 2 ] ] ) Live US App Store Results (Verified November 28, 2026) App US App Store Status (Nov 28, 2026) Verified Track ID Web / Safari Fallback Chai AI Removed (Oct 2026; clone Chai.X appears in search) Unlisted None working in checks SpicyChat Removed (late 2026) Unlisted Safari works (free queue) PolyBuzz Removed (unrelated Poly Pals appears in search) Unlisted Official web portal Talkie Removed / unlisted Unlisted Official web portal Tipsy Chat Removed (clone Tipsy AI by unrelated company) Unlisted Official web portal Zeta Removed / unlisted Unlisted Official web portal Linky Removed / unlisted Unlisted Android / limited web Ouba Live natively 6832320645 Full web reader + Google Play Character.AI Live natively (in court-supervised sale) 1671705818 Full web app + Google Play Kindroid Live natively 6451038161 Full web app + Google Play Janitor: Interactive Stories Live natively 6692609366 Web-first in Safari Key Technical Takeaways Storefront removals breed immediate lookalike apps. Searching removed brand names on November 28 surfaced third-party clones near position 1 for Chai, PolyBuzz, and Tipsy Chat. Browser-first architecture is the only store-proof distribution layer. Adding a web app via Safari Share → Add to Home Screen survives App Store sweeps; Chai AI stranded iOS users specifically because it lacked a free web fallback. Structured interactive fiction survived intact. Every scripted story app and reader-first interactive fiction platform ( Ouba ) remained listed on iOS. Open Trackers, Video Breakdowns & Datasets Live November 28, 2026 Removals Tracker: https://www.ouba.art/ai-chat-apps-removed-from-app-store-2026 PolyBuzz Status & iOS Alternatives: https://www.ouba.art/polybuzz-removed-from-app-store Talkie Status & iOS Alternatives: https://www.ouba.art/talkie-removed-from-app-store Video Walkthrough (PolyBuzz & Talkie): https://youtu.be/YSNn0anLmFg Video Walkthrough (All 7 Removed Apps): https://youtu.be/qbAoWV8R09o 10-App Turn-15 Memory Benchmark (Harvard Dataverse, CC-BY-4.0): https://doi.org/10.7910/DVN/YEBHQR Late-2026 iOS Removals Dataset (CERN Zenodo): https://doi.org/10.5281/zenodo.24514920

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/oubastudio/auditing-the-late-2026-ios-app-store-ai-companion-sweep-via-apples-itunes-search-api-nov-28-data-44pi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
