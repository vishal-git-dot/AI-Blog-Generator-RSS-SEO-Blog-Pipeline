---
title: "Searching 10,000 Printable Pages Without a Search Server: A Prebuilt Index, Synonyms and Kid-Friendly Typos"
slug: "searching-10000-printable-pages-without-a-search-server-a-prebuilt-index-synonyms-and-kid-friendly-typos"
author: "Akbo Ichou"
source: "devto_webdev"
published: "Fri, 25 Sep 2026 20:51:41 +0000"
description: "When a site grows past a few hundred pages, category browsing stops being enough. People want to type "t rex" or "unicorn easy" and get results instantly. Th..."
keywords: "string, length, search, level, rex, const, return, pages"
generated: "2026-09-25T21:21:27.487638"
---

# Searching 10,000 Printable Pages Without a Search Server: A Prebuilt Index, Synonyms and Kid-Friendly Typos

## Overview

When a site grows past a few hundred pages, category browsing stops being enough. People want to type "t rex" or "unicorn easy" and get results instantly. The usual answer is a hosted search service — but for a static content site, you often don't need one. The Coloring Companion is a library of 10,000+ free printable coloring pages — high-contrast black-and-white line art for toddlers, kids, teachers and adults, grouped into categories like animals, dinosaurs, holidays, flags, educational and easy pages. Here's the approach to fast, serverless search over a catalog that size. 1. Build a compact index at build time The browser doesn't need page bodies to search — just titles, categories, tags and difficulty. Emit a small JSON index during the build: interface Entry { id : number ; slug : string ; title : string ; // "Friendly T-Rex" cats : string []; // ["dinosaurs", "kids"] tags : string []; // ["t-rex", "tyrannosaurus", "dino"] level : " easy " | " medium " | " detailed " ; } With short keys and gzip, 10,000 entries fit comfortably in a single lazily-loaded file. It's only fetched when someone focuses the search box. 2. Normalize queries the way people actually type Search input on a coloring site comes from parents on phones and kids typing their own queries. Normalization does a lot of heavy lifting: const SYNONYMS : Record < string , string > = { trex : " t-rex " , " t rex " : " t-rex " , dino : " dinosaur " , dinos : " dinosaur " , xmas : " christmas " , kitty : " cat " , puppy : " dog " , unicorns : " unicorn " , }; export function normalize ( q : string ): string [] { let s = q . toLowerCase (). trim (). replace ( / [^ a-z0-9 \s - ] /g , " " ); for ( const [ k , v ] of Object . entries ( SYNONYMS )) s = s . replace ( new RegExp ( ` \\ b ${ k } \\ b` , " g " ), v ); return s . split ( / \s +/ ). filter (( t ) => t && ! [ " coloring " , " page " , " pages " , " free " , " printable " ]. includes ( t )); } Stripping words like "coloring" and "printable" matters: nearly every query contains them, and they match everything. 3. Treat difficulty as a filter, not a keyword "Easy" in a query is almost always a filter intent. Pull it out before matching: const LEVELS = [ " easy " , " medium " , " detailed " ] as const ; function extractLevel ( tokens : string []) { const level = tokens . find (( t ) => ( LEVELS as readonly string []). includes ( t )); return { level , rest : tokens . filter (( t ) => t !== level ) }; } 4. Score with simple weights A small scoring function beats a heavy library for this use case. Title matches outrank tag matches, which outrank category matches, with prefix matching for as-you-type results: function score ( e : Entry , tokens : string []): number { let s = 0 ; for ( const t of tokens ) { if ( e . title . toLowerCase (). includes ( t )) s += 5 ; if ( e . tags . some (( x ) => x . startsWith ( t ))) s += 3 ; if ( e . cats . some (( x ) => x . startsWith ( t ))) s += 1 ; } return s ; } export function search ( index : Entry [], q : string , limit = 48 ) { const { level , rest } = extractLevel ( normalize ( q )); return index . filter (( e ) => ! level || e . level === level ) . map (( e ) => ({ e , s : score ( e , rest ) })) . filter (( x ) => x . s > 0 || rest . length === 0 ) . sort (( a , b ) => b . s - a . s ) . slice ( 0 , limit ) . map (( x ) => x . e ); } 5. Tolerate small typos Kids misspell. A cheap edit-distance check on tokens that don't match anything catches "dinasour" and "unicron" without a fuzzy-search dependency: function within1 ( a : string , b : string ) { if ( Math . abs ( a . length - b . length ) > 1 ) return false ; let i = 0 , j = 0 , edits = 0 ; while ( i < a . length && j < b . length ) { if ( a [ i ] === b [ j ]) { i ++ ; j ++ ; continue ; } if ( ++ edits > 1 ) return false ; if ( a . length > b . length ) i ++ ; else if ( b . length > a . length ) j ++ ; else { i ++ ; j ++ ; } } return edits + ( a . length - i ) + ( b . length - j ) <= 1 ; } 6. Popular searches as a safety net Show a handful of popular searches (dinosaurs, T-Rex, Halloween, Christmas, mandalas, flags) under the box. Many visitors click one instead of typing — and it doubles as internal linking. Takeaways A prebuilt JSON index handles thousands of pages without a search server. Normalize for how people type: synonyms, stopwords, filters. Simple weighted scoring is fast and easy to tune. Add lightweight typo tolerance for young users. Find a page to print at thecoloringcompanion.com . How do you handle search on static sites?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/akbo_ichou_c41c249cc2783d/searching-10000-printable-pages-without-a-search-server-a-prebuilt-index-synonyms-and-1lcp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
