---
title: "How Fruit Ninja Works: Projectile Arcs and One Line of Geometry Slice Every Fruit"
slug: "how-fruit-ninja-works-projectile-arcs-and-one-line-of-geometry-slice-every-fruit"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 18:47:56 +0000"
description: "Fruit Ninja looks like it needs a sprite atlas and a physics engine. It doesn't. Strip it down and the whole game is two ideas stacked together: fruit are pr..."
keywords: "fruit, const, segment, one, line, bomb, distance, point"
generated: "2026-08-07T19:04:02.695536"
---

# How Fruit Ninja Works: Projectile Arcs and One Line of Geometry Slice Every Fruit

## Overview

Fruit Ninja looks like it needs a sprite atlas and a physics engine. It doesn't. Strip it down and the whole game is two ideas stacked together: fruit are projectiles thrown up from below the screen, and a "slice" is the oldest trick in collision detection — the shortest distance from a point to a line segment. Everything else is decoration. A fruit is just a projectile There are no scripted paths. A fruit is a circle with a position and a velocity, spawned below the bottom edge and thrown upward with a strong negative vertical velocity plus a sideways nudge toward the middle. From there, one line of gravity per tick bends the launch into a parabola — rise, slow, fall — for free. const GRAVITY = 900 ; // px/s^2, pulls everything down function spawnOne (){ const bomb = Math . random () < 0.12 ; // ~1 in 8 is a bomb const type = bomb ? " bomb " : ( Math . random () * FRUITS . length | 0 ); const r = bomb ? 30 : FRUITS [ type ]. r ; const x = rand ( W * 0.15 , W * 0.85 ); // random column const y = H + r + 10 ; // start just below the screen const vy = - rand ( 700 , 860 ); // thrown UP (negative y) const vx = clamp (( W / 2 - x ) * 0.6 , - 260 , 260 ) + rand ( - 60 , 60 ); fruits . push ({ x , y , vx , vy , r , type , rot : 0 , vrot : rand ( - 3 , 3 ), sliced : false }); } Advancing that physics naively — by however long the last frame took — means the fruit fly higher on a slow machine than a fast one. The fix is a fixed-timestep accumulator: bank the real elapsed time and spend it in equal 1/120 s chunks, so the simulation is identical on a 60Hz or a 144Hz screen. The blade is your recent pointer trail There's no sword sprite either. The blade is an array of the last places your pointer visited, each stamped with a time; anything older than ~130ms is dropped. The important part is that each new point paired with the previous one is a line segment — the exact stroke your hand just swept. The slice test — point-to-segment distance This is the heart of the whole game. A fruit is a circle; the swipe is a segment; the fruit is cut when the segment passes within the fruit's radius of its centre. To find that shortest distance you project the centre onto the infinite line through the segment to get a parameter t , clamp t to [0,1] so you stay on the segment (not the endless line), then compare the closest point's distance to the radius. Compare squared distances and there isn't even a square root. function segCircle ( ax , ay , bx , by , cx , cy , r ){ const dx = bx - ax , dy = by - ay ; const len2 = dx * dx + dy * dy ; let t = len2 ? (( cx - ax ) * dx + ( cy - ay ) * dy ) / len2 : 0 ; // project C onto A→B t = t < 0 ? 0 : t > 1 ? 1 : t ; // clamp to the segment const px = ax + t * dx , py = ay + t * dy ; // closest point on segment const ex = cx - px , ey = cy - py ; return ex * ex + ey * ey <= r * r ; // within the radius? → hit } Because one segment is tested against every fruit each move, a single swipe drawn across three fruit registers three slices in the same tick — which is exactly how combos work. A short timer resets on every cut; while the blade keeps slicing, the streak climbs. Slicing spawns two half-discs thrown perpendicular to the cut plus a burst of juice particles, all obeying the same gravity. Touch a bomb, or let a fruit fall off the bottom untouched, and you lose one of three lives. That's it: a parabola from one line of gravity, a segment from your last two pointer positions, and one distance test deciding every cut. No engine required. Play the live build (and read all eight code blocks) here: https://dev48v.infy.uk/game/day57-fruit-ninja.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/how-fruit-ninja-works-projectile-arcs-and-one-line-of-geometry-slice-every-fruit-4lfp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
