---
title: "Pinterest masonry two ways: one-line CSS columns vs shortest-column JavaScript, and the reading-order catch"
slug: "pinterest-masonry-two-ways-one-line-css-columns-vs-shortest-column-javascript-and-the-reading-order-catch"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Wed, 22 Jul 2026 08:27:52 +0000"
description: "A Pinterest board is a wall of cards of wildly different heights that still tile together with no ragged row gaps. I built the whole thing — the pins, both l..."
keywords: "column, pin, gap, masonry, colh, height, you, pins"
generated: "2026-07-22T08:36:37.029091"
---

# Pinterest masonry two ways: one-line CSS columns vs shortest-column JavaScript, and the reading-order catch

## Overview

A Pinterest board is a wall of cards of wildly different heights that still tile together with no ragged row gaps. I built the whole thing — the pins, both layout techniques behind one toggle, responsive columns, and the hover Save overlay — with no library, and the interesting part turned out to be that there are two genuinely different ways to get masonry, each with its own trade-off. Here's what I learned building it. Why CSS Grid can't do this The instinct is to reach for Grid, but Grid is built on rows: every cell in a row shares that row's track height. Put a short pin next to a tall one and the whole row becomes as tall as the tall pin, leaving a gap before the next row starts. Masonry needs each column to flow independently and pull the next item up into that gap — Grid's row model can't express it. (There is a grid-template-rows: masonry proposal, but it's experimental and not shipped across browsers.) That one limitation is the entire reason masonry is its own pattern. Technique A — CSS columns, one line The cheapest masonry is the multi-column layout. Set column-count and column-gap on the container, mark each pin break-inside: avoid so it never splits across a boundary, and the browser packs it for you. Zero JavaScript, no measuring. .board { column-count : 4 ; column-gap : 16px ; } /* the whole layout */ .board .pin { break-inside : avoid ; /* never split a pin across columns */ width : 100% ; margin : 0 0 16px ; /* the row gap */ } The reading-order catch This is the trade-off you must know before choosing it. CSS columns fills vertically : pins 1, 2, 3 go down the first column, then 4, 5, 6 down the second. So on screen, pin 5 sits under pin 4, not to its right — the reading order is column-major. col 1 col 2 col 3 col 4 [ 1 ] [ 5 ] [ 9 ] [13 ] [ 2 ] [ 6 ] [10 ] [14 ] [ 3 ] [ 7 ] [11 ] [15 ] For a gallery where order is irrelevant that's fine. But for a feed where "newest" should read left-to-right across the top, it's wrong — and there's no clean CSS fix, because the fill direction is intrinsic to how columns work. When order matters, you graduate to technique B. Technique B — JS masonry: shortest-column placement True masonry places pins yourself, in DOM order, each into whichever column is currently shortest . Keep an array of running column heights, all starting at zero. For each pin, find the index of the minimum, that's its column; place it, then add its measured height plus the gap back to that column's total. Because you always feed the shortest column the wall stays balanced, and because you walk pins in DOM order they read left-to-right across the top. const colH = new Array ( cols ). fill ( 0 ); // running height of each column pins . forEach ( pin => { let c = 0 ; // which column is shortest right now? for ( let k = 1 ; k < cols ; k ++ ) if ( colH [ k ] < colH [ c ]) c = k ; place ( pin , c , colH [ c ]); // drop it there colH [ c ] += pin . offsetHeight + GAP ; // grow that column }); You own the coordinates JS masonry means absolute positioning. Make the board position: relative and every pin position: absolute . Compute the column width from the container — (boardWidth − (cols−1)·gap) / cols — and set it on each pin first , so aspect-ratio resolves the height before you read offsetHeight . The pin's left is its column index times (colW + gap) ; its top is that column's running height. const colW = ( board . clientWidth - GAP * ( cols - 1 )) / cols ; pins . forEach ( p => { p . style . position = " absolute " ; p . style . width = colW + " px " ; }); const colH = new Array ( cols ). fill ( 0 ); pins . forEach ( p => { let c = 0 ; for ( let k = 1 ; k < cols ; k ++ ) if ( colH [ k ] < colH [ c ]) c = k ; p . style . left = c * ( colW + GAP ) + " px " ; p . style . top = colH [ c ] + " px " ; colH [ c ] += p . offsetHeight + GAP ; }); board . style . height = Math . max (... colH ) + " px " ; // absolutely-placed pins add no height The subtlety people miss: because the pins are absolutely positioned they no longer contribute to the container's height, so you must set the board's height to the tallest column yourself or the page below overlaps. Responsive, and the rest Column count follows the width — a plain function returning 2/3/4/5 by breakpoint — and for JS masonry you must re-layout on resize (throttled with requestAnimationFrame ), because the column width, and therefore every pin's height and position, changes. The pure-CSS route gets responsiveness almost free by swapping column-count for column-width . On top sits the hover overlay: a dark gradient that dims the image, faded in with opacity (not display , so nothing reflows), with Save as a persistent toggle you store in a Set rather than a hover effect. Flip between the two techniques and watch the numbered reading order: https://dev48v.infy.uk/design/day41-pinterest-masonry.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/pinterest-masonry-two-ways-one-line-css-columns-vs-shortest-column-javascript-and-the-2325

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
