---
title: "Serve a styled PDF invoice from FastAPI"
slug: "serve-a-styled-pdf-invoice-from-fastapi"
author: "Keenan Finkelstein"
source: "devto_python"
published: "Mon, 26 Oct 2026 22:05:54 +0000"
description: "An invoice endpoint needs a document renderer, your application's record lookup, and an HTTP response containing PDF bytes. Here is a runnable FastAPI exampl..."
keywords: "invoice, pdf, fastapi, fullbleed, download, python, response, renderer"
generated: "2026-10-26T22:30:36.498829"
---

# Serve a styled PDF invoice from FastAPI

## Overview

An invoice endpoint needs a document renderer, your application's record lookup, and an HTTP response containing PDF bytes. Here is a runnable FastAPI example with an editable HTML/CSS invoice, bundled fonts, and a small download page. Fullbleed is the MIT-licensed PDF engine used here; this walkthrough is published by the project. The sample is a fictional Northstar Studio invoice for Maple & Finch, with three line items totaling USD 1,870.00. Open the sample PDF Download the starter and open its fullbleed-python-invoice directory. Use Python 3.10–3.14 and create a virtual environment: python -m venv .venv Activate it with source .venv/bin/activate on macOS/Linux, or .venv\Scripts\Activate.ps1 in Windows PowerShell. Then install and start the app: python -m pip install fullbleed == 2.5.37 -r requirements-fastapi.txt python -m uvicorn fastapi_app:app --host 127.0.0.1 --port 8000 Open http://127.0.0.1:8000/ and select Download invoice . You can also request http://127.0.0.1:8000/invoices/INV-1042.pdf directly. The download is generated from the current template; the browser page shows a saved sample preview. The PDF portion of fastapi_app.py is small: from fastapi import FastAPI , HTTPException , Response from invoice import PDF_HEADERS , load_invoice , render_invoice class PDFResponse ( Response ): media_type = " application/pdf " app = FastAPI ( title = " Fullbleed invoice example " ) @app.get ( " /invoices/{invoice_id}.pdf " , response_class = PDFResponse ) def invoice_pdf ( invoice_id : str ) -> PDFResponse : invoice = load_invoice ( invoice_id ) if invoice is None : raise HTTPException ( status_code = 404 , detail = " Invoice not found " ) return PDFResponse ( render_invoice ( invoice ), headers = PDF_HEADERS ) The invoice import is the shared renderer included in the ZIP. load_invoice() currently returns the fictional record. Replace it with your application's authorized lookup before serving real invoices, keeping access checks before rendering. PDFResponse declares the PDF media type in the generated OpenAPI schema. Its content is already binary PDF data, which FastAPI's Response accepts directly . The route uses a normal def : Fullbleed's render call is synchronous, and the template is read from disk. FastAPI runs these path operations in its thread pool . Calling the same renderer directly inside async def would still occupy that event-loop thread during the call. The shared response headers make the result a private attachment: PDF_HEADERS = { " Content-Disposition " : ' attachment; filename= " invoice.pdf "' , " Cache-Control " : " private, no-store " , } A new engine renders each request into memory. There is no shared output filename, and rendering this document does not launch a browser or fetch fonts from the network. To change the document, edit templates/invoice.html for its structure and templates/invoice.css for typography, columns, spacing, and color. For example, .invoice .total styles the green total panel and its orange border. The local server reads these files for each download, so template edits do not require a restart. The renderer uses Decimal for amounts and escapes text before a single string.Template substitution. Placeholders include $customer , $number , $rows , and $total ; write $$ for a literal dollar sign in the template. Fonts and their licenses travel with the project and Fullbleed wheel. The included layout is a fixed one-page A4 sample for three items. Longer invoices need pagination work and output review. Tax, discounts, invoice numbering, authentication, and payment collection belong to your application. The ZIP also includes Flask and Django adapters using the same renderer. To check all three, stop the local server and run: python -m pip install -r requirements-check.txt python check_examples.py --out output/check Use a new output directory. The check exercises framework clients and real HTTP servers, including missing records, response headers, simultaneous downloads, embedded fonts, expected text and totals, and the saved preview. Inspect the resulting PDFs and output/check/verification.json after making changes. For a container, follow the Docker guide . For longer jobs, move rendering into your application's job queue and store the completed PDF for download. The full integration guide includes the framework variants. The source record identifies the download by source commit and hashes. Drafted and checked by an AI coding agent for the Fullbleed project, using Fullbleed 2.5.37 and FastAPI 0.142.2. The exact code excerpt was executed against the runnable starter.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fullbleed/serve-a-styled-pdf-invoice-from-fastapi-4klh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
