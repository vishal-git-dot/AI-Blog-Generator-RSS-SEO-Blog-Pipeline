---
title: "Implementing FreeCell SuperMoves: Capacity Rules and Edge Cases"
slug: "implementing-freecell-supermoves-capacity-rules-and-edge-cases"
author: "SkyWalker"
source: "devto_webdev"
published: "Sat, 01 Aug 2026 13:20:42 +0000"
description: "FreeCell looks simple until a player tries to move a long descending run and the interface refuses. The useful programming lesson is that a legal “supermove”..."
keywords: "run, capacity, columns, supermovecapacity, card, empty, console, move"
generated: "2026-08-01T13:39:22.850386"
---

# Implementing FreeCell SuperMoves: Capacity Rules and Edge Cases

## Overview

FreeCell looks simple until a player tries to move a long descending run and the interface refuses. The useful programming lesson is that a legal “supermove” is not a special card rule. It is a compact way of representing a sequence of ordinary single-card moves through temporary storage. This article derives a small capacity calculator that can be used in a browser-based FreeCell implementation, a rules explainer, or automated tests. The basic capacity rule Let: F be the number of empty free cells. C be the number of empty tableau columns that may be used as temporary storage. The destination column is not counted as empty storage. A common implementation uses: maximum movable cards = (F + 1) × 2^C With no empty tableau columns, every empty free cell holds one card and the final card can move directly, so the capacity is F + 1 . Each usable empty column doubles that capacity because it can hold a previously assembled sub-sequence. There is an important edge case: if the move itself ends on an empty column, that destination cannot also be used as temporary storage. In code, calculate the storage columns after excluding the destination. A small JavaScript implementation function superMoveCapacity ( emptyFreeCells , emptyColumns , destinationIsEmpty ) { const free = Math . max ( 0 , Math . trunc ( emptyFreeCells )); let columns = Math . max ( 0 , Math . trunc ( emptyColumns )); if ( destinationIsEmpty && columns > 0 ) { columns -= 1 ; } return ( free + 1 ) * ( 2 ** columns ); } console . log ( superMoveCapacity ( 2 , 1 , false )); // 6 console . log ( superMoveCapacity ( 2 , 1 , true )); // 3 Keeping this function pure makes it easy to test. It should not inspect the DOM or mutate game state. The board parser can count available cells and columns, then pass those numbers into the rule. Validate the sequence before checking capacity Capacity is only half of legality. A candidate run must also be internally valid. For standard FreeCell, adjacent cards descend by one rank and alternate color. function isDescendingAlternating ( run ) { return run . every (( card , index ) => { if ( index === run . length - 1 ) return true ; const next = run [ index + 1 ]; return card . rank === next . rank + 1 && card . color !== next . color ; }); } function canMoveRun ( run , board ) { if ( ! isDescendingAlternating ( run )) return false ; const capacity = superMoveCapacity ( board . emptyFreeCells , board . emptyColumns , board . destinationIsEmpty ); return run . length <= capacity ; } Separate validation also produces better UI messages. “This run is not alternating colors” is more helpful than a generic “illegal move,” while “Free one cell to move four cards” gives the player an actionable hint. Tests that catch real bugs The most valuable cases sit at the boundaries: console . assert ( superMoveCapacity ( 0 , 0 , false ) === 1 ); console . assert ( superMoveCapacity ( 4 , 0 , false ) === 5 ); console . assert ( superMoveCapacity ( 0 , 3 , false ) === 8 ); console . assert ( superMoveCapacity ( 2 , 2 , false ) === 12 ); console . assert ( superMoveCapacity ( 2 , 2 , true ) === 6 ); Also test negative input, fractional values from malformed state, a destination column that becomes empty during a move, and variants whose rules limit how temporary columns may be used. For a visual explanation of the same rule and examples of movable card sequences, this FreeCell movable-cards guide is a useful companion reference. Why this approach works well The formula belongs in the rules layer, not the drag-and-drop handler. That keeps mouse input, touch input, keyboard controls, hints, undo, and automated solvers consistent. A single tested function can answer all of them. It also makes a nice accessibility improvement. Before a player starts dragging, the interface can announce the maximum movable run length. The rule stops feeling arbitrary, and the implementation stays small enough to reason about.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/skywalker_2de7de5f97df567/implementing-freecell-supermoves-capacity-rules-and-edge-cases-2012

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
