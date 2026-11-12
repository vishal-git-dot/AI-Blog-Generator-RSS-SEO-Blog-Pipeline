---
title: "Lettering machine-translated manga: fitting text back into speech bubbles"
slug: "lettering-machine-translated-manga-fitting-text-back-into-speech-bubbles"
author: "Leo"
source: "devto_python"
published: "Thu, 12 Nov 2026 14:45:32 +0000"
description: "When people think about translating manga automatically, they think about the translation model. In practice the translation is the easy part. The hard part ..."
keywords: "text, page, balloon, manga, translation, looks, lettering, like"
generated: "2026-11-12T14:55:17.817829"
---

# Lettering machine-translated manga: fitting text back into speech bubbles

## Overview

When people think about translating manga automatically, they think about the translation model. In practice the translation is the easy part. The hard part is everything around it: finding the text, getting it off the page cleanly, and putting the translation back so the page still reads like a comic. This post walks through the image side of an automatic manga translator I work on, and what we learned by comparing our pages with official English and Korean editions. The pipeline Each page goes through five steps: Find the text. A detector marks the regions that contain text. Page numbers, headers and artist watermarks are not dialogue, so they are left alone. Find the speech bubbles. Knowing the shape of each balloon matters twice: once for cleaning and once for lettering. Read the text. Japanese is often vertical, Korean and Chinese mix scripts, and sound effects are drawn rather than typed. Hand-drawn sound effects outside balloons are usually best left as the artist drew them. Erase the original text. Letter the translation into the cleaned page. Translation sits between steps 3 and 5 and sees the whole page at once, so names and tone stay consistent from bubble to bubble. Erasing is harder than it looks The textbook answer is "mask the text and let an inpainting model fill the hole". On a plain white balloon that often leaves faint gray smudges where the letters used to be, and on screentone or detailed art it can invent texture that wasn't there. What worked better for us was treating different backgrounds differently: plain paper, text with a white outline drawn over artwork, and text sitting on gradients or art each get their own handling. We also make sure that nothing outside the text area changes, so the art around a balloon stays exactly as the artist drew it. Lettering: where it looks human or doesn't Making text fit a box is easy. Making it look lettered is not. A few principles mattered most: Fit the balloon, not the box. Text boxes are rectangles, balloons are ovals. Lines should follow the balloon's shape. Don't shout everything. Filling every balloon to the edge looks wrong next to a professionally lettered page. Ordinary dialogue on a page should look like it was lettered at one size; shouts get to be bigger. Keep words whole. Hyphenating dialogue makes it hard to read, so it should be a last resort. Make sure the font can actually draw the character. Some comic fonts claim to support a character but print nothing, which quietly produces blank bubbles in languages like Thai or Vietnamese. Pick readable colors. Text color guessed from a grayscale scan is often a muddy gray. Black on white (or white on black) is almost always what the original letterer intended. Every language breaks lines differently. English breaks at spaces, Chinese between characters with punctuation rules, Korean at spaces with its own habits for ellipses, and Thai needs a dictionary just to find the words. What we learned Most of the problems only show up at scale. A demo page looks fine; page 40 of a chapter is where a stray gray smudge, a hyphen in the wrong place or a bubble that's slightly too full gives it away. Comparing against official editions, page by page, taught us more than any metric did. Try it If you want to see the result on your own pages, Manga Translator is the web app built on this pipeline: upload a manga, manhwa or webtoon page in the browser and download it lettered in English or 50 other languages. I'd like to hear where the lettering still looks off.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/leomanga/lettering-machine-translated-manga-fitting-text-back-into-speech-bubbles-1hg7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
