---
title: "Show HN: LuaCAD – Parametric CAD Scripted in Lua"
slug: "show-hn-luacad-parametric-cad-scripted-in-lua"
author: "adius"
source: "hackernews"
published: "Fri, 14 Aug 2026 16:43:22 +0000"
description: "LuaCAD models solids in Lua rather than the OpenSCAD language, with operator overloading for CSG (`a + b`, `a - b`, `a * b`). It ships with a CLI and a deskt..."
keywords: "openscad, luacad, https, com, lua, language, all, github"
generated: "2026-08-14T19:00:48.683058"
---

# Show HN: LuaCAD – Parametric CAD Scripted in Lua

## Overview

LuaCAD models solids in Lua rather than the OpenSCAD language, with operator overloading for CSG (`a + b`, `a - b`, `a * b`). It ships with a CLI and a desktop app, including a preview area and a text editor. I've always been a big fan of OpenSCAD, but the SCAD language itself is unfortunately quite cobbled-together and is a very poorly designed programming language. LuaCAD takes all the good parts of OpenSCAD and combines them with one of the best scripting languages. It has now completely replaced OpenSCAD for me, and I think it provides a better experience than OpenSCAD for all use cases. I'd love to hear any reasons why LuaCAD shouldn't fully replace OpenSCAD! It’s fully open source and you can find the repo here: https://github.com/ad-si/LuaCAD Tech stack: - It's implemented in Rust and uses mlua ( https://github.com/mlua-rs/mlua ) to execute the Lua code. - Uses OpenCSG ( https://opencsg.org ) for fast and correct rendering of the 3D models (like OpenSCAD) - Uses Manifold ( https://github.com/elalish/manifold ) to create the manifold triangle meshes - Native support for all BOSL2 functions (i.e. implemented in Rust for better performance) Comments URL: https://news.ycombinator.com/item?id=49301215 Points: 34 # Comments: 6

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://luacad.ad-si.com

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
