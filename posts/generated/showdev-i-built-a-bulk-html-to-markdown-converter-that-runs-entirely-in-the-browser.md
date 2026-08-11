---
title: "ShowDev: I built a bulk HTML-to-Markdown converter that runs entirely in the browser"
slug: "showdev-i-built-a-bulk-html-to-markdown-converter-that-runs-entirely-in-the-browser"
author: "Christoph Dieck"
source: "devto_webdev"
published: "Tue, 11 Aug 2026 18:52:10 +0000"
description: "Most HTML-to-Markdown tools handle one file at a time. You paste some HTML, get Markdown back, repeat. That works for a quick snippet but not when you have 2..."
keywords: "html, markdown, you, files, built, one, get, folder"
generated: "2026-08-11T19:08:47.092299"
---

# ShowDev: I built a bulk HTML-to-Markdown converter that runs entirely in the browser

## Overview

Most HTML-to-Markdown tools handle one file at a time. You paste some HTML, get Markdown back, repeat. That works for a quick snippet but not when you have 200+ pages from a help center export sitting in a folder. I needed exactly that. I had a full site mirror (grabbed with wget --mirror ) and wanted clean Markdown I could feed into an LLM knowledge base. Nothing I found could handle it without uploading files to a server or converting one by one. So I built HTML to Markdown AI . How it works You drop a ZIP file (or individual HTML files) into the browser A Go-based conversion pipeline compiled to WebAssembly processes everything locally You get a ZIP back with clean GitHub-Flavored Markdown, folder structure preserved No server involved. Your files never leave your machine. The conversion pipeline The heavy lifting happens in Go/WASM. The pipeline: Strips navigation, footers, scripts, styles, and other boilerplate noise Extracts the main content from the page Converts to GFM with proper heading hierarchy, tables, code blocks, and links Handles batch processing so you can throw hundreds of files at it Why no built-in crawler? Intentional decision. Downloading HTML from someone else's site has legal implications depending on jurisdiction and terms of service. I don't want to be in that business. Downloading is also the easy part: wget -r -l 0 -np -k -E -p -e robots = off \ --reject-regex '\.(png|jpe?g|gif|svg|webp|woff2?|ttf|css|js|zip|pdf)$' \ -w 0.5 --random-wait \ https://docs.example.com/ That gives you a local folder with all the HTML. The hard and annoying part is turning that into clean, usable Markdown. That's what this tool solves. Stack Frontend: Astro + Tailwind Conversion engine: Go compiled to WebAssembly Processing: Entirely client-side, zero backend Try it https://www.html-to-markdown-ai.com Use cases I've tested it with: Help center exports (Zendesk, Confluence, custom wikis) Documentation sites mirrored with wget/httrack Scraped content for RAG pipelines Training data prep for fine-tuning If you work with LLMs and regularly need to get web content into a format they can digest, this might save you some time. Feedback welcome. What would make this more useful for your workflow?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cdieck88/showdev-i-built-a-bulk-html-to-markdown-converter-that-runs-entirely-in-the-browser-3p3e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
