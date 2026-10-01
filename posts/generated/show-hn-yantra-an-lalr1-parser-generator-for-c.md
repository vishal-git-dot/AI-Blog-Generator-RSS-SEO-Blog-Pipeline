---
title: "Show HN: Yantra – an LALR(1) parser generator for C++"
slug: "show-hn-yantra-an-lalr1-parser-generator-for-c"
author: "renjipanicker"
source: "hackernews"
published: "Thu, 01 Oct 2026 02:30:48 +0000"
description: "Yantra is a C++ parser generator: lexer, parser, and AST walker all generated from one tool. It builds the whole AST first, then walks it. Most LALR parser g..."
keywords: "number, yantra, ast, expr, parser, std, adding, walker"
generated: "2026-10-01T05:13:42.616053"
---

# Show HN: Yantra – an LALR(1) parser generator for C++

## Overview

Yantra is a C++ parser generator: lexer, parser, and AST walker all generated from one tool. It builds the whole AST first, then walks it. Most LALR parser generators (Yacc, Bison, Lemon) run your semantic actions during parsing, as each rule reduces, bottom-up. That means at the time a rule's action runs, you don't yet know what its parent looks like. This pushes a lot of grammars toward hand-built AST classes and a separate walking pass whenever you need to look ahead into siblings or defer a decision until more context is available. On the other hand, Yantra always builds the whole AST first, then walks it top-down in a separate pass, calling your semantic actions as it goes. A parent rule's action can run before its children are visited. A single grammar can define more than one walker. For example, one that emits C++, another that emits Java, from the same parse. The AST and the walker classes are both generated for you. A small example (full version, with compile commands, in the README): start := expr; expr := expr(a) PLUS expr(b) %{ std::cout << "Adding" << std::endl; %} expr := NUMBER(N) %{ std::cout << "Number: " << N.text << std::endl; %} NUMBER := "\d+"; PLUS := "\+"; WS := "\s+"!; Running this on "1 + 2 + 3" prints: Adding Number: 1 Adding Number: 2 Number: 3 The outer "Adding", the root of the tree, prints first, before either of its children. That's only possible because the whole tree exists before any action runs. Some other things about it: integrated lexer with mode support (for things like nested comments), an optional amalgamated single-file output mode with a generated main(), C++23, MIT licensed. It's young (0.5.1, pre-1.0) and single-maintainer, so treat it as early. I'd rather know what breaks than have it look more finished than it is. Known gaps are listed at https://github.com/TantrixAuto/yantra/blob/main/docs/known_l... Repo: https://github.com/TantrixAuto/yantra Feedback and questions are all welcome. I'll be around. Comments URL: https://news.ycombinator.com/item?id=49916997 Points: 13 # Comments: 5

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/TantrixAuto/yantra

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
