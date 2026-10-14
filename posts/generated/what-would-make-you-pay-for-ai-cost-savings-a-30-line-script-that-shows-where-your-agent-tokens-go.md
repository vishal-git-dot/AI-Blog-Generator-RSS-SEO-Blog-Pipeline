---
title: "What would make you pay for AI cost savings? A 30-line script that shows where your agent tokens go"
slug: "what-would-make-you-pay-for-ai-cost-savings-a-30-line-script-that-shows-where-your-agent-tokens-go"
author: "rene"
source: "devto_ai"
published: "Wed, 14 Oct 2026 11:29:21 +0000"
description: "A recent Ask HN asked: "Would you pay for saving AI cost?" and "what would you need to see before trusting to pay?" My answer: a number measured on my own lo..."
keywords: "you, const, not, what, pay, your, token, total"
generated: "2026-10-14T11:32:22.312041"
---

# What would make you pay for AI cost savings? A 30-line script that shows where your agent tokens go

## Overview

A recent Ask HN asked: "Would you pay for saving AI cost?" and "what would you need to see before trusting to pay?" My answer: a number measured on my own logs, before and after, that I can reproduce. Not a percentage claim from a landing page. So here is the measuring part, free. Run it on your own agent transcripts first; decide about fixes after. Step 1: find where the tokens go Most coding-agent cost is not your prompt. It is repeated context: the same file dumps, tool output and boilerplate resent every turn. This script takes a JSONL transcript (one message per line, with a content string) and reports which chunks repeat the most. // token-hotspots.mjs - node token-hotspots.mjs transcript.jsonl import fs from " node:fs " ; const lines = fs . readFileSync ( process . argv [ 2 ], " utf8 " ). split ( " \n " ). filter ( Boolean ); const approxTokens = s => Math . ceil ( s . length / 4 ); // rough: ~4 chars per token const seen = new Map (); let total = 0 ; for ( const l of lines ) { let m ; try { m = JSON . parse ( l ); } catch { continue ; } const text = typeof m . content === " string " ? m . content : JSON . stringify ( m . content ?? "" ); total += approxTokens ( text ); // fingerprint each 400-char block for ( let i = 0 ; i < text . length ; i += 400 ) { const k = text . slice ( i , i + 400 ); if ( k . length < 200 ) continue ; seen . set ( k , ( seen . get ( k ) || 0 ) + 1 ); } } const repeated = [... seen . entries ()]. filter (([, n ]) => n > 1 ); const wasted = repeated . reduce (( a , [ k , n ]) => a + approxTokens ( k ) * ( n - 1 ), 0 ); console . log ({ messages : lines . length , approxTotalTokens : total , approxRepeatedTokens : wasted , repeatedShare : total ? + ( wasted / total ). toFixed ( 3 ) : 0 }); repeated . sort (( a , b ) => b [ 1 ] - a [ 1 ]). slice ( 0 , 5 ) . forEach (([ k , n ]) => console . log ( ` ${ n } x ${ k . slice ( 0 , 80 ). replace ( / \n /g , " " )} ...` )); The repeatedShare number is the ceiling on what a de-duplication pass could save for that transcript. If it is 3%, do not pay anyone. If it is 40%, now you know why. Step 2: the usual fixes, in order of effort Stop re-reading unchanged files. Cache by path + mtime and send a reference instead of the dump. Truncate tool output at the source (tail of test logs, head+tail of long diffs). Pin a short, stable system prompt and move long rules into files loaded on demand. Summarize old turns instead of replaying them. Ask for terse output when you do not need prose. None of these needs a paid tool. The value of a paid checklist is only saving you the hour of working out the order and the thresholds. Honest limits The 4-chars-per-token estimate is rough; use your provider's tokenizer for billing-grade numbers. Repetition share is not the same as savings: some repeats are cached by the provider at a discount, so check your pricing. I have not measured savings across a population of users; run it on yours. If you want the checklist version of the fixes above (with the thresholds and the order I use), it is a pay-what-you-want download, $1 minimum: Prompt Token Diet Checklist . The script above is yours either way. What would you need to see before paying for something like this? I am curious which number convinces you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/renev3408/what-would-make-you-pay-for-ai-cost-savings-a-30-line-script-that-shows-where-your-agent-tokens-go-3eaj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
