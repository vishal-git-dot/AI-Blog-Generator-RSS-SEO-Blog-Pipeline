---
title: "Build a GST Invoice Parser in 70 Lines of Python"
slug: "build-a-gst-invoice-parser-in-70-lines-of-python"
author: "Archit Mittal"
source: "devto_python"
published: "Sat, 20 Jun 2026 03:41:45 +0000"
description: "If you run a small business in India, you know the monthly ritual: a folder full of vendor invoice PDFs, and a spreadsheet that needs GSTIN, invoice number, ..."
keywords: "invoice, gstin, row, compile, total, text, invoices, pdfs"
generated: "2026-06-20T04:12:08.213569"
---

# Build a GST Invoice Parser in 70 Lines of Python

## Overview

If you run a small business in India, you know the monthly ritual: a folder full of vendor invoice PDFs, and a spreadsheet that needs GSTIN, invoice number, date, taxable value, and GST amounts pulled out of every single one. Doing it by hand takes hours. Let's automate it in about 70 lines of Python. What we're building A script that: Scans a folder of invoice PDFs Extracts GSTIN, invoice number, date, taxable value, CGST/SGST/IGST, and total Validates the GSTIN format (including the checksum-style structure) Writes everything to a clean CSV you can import into Tally or Excel Setup pip install pdfplumber That's the only dependency. pdfplumber handles text extraction from digitally generated PDFs (which most GST invoices are). The code import csv import re import sys from pathlib import Path import pdfplumber # GSTIN: 2-digit state code + 10-char PAN + entity code + 'Z' + check char GSTIN_RE = re . compile ( r " \b\d{2}[A-Z]{5}\d{4}[A-Z]\d[A-Z]\d\b " ) INV_NO_RE = re . compile ( r " (?:Invoice\s*(?:No|Number|#)\.?\s*[:\-]?\s*)([A-Z0-9\/\-]+) " , re . I ) DATE_RE = re . compile ( r " \b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4})\b " ) AMOUNT_RE = re . compile ( r " (?:\u20b9|Rs\.?|INR)\s*([\d,]+\.?\d*) " ) LABELS = { " taxable " : re . compile ( r " taxable\s*(?:value|amount)\s*[:\-]?\s*(?:\u20b9|Rs\.?|INR)?\s*([\d,]+\.?\d*) " , re . I ), " cgst " : re . compile ( r " CGST[^\d]*([\d,]+\.\d{2}) " , re . I ), " sgst " : re . compile ( r " SGST[^\d]*([\d,]+\.\d{2}) " , re . I ), " igst " : re . compile ( r " IGST[^\d]*([\d,]+\.\d{2}) " , re . I ), " total " : re . compile ( r " (?:grand\s*total|total\s*amount|amount\s*payable)\s*[:\-]?\s*(?:\u20b9|Rs\.?|INR)?\s*([\d,]+\.?\d*) " , re . I ), } STATE_CODES = { f " { i : 02 d } " for i in range ( 1 , 39 )} def valid_gstin ( gstin : str ) -> bool : return bool ( GSTIN_RE . fullmatch ( gstin )) and gstin [: 2 ] in STATE_CODES def to_float ( s : str ) -> float : try : return float ( s . replace ( " , " , "" )) except ValueError : return 0.0 def parse_invoice ( pdf_path : Path ) -> dict : with pdfplumber . open ( pdf_path ) as pdf : text = " \n " . join ( page . extract_text () or "" for page in pdf . pages ) gstins = [ g for g in GSTIN_RE . findall ( text ) if valid_gstin ( g )] inv_no = INV_NO_RE . search ( text ) date = DATE_RE . search ( text ) row = { " file " : pdf_path . name , " vendor_gstin " : gstins [ 0 ] if gstins else " NOT FOUND " , " invoice_no " : inv_no . group ( 1 ) if inv_no else " NOT FOUND " , " date " : date . group ( 1 ) if date else " NOT FOUND " , } for field , pattern in LABELS . items (): m = pattern . search ( text ) row [ field ] = to_float ( m . group ( 1 )) if m else 0.0 # Sanity check: taxable + taxes should roughly equal total expected = row [ " taxable " ] + row [ " cgst " ] + row [ " sgst " ] + row [ " igst " ] row [ " mismatch " ] = " YES " if row [ " total " ] and abs ( expected - row [ " total " ]) > 1 else "" return row def main ( folder : str ): pdfs = sorted ( Path ( folder ). glob ( " *.pdf " )) if not pdfs : sys . exit ( f " No PDFs found in { folder } " ) rows = [ parse_invoice ( p ) for p in pdfs ] out = Path ( folder ) / " invoices_extracted.csv " with out . open ( " w " , newline = "" ) as f : writer = csv . DictWriter ( f , fieldnames = rows [ 0 ]. keys ()) writer . writeheader () writer . writerows ( rows ) print ( f " Parsed { len ( rows ) } invoices -> { out } " ) flagged = sum ( 1 for r in rows if r [ " mismatch " ]) if flagged : print ( f " Warning: { flagged } invoice(s) have tax totals that don ' t add up — check manually. " ) if __name__ == " __main__ " : main ( sys . argv [ 1 ] if len ( sys . argv ) > 1 else " . " ) Running it python gst_parser.py ~/Downloads/vendor-invoices/ Output: Parsed 23 invoices -> invoices_extracted.csv Warning: 2 invoice(s) have tax totals that don't add up — check manually. That mismatch flag is my favourite part. It catches data-entry errors on the vendor's side and extraction failures on ours — anything where taxable value + CGST + SGST + IGST doesn't land within ₹1 of the stated total gets flagged for a human look. Why regex and not AI? For digitally generated invoices, regex is faster, free, and deterministic. A month of invoices parses in under two seconds with zero API costs. Where this approach breaks down is scanned/photographed invoices — for those, add an OCR step with pytesseract before the regex pass, or hand the text to an LLM for extraction. Three upgrades worth making Vendor name capture. Most invoices put the vendor name within a couple of lines of the GSTIN. Grab the surrounding lines and you can auto-fill the vendor column too. GSTIN verification. The format check above catches typos, but the government's GST portal can confirm a GSTIN is actually registered. Useful before claiming input tax credit. HSN code extraction. If you need item-level detail for GSTR filings, pdfplumber 's extract_tables() handles the line-item tables most invoice formats use. Wrap-up Seventy lines, one dependency, and the monthly invoice grind becomes a two-second script run. The same pattern — extract text, regex the fields you care about, validate, write CSV — works for bank statements, salary slips, and purchase orders too. Follow me on Twitter @automate_archit for daily AI automation tips.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/automate-archit/build-a-gst-invoice-parser-in-70-lines-of-python-h50

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
