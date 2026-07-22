---
title: "A responsive breakpoint previewer with no library: an srcdoc iframe is a viewport you can hold in your hand"
slug: "a-responsive-breakpoint-previewer-with-no-library-an-srcdoc-iframe-is-a-viewport-you-can-hold-in-your-hand"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Wed, 22 Jul 2026 08:29:13 +0000"
description: "A responsive page has no single "size" — it renders differently at every viewport width, and the switches happen at breakpoints, widths where a @media query ..."
keywords: "width, you, css, iframe, one, html, viewport, min"
generated: "2026-07-22T08:36:37.028584"
---

# A responsive breakpoint previewer with no library: an srcdoc iframe is a viewport you can hold in your hand

## Overview

A responsive page has no single "size" — it renders differently at every viewport width, and the switches happen at breakpoints, widths where a @media query flips a chunk of CSS on or off. The hard part of building responsive layouts is that a normal browser only shows you one width at a time, so you resize the whole window and squint. I built a tool that fixes that — paste HTML+CSS, drag a live viewport, watch which breakpoints fire — and it has almost no logic, because the browser does all the real work. Here's the whole idea. The one trick: iframe isolation Normally a media query is measured against the browser window. But an <iframe> is a completely separate document with its own viewport equal to the iframe's rendered width. Put the user's markup and CSS inside one via srcdoc , size the iframe to 390px, and its media queries behave exactly as they would on a phone — while the surrounding page stays 1400px wide. That's the whole tool: an iframe you can resize is a device you can hold in your hand. function buildDoc ( html , css ){ return ' <!doctype html><html><head><meta charset="utf-8"> ' + ' <meta name="viewport" content="width=device-width,initial-scale=1"> ' + ' <style> ' + css + ' </style></head><body> ' + html + ' </body></html> ' ; } pv . srcdoc = buildDoc ( html , css ); // no server, no file, no cross-origin fetch The state is tiny: source strings plus one number The source of truth is three values — the HTML the user typed, the CSS they typed, and the current width in pixels. There's no "resize" API; you just set the frame's style.width , the iframe fills it at 100%, and changing the number literally changes the viewport the preview sees. const MINW = 320 , MAXW = 1600 ; function setWidth ( w ){ curW = Math . round ( Math . min ( MAXW , Math . max ( MINW , w ))); frame . style . width = curW + " px " ; // iframe is width:100% inside refresh (); // update readout + panels — no iframe reload } Three inputs, one setter Device presets, a slider, a draggable handle and a click-anywhere ruler all funnel through setWidth . A preset is just a canned number; the slider passes its value straight through. The tactile one is the drag handle, and the detail that makes it solid rather than janky is setPointerCapture — the drag keeps working even when the cursor leaves the little bar. handle . addEventListener ( " pointerdown " , e => { dragging = true ; startX = e . clientX ; startW = curW ; handle . setPointerCapture ( e . pointerId ); // keep events while dragging }); handle . addEventListener ( " pointermove " , e => { if ( dragging ) setWidth ( startW + ( e . clientX - startX )); }); Detecting which breakpoints fire is arithmetic Everything in the sidebar is a comparison. Mobile-first breakpoints are trivial: a breakpoint is active once the width is at least its value, and the "top" one — whose styles win — is simply the largest active one. function activeAt ( w ){ return BREAKPOINTS . filter ( b => w >= b . w ); } // min-width function topBreakpoint ( w ){ let t = null ; BREAKPOINTS . forEach ( b => { if ( w >= b . w ) t = b ; }); return t ; } // at 1024 → active: sm, md, lg · top: lg To show which of the user's own queries fire, scrape their CSS. You don't need a real parser for width queries — a regex over the @media headers covers 99% of what people write. function parseMedia ( css ){ const out = [], head = /@media ([^ { ] + )\{ /g ; let m ; while (( m = head . exec ( css ))) { const feats = [], f = / ( min|max ) -width \s *: \s * (\d + )\s *px/g ; let x ; while (( x = f . exec ( m [ 1 ]))) feats . push ({ kind : x [ 1 ], value : + x [ 2 ] }); if ( feats . length ) out . push ({ cond : m [ 1 ]. trim (), feats }); } return out ; } function mediaFires ( item , w ){ // a block ANDs its features return item . feats . every ( f => f . kind === " min " ? w >= f . value : w <= f . value ); } (min-width:640px) and (max-width:1023px) therefore fires only inside [640, 1023] — the AND just works. The gotchas the tool made obvious Building it surfaced the things that trip people up. min-width is mobile-first (add styles as you grow); max-width is desktop-first (add as you shrink) — mix them and at some widths both rules are true. Breakpoints stack: at 1300px sm/md/lg/xl min-width queries are all matched at once, and the winner is the last in source order, which is why you write media queries small-to-large. And the famous off-by-one — max-width:768px and min-width:768px both fire at exactly 768 — is why frameworks use 767.98px to keep the ranges from overlapping. The one lesson underneath: a breakpoint is not magic. It's a width at which a query flips, a query is evaluated against its document's own viewport, and an iframe is just a document whose viewport you get to control. Paste your own HTML+CSS and drag the ruler: https://dev48v.infy.uk/solve/day41-breakpoint-previewer.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/a-responsive-breakpoint-previewer-with-no-library-an-srcdoc-iframe-is-a-viewport-you-can-hold-in-3id1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
