---
title: "PDF to Markdown for RAG: the 4 problems that silently ruin your retrieval"
slug: "pdf-to-markdown-for-rag-the-4-problems-that-silently-ruin-your-retrieval"
author: "Extas Corporation"
source: "devto_python"
published: "Thu, 12 Nov 2026 00:13:32 +0000"
description: "PDFs are the worst input format for a RAG pipeline. The text is stored as positioned glyphs, not as paragraphs, so a naive extraction gives you broken lines,..."
keywords: "markdown, pdf, you, pages, text, tables, two, column"
generated: "2026-11-12T00:20:19.771272"
---

# PDF to Markdown for RAG: the 4 problems that silently ruin your retrieval

## Overview

PDFs are the worst input format for a RAG pipeline. The text is stored as positioned glyphs, not as paragraphs, so a naive extraction gives you broken lines, columns mixed together and tables turned into word soup. Then your chunks are bad, your embeddings are bad, and the model answers from garbage. Converting each PDF to Markdown first fixes most of this: headings give you natural chunk borders, tables stay readable, and the text is clean enough to embed. Here are the four problems that hurt retrieval the most, how to check for each, and two ways to do the conversion. 1. Two-column pages read in the wrong order Papers and journals use two columns. A simple extractor reads straight across the page, so line 1 of the left column is glued to line 1 of the right column. Check: open the output of a two-column paper and read the second paragraph. If the sentences stop making sense halfway through a line, the columns are mixed. 2. Hard line breaks and hyphenated words PDF lines end where the page ends, not where the sentence ends. You get infor- on one line and mation on the next, and a keyword search for "information" misses it. Check: search the output for -\n . A good converter joins the lines of a paragraph and repairs the split words. 3. Tables A table extracted as plain text loses its columns: the model can no longer tell which number belongs to which header. Markdown tables keep that link and LLMs read them well. Check: find a table in the PDF and look for | rows in the output. 4. Scanned pages A scanned page has no text layer at all. The extractor returns an empty string and that page silently disappears from your index. This is the most dangerous case, because nothing fails. Check: compare the number of pages with the number of characters. A 20-page document with 300 characters is a scan and needs OCR. Option A: do it locally with PyMuPDF For a handful of files with a text layer, this is enough: import pymupdf4llm # pip install pymupdf4llm md = pymupdf4llm . to_markdown ( "paper.pdf" ) open ( "paper.md" , "w" , encoding = "utf-8" ) . write ( md ) You will need to add OCR yourself (Tesseract) for scanned pages, and a queue if you have thousands of files. Option B: a hosted converter for bulk jobs Disclosure: this one is ours. We publish a hosted converter, PDF to Markdown for LLM & RAG , on Apify. It handles the four problems above: two-column reading order, re-joined paragraphs, Markdown tables, and OCR (Tesseract, 7 languages) for pages without a text layer. You give it URLs and it processes them in parallel. from apify_client import ApifyClient # pip install apify-client client = ApifyClient ( "YOUR_APIFY_TOKEN" ) run = client . actor ( "extas_corp/pdf-to-markdown" ) . call ( run_input = { "pdfUrls" : [ { "url" : "https://arxiv.org/pdf/1706.03762" } ] , "extractTables" : True , "ocrScannedPages" : True , } ) for doc in client . dataset ( run [ "defaultDatasetId" ] ) . iterate_items ( ) : print ( doc [ "title" ] , doc [ "pageCount" ] , "pages," , doc [ "ocrPages" ] , "OCR pages" ) markdown = doc [ "markdown" ] Each PDF comes back as one item with status , title , pageCount , ocrPages , tableCount , charCount and markdown . The ocrPages field answers problem 4 directly: you can see which documents were scans. It is free during launch: you only pay Apify's own platform usage, which the free monthly credits cover for small jobs. Limits: 100 MB per PDF, no password-protected files, and very complex merged-cell tables may come out simplified. If you only have one file, there is also a free browser version at hackthehydra.com with no account. Chunk on headings, not on character counts Once you have Markdown, split on headings so each chunk is one coherent section: import re def chunk_by_heading ( markdown , max_chars = 4000 ) : sections = re . split ( r "\n(?=#{1,3} )" , markdown ) for section in sections : for i in range ( 0 , len ( section ) , max_chars ) : yield section [ i : i + max_chars ] Keep the heading inside the chunk: it gives the embedding the context that the body text often lacks. Summary Convert to Markdown before chunking. Test on a two-column paper, a document with tables, and a scan before trusting any converter. Watch for pages with almost no characters: they are scans, and they vanish silently. What breaks most often in your PDF pipeline? I am collecting hard cases to test against.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/extascorp/pdf-to-markdown-for-rag-the-4-problems-that-silently-ruin-your-retrieval-gid

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
