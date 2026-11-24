---
title: "print("Hello, World!")"
slug: "printhello-world"
author: "duhbob"
source: "devto_python"
published: "Tue, 24 Nov 2026 21:52:28 +0000"
description: "The agents' conflict over the two MCP files of the night and its false reports MCP Financial Engine Project. Name: Micro Money (Micro-level Finance) Descript..."
keywords: "pass, mcp, files, financial, csv, not, xlsx, micro"
generated: "2026-11-24T22:10:49.159628"
---

# print("Hello, World!")

## Overview

The agents' conflict over the two MCP files of the night and its false reports MCP Financial Engine Project. Name: Micro Money (Micro-level Finance) Description: An accurate Arabic financial auditing engine that works as an MCP server. :: Tools: Python language (Python 3.10+) pandas library (for batch analysis and processing of big data) openpyxl library (for reading and exporting Excel files in streaming mode) mcp >= 2.0 library (Model Context Protocol) :: Idea: Building a high-precision Arabic financial auditor that operates as an MCP server, designed with clean software architecture inside the Micro-level-Finance folder that completely separates strict accounting accuracy from the AI tools interface. :: The crazy AI agent assistants: I have mobilized a swarm of awesome agents that received high scores, strong global ratings, and dazzling promotions. Errors: Accepting .xlsm files (macro-enabled) and missing project files (requirements.txt and sample_ledger.csv) Delimiter Collision in duplicate detection and double payment fingerprints. File Existence Oracle and exposing internal exception details. Storing financial data and Personally Identifiable Information (PII) in plaintext in the system temporary folder. Indirect Prompt Injection to the model via ledger data. Absence of XML Bomb / Zip Bomb protection, not installing defusedxml, and lack of consumption limits (DoS). Formula / CSV Injection in exported Excel files. Arbitrary folder creation and writing, overwriting existing files + bypassing same-file checks via Symlinks. Arbitrary file reading and path traversal + NTLM leaking via UNC paths. Major Problems: parse_strict_decimal — accepts negative numbers, but normalize_raw_digits might corrupt them Evidence: The pattern \s deletes all spaces. However, negative numbers in the format (1,500) (accounting format) or 1 500- will not be understood. Most importantly: re.match(r"^-?\d+(.\d+)?$", s) — if the output is "1,500" (the comma wasn't deleted because it's not in the list? No, , is present) However, the Arabic decimal point ٫ is translated to . in ARABIC_TO_WESTERN — good. But the Arabic comma ، is translated to . and this is a fatal error: Fixes: The fixes have been modified successfully; the financial engine still needs skills that I left for the company owner or accountant to add the skills suitable for them Conclusion: The programmer and developer still have an active role. Just imagine, only two Python files whose mission is financial auditing via MCP—most of the agents and a swarm of strong models had a wild night carrying in its darkness whispers among them: this one made a mistake with the comma, this one made a mistake with the percentage, and this one mixed up dates with phone numbers, and another does not differentiate, and another got extremely drunk and started hallucinating. Therefore, the human mind must intervene and tell them in the language of code: this code is ready and the library is ready, just fix it. # Test Case Status Observed Result 1 MCP Tool Discovery ✅ PASS Discovered list_excel_sheets and audit_massive_excel 2 list_excel_sheets on CSV ✅ PASS Detected CSV format and returned guidance 3 Full Audit + Clean .xlsx Export ✅ PASS Audited 10 rows and exported plugin_test_clean_export.xlsx cleanly 4 Smart Schema & Decimal Precision ✅ PASS Accurate totals ( 10901.00 subtotal, 1625.16 VAT, 12531.16 total); رقم_الجوال classified as identifier (not summed) 5 15% VAT & Fraud Detection ✅ PASS Detected 2 VAT/arithmetic issues (rows 4 & 10), 2 suspected double payments, 1 exact duplicate row, 1 invalid number, 1 invalid date 6 Round-Trip .xlsx Inspection & Audit ✅ PASS Listed sheet 'البيانات_المفرزة' and re-audited all 10 rows 7 Export Overwrite Protection ✅ PASS Blocked overwriting existing export file when allow_overwrite=False 8 Path Security (Traversal / UNC / Oracle) ✅ PASS Blocked ..\..\Windows\fake.xlsx , blocked \\attacker\share\ledger.xlsx , and enforced extension check before existence check 9 Invalid vat_tolerance ( NaN ) ✅ PASS Rejected non-finite tolerance cleanly 10 Formula Injection & XML Protection ✅ PASS Neutralized =HYPERLINK(...) to '=HYPERLINK(...) , preserved -500 as a true numeric cell, and verified openpyxl.xml.DEFUSEDXML == True The micro-level-finance plugin is fully verified, hardened, and ready for production use on Excel and CSV ledgers within the configured base directory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/duhbob/printhello-world-3p88

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
