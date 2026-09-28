---
title: "Making an SVG cat walk: planted feet, bones and a gravity arc"
slug: "making-an-svg-cat-walk-planted-feet-bones-and-a-gravity-arc"
author: "Usman Bashir"
source: "devto_ai"
published: "Mon, 28 Sep 2026 04:24:23 +0000"
description: "If you have ever animated a character in SVG, you have probably met the three classic failures: a limb that tears away from the body at the joint, feet that ..."
keywords: "body, svg, feet, first, one, mcp, foot, walk"
generated: "2026-09-28T04:46:35.839668"
---

# Making an SVG cat walk: planted feet, bones and a gravity arc

## Overview

If you have ever animated a character in SVG, you have probably met the three classic failures: a limb that tears away from the body at the joint, feet that skate across the floor, and a jump that feels floaty. We hit all three while making a line-drawn cat jump and walk, and each one has a clean, well-known fix from animation and physics. Some context first: both tools here come from SVG Lab (svglab.app). Opus 5.5 drew this cat through the SVG Lab MCP in the SVG Lab editor, anchor by anchor from a reference line drawing, with no auto-tracing; the SVG Lab MCP is in early access now. Opus 5.5 then animated it through the SVG Animate MCP , a separate engine for our upcoming animation platform, which is still in development. This post covers the ideas, not the implementation. Failure 1: the joint tears Rotating a leg path around a pivot is the first thing everyone tries. At small angles it is fine. At 20 degrees, the top of the leg path leaves the body outline and the silhouette breaks. The standard answer is a rig: bones inside the drawing, with the outline weighted to them. Points mid-bone follow one bone. Points near a joint blend between the two bones that meet there, so the bend is smooth. Points above the chain's first joint stay with the body, so the limb stays attached. One practical lesson: let the body's outline blend slightly with the upper leg as well. Skin stretches at a hip. A perfectly rigid body next to a bending leg still shows a seam. Failure 2: the feet skate Foot sliding comes from animating legs by angle while the body translates independently. The fix is inverse kinematics: specify where the foot is, solve the joint angles to reach it. For a walk, each foot runs a stance and swing schedule: Plant the foot ahead of the hip. Hold it fixed in the ground frame while the body moves over it. Lift it once it is behind the hip and swing it forward on a low arc. Plant it again, one stride on. Measured over every stance of all four paws, the worst drift was 0.04 px. Two details that matter more than they look: accelerate the body from rest and decelerate it to rest, and make the last step bring every foot back under the body. Then the clip starts and ends in the same pose, with no pop. Failure 3 (a sneaky one): the wrong gait Cats walk in a lateral sequence: hind, same-side fore, other hind, other fore, with at least two feet down at all times. Our first footfall plot showed a diagonal sequence instead. It looked plausible on screen. The plot made it undeniable. If you only take one thing from this post: plot your footfalls as lanes. It is the fastest gait debugger there is. The jump: physics first, then animation principles The body path is a physics problem: Crouch (anticipation), feet planted, knees bending. Push off, accelerating upward to a take-off speed. Fly on a parabola that starts at exactly that take-off speed, peaks at the chosen height and lands on time. Absorb the landing: front feet first, compress, settle. The bug we shipped to ourselves first: the push ended at zero speed and the flight began at full speed. Every frame looked fine; the motion had a hitch. Keep position and velocity continuous across phases. Also clamp airborne feet above the ground plane, because body pitch can swing a trailing leg through the floor. Test it like code Treat motion like any other output with invariants: Sample the timeline at a fixed rate, not just at keyframes. Track each foot in the ground frame. Assert that stance drift stays under half a pixel. Assert that at least two feet are down during a walk. Plot footfalls and check the order. Inspect joints at extreme poses, zoomed in. The SVG Lab MCP is available in early access now at svglab.app/mcp-early-access . The SVG Animate MCP is in development and coming soon.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/usman_basheers/making-an-svg-cat-walk-planted-feet-bones-and-a-gravity-arc-2p8k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
