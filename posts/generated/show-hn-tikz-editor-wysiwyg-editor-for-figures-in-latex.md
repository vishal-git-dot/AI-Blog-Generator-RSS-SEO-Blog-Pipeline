---
title: "Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX"
slug: "show-hn-tikz-editor-wysiwyg-editor-for-figures-in-latex"
author: "DominikPeters"
source: "hackernews"
published: "Tue, 23 Jun 2026 14:24:21 +0000"
description: "Hi all! TikZ is a widely-used LaTeX package for drawing figures in papers. It uses commands like \draw[->] (0,0) -- (1,2); to draw lines, shapes, text, etc. ..."
keywords: "tikz, code, source, latex, app, editor, wysiwyg, figures"
generated: "2026-06-23T15:13:55.039633"
---

# Show HN: TikZ Editor – WYSIWYG editor for figures in LaTeX

## Overview

Hi all! TikZ is a widely-used LaTeX package for drawing figures in papers. It uses commands like \draw[->] (0,0) -- (1,2); to draw lines, shapes, text, etc. Academics usually code up their figures by hand, so there is lots of twiddling around with the coordinates and recompiling until things look nice. I guess it’s a bit like SVG, but it’s more code than markup, for example it has loops with \foreach. I built an open-source WYSIWYG TikZ editor (available for web and desktop) that allows you to edit your TikZ source code visually by dragging and resizing elements. It simultaneously shows the source code and the rendered figure, and lets you edit either one while the two views stay in sync. I’m not aware of any other editors that are simultaneously source editors and WYSIWYG (even for editing SVG or HTML), and I’m quite pleased with how well the combination works. The way the app is implemented is by parsing the TikZ code, and at all times keeping track of the exact source location of each object. Thereby, when a user drags an element to a new position, the app can override just the numbers in the coordinate without changing anything else in the code (such as line breaks or indentation). This approach essentially required reimplementing a large fraction of TikZ, which is the kind of task that no human would ever want to do. I think building software that doesn’t exist yet because it would be impossibly tedious to code up is one of the great new possibilities thanks to coding agents, and it’s worth brainstorming for other examples. (This app was built almost entirely by Codex.) Implementing the app came with lots of fun side quests, including building converters from SVG / pptx / ipe to TikZ, re-implementing the LaTeX hyphenation and line-breaking algorithm to support multi-line nodes, and making a color picker that uses the red!20!black color mixing notation used in LaTeX papers. Comments URL: https://news.ycombinator.com/item?id=48645437 Points: 10 # Comments: 2

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://tikz.dev/editor/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
