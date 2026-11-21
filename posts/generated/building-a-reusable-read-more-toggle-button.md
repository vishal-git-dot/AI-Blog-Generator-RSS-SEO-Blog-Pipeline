---
title: "Building a reusable read more toggle button"
slug: "building-a-reusable-read-more-toggle-button"
author: "nayem"
source: "devto_webdev"
published: "Sat, 21 Nov 2026 18:40:52 +0000"
description: "A bio on a wedding site, a long review on a poster page, a description on a dashboard card. Three places, one pattern: a boolean, a button, a slice of text. ..."
keywords: "button, text, one, lines, read, expanded, bio, when"
generated: "2026-11-21T18:56:47.822778"
---

# Building a reusable read more toggle button

## Overview

A bio on a wedding site, a long review on a poster page, a description on a dashboard card. Three places, one pattern: a boolean, a button, a slice of text. Each copy had drifted a little, different truncation lengths, different labels, one missing the collapse state entirely. That is the shape of a component that should exist once. When the same behavior shows up in three places, the question is not how to write it a fourth time, it is where it lives. The fix is one component with a clear contract: it takes text and a line count, and it owns the boolean, the button, and the accessible state. Two details make it feel finished instead of hacked together: truncation by lines instead of characters, and a button that hides itself when there is nothing to expand. the inline version The inline version is ten lines, and ten lines feel too small to abstract. A useState boolean, a slice of the text, and a button that flips it. It works fine the first time. The cost shows up on the second and third copy, when each one picks up its own quirks. One truncates at 100 characters, one at 150. One says Show more, one says Read more. One forgets the Read less state entirely, so the text grows and has no way back. BioCard.tsx import { useState } from 'react' ; function BioCard ( { bio } : { bio : string } ) { const [ expanded , setExpanded ] = useState ( false ) ; const preview = bio . slice ( 0 , 120 ) ; return ( < div > < p > { expanded ? bio : preview + '...' } </ p > < button type = 'button' onClick = { ( ) => setExpanded ( ( prev ) => ! prev ) } > { expanded ? 'Read less' : 'Read more' } </ button > </ div > ) ; } There is also a quieter bug hiding in the slice. Cutting at 120 characters cuts mid-word, so the preview ends on a half word like "wedd...", and the ellipsis lands wherever the count ran out instead of at the end of a sentence. It reads like the page glitched, because it kind of did. one component, every bio The reusable version moves the boolean inside a component and lets the caller pass the text and the number of lines. Truncation moves to CSS with line-clamp , which clamps by lines instead of characters, so the text always ends cleanly at a line break and the browser adds the ellipsis for you. The button label and the aria-expanded attribute both read the same boolean, so a screen reader hears the same state the sighted user sees. ReadMore.tsx import { useState } from 'react' ; type ReadMoreProps = { text : string ; lines ?: number ; } ; export function ReadMore ( { text , lines = 3 } : ReadMoreProps ) { const [ expanded , setExpanded ] = useState ( false ) ; const clampedStyle : React . CSSProperties = expanded ? { } : { display : '-webkit-box' , WebkitLineClamp : lines , WebkitBoxOrient : 'vertical' , overflow : 'hidden' , } ; return ( < div > < p style = { clampedStyle } > { text } </ p > < button type = 'button' aria - expanded = { expanded } onClick = { ( ) => setExpanded ( ( prev ) => ! prev ) } > { expanded ? 'Read less' : 'Read more' } </ button > </ div > ) ; } Every place that needed a toggle before now becomes one line. The bio, the review, and the description all pass their text in and get the same behavior, the same label, and the same accessible state. When the design changes, there is one file to change instead of three. Usage.tsx import { ReadMore } from './ReadMore' ; < ReadMore text = { vendor . bio } /> < ReadMore text = { review . body } lines = { 2 } /> < ReadMore text = { product . description } lines = { 4 } /> Try it: the read more toggle, live Try it live on nayemalam.com . The demo above is the component from this post, running with a real paragraph. Collapse it to three lines, expand it to the full text, and notice the button label and the expanded state change together. Nothing about it is special, and that is the point. A toggle that works the same everywhere is a toggle you stop thinking about. the button should disappear when the text is short The one loose end is a short bio. If the text already fits in three lines, the Read more button sits there doing nothing, and clicking it changes nothing, which looks broken even though nothing is broken. The fix is a measurement: after render, compare the paragraph's scrollHeight to its clientHeight , and only show the button when the full text is taller than the clamped box. Three additions to the same component, using useRef and useEffect , handle it. ReadMore.tsx import { useEffect , useRef , useState } from 'react' ; const textRef = useRef < HTMLParagraphElement > ( null ) ; const [ clamped , setClamped ] = useState ( false ) ; useEffect ( ( ) => { const el = textRef . current ; if ( el ) { setClamped ( el . scrollHeight > el . clientHeight ) ; } } , [ text , lines ] ) ; // Attach the ref to the paragraph, then render the button only when needed: { clamped && ( < button type = 'button' onClick = { ( ) => setExpanded ( ( prev ) => ! prev ) } > { expanded ? 'Read less' : 'Read more' } </ button > ) } The rule I use: a component earns its place the second time you need it, not the first. One boolean, one button, and one file to change when the design changes. The clamp handles the truncation, the button handles the state, and the measurement hides the button when there is nothing to expand. Small pieces like this are where a codebase stays calm, because the same behavior in ten places comes from one place. Originally posted on nayemalam.com/blog .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nayemalam/building-a-reusable-read-more-toggle-button-55fe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
