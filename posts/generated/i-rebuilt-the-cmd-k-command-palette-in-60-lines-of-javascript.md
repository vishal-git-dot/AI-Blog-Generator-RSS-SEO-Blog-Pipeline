---
title: "I Rebuilt the Cmd-K Command Palette in ~60 Lines of JavaScript"
slug: "i-rebuilt-the-cmd-k-command-palette-in-60-lines-of-javascript"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Wed, 17 Jun 2026 15:38:53 +0000"
description: "Every great app has it now: hit ⌘K, a palette pops up, you fuzzy-type a few letters, hit Enter, done. Linear, Raycast, VS Code, GitHub. It feels like deep ma..."
keywords: "command, one, sel, palette, you, fuzzy, key, run"
generated: "2026-06-17T15:50:36.573064"
---

# I Rebuilt the Cmd-K Command Palette in ~60 Lines of JavaScript

## Overview

Every great app has it now: hit ⌘K, a palette pops up, you fuzzy-type a few letters, hit Enter, done. Linear, Raycast, VS Code, GitHub. It feels like deep machinery — it's about 60 lines of vanilla JavaScript . ⌘ Try it live: https://dev48v.infy.uk/design/day10-command-palette.html 1. One global shortcut The whole feature hinges on a single document-level listener. You MUST preventDefault — browsers bind Ctrl+K to their own search: document . addEventListener ( " keydown " , e => { if (( e . metaKey || e . ctrlKey ) && e . key === " k " ) { e . preventDefault (); openPalette (); } }); 2. Commands are data, not buttons Every action becomes one object. The UI is generic — it lists objects and calls run() on the chosen one: const COMMANDS = [ { icon : " 🌙 " , label : " Toggle dark mode " , group : " Theme " , run : toggleDark }, { icon : " 📄 " , label : " New file " , group : " File " , run : newFile }, ]; Adding a command is adding one line, never new markup. 3. Fuzzy matching feels like mind-reading Palettes don't do substring match — they do subsequence match: the query's characters appear in order, not necessarily adjacent. So tgldk finds "Toggle dark mode": function fuzzy ( q , text ) { let i = 0 ; for ( const ch of text . toLowerCase ()) if ( ch === q [ i ]) i ++ ; return i === q . length ; // all query chars found, in order } A tiny loop with one pointer — and it's why you can fly through commands with sloppy half-typed queries. 4. Keyboard-first navigation The point is to never touch the mouse. Up/Down move a selection index (modulo wraparound), Enter runs, Escape closes: if ( e . key === " ArrowDown " ) sel = ( sel + 1 ) % shown . length ; if ( e . key === " ArrowUp " ) sel = ( sel - 1 + shown . length ) % shown . length ; if ( e . key === " Enter " ) { shown [ sel ]. run (); close (); } 5. Autofocus is the whole UX The detail that makes it feel instant: focus the input the moment it opens, so the user types immediately — no click: overlay . show (); input . focus (); The takeaway Global shortcut + command data + fuzzy filter + autofocus. That's the entire command palette. Build it once and you understand the interaction pattern behind half of modern power-user tooling. Open the demo and press ⌘K.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-rebuilt-the-cmd-k-command-palette-in-60-lines-of-javascript-3a1l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
