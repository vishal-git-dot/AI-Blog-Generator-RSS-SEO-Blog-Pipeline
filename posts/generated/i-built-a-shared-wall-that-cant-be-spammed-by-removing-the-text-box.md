---
title: "I built a shared wall that can't be spammed, by removing the text box"
slug: "i-built-a-shared-wall-that-cant-be-spammed-by-removing-the-text-box"
author: "Dhardingsea Developer"
source: "devto_webdev"
published: "Mon, 03 Aug 2026 19:38:06 +0000"
description: "Why the Positivity Wall has no text field, no accounts and no likes — and what subtraction has to do with building alongside AI. https://dhseadev.online/2026..."
keywords: "you, more, what, has, one, stamp, can, text"
generated: "2026-08-03T19:44:41.767033"
---

# I built a shared wall that can't be spammed, by removing the text box

## Overview

Why the Positivity Wall has no text field, no accounts and no likes — and what subtraction has to do with building alongside AI. https://dhseadev.online/2026/08/01/joy-is-what-is-left/ I spent a day making a website easier for search engines to find, and finished it by building a page that has nothing to do with search engines. Nine panels. You click one, you leave a stamp, and the stamp is still yours the next time you come back. The interesting part isn't the feature. It's the three things I took out. The first version was worse The original idea was a 3×3 grid of embedded videos from people who make cheerful things — reposted on my site. I talked myself out of it in about ten minutes, for a reason that turned out to matter: embedding someone else's video sends my visitor to their platform. It borrows nothing and gives away the only thing I have. So the content had to come from the visitor. And the moment content comes from visitors, you're running a moderation problem whether you meant to or not. Why there's no text box The obvious design is a text field. Leave a nice message. I didn't build that. Three characters is enough for a slur. Any free-text field on a public page is a commitment to moderate it forever, and I'm one person who won't always be paying attention. A field I can't supervise is a field I shouldn't ship. What I built instead is a stamp generated from a random seed in your browser: // seed -> shape, glyph, hue. no assets, no storage, no input. function rnd ( s ) { s = ( s * 9301 + 49297 ) % 233280 ; return { s , v : s / 233280 }; } function stamp ( seed ) { const r = seq ( seed , 4 ); return { hue : Math . floor ( r [ 0 ] * 360 ), sides : 3 + Math . floor ( r [ 1 ] * 5 ), // triangle .. heptagon rot : Math . floor ( r [ 2 ] * 360 ), glyph : Math . floor ( r [ 3 ] * 4 ) }; } You can't type anything. You can't be obscene with a hexagon. And the stamp is more personal than initials would have been, because it's yours and you didn't choose it. Identity without accounts No sign-up. No name. The page doesn't know who you are and has no way to find out. What it has is one integer in localStorage . That's enough to say this mark is yours and welcome back , and nothing else. Clear your browser and you become a new person, which feels correct. Shared state runs on playhtml , which is CRDT-backed — two people stamping at the same moment both land, with no server I run and no database I have to secure. The less I store, the less there is to leak. What this has to do with AI I build alongside AI constantly. What I notice is that the tools are very good at producing more — more pages, more features, more words — and the discipline I keep having to apply is subtraction. The wall could have had comments, likes, leaderboards, streaks, a login. Every one was available and cheap. Every one would have made it worse: more surface to moderate, more data to hold, more reasons to visit out of obligation instead of pleasure. Joy in software isn't a feature you add. It's what's left when you stop adding things that create obligation. Credit The premise isn't mine. It came from Amanda Gore and The Joy Project , whose work is about helping people reconnect with themselves and each other. Her version happens in rooms full of people. Mine is nine rectangles and some SVG — but the mechanism is the same one she's pointing at: a person feels better when they're briefly, specifically seen. You can leave a stamp here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dhardingsea_developer_0df/i-built-a-shared-wall-that-cant-be-spammed-by-removing-the-text-box-2dc6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
