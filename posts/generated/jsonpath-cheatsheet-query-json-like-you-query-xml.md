---
title: "JSONPath Cheatsheet: Query JSON Like You Query XML"
slug: "jsonpath-cheatsheet-query-json-like-you-query-xml"
author: "pulkitgovrani"
source: "devto_webdev"
published: "Sat, 03 Oct 2026 04:30:00 +0000"
description: "JSONPath is a query language for picking values out of a JSON document, in the same spirit that XPath works for XML. It shows up in API tools, monitoring sys..."
keywords: "books, store, price, jsonpath, title, returns, query, tools"
generated: "2026-10-03T04:45:33.030441"
---

# JSONPath Cheatsheet: Query JSON Like You Query XML

## Overview

JSONPath is a query language for picking values out of a JSON document, in the same spirit that XPath works for XML. It shows up in API tools, monitoring systems, Kubernetes, and test frameworks. It became an IETF standard (RFC 9535) in 2024, but many tools still implement slightly different dialects. A sample document { "store" : { "books" : [ { "title" : "A" , "price" : 8.95 , "tags" : [ "new" ] }, { "title" : "B" , "price" : 12.99 }, { "title" : "C" , "price" : 22.99 } ], "owner" : "Sam" } } The core syntax $ is the root of the document. .name or ['name'] selects a child by name: $.store.owner returns "Sam". [n] selects an array element by index: $.store.books[0].title returns "A". * is a wildcard: $.store.books[*].title returns every title. .. is recursive descent, searching at any depth: $..price returns every price anywhere. [start:end] slices arrays: $.store.books[0:2] returns the first two books. [?(@.price < 10)] filters items, where @ is the current element: $.store.books[?(@.price < 10)] returns books cheaper than 10. Worked examples All titles: $.store.books[*].title gives A, B, C. Cheap books: $.store.books[?(@.price < 15)].title gives A and B. Books with tags: $.store.books[?(@.tags)] returns only book A. The last book: $.store.books[-1] in dialects that support negative indexes. Dialect differences to watch Filter syntax varies: some tools require parentheses (?(...)), others accept ?(...) or just ?.... Negative indexes, slices, and functions like length() are not supported everywhere. Behavior on missing keys differs: some tools return an empty result, others raise an error. String comparison and regex support in filters vary. Test your query first Paste your JSON and query into a tester and see what it returns before you use the path in a config or script. Do it locally if the JSON contains real data. Frequently asked questions What does $.. mean in JSONPath? $ is the root and .. is recursive descent, so $..name finds every 'name' key at any depth. How do I filter an array in JSONPath? Use a filter expression such as [?(@.price < 10)], where @ refers to each element being tested. Is JSONPath the same as jq? No. jq is a full command-line processor with its own language. JSONPath is a simpler query syntax that many tools embed. Is JSONPath standardized? Yes. RFC 9535 was published in 2024, but older implementations may differ from it. Try it: JSONPath Tester — free, runs in your browser, nothing is uploaded. Originally published at ilovekit.app .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pulkitgovrani/jsonpath-cheatsheet-query-json-like-you-query-xml-4i1g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
