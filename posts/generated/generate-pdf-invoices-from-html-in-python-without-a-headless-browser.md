---
title: "Generate PDF invoices from HTML in Python — without a headless browser"
slug: "generate-pdf-invoices-from-html-in-python-without-a-headless-browser"
author: "Hani Amro"
source: "devto_python"
published: "Wed, 24 Jun 2026 09:30:19 +0000"
description: "Almost every app eventually has to turn HTML into a PDF: invoices, receipts, reports, tickets, certificates. The reflex is "spin up Puppeteer / headless Chro..."
keywords: "html, page, pdf, you, right, invoice, class, weasyprint"
generated: "2026-06-24T09:40:50.188555"
---

# Generate PDF invoices from HTML in Python — without a headless browser

## Overview

Almost every app eventually has to turn HTML into a PDF: invoices, receipts, reports, tickets, certificates. The reflex is "spin up Puppeteer / headless Chrome." Then you inherit: a ~300 MB Chromium in every container, --no-sandbox and font headaches, Chrome crashing under load and memory leaks, slow cold starts that make serverless painful. You wanted a PDF. You got a browser to babysit. For HTML + CSS — which is what invoices are — you don't need a browser. Here's the lighter way. Contents WeasyPrint: HTML/CSS → PDF, no browser A real, styled invoice The margins / sizing gotcha Multi-page reports: page numbers + headers When you DO still need a browser Prefer not to host it yourself? Wrap-up WeasyPrint turns HTML and CSS into PDF without a browser pip install weasyprint # system libs (Debian/Ubuntu): apt install libpango-1.0-0 libpangocairo-1.0-0 from weasyprint import HTML HTML ( string = " <h1>Invoice #1042</h1><p>Total: $99</p> " ). write_pdf ( " invoice.pdf " ) That's the whole dependency story. No Chromium, no sandbox flags. A real, styled invoice from weasyprint import HTML INVOICE = """ <!doctype html><html><head><meta charset= " utf-8 " ><style> body { font-family: Arial, sans-serif; color:#1a1a1a; } .head { display:flex; justify-content:space-between; } h1 { color:#2563eb; margin:0; } table { width:100%; border-collapse:collapse; margin-top:24px; } th,td { padding:10px 8px; border-bottom:1px solid #e5e7eb; text-align:left; } th { background:#f8fafc; } .right { text-align:right; } .total { font-size:1.2em; font-weight:700; } </style></head><body> <div class= " head " > <div><h1>Invoice</h1><div>#1042 · 23 Jun 2026</div></div> <div class= " right " ><strong>Acme Corp</strong><br>billing@acme.com</div> </div> <table> <tr><th>Item</th><th class= " right " >Qty</th><th class= " right " >Price</th></tr> <tr><td>API plan — Pro</td><td class= " right " >1</td><td class= " right " >$12.00</td></tr> <tr><td>Overage (320 req)</td><td class= " right " >320</td><td class= " right " >$0.96</td></tr> <tr><td class= " right total " colspan= " 2 " >Total</td><td class= " right total " >$12.96</td></tr> </table> </body></html> """ HTML ( string = INVOICE ). write_pdf ( " invoice.pdf " ) You control every pixel with normal CSS — no template-engine lock-in. The gotcha everyone hits with margins and sizing Two complaints come up constantly with HTML→PDF: Huge side margins → that's the page margin, not your HTML. Content looks shrunk/tiny → the converter is doing "shrink to fit" because your layout is wider than the page. Both are fixed with a CSS @page rule — the bit most online converters silently ignore: @page { size : A4 ; /* or Letter, A5, or "210mm 297mm" */ margin : 12mm ; /* exactly what you want; margin: 0 for edge-to-edge */ } For the shrinking problem, make sure your content width fits the page (use mm/relative units, not a fixed 1200px container) — then nothing gets scaled down. Multi-page reports with page numbers and repeating headers For anything longer than a page, @page gives you running page numbers in pure CSS — no JS, no manual pagination: @page { size : A4 ; margin : 20mm 15mm ; @bottom-center { content : "Page " counter ( page ) " of " counter ( pages ); } } thead { display : table-header-group ; } /* repeat the header row on every page */ Already have a Word or Excel template? Don't rebuild it in HTML — convert it with headless LibreOffice: soffice --headless --convert-to pdf --outdir out/ invoice.docx Call it via subprocess ; give each call its own -env:UserInstallation=file:///tmp/lo_xyz dir so concurrent runs don't collide. When you DO still need a real browser Honest caveat: WeasyPrint doesn't run JavaScript. If your document only exists after client-side JS draws it (a heavy charting lib, a SPA view), you still need headless Chrome for that one case. For static HTML + CSS — 95% of invoices, reports, and receipts — WeasyPrint is lighter, faster, and safer. Prefer not to host it at all? Running WeasyPrint means installing Pango/Cairo and keeping it patched. If it's one feature among many, offload it to an HTTP call. I maintain a flat-priced PDF API where html-to-pdf is one endpoint (SSRF-hardened — internal URLs are blocked — and the same key also does merge, OCR, Office→PDF, etc.). Free tier is 1,000 requests/month, no card. Disclosure: I built it. import requests requests . post ( " https://pdf-tools-api2.p.rapidapi.com/html-to-pdf " , headers = { " X-RapidAPI-Key " : " YOUR_KEY " , " X-RapidAPI-Host " : " pdf-tools-api2.p.rapidapi.com " }, data = { " html " : INVOICE , " page_size " : " A4 " }, ) Wrap-up You don't need to ship a browser to make a PDF. For HTML + CSS, WeasyPrint renders invoices and reports in one call, @page gives you exact margins and page numbers, and LibreOffice covers Word/Excel templates. Save headless Chrome for the rare JS-rendered case. Your turn: what are you generating — invoices, reports, labels? And what bit you: margins, fonts, or page breaks? 👇 Try the PDF API free — 1,000 requests/month, no card *Built and maintained by a solo developer (based in Syria) who actually answers — questions welcome in the comments!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/h_amro_13de6b93cc1ce/generate-pdf-invoices-from-html-in-python-without-a-headless-browser-34l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
