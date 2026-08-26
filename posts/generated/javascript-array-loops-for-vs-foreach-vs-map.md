---
title: "JavaScript Array Loops: for vs forEach vs map"
slug: "javascript-array-loops-for-vs-foreach-vs-map"
author: "Muhammad Wasif"
source: "devto_webdev"
published: "Wed, 26 Aug 2026 12:54:49 +0000"
description: "Use map when you want a new array, filter when you want fewer items, for...of when you need to break or await , and a plain for loop only when you are loopin..."
keywords: "foreach, array, you, map, const, nums, when, await"
generated: "2026-08-26T13:01:59.366739"
---

# JavaScript Array Loops: for vs forEach vs map

## Overview

Use map when you want a new array, filter when you want fewer items, for...of when you need to break or await , and a plain for loop only when you are looping over millions of items and have measured that it matters. forEach sits in an awkward middle: it reads nicely, but it cannot break and it silently ignores await — which makes it the wrong default more often than people realise. Quick decision table You want to... Use Why Transform every item into something new map Returns a new array, same length Keep only some items filter Returns a new, shorter array Boil the array down to one value reduce Sum, total, grouped object Stop early / break for...of forEach cannot be stopped await something each time round for...of forEach does not wait Just do a side effect (log, push, update DOM) for...of or forEach Both fine; for...of is safer Squeeze out speed on a huge array for Measurably faster, but see the benchmark forEach vs map map builds and returns a new array . forEach returns undefined — it exists purely for side effects. const nums = [ 1 , 2 , 3 , 4 , 5 ]; const doubled = nums . map ( n => n * 2 ); console . log ( doubled ); // [2, 4, 6, 8, 10] console . log ( nums ); // [1, 2, 3, 4, 5] ← original untouched console . log ( nums . forEach ( n => n * 2 )); // undefined The practical rule: if you're not using the returned array, you shouldn't be using map . Calling map purely for side effects builds a whole array you then throw away, and it misleads the next reader into hunting for a result that never gets used. You can't break out of forEach A return inside the callback only ends that one call — the loop keeps going: const nums = [ 1 , 2 , 3 , 4 , 5 ]; let visited = 0 ; nums . forEach ( n => { visited ++ ; if ( n > 3 ) return ; // looks like a break, isn't one }); console . log ( visited ); // 5 — every item was still visited With for...of , break does what you expect: let found = null ; for ( const n of nums ) { if ( n > 3 ) { found = n ; break ; } } console . log ( found ); // 4 If you only need to know whether something matches, find , some , every and includes all stop as soon as they have their answer. The async bug This is the one that costs real debugging hours: async function withForEach ( ids ) { const results = []; ids . forEach ( async ( id ) => { results . push ( await fetchThing ( id )); // runs later, too late }); return results ; // [] ← empty, every time } It returns an empty array. No error, no warning — forEach fires off the promises, ignores all of them, and returns. Use for...of , which genuinely pauses at each await : async function withForOf ( ids ) { const results = []; for ( const id of ids ) { results . push ( await fetchThing ( id )); // waits properly } return results ; // [1, 2, 3, 4, 5] } That runs the requests one after another . If they're independent and you want them concurrent, don't loop at all: const results = await Promise . all ( ids . map ( id => fetchThing ( id ))); for...of with await is sequential — use it when each step depends on the last, or when you're being gentle on a rate-limited API. Promise.all is concurrent and finishes as fast as the slowest request. Getting the index for ( const [ i , n ] of nums . entries ()) { console . log ( i , n ); // 0 1 / 1 2 / 2 3 ... } nums . forEach (( n , i ) => console . log ( i , n )); nums . map (( n , i ) => ` ${ i } : ${ n } ` ); Is a for loop actually faster? Yes — and far less often than people assume. Summing an array of 10 million numbers on Node v24: Loop Time for 88 ms for...of 577 ms forEach 750 ms So a classic for loop is roughly 8× faster than forEach at that size. That sounds dramatic until you scale it down: for an array of 1,000 items — which covers the overwhelming majority of real code — the same gap is well under a millisecond. Treat these as a rough shape rather than a law; results shift with the engine, the version and what the callback does. Write the clearest loop first. Reach for a plain for when you've measured a real bottleneck, not because a benchmark article said it was faster. The sparse array gotcha const sparse = [ 1 , , 3 ]; // note the missing middle item let a = 0 ; sparse . forEach (() => a ++ ); let b = 0 ; for ( const _ of sparse ) b ++ ; console . log ( a , b ); // 2 3 forEach (and map , and filter ) skip the hole ; for...of visits it as undefined . Rare, but genuinely confusing when it bites — two loops over the same array producing different counts. A few things people ask Should I use forEach or for...of? Prefer for...of as your default for side effects. It supports break and continue , works correctly with await , and handles sparse arrays predictably. forEach is fine for short synchronous callbacks — just never when async is involved. Does map change the original array? No. It returns a new array and leaves the original alone, which is why it fits well with React state. Be aware the items aren't deep-copied though: if your array holds objects, both arrays point at the same objects. What about for...in? Avoid it for arrays. for...in loops over keys , gives you strings ( "0" , "1" ) rather than numbers, and includes inherited enumerable properties. It's meant for plain objects. The short version: pick the loop that says what you mean. map announces "I'm building a new array", filter announces "I'm narrowing this down", and for...of announces "I'm doing something for each item, and I might stop or wait." Speed almost never decides it — clarity does. Originally published at cybercodelab.online .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wasifkhan111/javascript-array-loops-for-vs-foreach-vs-map-h6n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
