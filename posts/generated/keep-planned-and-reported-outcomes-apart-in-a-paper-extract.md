---
title: "Keep planned and reported outcomes apart in a paper extract"
slug: "keep-planned-and-reported-outcomes-apart-in-a-paper-extract"
author: "bao han"
source: "devto_python"
published: "Sun, 22 Nov 2026 05:23:30 +0000"
description: "A clinical evidence-table importer should not replace a protocol outcome with the paper's outcome just because both are labelled “symptom score”. Keep both s..."
keywords: "not, source, reported, differences, row, planned, reason, protocol"
generated: "2026-11-22T06:01:01.629381"
---

# Keep planned and reported outcomes apart in a paper extract

## Overview

A clinical evidence-table importer should not replace a protocol outcome with the paper's outcome just because both are labelled “symptom score”. Keep both source-linked entries for review. This small Python example flags literal differences in endpoint, time point and analysis metric. A missing protocol is a separate state. The numbers and source names below are synthetic teaching material; this code does not judge a real trial. FIELDS = ( "endpoint" , "timepoint" , "metric" ) def audit ( row ) : if not isinstance ( row , dict ) : raise ValueError ( "a record is required" ) reported = row . get ( "reported" ) def check ( obj , keys ) : if not isinstance ( obj , dict ) or any ( not isinstance ( obj . get ( k ) , str ) or not obj [ k ] . strip ( ) for k in keys ) : raise ValueError ( "non-empty source-linked text fields required" ) check ( reported , ( * FIELDS , "source" ) ) planned = row . get ( "planned" ) if planned is None : return { "status" : "protocol_not_available" , "differences" : None } check ( planned , ( * FIELDS , "source" , "version_date" ) ) differences = [ k for k in FIELDS if planned [ k ] . strip ( ) != reported [ k ] . strip ( ) ] reason = row . get ( "reason" ) if reason is not None : check ( row , ( "reason" , "reason_source" ) ) return { "status" : "needs_source_review" if differences else "no_text_difference" , "differences" : differences , "reason_status" : "source_supplied" if reason else "not_found" , } row = { "planned" : dict ( endpoint = "symptom score" , timepoint = "week 12" , metric = "change from baseline" , source = "synthetic protocol p4" , version_date = "2026-01-01" ) , "reported" : dict ( endpoint = "symptom score" , timepoint = "week 24" , metric = "change from baseline" , source = "synthetic paper Table2" ) , } print ( audit ( row ) ) # {'status': 'needs_source_review', 'differences': ['timepoint'], # 'reason_status': 'not_found'} print ( audit ( { "reported" : row [ "reported" ] } ) ) # {'status': 'protocol_not_available', 'differences': None} The first result retains the week-12 versus week-24 difference. It does not infer when or why a change occurred. The second result says that the protocol was unavailable, rather than treating the paper's description as proof of what was prespecified. Six invalid records were run locally and rejected: a missing record, missing reported data, a non-text field, a blank locator, a reason without its source, and an empty protocol date. A same-text control produced no_text_difference . This is a text preflight. Case, wording or equivalent time expressions can produce false differences; a same-text result does not establish methodological agreement. Open the dated protocol or registry, the paper and any amendment. Check the outcome definition, time point, analysis metric and the stated reason. A locator can be populated but wrong, and a supplied date does not establish that a plan preceded access to outcome data. Do not turn these flags into an automatic misconduct or risk-of-bias verdict. We build RigorMed, an AI research workspace. For a small first task, organize 2–3 papers you are allowed to use into a source-linked evidence table, then check the relevant passages yourself. Research execution uses account credits. This example was run locally on synthetic records, not on patient data or a customer project. Source-linked evidence-table starter Reporting reference: CONSORT 2025 explanation and elaboration, item 10 . Our import contract and code are teaching choices, not a CONSORT compliance certificate.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nanchuangresearch/keep-planned-and-reported-outcomes-apart-in-a-paper-extract-3l7l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
