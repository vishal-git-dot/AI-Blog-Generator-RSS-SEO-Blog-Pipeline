---
title: "I built HandFonty: turn your handwriting into an installable font in your browser"
slug: "i-built-handfonty-turn-your-handwriting-into-an-installable-font-in-your-browser"
author: "Leora Bailey"
source: "devto_webdev"
published: "Mon, 26 Oct 2026 12:23:52 +0000"
description: "A personal handwriting font can give a side project, invitation, or design a voice that a stock typeface cannot. But making one often means printing a templa..."
keywords: "you, font, your, can, letters, make, handfonty, handwriting"
generated: "2026-10-26T12:37:04.186882"
---

# I built HandFonty: turn your handwriting into an installable font in your browser

## Overview

A personal handwriting font can give a side project, invitation, or design a voice that a stock typeface cannot. But making one often means printing a template, scanning it, and moving between tools. I built HandFonty to make that workflow happen in the browser: draw your characters, refine how they fit together, and download a real OTF or TTF font. Here is how it works, and a few of the design decisions behind it. 1. Draw the letters yourself Each character has its own guided cell, with a baseline and a faint reference letter. You can draw with a mouse, finger, or stylus, and choose a pen, marker, or fountain-nib brush. Adjustable smoothing helps clean up shaky strokes. The reference letters are drawing guides; they are never included in your exported font. This is a hands-on lettering tool: the characters come from your strokes. You do not need to scan a page or install a desktop font editor. 2. Make the letters work together A collection of nice-looking letters is only the beginning. Once you type a sentence, uneven spacing can become much more noticeable than the shape of an individual glyph. HandFonty lets you adjust the space before and after each character, its vertical position and scale, and the global letter spacing. Neighbouring letters stay visible while you make changes, so you can judge the rhythm of the text. There are also glyph variants and custom ligatures in the Pro feature set, for lettering that needs more than one version of a character or a custom combination of letters. 3. Preview and export an actual font Preview a pangram or type your own text, then build and download OTF and TTF files. These are vector fonts that can be installed on macOS and Windows and used in design tools. One deliberate choice: missing characters are never silently replaced with letters from another font. An incomplete export is clearly marked as a draft. I want the output to reflect what you actually drew. What you can make A personal handwriting font for notes, cards, invitations, or journals. A reusable typeface from your calligraphy or brush lettering. Custom lettering for a prototype or a personal design project. The editor works in desktop and mobile browsers and has English and Simplified Chinese interfaces. Your first font is free to make and export for personal use, with no card required. Pro unlocks start at $5.99 per font and include commercial licensing and additional features. There is also an optional Studio subscription. Full pricing and plan details . Try it and tell me what feels awkward You can try it at handfonty.com . I would especially like feedback on the spacing workflow: when you preview a sentence made from your own handwriting, which adjustment do you wish were easier to make?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/larusyang/i-built-handfonty-turn-your-handwriting-into-an-installable-font-in-your-browser-2ak5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
