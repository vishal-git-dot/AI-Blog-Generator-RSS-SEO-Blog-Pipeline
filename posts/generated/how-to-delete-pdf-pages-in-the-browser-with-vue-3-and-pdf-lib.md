---
title: "How to Delete PDF Pages in the Browser with Vue 3 and pdf-lib"
slug: "how-to-delete-pdf-pages-in-the-browser-with-vue-3-and-pdf-lib"
author: "sunshey"
source: "devto_webdev"
published: "Tue, 25 Aug 2026 12:52:13 +0000"
description: "Deleting pages from PDF seems simple, but there are important considerations around index management and data safety. Here's how to build a browser-based PDF..."
keywords: "index, pdf, const, value, page, pages, pagestodelete, deleting"
generated: "2026-08-25T12:56:12.657125"
---

# How to Delete PDF Pages in the Browser with Vue 3 and pdf-lib

## Overview

Deleting pages from PDF seems simple, but there are important considerations around index management and data safety. Here's how to build a browser-based PDF page deletion tool with Vue 3 and pdf-lib . The challenge: Index management When deleting multiple pages, the indices shift. If you delete page 2 first, what was page 3 becomes page 2. This can lead to deleting the wrong pages if not handled correctly. The stack Vue 3 with Composition API pdf-lib for PDF manipulation Vite for bundling The core implementation < script setup lang= "ts" > import { ref } from ' vue ' import { PDFDocument } from ' pdf-lib ' const file = ref < File | null > ( null ) const pagesToDelete = ref < number [] > ([]) const deleting = ref ( false ) const result = ref < Uint8Array | null > ( null ) async function deletePages () { if ( ! file . value || pagesToDelete . value . length === 0 ) return deleting . value = true const arrayBuffer = await file . value . arrayBuffer () const pdf = await PDFDocument . load ( arrayBuffer ) const totalPages = pdf . getPageCount () // Validate and sort indices (delete from back to front) const validIndices = pagesToDelete . value . filter ( index => index >= 0 && index < totalPages ) . sort (( a , b ) => b - a ) // Descending order for ( const index of validIndices ) { pdf . removePage ( index ) } result . value = await pdf . save () deleting . value = false } </ script > Key implementation details 1. Index validation Ensure indices are within bounds: const validIndices = pagesToDelete . value . filter ( index => index >= 0 && index < totalPages ) 2. Delete from back to front Prevent index shift issues: . sort (( a , b ) => b - a ) // Descending order 3. User interface Provide a visual page selector: <div class= "page-grid" > <div v-for= "(page, index) in totalPages" :key= "index" :class= "['page-item', { deleted: pagesToDelete.includes(index) }]" @ click= "togglePage(index)" > {{ index + 1 }} </div> </div> 4. Batch operations Support selecting multiple pages: function togglePage ( index : number ) { const pos = pagesToDelete . value . indexOf ( index ) if ( pos >= 0 ) { pagesToDelete . value . splice ( pos , 1 ) } else { pagesToDelete . value . push ( index ) } } Limitations No undo Once pages are deleted, they cannot be recovered. Solution : Always keep a backup of the original PDF. Large files Very large PDFs may cause memory issues. Solution : Process in smaller batches or use Web Workers. Summary Building a browser-based PDF page deletion tool involves: Loading the PDF with pdf-lib Validating page indices Sorting for back-to-front deletion Removing pages and saving Try it at en.sotool.top/delete-pages .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sunshey/how-to-delete-pdf-pages-in-the-browser-with-vue-3-and-pdf-lib-2gge

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
