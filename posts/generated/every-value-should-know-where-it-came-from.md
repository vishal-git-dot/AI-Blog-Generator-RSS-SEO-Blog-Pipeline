---
title: "Every value should know where it came from"
slug: "every-value-should-know-where-it-came-from"
author: "JSLab"
source: "devto_webdev"
published: "Wed, 21 Oct 2026 16:51:08 +0000"
description: "You run your code. Something prints 42 . Which line printed it? If you had to stop and think, this post is for you. It's about one small idea that makes feed..."
keywords: "you, line, value, log, total, your, output, const"
generated: "2026-10-21T16:57:15.638655"
---

# Every value should know where it came from

## Overview

You run your code. Something prints 42 . Which line printed it? If you had to stop and think, this post is for you. It's about one small idea that makes feedback loops better: every value should carry the address of the line that produced it. The problem with a flat list Here's a small script. Nothing exotic. const orders = [ { id : 1 , total : 40 }, { id : 2 , total : 15 }, { id : 3 , total : 0 }, ]; const paid = orders . filter (( o ) => o . total > 0 ); const revenue = paid . reduce (( sum , o ) => sum + o . total , 0 ); const average = revenue / paid . length ; console . log ( paid . length ); console . log ( revenue ); console . log ( average ); Run it and you get 2 , 55 and 27.5 . Fine. But those three numbers have lost their origin. You know the order they appeared in. You have to remember which console.log was which. Now imagine this script at 300 lines, with logs in loops, helpers and callbacks. The output is a pile of values with no return address. You end up writing labels by hand: console.log("paid.length:", paid.length) . That works, but you're doing bookkeeping the machine could do for you. The idea: anchor output to the source Give every result, log and error a line number. Then three nice things fall out. 1. You stop labelling. The line number is the label. 2. You can navigate both ways. Hover a row in the output and the matching line in the editor lights up. Put your cursor on a line and the rows it produced light up. Click a row's line number and you jump to the code. 3. Errors get an address. A stack trace is a list of places. If those places are your lines, the trace becomes a set of links instead of a puzzle. We build JSLab around this idea, so it's the worked example here — it's our own tool, so discount the praise accordingly. Fast loop, anchored output JSLab is a JavaScript and TypeScript scratchpad for macOS. You type; it runs. Auto Run fires after a short pause in typing (300 ms by default, and you can change it in Settings → Advanced). ⌘R runs on demand. Each result, log and error shows up beside the line that produced it. The output panel has four filter chips, All, Results, Logs and Errors, each with a live count. Counts stay visible even at zero, which is oddly satisfying. Why does speed matter for this idea? Because anchoring and latency multiply. If the result lands next to the line right after you stop typing, you can change one character and see exactly which value moved. The feedback is local in space and in time. Let the tool do the logging Take the same script, with Auto Log on. Auto Log shows the value of each top-level expression beside its line, so you rarely need console.log . It skips assignments and console.* calls. So this works with no logging at all: const orders = [ { id : 1 , total : 40 }, { id : 2 , total : 15 }, { id : 3 , total : 0 }, ]; orders . filter (( o ) => o . total > 0 ); orders . length ; Two expressions, two values, each beside its own line. When you want a value from the middle of something, magic comments do it. Append //? to log the value on that line: const paid = orders . filter (( o ) => o . total > 0 ); //? There's also /*?*/ for logging mid-expression, and a form with $ as a placeholder for the value, like //? $.length , for logging something derived from it. The editor docs list the exact syntax; I'd rather you read it there than trust my paraphrase. Logging without editing Sometimes you don't want to touch the code at all. Logpoints do that. Click the gutter, or press F9 on a line, and that line is logged every time it runs. Press ⇧⌘F9 to clear all logpoints in the tab. This is the same idea again. The log is anchored to a line, and the line stays untouched. Errors with an address Here's the case where anchoring pays off most. function parsePrice ( raw ) { const value = Number ( raw . replace ( " $ " , "" )); if ( Number . isNaN ( value )) { throw new Error ( `Bad price: ${ raw } ` ); } return value ; } const prices = [ " $4 " , " $12 " , " twelve " ]. map ( parsePrice ); The third item throws. In JSLab the error row is tinted and marked in the editor margin. Its stack frames are mapped back to your source lines, so they point at the code you wrote. You click the frame, and you're on the line. Nobody has ever said "I wish my stack trace pointed somewhere else." Values you can poke Anchored output is only useful if you can inspect it. Objects, arrays, Maps and Sets expand one level at a time, and ⌥→ expands everything nested. Right-click a value to copy it as plain text, as JSON, or as a path like $.users[3]["my-key"] . Copy All lives on the empty space in the panel. What you can steal even if you never install anything The tool is the example. The idea works anywhere: Tag output with its source. In your own logger, include file and line. Future you will say thanks. Prefer expressions over statements for debugging. If you can see a value without editing code, you'll look at more values. Shorten the loop. The closer in time a result arrives, the less you have to hold in your head. Make errors point at your code, not the runtime's. Source maps exist for this reason. A practical note JSLab runs your code in a separate Bun process, so an infinite loop or a crash doesn't take the editor down. It's for Apple Silicon Macs on macOS 14 or later. There's a 14-day free trial. JSLab launches on November 15. Until then you can read the site and the docs at js-lab.app and the output docs . If one idea stays with you, make it this: a value without a line number is a value without a story. Go give your output an address.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jslab/every-value-should-know-where-it-came-from-ofb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
