---
title: "CSV vs CSV UTF-8: the same rows in four encodings, byte by byte"
slug: "csv-vs-csv-utf-8-the-same-rows-in-four-encodings-byte-by-byte"
author: "lei zhang"
source: "devto_python"
published: "Thu, 12 Nov 2026 00:15:14 +0000"
description: ""CSV" and "CSV UTF-8" sound like two formats. They are the same format: CSV describes the rows and columns, UTF-8 describes how the characters are stored as ..."
keywords: "utf, bytes, bom, csv, windows, file, encoding, rows"
generated: "2026-11-12T00:20:19.770384"
---

# CSV vs CSV UTF-8: the same rows in four encodings, byte by byte

## Overview

"CSV" and "CSV UTF-8" sound like two formats. They are the same format: CSV describes the rows and columns, UTF-8 describes how the characters are stored as bytes. The only other thing that differs is an optional three-byte mark at the start of the file. To see exactly what changes, I saved the same three rows ( Zoë Müller , José Peña , Chloé Dubois ) in four encodings and read the bytes. The same rows, four encodings Encoding Size First bytes ë is stored as UTF-8 with BOM 88 bytes EF BB BF 69 64 2C C3 AB UTF-8, no BOM 85 bytes 69 64 2C 6E 61 6D C3 AB Windows-1252 77 bytes 69 64 2C 6E 61 6D EB UTF-16 LE with BOM 156 bytes FF FE 69 00 64 00 EB 00 Three things stand out: For plain English text, UTF-8 and Windows-1252 store identical bytes. Both files start 69 64 2C ("id,"). The difference only shows up with accented or non-Latin letters. The first two rows differ by exactly three bytes: EF BB BF , the byte order mark (BOM). The Unicode FAQ describes it, for UTF-8, as a signature that identifies the encoding. Windows-1252 is smaller, but it only covers Western European letters. Asking Python to save 東京 as Windows-1252 raises an error; with errors="replace" the two characters become ?? . What a wrong guess looks like A CSV file on disk does not say which encoding it uses ( RFC 4180 leaves the character set to a MIME parameter), so software guesses. A wrong guess gives one of two recognisable patterns: You see What happened Fix ZoÃ« MÃ¼ller UTF-8 bytes read as Windows-1252 Re-open as UTF-8 Zo� M�ller Windows-1252 bytes read as UTF-8 Re-open as Windows-1252 The first can be undone by re-reading the original. If a program has already saved the file with replacement characters, those letters are gone from that copy. The BOM cuts both ways Microsoft says a UTF-8 CSV opens normally in Excel if it was saved with the mark . Scripts are a different story. Python 3.9.6 with csv.DictReader : File Opened as First column name Result UTF-8 with BOM utf-8 \ufeffid row["id"] fails: the name has an invisible character UTF-8 with BOM utf-8-sig id Correct UTF-8, no BOM utf-8-sig id Correct, so this setting is safe for both Windows-1252 utf-8 — UnicodeDecodeError at the first ë Which one to choose Opened by people in Excel: UTF-8 with BOM. Code, a database or an API: UTF-8 without BOM, unless its documentation says otherwise. When reading in Python, encoding="utf-8-sig" handles both. A legacy system that asks for "ANSI": Windows-1252, only if all your characters fit, and check for lost characters afterwards. Excel's own "CSV (Comma delimited)" and "CSV UTF-8 (Comma delimited)" both use commas; the name before the brackets is about the encoding. Microsoft's format table does not name an encoding for the plain one, so check a saved file rather than trusting the name. The four test files, the full write-up and a browser tool that shows a file's encoding and saves UTF-8 with or without a BOM are on CSVLane . It runs in the browser tab, so the file is not uploaded. This post was prepared with AI assistance and adapted from the original article on csvlane.com; the byte counts and Python results come from the test files linked there.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lei_zhang_b6e446ccf73eac3/csv-vs-csv-utf-8-the-same-rows-in-four-encodings-byte-by-byte-1ik7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
