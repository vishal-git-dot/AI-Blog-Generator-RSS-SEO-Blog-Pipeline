---
title: "My PPTX converter silently dropped half a pitch deck — SmartArt text lives in a different XML part"
slug: "my-pptx-converter-silently-dropped-half-a-pitch-deck-smartart-text-lives-in-a-different-xml-part"
author: "InApp"
source: "devto_ai"
published: "Mon, 05 Oct 2026 23:36:02 +0000"
description: "A user ran their investor deck through my PPTX-to-Markdown converter and chunks of content just vanished. No errors. Titles, bullet lists, tables all fine — ..."
keywords: "text, content, slide, decks, pptx, deck, smartart, lives"
generated: "2026-10-05T23:55:08.865300"
---

# My PPTX converter silently dropped half a pitch deck — SmartArt text lives in a different XML part

## Overview

A user ran their investor deck through my PPTX-to-Markdown converter and chunks of content just vanished. No errors. Titles, bullet lists, tables all fine — but an entire market-growth section came back nearly empty. I unzipped the .pptx (it's just a ZIP of XML parts) and compared a broken slide against a working one. The text boxes I expected were there, but the missing content sat inside <p:graphicFrame> elements referencing a diagram namespace. PowerPoint SmartArt isn't stored in the slide at all — the shape is only a placeholder holding a relationship ID. The actual text lives in /ppt/diagrams/data1.xml , as a hierarchy of nodes with its own paragraph runs. My parser walked <p:sp> shape elements only. SmartArt is a graphicFrame with a dgm:relIds reference — a different animal entirely. Every deck I'd tested with was built from plain text boxes, so my tests were green while a huge class of real decks dropped content silently. The fix: resolve each graphicFrame's relationship, parse the diagram data part, walk the dgm:pt nodes and pull the <a:t> runs inside each, then emit them as a bullet list at the position where the frame sits on the slide, so reading order is preserved alongside the shapes before and after it. Grouped shapes had the same bug, by the way — text inside a group lives in the group's sub-shapes, not the top level. The lesson I took: "extract the text from a slide" is a fiction for OOXML formats. Text is scattered across parts joined by relationships, and PowerPoint features you never use still show up in real decks. Synthetic test files built the same way as your parser will always pass. Real decks created from Microsoft's own templates are the only test suite that matters. I ended up packaging it as https://x402.freeq.one/tools/pptx_to_markdown.html so pipelines can turn decks — diagram content included — into LLM-readable text without a PowerPoint install.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/imapphelp/my-pptx-converter-silently-dropped-half-a-pitch-deck-smartart-text-lives-in-a-different-xml-part-14kp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
