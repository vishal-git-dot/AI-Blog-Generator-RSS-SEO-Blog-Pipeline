---
title: "# I Shipped a Working Win-Check... That Could Be Wrong 9 Times Out of 10"
slug: "i-shipped-a-working-win-check-that-could-be-wrong-9-times-out-of-10"
author: "BlackJosh007"
source: "devto_webdev"
published: "Sat, 29 Aug 2026 20:40:51 +0000"
description: "While building Tenzies (my React capstone from freeCodeCamp), I hit a problem that looked simple on the surface: check if the player won. The rule is easy to..."
keywords: "die, diceno, all, value, every, loop, count, check"
generated: "2026-08-29T20:45:19.187326"
---

# # I Shipped a Working Win-Check... That Could Be Wrong 9 Times Out of 10

## Overview

While building Tenzies (my React capstone from freeCodeCamp), I hit a problem that looked simple on the surface: check if the player won. The rule is easy to say out loud: all 10 dice must be held, and all 10 must show the same value. Turning that into code taught me more about array logic than any tutorial had so far — mostly because my first version had a bug I didn't even know to look for. My First Attempt I reached for a for loop and a counter: let count = 0 ; for ( let i = 0 ; i < diceNo . length - 1 ; i ++ ) { if ( diceNo [ i ]. isHeld && ( diceNo [ i ]. value == diceNo [ i + 1 ]. value )) { count += 1 ; if ( count === diceNo . length - 1 ) console . log ( " you won " ); } } The logic, in my head: compare each die to the next die. If they match in value and the current one is held, count it. With 10 dice, there are 9 pairs — so if all 9 comparisons pass, count hits 9, and that means everyone matches. Right? It worked. I tested it, saw "you won" print at the right time, and felt genuinely proud — until I looked at the instructor's solution and saw the whole thing done in three lines with .every() . My first reaction was honestly "that feels like cheating." My second, more useful reaction was: wait, is my version even correct? The Bug I Almost Missed Look closely at the loop bounds: i < diceNo.length - 1 . With 10 dice, i runs from 0 to 8. The isHeld check only ever runs on diceNo[i] — the last die, at index 9, never gets its isHeld checked at all. So picture this scenario: dice 0 through 8 are all held and all show a 4. Die 9 shows a 4 too, purely by chance, but the player never held it. My loop would still count 9 matches and declare a win — even though one die was never actually locked in by the player. The bug isn't loud; it only shows up in a specific edge case, which is exactly why I didn't catch it just by playing the game normally. The Fix let gameWon = false ; if ( diceNo . every ( die => die . isHeld ) && diceNo . every ( die => die . value === diceNo [ 0 ]. value ) ) { gameWon = true ; } Two separate, symmetric checks: are all 10 held? and do all 10 match the first die's value? Every die gets checked, every time, with no off-by-one gap hiding at the edges. That's the real reason this version is better — not brevity for its own sake, but that it's structurally impossible to skip a die. The Lesson The takeaway for me isn't "loops bad, array methods good." It's this: when a loop's bounds don't map 1:1 to "check every item," ask what you're actually excluding — and whether that exclusion is intentional. .every() forced correctness by construction. My loop left a gap I had to go looking for. Also — I've officially learned to check whether a built-in method already solves my problem before I hand-roll a loop and a counter. Lesson paid for in stress, but paid. What's Next I'm planning to extend the game with: A timer + roll counter, to track how fast you can win Dice styled with actual pips instead of numbers Full keyboard navigation for accessibility Live demo: https://tenzies-six-silk.vercel.app/ Repo: https://github.com/BlackJosh007/tenzies

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blackjosh007/-i-shipped-a-working-win-check-that-could-be-wrong-9-times-out-of-10-48b0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
