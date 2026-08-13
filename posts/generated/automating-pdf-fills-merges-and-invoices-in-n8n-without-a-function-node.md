---
title: "Automating PDF fills, merges, and invoices in n8n without a Function node"
slug: "automating-pdf-fills-merges-and-invoices-in-n8n-without-a-function-node"
author: "PDFops"
source: "devto_webdev"
published: "Thu, 13 Aug 2026 13:06:51 +0000"
description: "Most n8n workflows that touch PDFs end up in the same place: an HTTP Request node with a hand-built multipart body, or a Code node calling pdf-lib and hoping..."
keywords: "pdf, node, invoice, fill, key, nodes, pdfops, one"
generated: "2026-08-13T13:23:07.314702"
---

# Automating PDF fills, merges, and invoices in n8n without a Function node

## Overview

Most n8n workflows that touch PDFs end up in the same place: an HTTP Request node with a hand-built multipart body, or a Code node calling pdf-lib and hoping the binary handling survives the next n8n upgrade. n8n-nodes-pdfops is a verified community node that turns PDF inspect, fill, merge, and invoice generation into typed n8n operations, with binary PDFs flowing in and out like any other node. Installing it On n8n Cloud, open the nodes panel and search "PDFops"; it installs in one click because it carries n8n's verified badge. Self-hosted, it's Settings → Community Nodes → Install, or from the CLI: n8n community-node install n8n-nodes-pdfops The node works with no credential at all, against the same 100-requests-per-IP-per-month anonymous tier the playground uses. Add a PDFops API credential (an API key in the X-API-Key header) once you want a higher quota or the usage operation described below. The five operations One node, five operations, picked from a dropdown: Inspect Fields lists a PDF's AcroForm field names, types, and current values, plus a fill template you can paste straight into the next node. Fill Form writes values into those fields and can flatten the result so it stops being editable. Merge concatenates every PDF on the incoming items, in item order, into one file. Generate Invoice renders a complete invoice PDF from a JSON object, no template required. Get Usage returns tier, quota, used, and reset date for a key. Fill, merge, and invoice are deterministic: run the same workflow twice on the same input and the output PDF is byte-identical, so a re-run never shows up as a spurious diff in whatever you archive it to. A worked example: fill from a webhook, catch the typo first The node ships with three ready-to-import workflow templates. The one worth walking through end to end is fill and flatten PDF forms from webhook data , because it solves the failure mode that makes "just fill the PDF" workflows unreliable: a field name typed wrong in the JSON payload doesn't error, it just fills nothing, and the caller gets back a document that looks correct until someone opens it. The workflow receives a webhook carrying a PDF URL, an email address, and a fields object, validates the payload, then runs Inspect Fields on the blank PDF before it fills anything. A Code node diffs the requested field names against the real ones the inspect call returned. Any name that doesn't match routes straight to an error response, naming the bad field, instead of silently producing a blank form. Only a payload that passes the diff reaches Fill Form with flatten on, so the result can't be edited after it ships. From there it fans out: Gmail sends the filled PDF, Google Drive archives a copy, and the caller gets a JSON receipt. Swap Gmail for SMTP or Slack and Drive for S3 without touching the PDF steps; none of them know or care where the file ends up. Two more recipes, already built Merge two forms into one packet. A workflow named onboarding packet from two PDF forms takes two blank PDF URLs and two field objects (a new-hire packet, a new-tenant packet, whatever your business fills in pairs), fills each with its own Fill Form node, waits for both branches, and joins them with Merge so the first form always lands as page one. It refuses to upload a packet unless both branches actually filled, so a partial run never produces a half-finished file that looks whole. An invoice on every Stripe payment. A Stripe trigger on payment_intent.succeeded feeds a Code node that shapes the charge into invoice JSON, and this is the step where most hand-rolled invoice code breaks quietly: Stripe reports amounts in the smallest currency unit, but JPY, KRW, and thirteen other currencies don't have 100 of those units, so a reflexive amount / 100 issues an invoice a hundred times too small. The template checks the currency against a zero-decimal list before it divides. Generate Invoice renders the deterministic PDF, then it archives to S3, emails the customer when an address is on file, and logs a row to a spreadsheet ledger. A failed render posts to Slack with the payment ID, so a missing invoice gets noticed instead of just not existing. Keyless works; a key gets you further Every operation runs without a credential at the shared 100/IP/mo anonymous rate, the same limit the API enforces everywhere else. A free API key (250 requests/month, email in, key out, no card) raises that ceiling and is required for the Get Usage operation, which returns your remaining quota so a workflow can check headroom before it burns the month's last call. Paid tiers exist once a workflow outgrows 250 a month, but the free key runs a real production automation, not just a demo. Try it Search "PDFops" in the n8n nodes panel, or install n8n-nodes-pdfops self-hosted. The three templates above are importable as-is from the node's npm page ; swap in your own PDF, Stripe account, or storage provider and the PDF steps don't change. Building on the raw API instead? Start at /docs or the OpenAPI spec .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pdfops/automating-pdf-fills-merges-and-invoices-in-n8n-without-a-function-node-318b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
