---
title: "I Rebuilt Slack's Message Box With Plain HTML, CSS and JS"
slug: "i-rebuilt-slacks-message-box-with-plain-html-css-and-js"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 20:59:53 +0000"
description: "The message box at the bottom of Slack looks trivial. It is not. It grows as you type, formats your text, sends on Enter but not Shift+Enter, and never feels..."
keywords: "text, enter, box, editor, slack, send, textarea, replace"
generated: "2026-06-15T21:11:31.715824"
---

# I Rebuilt Slack's Message Box With Plain HTML, CSS and JS

## Overview

The message box at the bottom of Slack looks trivial. It is not. It grows as you type, formats your text, sends on Enter but not Shift+Enter, and never feels janky. Rebuilding it is one of the best front-end exercises I know — so let me do it from scratch, pure HTML/CSS/JS. This is Day 8 of DesignFromZero, where I rebuild a polished real-world UI every day. The textarea that grows itself A normal textarea is a fixed box with an ugly scrollbar. Slack's grows to fit your text, up to a cap, then scrolls. The trick is two lines, run on every keystroke: editor . style . height = " auto " ; // let it shrink first editor . style . height = editor . scrollHeight + " px " ; // grow to fit content Why reset to auto first? Because scrollHeight only ever grows — if you don't reset, deleting text leaves the box stuck tall forever. Resetting lets it collapse, then re-measuring gives the true height. This reset-then-measure is the gotcha; almost everyone hits it once. Pair it with CSS for the scroll cap: #editor { max-height : 200px ; overflow-y : auto ; resize : none ; } A toolbar that wraps your selection Bold and italic don't restyle the box — they insert Slack's markdown around whatever you've selected. Grab the selection, splice marker characters on both sides, restore the cursor: const { selectionStart : a , selectionEnd : b , value : v } = editor ; const sel = v . slice ( a , b ) || " text " ; editor . value = v . slice ( 0 , a ) + " * " + sel + " * " + v . slice ( b ); // *bold* It's plain text editing, not rich text — which is exactly why it's robust, copy-pasteable, and survives a page reload. The keybinding that defines a chat app Plain Enter sends; Shift+Enter makes a new line. One handler: editor . onkeydown = e => { if ( e . key === " Enter " && ! e . shiftKey ) { e . preventDefault (); send (); } }; Get this wrong and your app feels broken. Get it right and nobody notices — which is the goal. Render the markdown on send When the message posts, the raw *text* becomes real formatting via a few regex replacements — always escaping < first, so nobody can inject HTML: text . replace ( /&/g , " &amp; " ). replace ( /</g , " &lt; " ) . replace ( / \*( .+ ?)\* /g , " <b>$1</b> " ) . replace ( /_ ( .+ ?) _/g , " <i>$1</i> " ) . replace ( /` ( .+ ?) `/g , " <code>$1</code> " ); The polish that sells it A few small touches make the composer feel "real": the rounded container that gets a focus ring ( :focus-within ), the send button that disables itself when the box is empty, and the tiny "Enter to send · Shift+Enter for new line" hint underneath. None are hard; together they're the difference between a textarea and Slack's textarea. The takeaway The whole composer is: a self-measuring textarea + a toolbar that wraps the selection + one keydown rule + a render-on-send step. That same skeleton powers the comment box on GitHub, the composer in Linear, the reply field in Gmail. Build it once and you can build all of them. 👉 Try the live composer (type multi-line, select + format, Enter to send): https://dev48v.infy.uk/design/day8-slack-input.html 🌐 All designs: https://dev48v.infy.uk/designfromzero.php Tomorrow: Notion's slash-command menu.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-rebuilt-slacks-message-box-with-plain-html-css-and-js-4b4o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
