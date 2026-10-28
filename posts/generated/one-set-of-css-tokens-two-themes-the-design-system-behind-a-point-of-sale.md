---
title: "One set of CSS tokens, two themes: the design system behind a point of sale"
slug: "one-set-of-css-tokens-two-themes-the-design-system-behind-a-point-of-sale"
author: "Zohaib Ahmad"
source: "devto_webdev"
published: "Wed, 28 Oct 2026 04:42:50 +0000"
description: "A point of sale is used for eight hours straight, often in a bright shop and sometimes in a dim one. So Tilly POS needed a calm interface, a real dark mode, ..."
keywords: "primary, one, dark, surface, ink, var, tokens, pos"
generated: "2026-10-28T05:00:43.285700"
---

# One set of CSS tokens, two themes: the design system behind a point of sale

## Overview

A point of sale is used for eight hours straight, often in a bright shop and sometimes in a dim one. So Tilly POS needed a calm interface, a real dark mode, and — because I'm one developer — a way to get both without writing every style twice. The answer is boring and it works: design tokens as CSS custom properties, and components that only ever use tokens. Tokens: names for decisions, not colours :root , [ data-theme = "light" ] { --bg : #f8fafc ; --surface : #ffffff ; --surface-muted : #f1f5f9 ; --border : #e2e8f0 ; --ink : #0f172a ; --ink-muted : #475569 ; --primary : #4f46e5 ; --primary-hover : #4338ca ; } [ data-theme = "dark" ] { --bg : #020617 ; --surface : #0f172a ; --surface-muted : #1e293b ; --border : #1e293b ; --ink : #f1f5f9 ; --ink-muted : #94a3b8 ; --primary : #818cf8 ; --primary-hover : #a5b4fc ; } The names describe what the colour is for — background, surface, ink, primary — never what it looks like . --ink is near-black in light mode and near-white in dark mode, and no component needs to know. Components: only tokens, no raw colours .pos-btn--primary { background : var ( --primary ); color : var ( --on-primary ); } .pos-btn--primary :hover { background : var ( --primary-hover ); } .pos-btn--secondary { background : var ( --surface ); color : var ( --ink ); border-color : var ( --border-strong ); } .pos-btn--secondary :hover { background : var ( --surface-muted ); } Switch the theme with one attribute: <html data-theme= "dark" > Every component follows, because none of them contain a colour of their own. Adding a third theme (high contrast, a client's brand) is one more block of variables. Rules that kept it calm These came from the design guidelines I wrote before building any screen: One primary action per view. Exactly one primary button; everything else is secondary or ghost. Status is never colour alone. "Paid", "Pending", "Refunded" always have a word and an icon, so they work for colour-blind users and in dark mode. Borders, not shadows. Structure comes from hairline borders on surfaces; shadows only lift things that float, like dialogs and toasts. Numbers line up. Every amount uses font-variant-numeric: tabular-nums , so columns of money align. Plain CSS classes, framework-neutral. The components are pos- classes, so the same markup works in Angular, React, Vue, Blazor or a static page. In Angular they sit in Tailwind v4's components layer. The result The same dashboard and checkout render in light and dark from one stylesheet, and adding a screen means composing existing classes instead of inventing colours. I've packaged the whole system — 19 components, the dashboard and checkout screens, light and dark tokens (CSS and JSON), Lucide icons and an Angular + Tailwind v4 setup guide — as Tilly UI . How do you handle themes — CSS variables, Tailwind's dark: variant, or something else?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zohaibahmad/one-set-of-css-tokens-two-themes-the-design-system-behind-a-point-of-sale-1j06

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
