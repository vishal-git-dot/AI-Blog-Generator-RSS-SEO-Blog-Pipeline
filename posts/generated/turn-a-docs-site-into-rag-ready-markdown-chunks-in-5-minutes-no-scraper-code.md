---
title: "Turn a docs site into RAG-ready Markdown chunks in 5 minutes (no scraper code)"
slug: "turn-a-docs-site-into-rag-ready-markdown-chunks-in-5-minutes-no-scraper-code"
author: "Rabii Slimane"
source: "devto_python"
published: "Thu, 12 Nov 2026 23:06:57 +0000"
description: "You want a chatbot that answers questions about a library's documentation. The hard part is rarely the LLM. It is getting the docs out of HTML and into clean..."
keywords: "fastapi, page, pages, chunks, docs, chunk, you, url"
generated: "2026-11-12T23:24:23.222918"
---

# Turn a docs site into RAG-ready Markdown chunks in 5 minutes (no scraper code)

## Overview

You want a chatbot that answers questions about a library's documentation. The hard part is rarely the LLM. It is getting the docs out of HTML and into clean, well-cut chunks: no navigation menus, no cookie banners, no footers repeated on every page, and chunks that keep track of which section they came from. This walkthrough takes the FastAPI documentation, converts it to Markdown, cuts it into ~400-token chunks with their heading path, and loads them into a local vector store. Total code: about 25 lines of Python. What you need Python 3.9+ A free Apify account (the free plan's monthly credit covers this tutorial many times over) pip install apify-client chromadb We use the Web Page to Markdown Actor for the conversion. Disclosure: I built it. It costs $1 per 1,000 pages converted, and failed pages are free. Everything below also works with any tool that gives you clean Markdown plus heading-aware chunks; this one just does both in one call. Step 1: Point it at the sitemap Most docs sites publish a sitemap.xml . Giving the sitemap instead of a list of URLs means new pages are picked up automatically the next time you run it. import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ "APIFY_TOKEN" ] ) run = client . actor ( "blueberry_rainstorm/web-page-to-markdown" ) . call ( run_input = { "urls" : [ ] , # only the sitemap this time "sitemapUrls" : [ { "url" : "https://fastapi.tiangolo.com/sitemap.xml" } ] , "maxPages" : 50 , # keep the first test small "contentMode" : "main" , # drop menus, sidebars and footers "chunkSize" : 400 , # ~tokens per chunk "chunkOverlap" : 50 , } ) pages = list ( client . dataset ( run [ "defaultDatasetId" ] ) . iterate_items ( ) ) print ( len ( pages ) , "pages" ) On a test run with maxPages: 5 , the five pages came back in 2.4 seconds without a browser, because the FastAPI docs are static HTML. JavaScript-only pages are detected and re-rendered in Chrome automatically. Step 2: Look at what came back Each page is one item with metadata, the full Markdown, and the chunks: { "url" : "https://fastapi.tiangolo.com/" , "status" : "ok" , "title" : "FastAPI - FastAPI" , "description" : "FastAPI framework, high performance, easy to learn, fast to code, ready for production" , "language" : "en" , "canonicalUrl" : "https://fastapi.tiangolo.com/" , "wordCount" : 2134 , "approxTokens" : 4139 , "renderedWithBrowser" : false , "markdown" : "# FastAPI - FastAPI\n\n*FastAPI framework, high performance, easy to learn..." , "chunks" : [ { "index" : 0 , "headingPath" : "FastAPI - FastAPI" , "text" : "..." , "approxTokens" : 400 } ] } Two fields matter most for RAG: headingPath (for example Concurrency and async / await - FastAPI > In a hurry? ). Store it as metadata, and prepend it to the chunk text before embedding. A chunk that starts "Use async def when..." is much easier to retrieve when the embedding also knows it sits under "Concurrency and async / await". approxTokens lets you check the budget before you embed: on our 5-page test the pages ranged from 103 to 5,428 tokens and became 89 chunks in total. Step 3: Load the chunks into a vector store Chroma runs locally and embeds with a small default model, so there is nothing else to sign up for. import chromadb db = chromadb . PersistentClient ( path = "./fastapi-index" ) col = db . get_or_create_collection ( "fastapi-docs" ) ids , docs , metas = [ ] , [ ] , [ ] for page in pages : if page [ "status" ] != "ok" : continue # failed pages are listed, not charged for chunk in page . get ( "chunks" ) or [ ] : ids . append ( f '{page["url"]}#{chunk["index"]}' ) docs . append ( f '{chunk["headingPath"]}\n\n{chunk["text"]}' ) metas . append ( { "url" : page [ "url" ] , "title" : page . get ( "title" ) or "" , "section" : chunk [ "headingPath" ] } ) col . upsert ( ids = ids , documents = docs , metadatas = metas ) print ( col . count ( ) , "chunks indexed" ) Using the page URL plus the chunk index as the id makes re-runs safe: upsert replaces chunks instead of duplicating them. Step 4: Ask it something hits = col . query ( query_texts = [ "When should I use async def instead of def?" ] , n_results = 3 ) for meta in hits [ "metadatas" ] [ 0 ] : print ( meta [ "section" ] , "->" , meta [ "url" ] ) Pass the top chunks, with their URLs, to the LLM of your choice and ask it to cite the URL. Because each chunk carries its source page and section, the answer can link back to the exact part of the docs. Tips from running this on real sites Main content vs full page. "contentMode": "main" is right for docs, blogs and articles. For homepages, product pages and listings, use "full" so nothing important is cut. Strip site-specific clutter with removeSelectors , for example .related-posts, #comments, .edit-this-page . Keep it fresh. Schedule the run weekly in Apify and re-run the upsert. Only pages that exist get re-embedded, and the ids stay stable. Respect the site. Use it on documentation you are allowed to reuse (your own, or open-source docs under a permissive license), and keep maxConcurrency modest on small sites. Cost of this tutorial 50 pages at $1 per 1,000 pages is $0.05. The Chroma part runs on your machine for free. If you try this on another docs site and something comes out messy (tables, code blocks, odd navigation), tell me which site in the Actor's Issues tab and I will look at it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rabii_slimane_22e39df3bdd/turn-a-docs-site-into-rag-ready-markdown-chunks-in-5-minutes-no-scraper-code-59j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
