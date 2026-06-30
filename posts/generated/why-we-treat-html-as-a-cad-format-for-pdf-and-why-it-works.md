---
title: "Why We Treat HTML as a CAD Format for PDF (And Why It Works)"
slug: "why-we-treat-html-as-a-cad-format-for-pdf-and-why-it-works"
author: "Bonzai2Carn"
source: "devto_webdev"
published: "Tue, 30 Jun 2026 04:00:00 +0000"
description: "Most PDF-to-HTML tools stop at extraction. You get a dump of text, maybe some tables, and a "download HTML" button. That's the end of the story. We didn't st..."
keywords: "you, html, edit, pdf, what, element, drag, document"
generated: "2026-06-30T04:06:54.983552"
---

# Why We Treat HTML as a CAD Format for PDF (And Why It Works)

## Overview

Most PDF-to-HTML tools stop at extraction. You get a dump of text, maybe some tables, and a "download HTML" button. That's the end of the story. We didn't stop there. And the reason is simple: extracted HTML is not a document you're done with. It's a document you're about to edit. PDF Processor Repo The problem with "extracted output" When you extract a PDF, you get a structural snapshot of the original. That snapshot is close to what you want, but rarely exactly what you want. Tables have merged cells that should be split. Headings got classified as paragraphs. A two-column layout that made sense in print looks wrong on a screen. A numbered list starts at 3 because the PDF had a callout box in between. Most tools hand you this output and say: open it in Word, fix it there. That's a context switch. Every context switch is friction. Friction compounds. HTML is already a spatial document format Here's what most people don't realize: HTML rendered in a browser is a box model. Every element (every heading, paragraph, table, callout) is a box with dimensions, position, and CSS-computed layout. The browser calculates all of this automatically. That box model is essentially a CAD coordinate system. You already have: Positioned containers (zones, columns, regions) Reflowable layout (CSS Grid) Semantic element types (headings, paragraphs, lists, tables) A full editing surface (contenteditable) What was missing was the interaction layer to treat it like one. Two modes, one surface The Doc tab in Ginexys PDF Processor has two modes on the same surface: Edit Mode: the existing contenteditable surface. Click into text, type, use the formatting toolbar. The browser handles all the text editing mechanics. This is what you use when you're making content corrections. Selection Mode: a layout editing layer. Click "Select" in the toolbar. Now every extracted zone and region gets a drag handle. You can: Drag zones to reorder sections of the page Drag individual regions (headings, paragraphs, tables) within or across zones Marquee-select multiple regions and group them into a new zone Right-click any element and choose "Edit Code" to see and edit its raw HTML in a Monaco editor Switch back to Edit Mode with the same button. The two modes share the same DOM, with no conversion and no re-render. Why not absolute positioning? The obvious CAD metaphor is Figma: drag elements freely, place them anywhere. We explicitly chose not to do this. The reason is that our output is HTML, and HTML in a browser is a flow document. Absolute positioning breaks that. An absolutely-positioned element is outside the flow: it doesn't affect other elements, doesn't respond to container resizes, and doesn't export correctly to Markdown or XML or DOC. Drag-to-reorder in document flow is more useful than drag-to-anywhere. You're reorganizing a document, not designing a poster. Edit Code: the escape hatch Every extracted element has a "Edit Code" option in the right-click menu. This opens a Monaco editor dialog with the element's raw outerHTML . You can: Add a CSS class Change the tag from <h4> to <h3> Rewrite a paragraph's content entirely Fix a table cell that parsed incorrectly Add an attribute Click Apply. The element is replaced in the live DOM. The change propagates to the Monaco source editor and the Visual Diff tab automatically. This is the escape hatch that makes the higher-level tools trustworthy. If the drag handles can't express what you need, the code editor can. The export chain closes the loop Selection Mode and Edit Code aren't decorative. Every change you make in the Doc tab flows through the same sync coordinator ( applyHtmlEverywhere ) that the Monaco source editor uses. When you export: HTML: the edited DOM, with images inlined as base64 Markdown: converted from the live DOM structure (real GFM: pipe tables, ### headings, - bullets ) XML: semantic tree ( <heading level="3"> , <table><row><cell> ) DOC: Office Open XML envelope, opens in Word/LibreOffice/Google Docs PDF: browser print dialog, scoped to the Doc content What you see is what you export. SiaS: the tool works without the service This is the SiaS (Software-in-a-Service) model applied. The offline tool, which includes geometry extraction, Doc editing, Selection Mode, Edit Code, and all five export formats, works entirely without an account, without a server, without any network connection. The AI layer (Docling-powered extraction, GINEX schema analysis) sits on top. It makes the tool smarter. But the tool is already useful without it. The CAD layer is part of the base tool. It always will be. Ginexys PDF Processor is available at ginexys.com. Free, offline, no account required.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bonzai2carn/why-we-treat-html-as-a-cad-format-for-pdf-and-why-it-works-1j8f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
