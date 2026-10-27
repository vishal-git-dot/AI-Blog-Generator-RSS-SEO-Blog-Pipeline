---
title: "Firing Doxygen: Native Parser Architecture and Adopting libclang"
slug: "firing-doxygen-native-parser-architecture-and-adopting-libclang"
author: "Flude team"
source: "devto_python"
published: "Tue, 27 Oct 2026 04:10:13 +0000"
description: "Doxygen had been with us since day one. At the MVP stage, it was a conscious and absolutely correct choice: it allowed us not to write a C++ parser from scra..."
keywords: "parser, doxygen, native, libclang, parsers, architecture, but, planned"
generated: "2026-10-27T04:29:39.750966"
---

# Firing Doxygen: Native Parser Architecture and Adopting libclang

## Overview

Doxygen had been with us since day one. At the MVP stage, it was a conscious and absolutely correct choice: it allowed us not to write a C++ parser from scratch, but to immediately focus on business logic and documentation rendering. But as we transitioned from local scripts to a cloud SaaS, Doxygen turned into a burden. It couldn't cache the AST, its binary was too bulky, and its internal parser broke from C++ templates (remember the SFINAE incident from the previous episode , which forced us to write crutches via INPUT_FILTER ). It was time to do what we planned from the very beginning: fire Doxygen and migrate the system to native parsers. Divide and Conquer We never harbored illusions about creating a "universal parser". Just like with Doxygen dialects, we initially designed the system for separate parsers for each language. A tool that equally well understands hellish C++ templates with SFINAE and dynamic Python decorators simply doesn't exist. Therefore, we conducted research and selected the perfect, native tool for each language: Python: The built-in ast module. No one will parse Python better than the interpreter itself (planned). C# and Java: tree-sitter —an incredibly fast and modern incremental parser that has become an industry standard (planned). C++: Our most complex language and the first candidate for implementation. Boss Fight: C++ and libclang We started the implementation of native parsers specifically with C++, as it was the most critical vector. Trying to parse modern C++ with regexes or lightweight parsers is pure suicide. Preprocessors, macros, templates, and operator overloading will break any homegrown tool. That's why we took libclang . Only a true compiler frontend can output a 100% accurate AST for C++. Yes, integrating with a C++ API from Python is not an easy task, but it's the only guarantee that we will correctly understand all the client's code. The Triumph of Planned Architecture (Intermediate Representation) The most beautiful part about moving to libclang was that we didn't have to rewrite the renderers (that same hugo_markdown we talked about in the previous article ). This became possible because our architecture, from day one, was based on an Intermediate Representation (IR). All parsers are required to convert the result of their work into a unified ProjectCatalog structure. The new parser based on libclang simply started assembling the exact same ProjectCatalog that Doxygen used to output. The rendering layer didn't even know that the engine under the hood had changed. The architecture laid down at the start of the project worked exactly as intended. Conclusion The core was freed from a heavy third-party dependency that prevented caching implementation. We closed a huge security hole (by removing INPUT_FILTER ) and significantly lightened our cloud workers. Transitioning to a native parser is the technical step that finally turned an MVP utility into a serious product. But as soon as we connected libclang to real projects, a surprise awaited us. The native parser turned out to be blind: it flat-out refused to see the C++ standard libraries. How we searched for paths to GCC system headers on Linux and survived with MSVC-STL on Windows—read about it in the next episode. Originally published on our blog: https://blog.flude.guide/blog/firing-doxygen-native-cpp-parser Also read us: Telegram channel RSS feed

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flude_team/firing-doxygen-native-parser-architecture-and-adopting-libclang-11i3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
