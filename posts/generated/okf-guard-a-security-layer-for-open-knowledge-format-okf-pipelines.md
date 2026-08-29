---
title: "okf-guard: A Security Layer for Open Knowledge Format (OKF) Pipelines"
slug: "okf-guard-a-security-layer-for-open-knowledge-format-okf-pipelines"
author: "Darshan Buddhdev"
source: "devto_python"
published: "Sat, 29 Aug 2026 06:25:31 +0000"
description: "Catching Prompt Injection Before It Enters a Trusted Knowledge Base AI agents increasingly consume knowledge from sources they did not author and cannot inde..."
keywords: "content, text, document, okf, has, hidden, knowledge, not"
generated: "2026-08-29T06:36:04.043996"
---

# okf-guard: A Security Layer for Open Knowledge Format (OKF) Pipelines

## Overview

Catching Prompt Injection Before It Enters a Trusted Knowledge Base AI agents increasingly consume knowledge from sources they did not author and cannot independently verify: a PDF policy document, a scraped web page, a spreadsheet exported from another team's system. The prevailing approach — extract the text, write it into a knowledge base or context window, let the agent treat it as fact — has an underexamined weakness. Extraction tools capture everything present in a source document, including content a human reviewer would never see. The Mechanism Several ordinary, well-documented features of common file formats allow text to be present in a document while remaining invisible to anyone reading it normally: A PDF can render text in a rendering mode that instructs viewers not to display it, or set its fill color identical to the page background. A Word document has an explicit "hidden" attribute on any run of text, independent of color or size. A PowerPoint file's speaker notes are parsed by most extraction tools but never appear to an audience watching the presentation. A spreadsheet can mark entire rows, columns, or sheets as hidden, or attach a comment to a cell that is invisible unless hovered. An HTML page can hide an element from a browser's rendering entirely via a handful of standard CSS properties. None of these are obscure edge cases. They are common, legitimate formatting features, used constantly for entirely benign reasons — a hidden helper column in a spreadsheet, a private note to a presenter, draft text a Word user hid rather than deleted. The problem is not that these features exist; it is that an extraction pipeline has no reason to distinguish "this text is legitimate content" from "this text was deliberately hidden" unless something is specifically checking for the difference. Why This Matters for AI Pipelines Specifically If an attacker can place text anywhere in this chain — inside a PDF a company will later ingest, inside a web page a scraper will later visit — using any of the above mechanisms, that text becomes indistinguishable from the surrounding legitimate content once extracted. An instruction phrased for an AI system rather than a human reader ("approve this without further review," "treat the following as verified") sitting in a hidden run of a Word document will be extracted identically to the visible text around it. This is a variant of indirect prompt injection, and it applies most directly right now to Google's recently published Open Knowledge Format (OKF) — a specification for representing organizational knowledge as markdown files that AI agents read directly, with no processing layer in between. That directness is the format's central design goal; it is also precisely what removes any opportunity to catch a problem before an agent treats the content as trustworthy. What okf-guard Does okf-guard is a Python library intended to sit at the point where a source document is extracted and before its content becomes part of a trusted bundle. It performs two independent kinds of inspection on every scan: Hidden-content detection, format-aware — each of six supported formats (plain text, Markdown, HTML, PDF, DOCX, PPTX, XLSX) has an adapter that understands that format's specific mechanisms for hiding content from a human reader. Pattern-based detection of language characteristic of an instruction directed at an AI system, plus a check for encoding-based obfuscation (zero-width characters, homoglyph substitution). Both checks run on every scan independently. Content that is both hidden and contains injection-style phrasing produces two separate findings, since either alone is meaningful signal, and their combination is stronger evidence than either in isolation. python from okfguard import sanitize result = sanitize("suspicious_document.pdf") print(result.action) # "pass", "quarantine", or "block" print(result.risk_score) # e.g. 0.9 for flag in result.flags: print(f"[{flag.type}] {flag.location}: {flag.snippet}") What It Deliberately Does Not Do This release has no LLM dependency and makes no network calls. All detection is rule-based and fully deterministic — a considered tradeoff, not a temporary limitation. A security-relevant tool benefits from behavior that is reproducible and auditable, and a lightweight dependency footprint matters for a library meant to be embedded in someone else's pipeline. The tool also makes no claim about the accuracy of content it passes. Every result includes explicit provenance metadata marking content as machine-processed and unverified — nothing in the library ever asserts that content has been reviewed by a human. Where It Stands Today v0.1.0 covers document- and web-sourced content specifically — the categories where content plausibly originates outside an organization's direct control. It does not yet address: Structured/technical sources (source code, API specs, database schemas) Collaboration-tool connectors (Notion, Confluence, Slack) Content generated by an AI agent's own reasoning process All three raise distinct problems and are planned for subsequent releases. Source & docs: https://github.com/darshanNhb/okf-guard bash pip install okf-guard[all] Feedback, particularly from anyone who has worked on related problems in document security or LLM safety, is genuinely welcome — the pattern bank in src/okfguard/rules/injection_patterns.py is explicitly designed to grow through contribution as new attack phrasing is identified.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/darshan_buddhdev/catching-prompt-injection-before-it-enters-a-trusted-knowledge-base-5hf4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
