---
title: "I built a PDF toolkit that never uploads your files"
slug: "i-built-a-pdf-toolkit-that-never-uploads-your-files"
author: "Jose Dario"
source: "devto_webdev"
published: "Fri, 13 Nov 2026 14:10:13 +0000"
description: "Every "free" PDF converter I tried asked me to upload the file first. For a bank statement or a signed contract, that is the whole problem: you are handing a..."
keywords: "pdf, you, file, not, page, would, text, first"
generated: "2026-11-13T14:27:37.206972"
---

# I built a PDF toolkit that never uploads your files

## Overview

Every "free" PDF converter I tried asked me to upload the file first. For a bank statement or a signed contract, that is the whole problem: you are handing a document to a server you know nothing about, and hoping it gets deleted. So I built ConvUp , a converter that runs entirely in the browser. No upload endpoint, no account, no watermark. What is actually possible in a browser today More than I expected. The stack: pdf-lib — create, merge, split, rotate, number pages, draw text, embed images. pdf.js — render pages to canvas for JPG export and for OCR input. Tesseract.js — OCR in a Web Worker, with the language model cached after first use. JSZip — build .docx and .zip files client-side. Web Audio + a Worker — decode and re-encode audio to MP3/WAV. The only network requests are the app's own static files and, for OCR, the Tesseract language model from a public CDN. Your document never appears in any request. That is verifiable: open DevTools, go to Network, convert a file. Rotating a PDF is one attribute, not a re-render The first tool I wrote was "rotate pages". It is four lines: const doc = await PDFDocument . load ( bytes ) ; const page = doc . getPages ( ) [ i ] ; const current = page . getRotation ( ) . angle || 0 ; page . setRotation ( degrees ( ( current + 90 ) % 360 ) ) ; No pixels are touched. A PDF page carries a rotation attribute that the viewer applies when drawing; changing it fixes a sideways scan without recompressing anything, so text stays selectable and images keep their resolution. That distinction matters: most online tools re-render the page to an image and hand you back a heavier, blurrier file. The three parts that are genuinely hard 1. Scanned PDFs. A scan has no text layer. Converting it to Word gives you an empty document. The honest fix is OCR first, then convert — and even then, accuracy depends on 300 dpi, straight pages and printed text. Handwriting and shadows still fail. 2. Multi-column layouts. A PDF does not store paragraphs; it stores text fragments at coordinates. To rebuild a document you group fragments by baseline and guess the reading order. Single column: fine. Two or three columns, tables, footers mixed into the body: the order comes out scrambled and needs manual fixes. I decided not to pretend otherwise and said so in the UI. 3. Memory. Everything happens in the tab. A 200 MB audio file or a 600-page scan can kill it. The limits (15 minutes of audio, 40 PDFs to merge, 500 MB per file) exist because the browser is the machine doing the work. The trade-off nobody mentions Local processing means the user's device pays the cost. A 40-page scanned PDF compressed in the browser takes seconds to minutes depending on the CPU, while a server farm would do it in one. I think it is the right trade for documents you would not email to a stranger, but it is a trade. Ads, stated plainly The site is free and has ads. They load when you open a tool, and in the EU, the UK and Switzerland only after you accept. No pop-ups on the homepage, no forced clicks, no "wait 30 seconds to download". The file is generated before any ad gate. What I would do differently I would start with the guides, not the tools. Search traffic came from "compress a PDF for a 2 MB form", not from "pdf converter". I would test on a low-end Android phone from day one. That is where memory limits actually bite. I would not build eleven tools before validating one. If you want to try it: convup.lodcrafttools.workers.dev . If something breaks, tell me which file and what you expected — I would rather fix a real failure than add a feature nobody asked for.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lodcraftgames/i-built-a-pdf-toolkit-that-never-uploads-your-files-l0a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
