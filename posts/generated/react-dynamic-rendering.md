---
title: "React: Dynamic rendering"
slug: "react-dynamic-rendering"
author: "Atilla Baspinar"
source: "devto_webdev"
published: "Tue, 29 Sep 2026 12:29:47 +0000"
description: "Rendering a built-in element or a custom component dynamically In JSX, React distinguishes between: built-in HTML elements: lowercase names like div , button..."
keywords: "button, component, children, react, tag, custom, box, div"
generated: "2026-09-29T12:30:40.037881"
---

# React: Dynamic rendering

## Overview

Rendering a built-in element or a custom component dynamically In JSX, React distinguishes between: built-in HTML elements: lowercase names like div , button , section custom components: capitalized names like Card , Button , Profile A common pattern is to pass the element/component as a prop and render it dynamically. type BoxProps = { as ?: React . ElementType ; children : React . ReactNode ; }; function Box ({ as : Component = ' div ' , children }: BoxProps ) { return < Component > { children } </ Component >; } export default function App () { return ( <> < Box as = "section" > This is a section </ Box > < Box as = { CustomCard } > This uses a custom component </ Box > </> ); } function CustomCard ({ children }: { children : React . ReactNode }) { return < div style = { { border : ' 1px solid #ccc ' , padding : 12 } } > { children } </ div >; } Important rules: as="section" renders a built-in HTML tag. as={CustomCard} renders a custom React component. The component name must start with an uppercase letter. as is just a prop name here; React does not give it special meaning by itself. A simpler version is also valid: function Button ({ Tag = ' button ' , children , ... props }) { return < Tag { ... props } > { children } </ Tag >; } Then: < Button Tag = "a" href = "#" > Link </ Button > < Button Tag = { PrimaryButton } > Custom button </ Button >

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/atilla_baspinar_c5c68ec63/react-dynamic-rendering-2od4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
