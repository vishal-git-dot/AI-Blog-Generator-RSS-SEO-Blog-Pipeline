---
title: "The iOS Toggle Switch Is a Hidden Checkbox: Two CSS Rules and Zero JavaScript"
slug: "the-ios-toggle-switch-is-a-hidden-checkbox-two-css-rules-and-zero-javascript"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 18:48:38 +0000"
description: "Most "toggle switch" components are a <div> wearing a costume — and they pay for it forever, hand-rebuilding focus, keyboard support, form submission, and ac..."
keywords: "checked, input, track, thumb, switch, checkbox, toggle, css"
generated: "2026-08-07T19:04:02.695225"
---

# The iOS Toggle Switch Is a Hidden Checkbox: Two CSS Rules and Zero JavaScript

## Overview

Most "toggle switch" components are a <div> wearing a costume — and they pay for it forever, hand-rebuilding focus, keyboard support, form submission, and accessibility, usually skipping three of the four. There's a better way: a toggle switch and a checkbox are the same thing — one boolean, on or off. So build the switch from a real <input type="checkbox"> and restyle it. You inherit everything hard for free. Hide the checkbox, but keep it real The trick is hiding the default box without disabling it. display:none and visibility:hidden both remove it from the tab order and kill the keyboard — fatal for a control. Instead, stretch the input over the whole switch at opacity:0 . It's invisible, yet still focusable, still Space-togglable, still the owner of :checked . It sits on top to catch clicks; the visible track and thumb are pointer-events:none . <label class= "sw" > <input type= "checkbox" role= "switch" aria-label= "Wi-Fi" > <span class= "sw-track" ><span class= "sw-thumb" ></span></span> </label> .sw { position : relative ; display : inline-flex ; width : 52px ; height : 32px ; cursor : pointer ; } .sw > input { position : absolute ; inset : 0 ; width : 100% ; height : 100% ; margin : 0 ; opacity : 0 ; z-index : 2 ; } /* invisible, on top, still live */ .sw-track , .sw-thumb { pointer-events : none ; } role="switch" makes assistive tech announce "on / off" instead of "checked / not checked", while the state still comes straight from the checkbox's native checked . The whole animation is one :checked selector Here's the entire behaviour. When the hidden input is checked, the sibling combinator ~ repaints the track and slides the thumb. No JavaScript, no state variable — CSS reads the state directly. .sw > input :checked ~ .sw-track { background : var ( --track-on ); } .sw > input :checked ~ .sw-track .sw-thumb { transform : translateX ( calc ( var ( --w ) - var ( --h ))); } The travel distance is exactly width − height . The thumb starts pad from the left and must finish pad from the right; the two pads cancel, leaving w − h . That single expression is why every size just works — the knob moves on transform , which the compositor handles without layout or paint, so it stays 60fps even on a weak device. The spring is one cubic-bezier A linear slide feels mechanical. Ease the transform with a bezier whose second control point rises above 1 and the curve overshoots the target and settles back — a spring, in one line, no keyframes: .sw-thumb { transition : transform .42s cubic-bezier ( .34 , 1.56 , .64 , 1 ); } /* 1.56 > 1 = overshoot */ A gentler overshoot reads as "iOS"; a punchier one ( cubic-bezier(.2, 1.75, .3, 1) ) reads as "Material". Variants, disabled, and loading fall out for free Because every dimension and colour is a CSS custom property, a variant is just a class that re-sets a few: sizes swap --w --h --pad , themes repoint --track-on , Material thins the track and grows the thumb. A disabled native checkbox already refuses clicks and focus, so you only need to look disabled via :has(> input:disabled) . Loading is a ::after spinner in the thumb plus aria-busy="true" . JavaScript stays optional polish — mirroring input.checked into aria-checked and, if you want it, drag-to-toggle with pointer capture that hands the settle animation back to CSS. But the pure-CSS switch is already fully working, keyboard-accessible, and form-submittable. Keep the checkbox real and you inherit focus, the keyboard, forms, and a11y for nothing. See the full gallery, drag-to-toggle, and all ten build steps live: https://dev48v.infy.uk/design/day57-ios-toggles.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/the-ios-toggle-switch-is-a-hidden-checkbox-two-css-rules-and-zero-javascript-5ghi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
