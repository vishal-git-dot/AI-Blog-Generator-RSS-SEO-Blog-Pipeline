---
title: "One Flag, Three Consequences: Switching Scoring Rules Mid-Match"
slug: "one-flag-three-consequences-switching-scoring-rules-mid-match"
author: "Vladimir Ushakov"
source: "devto_webdev"
published: "Fri, 21 Aug 2026 06:49:32 +0000"
description: "Cat Laundry is a 4×4 strategy duel. A move starts by clicking one of your own cats. That cat changes to the opponent's color, while your color propagates alo..."
keywords: "scoring, game, late, points, one, match, move, same"
generated: "2026-08-21T06:55:13.098304"
---

# One Flag, Three Consequences: Switching Scoring Rules Mid-Match

## Overview

Cat Laundry is a 4×4 strategy duel. A move starts by clicking one of your own cats. That cat changes to the opponent's color, while your color propagates along the four diagonals. When the wave stops, completed squares, diamonds, and crosses are scored. That was already an unusual rule set. The late game added a second problem: how do you change scoring rules during a live match without making the result feel arbitrary? The rule I shipped is called Spin Cycle : when either player reaches 70 points, late game begins; squares and diamonds stop scoring; only crosses count, for 10 points each; the winning target remains 100; cat rotation becomes visibly faster. The important part is not the threshold itself. It is making the state transition, scoring code, and visual feedback describe the same event. Change state after scoring, not before The match keeps one boolean: let finalPhase = false ; function activateFinalPhase () { if ( finalPhase || matchTarget < 100 || Math . max ( humanScore , aiScore ) < 70 ) { return false ; } finalPhase = true ; return true ; } The timing matters. I call this only after the current move has finished finding patterns and adding their points. That means the move which takes a player from 68 to 73 is evaluated under the original rules. Only the following state is late game. If I switched the flag while the wave was still resolving, the same move could begin under one scoring table and finish under another. The return value is useful too. true does not merely mean that late game is active; it means that this exact scoring event started it. The UI can therefore announce the transition once instead of repeating a banner after every later move. Put the rule filter next to pattern detection Squares, diamonds, and crosses all pass through completedPatterns() . Spin Cycle does not add a parallel scoring system. It narrows the existing candidate list: for ( const pattern of PATTERNS ) { if ( finalPhase && ! pattern . name . startsWith ( ' КРЕСТ ' )) continue ; const scoredPattern = finalPhase ? { ... pattern , points : 10 } : pattern ; // Find placements that match the board and touch this move. } This gives the state flag two explicit effects in one place: non-cross patterns are ignored; every surviving cross is worth 10. The rest of the scoring pipeline stays unchanged: overlapping figures are resolved, points are summed, used cells are recycled, and the next turn begins. Keeping the filter here also makes AI simulation use the same rules. The AI evaluates candidate moves through the same pattern function instead of maintaining a second late-game scoring table that could drift away from the real match. Visual feedback must read the same flag The board renderer applies a final-phase class from that same boolean. CSS makes the washing-machine motion more aggressive, while the score event that flips the flag replaces the normal status copy with a direct explanation: const phaseStarted = activateFinalPhase (); ui . status . textContent = phaseStarted ? ' 70 POINTS · SPIN MODE ACTIVATED ' : normalStatus ; ui . log . textContent = phaseStarted ? ' ONLY CROSSES SCORE · EACH CROSS +10 POINTS ' : normalLog ; This creates a causal sequence the player can follow: a move completes; points are awarded; a score reaches 70; the transition message appears; the board accelerates; future scoring accepts only crosses. The animation is not decoration. It is a persistent reminder that the scoring function is now in a different mode. Why keep the target at 100? Changing the scoring system and the victory target at the same time would create two moving references. Keeping 100 preserves the player's existing progress while the set of useful shapes becomes narrower. A 10-point cross is also large enough to make a late reversal possible. The leading player cannot simply wait for the score to finish itself: both players still need to build or interrupt a cross. One state, three consumers Spin Cycle became easier to reason about once I treated it as a state transition with three consumers: game logic filters patterns and changes cross value; presentation accelerates the cats and keeps a visible late-game style; event copy explains exactly when and why the transition happened. If any one of those consumers derived late game independently, the match could display Spin Cycle while scoring a square, or score a 10-point cross before the player saw the rule change. You can play Cat Laundry in the browser . When a game changes rules mid-match, what visual signal would make you trust that the new scoring mode has actually taken effect?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/straightfunctor/one-flag-three-consequences-switching-scoring-rules-mid-match-3kd1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
