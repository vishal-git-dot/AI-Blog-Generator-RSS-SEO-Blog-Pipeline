---
title: "I generated a pixel font in pure Python with fonttools (no font editor)"
slug: "i-generated-a-pixel-font-in-pure-python-with-fonttools-no-font-editor"
author: "Zerrin Arslan"
source: "devto_python"
published: "Thu, 25 Jun 2026 19:32:28 +0000"
description: "I needed a font last week — not to use one, to ship one. Long story short, the cleanest way to get listed on the big font directories is to publish your own ..."
keywords: "font, pen, glyph, fonttools, you, one, cell, ttglyphpen"
generated: "2026-06-25T20:09:21.019418"
---

# I generated a pixel font in pure Python with fonttools (no font editor)

## Overview

I needed a font last week — not to use one, to ship one. Long story short, the cleanest way to get listed on the big font directories is to publish your own typeface, and I'm not a type designer. No FontForge, no Glyphs, no years of Bézier practice. So I did the programmer thing: I generated one in pure Python with fonttools . No GUI, no GPU, a few seconds of CPU. Here's how. The trick: a pixel font is just rectangles A pixel/bitmap typeface is the easiest kind to generate by code, because every glyph is a grid of filled cells. Define each letter as a 5×7 bitmap, draw a square for every "on" cell, and you have an outline. No curves to hand-tune. G = { " A " : [ " 01110 " , " 10001 " , " 10001 " , " 11111 " , " 10001 " , " 10001 " , " 10001 " ], " B " : [ " 11110 " , " 10001 " , " 10001 " , " 11110 " , " 10001 " , " 10001 " , " 11110 " ], # ... A–Z, 0–9, punctuation } Drawing a glyph with a pen fonttools gives you a TTGlyphPen . For each filled cell, draw a square contour: from fontTools.pens.ttGlyphPen import TTGlyphPen PX = 120 # cell size in font units def make_glyph ( rows ): pen = TTGlyphPen ( None ) for ry , row in enumerate ( rows ): for cx , ch in enumerate ( row ): if ch == " 1 " : x , y = cx * PX , ( 6 - ry ) * PX # flip: row 0 is top pen . moveTo (( x , y )); pen . lineTo (( x + PX , y )) pen . lineTo (( x + PX , y + PX )); pen . lineTo (( x , y + PX )) pen . closePath () return pen . glyph () Assembling the font with FontBuilder FontBuilder wires the glyphs, character map, metrics and metadata into a real .ttf : from fontTools.fontBuilder import FontBuilder fb = FontBuilder ( 1000 , isTTF = True ) # 1000 units per em fb . setupGlyphOrder ([ " .notdef " , " space " ] + list ( G )) fb . setupCharacterMap ({ ord ( c ): c for c in G } | { 32 : " space " }) fb . setupGlyf ({ " space " : TTGlyphPen ( None ). glyph (), ** { c : make_glyph ( rows ) for c , rows in G . items ()}}) fb . setupHorizontalMetrics ({ g : ( 820 , 60 ) for g in fb . font . getGlyphOrder ()}) fb . setupHorizontalHeader ( ascent = 900 , descent =- 150 ) fb . setupNameTable ({ " familyName " : " Boxel " , " styleName " : " Regular " , ...}) fb . setupOS2 (); fb . setupPost () fb . save ( " Boxel-Regular.ttf " ) That's a working, installable font. Three things that bit me Lowercase. I only defined A–Z, so typing "hello" rendered as tofu (□□□□□). Fix for a caps-only design: map a-z to the same glyph as A-Z in the cmap, so lowercase shows the uppercase shape instead of blanks: for c in G : cmap [ ord ( c )] = c if " A " <= c <= " Z " : cmap [ ord ( c . lower ())] = c The viewBox flip. Font Y goes up, your bitmap rows go down. (6 - ry) flips it. Forget this and your letters are upside down. Name table completeness. Some validators want license URL (name ID 14) alongside the license text (ID 13). Cheap to add, saves a rejection. Verify it before you trust it Don't eyeball it — render every character: from PIL import ImageFont f = ImageFont . truetype ( " Boxel-Regular.ttf " , 64 ) # draw "HELLO hello 12345 Test!" and check: any boxes = missing glyph If a cell comes out blank, the glyph or cmap entry is missing. Result I made three styles this way — square, dot-matrix, and stencil — by swapping the cell-drawing function (square vs circle vs notched). It's a family called Boxel , free for personal use. The whole thing is a single script; no design tool ever opened. fonttools is one of those libraries that turns "I can't do that" into "oh, it's 80 lines." If you've ever wanted a custom display font and bounced off the editors, generating a pixel one in code is a fun afternoon. (And if you just want fonts to download, that's literally what I build .) What would you generate — a bitmap font, an icon font, something weirder?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fontbox/i-generated-a-pixel-font-in-pure-python-with-fonttools-no-font-editor-17hp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
