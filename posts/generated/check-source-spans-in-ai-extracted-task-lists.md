---
title: "Check source spans in AI-extracted task lists"
slug: "check-source-spans-in-ai-extracted-task-lists"
author: "Dmitry Lukashov"
source: "devto_python"
published: "Sun, 18 Oct 2026 10:08:02 +0000"
description: "An extracted task can cite a real line ID while quoting words that are not in that line. A small source-span check makes that error visible before you use th..."
keywords: "not, row, source, quote, start, end, check, good"
generated: "2026-10-18T10:43:33.396401"
---

# Check source spans in AI-extracted task lists

## Overview

An extracted task can cite a real line ID while quoting words that are not in that line. A small source-span check makes that error visible before you use the row as evidence. This exercise has six fictional lines. Maya promises to send an agenda, Noah commits to checking two totals, and Friday remains a proposal. All candidate outputs below are deliberate fixtures, not captured responses from a model. Ask your extractor for a narrow output: Extract explicit personal commitments. Return a JSON array with line_id, start, end and quote. Quote the source verbatim. Use zero-based Python string indexes into the line text, including the speaker prefix; end is exclusive. Keep proposals and unassigned requests out of the commitment list. The runnable source and README contain the same example. Save the code below as source_span_gate.py ; it uses only Python's standard library. import json # Fictional source lines. Candidate outputs below are also synthetic. SOURCES = { " L1 " : " Maya: I will send the agenda. " , " L2 " : " Noah: Could we review it on Friday? " , " L3 " : " Maya: Friday is still a proposal. " , " L4 " : " Leo: Please check both totals. " , " L5 " : " Noah: I will check both totals. No deadline yet. " , " L6 " : " Maya: Nobody is assigned to send the final file. " , } GOOD = """ [ { " line_id " : " L1 " , " start " :6, " end " :29, " quote " : " I will send the agenda. " }, { " line_id " : " L5 " , " start " :6, " end " :31, " quote " : " I will check both totals. " } ] """ def check ( raw ): rows = json . loads ( raw ) if not isinstance ( rows , list ): raise ValueError ( " expected an array " ) seen = set () for number , row in enumerate ( rows , 1 ): if not isinstance ( row , dict ) or set ( row ) != { " line_id " , " start " , " end " , " quote " }: raise ValueError ( f " row { number } : unexpected fields " ) ref , start , end , quote = ( row [ " line_id " ], row [ " start " ], row [ " end " ], row [ " quote " ] ) if not isinstance ( ref , str ) or ref not in SOURCES : raise ValueError ( f " row { number } : unknown source line " ) if ( type ( start ) is not int or type ( end ) is not int or not 0 <= start < end <= len ( SOURCES [ ref ]) ): raise ValueError ( f " row { number } : invalid span bounds " ) if not isinstance ( quote , str ) or SOURCES [ ref ][ start : end ] != quote : raise ValueError ( f " row { number } : quote does not match source " ) span = ( ref , start , end ) if span in seen : raise ValueError ( f " row { number } : duplicate span " ) seen . add ( span ) return len ( rows ) if __name__ == " __main__ " : examples = { " good " : GOOD , " changed_word " : GOOD . replace ( " send the agenda " , " approve the agenda " ), " wrong_offset " : GOOD . replace ( '" start " :6 ' , '" start " :7 ' , 1 ), " unknown_line " : GOOD . replace ( '" L1 "' , '" L99 "' , 1 ), } for name , raw in examples . items (): try : print ( f " { name } : PASS ( { check ( raw ) } spans) " ) except ValueError as error : print ( f " { name } : FAIL ( { error } ) " ) Run: python3 -B source_span_gate.py The locally executed output was: good: PASS (2 spans) changed_word: FAIL (row 1: quote does not match source) wrong_offset: FAIL (row 1: quote does not match source) unknown_line: FAIL (row 1: unknown source line) The good fixture selects two exact pieces of evidence: Source Expected interpretation Agreed deadline L1, indexes 6:29 Maya will send the agenda. Unknown L5, indexes 6:31 Noah will check both totals. Unknown The changed-word fixture replaces “send” with “approve” in the candidate quote. The source stays unchanged, so the check rejects it. The other two fixtures move an offset or invent a source ID. They are rejected even though the JSON is parseable. The offsets refer to Python string positions, not UTF-8 byte positions. The JSON documentation describes parsing; the sequence documentation defines the slicing convention used here. A passing row establishes only that its quote matches the selected source span. It does not establish that the quote supports a proposed interpretation, that the list is complete, or that the source itself is true. An extractor could omit Noah's commitment and still produce valid spans for Maya. Keep a short manual review beside this check: L2 asks about Friday and L3 still calls it a proposal, so Friday is not an agreed deadline. L6 leaves the final file without a sender. Neither detail should turn into an assigned, dated task just because a nearby quote passes. For a real integration, first decide how to handle those semantic and completeness checks. This teaching function is not a complete production-input or JSON-hardening layer. It connects to no model, CRM or network. Disclosure: AI agents prepared this article and code. The source lines and outputs are synthetic; the exact code shown above was run locally. No model API was called. Dmitry Lukashov (Дмитрий Лукашов) — founder of Lookatshow, instructor and expert in applied AI at the Russian School of Management. Public author reference .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lookatshow/check-source-spans-in-ai-extracted-task-lists-4233

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
