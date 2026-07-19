---
title: "A CSV quality report should not echo the data it rejects"
slug: "a-csv-quality-report-should-not-echo-the-data-it-rejects"
author: "elecson"
source: "devto_python"
published: "Sun, 19 Jul 2026 13:19:01 +0000"
description: "CSV validation usually starts with rules: required fields, types, ranges, allowed values, and uniqueness. But if the validation output will be attached to an..."
keywords: "csv, report, not, should, data, row, input, validation"
generated: "2026-07-19T13:36:01.812387"
---

# A CSV quality report should not echo the data it rejects

## Overview

CSV validation usually starts with rules: required fields, types, ranges, allowed values, and uniqueness. But if the validation output will be attached to an issue or sent to a teammate, there is an earlier design question: Should the report repeat the value that failed? For customer exports, the answer should usually be no. Email addresses, transaction identifiers, employee data, and internal account states can leak through a report even when the original CSV stays private. I used three separate fields for each validation failure: Location — physical CSV row and named column. Reason — a stable code such as type_mismatch or duplicate_value . Value — omitted by default and included only through an explicit option. The first two fields are normally enough to repair an export: row 3, signup_date: expected %Y-%m-%d row 8, customer_id: duplicate_value Neither message needs to copy the rejected date or customer identifier. Redaction does not have to break reproducibility A report can omit raw values while still recording: the SHA-256 hash of the input; the SHA-256 hash of the rule file; stable error codes; row and column locations; a generated timestamp. Two authorized people can then confirm that they validated identical input bytes. A hash is a build fingerprint, not anonymization, so small or predictable secrets still need care. Offline should mean offline For the small CLI I built around this idea, the generated HTML uses embedded CSS and no JavaScript, remote fonts, analytics, or CDN assets. The validator uses only Python's standard library and does not upload the CSV. That narrow scope has tradeoffs. It expects Python 3.10+, UTF-8 CSV input, and files that fit in memory. It does not guess encodings, repair data, or open Excel files. Exit codes make the report operational The command distinguishes three outcomes: 0 checks completed and passed 1 checks completed and found violations 2 the check could not run This lets the same run create a human-readable HTML report and machine-readable JSON while still blocking a local script or CI job. The broader lesson is simple: when a report may travel farther than its input, make data minimization the default rather than an afterthought. Disclosure: I built DataProof CSV , the small offline source toolkit described in this post. It includes failing and passing synthetic fixtures, redacted HTML/JSON reports, tests, and editable Python source: View DataProof CSV on Gumroad AI assistance disclosure: This article was prepared with AI assistance and reviewed by the product creator before publication.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/square12_82a85fc8609fdd1f/a-csv-quality-report-should-not-echo-the-data-it-rejects-4h96

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
