---
title: "Structural JSON Diff From Scratch: Compare Meaning, Not Lines, and Emit an RFC 6902 Patch"
slug: "structural-json-diff-from-scratch-compare-meaning-not-lines-and-emit-an-rfc-6902-patch"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 18:50:03 +0000"
description: "A plain text diff treats JSON as lines of characters, so it lies about JSON. Reformat a file, reorder two keys, or add a trailing comma and it screams that e..."
keywords: "path, return, node, changed, one, kind, json, typeof"
generated: "2026-08-07T19:04:02.694898"
---

# Structural JSON Diff From Scratch: Compare Meaning, Not Lines, and Emit an RFC 6902 Patch

## Overview

A plain text diff treats JSON as lines of characters, so it lies about JSON. Reformat a file, reorder two keys, or add a trailing comma and it screams that everything changed — even though the data is identical. A structural diff parses both sides into real trees and compares meaning: order-insensitive for object keys, index-aligned for arrays, type-aware at every leaf. The whole thing is one small recursive function. Type-aware equality typeof alone isn't enough — typeof null and typeof [] both return "object" . One helper returns the six JSON shapes so a shape change (the number 10 becoming the string "10" ) counts as a real change, not a coincidence. function typeOf ( v ){ if ( v === null ) return " null " ; if ( Array . isArray ( v )) return " array " ; return typeof v ; // "object" | "string" | "number" | "boolean" } const MISSING = Symbol ( " missing " ); // a key present on only one side The recursive core Missing on one side is an add or a remove; different types is a change; same container type means recurse; same primitive means compare. Each call returns a tiny node recording its verdict. function diffNode ( a , b ){ if ( a === MISSING ) return { kind : " added " , value : b }; if ( b === MISSING ) return { kind : " removed " , value : a }; const ta = typeOf ( a ), tb = typeOf ( b ); if ( ta !== tb ) return { kind : " changed " , cont : false , before : a , after : b }; if ( ta === " object " ) return diffObject ( a , b ); if ( ta === " array " ) return diffArray ( a , b ); return a === b ? { kind : " unchanged " , cont : false , before : a } : { kind : " changed " , cont : false , before : a , after : b }; } Objects collect the union of keys from both sides into a set, so reordering keys is invisible and a key on only one side becomes an add or a remove. Arrays have no keys to match on, so the simple, predictable rule is to align position i to position i up to the longer length — honest, though it means an insert near the front cascades into a wall of "changed" (no move detection). Name the location: JSON-Pointer A path is just the trail of keys and indices you descended through. RFC 6901 joins them with / and escapes the two ambiguous characters: a literal / in a key becomes ~1 , a literal ~ becomes ~0 . The root is the empty string. const escToken = t => String ( t ). replace ( /~/g , " ~0 " ). replace ( / \/ /g , " ~1 " ); const pointer = path => path . length ? path . map ( escToken ). map ( t => " / " + t ). join ( "" ) : "" ; // ["meta","reviews"] -> "/meta/reviews" // ["paths","/api/v1"] -> "/paths/~1api~1v1" A diff you can execute Once you know what changed and where, the labelled tree turns straight into an RFC 6902 JSON-Patch — a list of add / remove / replace ops any compliant library can apply to reproduce after from before . An added node is one add , a removed node one remove , a changed leaf one replace . A changed container emits nothing itself — you recurse so the ops land on the exact leaves that moved. function buildPatch ( node , path , ops ){ switch ( node . kind ){ case " added " : ops . push ({ op : " add " , path : pointer ( path ), value : node . value }); break ; case " removed " : ops . push ({ op : " remove " , path : pointer ( path ) }); break ; case " changed " : if ( node . cont ) node . children . forEach ( c => buildPatch ( c . node , [... path , c . key ], ops )); else ops . push ({ op : " replace " , path : pointer ( path ), value : node . after }); break ; // "unchanged": emit nothing } } Prove it with the assertions that separate structural from textual: diffNode({a:1,b:2}, {b:2,a:1}).kind === "unchanged" (key order ignored) and diffNode(10, "10").kind === "changed" (type matters). Because it compares meaning instead of characters, it shrugs off the whitespace and reorders that fool a line diff — the right way to compare data instead of the way it happens to be printed. Paste two documents and watch the colour-coded tree and the emitted patch update live: https://dev48v.infy.uk/solve/day57-json-diff.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/structural-json-diff-from-scratch-compare-meaning-not-lines-and-emit-an-rfc-6902-patch-3987

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
