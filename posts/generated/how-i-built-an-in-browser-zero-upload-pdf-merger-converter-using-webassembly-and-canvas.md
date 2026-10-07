---
title: "How I Built an In-Browser, Zero-Upload PDF Merger & Converter Using WebAssembly and Canvas"
slug: "how-i-built-an-in-browser-zero-upload-pdf-merger-converter-using-webassembly-and-canvas"
author: "Taqi Raza"
source: "devto_webdev"
published: "Wed, 07 Oct 2026 22:35:28 +0000"
description: "Whenever you search for a simple utility like "Merge PDF" or "Convert WebP to PNG" , you are usually greeted by the same frustrating experience: A 15MB file ..."
keywords: "pdf, const, browser, await, zero, document, memory, mergedpdf"
generated: "2026-10-07T22:56:27.548053"
---

# How I Built an In-Browser, Zero-Upload PDF Merger & Converter Using WebAssembly and Canvas

## Overview

Whenever you search for a simple utility like "Merge PDF" or "Convert WebP to PNG" , you are usually greeted by the same frustrating experience: A 15MB file upload limit behind an aggressive paywall. A subscription pop-up asking for $12/month. Your sensitive personal documents (tax returns, signed contracts, medical records) getting uploaded to an untrusted remote server. As developers, we know that modern browsers have hardware-accelerated GPUs, multi-threaded Web Workers, and WebAssembly. There is zero technical justification for uploading a document to a cloud server just to merge two pages or change an image format. So I decided to build SwiftUtils — a suite of 100% client-side, zero-upload web utilities that process everything directly in browser memory. Here is the exact technical architecture behind how it works. 1. In-Browser PDF Merging with Zero Cloud Leaks Most online PDF services transmit your PDFs across the wire to a backend running poppler or pdfcpu . Instead, we can load the document structure directly into browser memory using pdf-lib : javascript import { PDFDocument } from 'pdf-lib'; async function mergePDFsInBrowser(fileList) { // 1. Create a fresh document in browser memory const mergedPdf = await PDFDocument.create(); for (const file of fileList) { const arrayBuffer = await file.arrayBuffer(); // 2. Parse the PDF structure locally const pdf = await PDFDocument.load(arrayBuffer); const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices()); // 3. Append pages to the merged document copiedPages.forEach((page) => mergedPdf.addPage(page)); } // 4. Save and generate a local memory blob const pdfBytes = await mergedPdf.save(); const blob = new Blob([pdfBytes], { type: 'application/pdf' }); return URL.createObjectURL(blob); }

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/taqi_raza_92/how-i-built-an-in-browser-zero-upload-pdf-merger-converter-using-webassembly-and-canvas-1351

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
