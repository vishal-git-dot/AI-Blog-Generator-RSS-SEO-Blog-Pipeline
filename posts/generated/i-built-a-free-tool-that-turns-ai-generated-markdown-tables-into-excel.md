---
title: "I built a free tool that turns AI-generated Markdown tables into Excel"
slug: "i-built-a-free-tool-that-turns-ai-generated-markdown-tables-into-excel"
author: "Lanxk"
source: "devto_webdev"
published: "Fri, 16 Oct 2026 20:19:36 +0000"
description: "Tables from ChatGPT, Claude or Gemini are written in Markdown. Paste one into Excel and every row ends up in column A, pipes and all. So I built a free onlin..."
keywords: "excel, markdown, tables, built, free, tool, paste, xlsx"
generated: "2026-10-16T20:47:14.408196"
---

# I built a free tool that turns AI-generated Markdown tables into Excel

## Overview

Tables from ChatGPT, Claude or Gemini are written in Markdown. Paste one into Excel and every row ends up in column A, pipes and all. So I built a free online tool that converts Markdown tables straight into Excel: https://md-to.com/markdown-to-excel/ Features Paste a whole AI answer or upload a .md file, and every table is extracted automatically Several tables become several sheets, named after the heading above each table 1,234.50 and 12.5% are saved as real numbers; IDs longer than 15 digits stay as text so Excel can't round them Bold, frozen header row and auto-sized columns Download an .xlsx , or copy with one click and paste into Excel Runs entirely in the browser: no uploads, free, no signup How it's built An .xlsx file is a zip archive with a few XML parts. Instead of SheetJS, the tool uses a small hand-written XLSX writer and zips the parts with fflate , with no new dependencies: import { strToU8 , zipSync } from ' fflate ' ; files [ ' xl/styles.xml ' ] = strToU8 ( styles . toXml ()); files [ ' xl/sharedStrings.xml ' ] = strToU8 ( strings . toXml ()); return zipSync ( files , { level : 6 });

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lanxk/i-built-a-free-tool-that-turns-ai-generated-markdown-tables-into-excel-126g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
