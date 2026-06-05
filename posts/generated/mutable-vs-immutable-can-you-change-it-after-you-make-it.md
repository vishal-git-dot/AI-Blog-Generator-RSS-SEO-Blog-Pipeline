---
title: ""Mutable" vs "Immutable": Can You Change It After You Make It?"
slug: "mutable-vs-immutable-can-you-change-it-after-you-make-it"
author: "Mohamed Idris"
source: "devto_webdev"
published: "Fri, 05 Jun 2026 09:27:00 +0000"
description: "You copy an array to be "safe," tweak the copy, and somehow the original changes too. You stare at the screen. You didn't touch the original. Did the compute..."
keywords: "you, original, copy, new, change, mutable, immutable, can"
generated: "2026-06-05T09:49:03.895018"
---

# "Mutable" vs "Immutable": Can You Change It After You Make It?

## Overview

You copy an array to be "safe," tweak the copy, and somehow the original changes too. You stare at the screen. You didn't touch the original. Did the computer just lie to you? Welcome to the world of mutable and immutable . Two words that explain a ton of "wait, why did that change?" bugs. The idea in one line Mutable means "can be changed after it's made." Immutable means "locked forever once it's made." The metaphor: a whiteboard vs a printed photo WHITEBOARD (mutable) PRINTED PHOTO (immutable) wipe it, rewrite it can't edit it same board, new content want a change? print a NEW photo A whiteboard is mutable . You change what's on it, but it's still the same board. A printed photo is immutable . You can't change it. If you want a different picture, you make a brand new print and keep (or toss) the old one. How it bites you in code const original = [ 1 , 2 , 3 ] const copy = original // NOT a copy! both names point to the SAME array copy . push ( 4 ) console . log ( original ) // [1, 2, 3, 4] <- surprise! the original changed too copy = original did not make a new array. It just gave the same whiteboard a second name. Writing through one name shows up under the other. Arrays and objects in JavaScript are mutable, so this trap is everywhere. // The fix: make a real new array (a fresh print), then change that const original = [ 1 , 2 , 3 ] const copy = [... original ] // new array with the same items copy . push ( 4 ) console . log ( original ) // [1, 2, 3] <- safe! console . log ( copy ) // [1, 2, 3, 4] A real case: React state React leans hard on immutability. If you change state in place, React often can't tell anything changed, so your screen doesn't update. // Wrong: mutating the same array. React may not re-render. todos . push ( newTodo ) setTodos ( todos ) // Right: hand React a brand new array setTodos ([... todos , newTodo ]) The rule "don't mutate state, replace it" is this exact idea. Treat state like a printed photo: make a new one instead of scribbling on the old. Gotchas juniors hit 1. Thinking = copies. For arrays and objects, = copies the reference (the name), not the contents. Both names share one thing. 2. const does not mean immutable. const arr = [1,2] just means you can't point arr at something else. You can still arr.push(3) . The box is locked; the contents are not. 3. Shallow copies only go one level deep. [...arr] copies the top level. Nested objects inside are still shared. Deep data needs deeper copying. Recap Mutable = changeable after creation (a whiteboard). Immutable = locked after creation (a printed photo). In JS, = shares the same thing; it does not copy it. For safe updates (especially React state), make a new value instead of changing the old one. Your turn Run the const copy = original; copy.push(4) example yourself and watch the original change. Then fix it with [...original] . Once that "aha" lands, explain "whiteboard vs printed photo" to a friend.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/edriso/mutable-vs-immutable-can-you-change-it-after-you-make-it-58gc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
