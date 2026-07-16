---
title: "Browser-Based PDF Page Editing with Vue 3 and pdf-lib"
slug: "browser-based-pdf-page-editing-with-vue-3-and-pdf-lib"
author: "sunshey"
source: "devto_webdev"
published: "Thu, 16 Jul 2026 13:41:19 +0000"
description: "True PDF text editing is hard. PDF was designed as a fixed-layout format, not an editable document format. But page-level edits — reorder, rotate, delete, in..."
keywords: "pdf, page, const, pages, editing, value, lib, file"
generated: "2026-07-16T14:05:41.531154"
---

# Browser-Based PDF Page Editing with Vue 3 and pdf-lib

## Overview

True PDF text editing is hard. PDF was designed as a fixed-layout format, not an editable document format. But page-level edits — reorder, rotate, delete, insert, sign, watermark — are much easier, and they cover most real-world PDF needs. This post walks through a browser-based page editor built with Vue 3 and pdf-lib . Why browser-based page editing? Most PDF edits people actually need are structural: Reorder pages before a meeting Delete the blank page at the end Rotate a scanned page Insert pages from another PDF Add a signature or watermark Add page numbers to a report A browser-based tool handles these without uploading files to a server. That matters for contracts, resumes, and financial documents. The stack Vue 3 with Composition API pdf-lib for page-level manipulation pdfjs-dist for thumbnails and metadata Native File API for local uploads Minimal implementation < script setup lang= "ts" > import { ref } from ' vue ' import { PDFDocument } from ' pdf-lib ' const pages = ref < { file : File ; pdf : PDFDocument ; thumbnail : string }[] > ([]) const selectedPages = ref < number [] > ([]) async function loadPdf ( file : File ) { const bytes = await file . arrayBuffer () const pdf = await PDFDocument . load ( bytes ) pages . value . push ({ file , pdf , thumbnail : await renderThumbnail ( pdf ) }) } async function rotatePage ( pageIndex : number , degrees : number ) { const page = pages . value [ pageIndex ]. pdf . getPage ( pageIndex ) page . setRotation ({ angle : page . getRotation (). angle + degrees }) } async function deletePage ( pageIndex : number ) { const pdf = pages . value [ 0 ]. pdf pdf . removePage ( pageIndex ) pages . value = pages . value . filter (( _ , i ) => i !== pageIndex ) } async function movePage ( fromIndex : number , toIndex : number ) { const pdf = pages . value [ 0 ]. pdf // pdf-lib doesn't support movePage, so we rebuild page order const newOrder = [... Array ( pdf . getPageCount ()). keys ()] newOrder . splice ( fromIndex , 1 ) newOrder . splice ( toIndex , 0 , fromIndex ) const reordered = await PDFDocument . create () for ( const i of newOrder ) { const [ copiedPage ] = await reordered . copyPages ( pdf , [ i ]) reordered . addPage ( copiedPage ) } pages . value [ 0 ]. pdf = reordered } async function saveResult () { const pdf = pages . value [ 0 ]. pdf const bytes = await pdf . save () const blob = new Blob ([ bytes ], { type : ' application/pdf ' }) downloadBlob ( blob , ' edited.pdf ' ) } function downloadBlob ( blob : Blob , filename : string ) { const url = URL . createObjectURL ( blob ) const a = document . createElement ( ' a ' ) a . href = url a . download = filename a . click () URL . revokeObjectURL ( url ) } </ script > The key is that pdf-lib treats pages as objects you can manipulate: add, remove, copy, rotate, and reorder. It does not rewrite the text layer, which is why page-level editing is fast and reliable. Inserting pages from another PDF A common need is to insert pages from one PDF into another. With pdf-lib , this is straightforward: async function insertPages ( sourcePdf , targetPdf , insertAfterIndex ) { const sourcePages = await sourcePdf . getPages () const targetPageCount = targetPdf . getPageCount () // Copy pages from source to target const copiedPages = await targetPdf . copyPages ( sourcePdf , sourcePages . map (( _ , i ) => i ) ) // Insert after the specified index copiedPages . forEach (( page , i ) => { targetPdf . insertPage ( insertAfterIndex + i + 1 , page ) }) } The limits of browser-based editing Page-level editing is not the same as text editing. If a user needs to change the actual words inside a PDF, you are looking at a much harder problem: PDFs store text as glyph positions, not as editable paragraphs Fonts may be embedded or subsetted Layout changes can break the entire page For text-level editing, redirect users to a desktop tool like Wondershare PDFelement . UX tips from a live tool At en.sotool.top/organize-pdf , we learned a few things: Thumbnails matter. Users want to see the page before they delete, rotate, or reorder it. Undo is essential. Accidental page deletion is common. We track page states so users can undo. Separate edit and download. Track "completed edit" and "downloaded" as separate events. Be honest about limits. The page clearly states what can and cannot be edited. Users trust that. Tracking the funnel We use GA4 custom events: onFileUpload ( file ) onActionClick ( ' organize ' ) onPageAction ( ' rotate ' | ' delete ' | ' insert ' | ' reorder ' ) onCompleted ({ page_count : pages . value . length }) onDownload ({ file_count : 1 }) This shows which actions users actually perform and where they drop off. Going further For page-level PDF editing, pdf-lib plus Vue 3 is enough. If you need to edit text, OCR, or create complex forms, you need a desktop PDF editor. Want to see the full source? The site is built in public at github.com/sunshey/pdf-tool . If you need desktop-grade PDF editing — text editing, OCR, form management, or certified redaction — check out Wondershare PDFelement .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sunshey/browser-based-pdf-page-editing-with-vue-3-and-pdf-lib-3051

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
