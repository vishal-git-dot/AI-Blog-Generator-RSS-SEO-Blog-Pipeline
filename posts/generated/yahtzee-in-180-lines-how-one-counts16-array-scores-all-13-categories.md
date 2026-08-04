---
title: "Yahtzee in 180 lines: how one counts[1..6] array scores all 13 categories"
slug: "yahtzee-in-180-lines-how-one-counts16-array-scores-all-13-categories"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Tue, 04 Aug 2026 08:45:43 +0000"
description: "Yahtzee looks like thirteen unrelated scoring rules bolted together: sum your 1s, chase a full house, hunt a five-of-a-kind, settle for "chance." Sit down to..."
keywords: "return, cat, dice, three, null, one, let, function"
generated: "2026-08-04T08:46:37.697563"
---

# Yahtzee in 180 lines: how one counts[1..6] array scores all 13 categories

## Overview

Yahtzee looks like thirteen unrelated scoring rules bolted together: sum your 1s, chase a full house, hunt a five-of-a-kind, settle for "chance." Sit down to build it and you find the opposite is true — every one of those rules is a single question asked of the same tiny array. There is no dice-physics engine, no rules table, no board object. Just five integers, a scorecard, and about 180 lines of vanilla JavaScript. The whole game is a handful of variables Five integers hold the dice faces, five booleans mark which you're keeping on the re-roll, a counter tracks how many of your three throws remain, and the scorecard is a plain object mapping each of thirteen box names to a number once scored or null while it's still open. let dice = [ null , null , null , null , null ]; // the five faces, 1..6 let held = [ false , false , false , false , false ]; // which you keep on re-roll let rollsLeft = 3 ; // three throws per turn let scores = {}; // box → number, or null = open A "roll" re-throws only the loose dice — that one if (!held[i]) is the entire hold-and-reroll gamble the game rests on: function roll (){ for ( let i = 0 ; i < 5 ; i ++ ) if ( ! held [ i ]) dice [ i ] = 1 + Math . floor ( Math . random () * 6 ); // loose ones only rollsLeft -- ; } One helper collapses thirteen rules into almost nothing Here is the trick. Walk the five dice once and tally how many showed each face into a seven-slot histogram (index 0 unused, 1–6 the faces). From that single array every category becomes one expression. function counts ( d ){ // histogram of the faces const c = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 ]; // c[1]..c[6] for ( const x of d ) c [ x ] ++ ; return c ; } function sum ( d ){ return d . reduce (( a , b ) => a + b , 0 ); } // dice [5,2,5,5,2] → counts [0,0,2,0,0,3,0] : three 5s, two 2s Now every score reads straight out of counts . "Three of a kind" asks whether any face reaches 3; a straight is a run of consecutive non-zero slots; "sixes" is c[6] * 6 : function longestRun ( c ){ // consecutive present faces let run = 0 , best = 0 ; for ( let f = 1 ; f <= 6 ; f ++ ){ run = c [ f ] ? run + 1 : 0 ; best = Math . max ( best , run ); } return best ; } function scoreFor ( cat , d ){ const c = counts ( d ), total = sum ( d ); if ( cat in FACE ) return c [ FACE [ cat ]] * FACE [ cat ]; if ( cat === " threeKind " ) return c . some ( n => n >= 3 ) ? total : 0 ; if ( cat === " fourKind " ) return c . some ( n => n >= 4 ) ? total : 0 ; if ( cat === " fullHouse " ) return c . includes ( 3 ) && c . includes ( 2 ) ? 25 : 0 ; if ( cat === " smallStraight " ) return longestRun ( c ) >= 4 ? 30 : 0 ; if ( cat === " largeStraight " ) return longestRun ( c ) >= 5 ? 40 : 0 ; if ( cat === " yahtzee " ) return c . some ( n => n === 5 ) ? 50 : 0 ; if ( cat === " chance " ) return total ; } Why the bonus lands at exactly 63 The famous +35 upper bonus is a single comparison — but the magic number is worth pausing on. If your six upper boxes together reach 63 or more, you collect the bonus: function upperBonus (){ return upperSubtotal () >= 63 ? 35 : 0 ; // 63 = three of every face } Why 63? Because 63 is precisely three of each face : 3×1 + 3×2 + … + 3×6 = 3 × 21 = 63. Averaging three-of-a-kind across the top half is the break-even line the designers chose, and the whole bonus is one >= 63 test. Because scoreFor is pure — dice in, number out — it doubles as the live green preview on every open box, and committing a box is three lines of bookkeeping. The grand total is just the upper subtotal plus the bonus plus the lower boxes, and since unscored boxes are null (counted as zero), the same total function runs live during play and as the final score. That's the lesson: a pile of special-case rules often hides one small shared representation. Find the histogram, and Yahtzee scores itself. Play the full game, step through the scoring engine, and copy the code block by block at the live build: https://dev48v.infy.uk/game/day54-yahtzee.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/yahtzee-in-180-lines-how-one-counts16-array-scores-all-13-categories-k3m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
