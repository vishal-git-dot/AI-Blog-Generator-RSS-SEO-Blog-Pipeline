---
title: "cast(bool, x) is a promise to the type checker. At runtime it is the identity function."
slug: "castbool-x-is-a-promise-to-the-type-checker-at-runtime-it-is-the-identity-function"
author: "Mahiro Hirakawa"
source: "devto_python"
published: "Sat, 12 Sep 2026 15:08:59 +0000"
description: "In google/adk-python , the value that decides whether a tool call needs human confirmation reaches its caller through cast(bool, await ...) . typing.cast ret..."
keywords: "cast, bool, what, not, value, none, tool, nothing"
generated: "2026-09-12T15:20:16.503023"
---

# cast(bool, x) is a promise to the type checker. At runtime it is the identity function.

## Overview

In google/adk-python , the value that decides whether a tool call needs human confirmation reaches its caller through cast(bool, await ...) . typing.cast returns its second argument. That is the entire implementation: def cast ( typ , val ): """ Cast a value to a type. This returns the value unchanged. """ return val It exists so a static checker will stop complaining, and it does nothing at all when the program runs. If the awaited expression produces None , the caller receives None . The caller then tests it for truth and skips the confirmation. >>> from typing import cast >>> cast ( bool , None ) is None True >>> if cast ( bool , None ): print ( " confirm " ) # prints nothing That is the same ending as the coercion defect filed against openai-agents-python as issue #4845. Different route. This one arrives by declaration instead of by conversion. Why a static analyser has nothing to say Ask a type checker what cast(bool, x) is and it answers bool . Correctly. That is what cast is for. The programmer asserted the type and the checker took the assertion. There is no diagnostic to emit and no line to highlight. A grep-shaped tool has a different problem: the pair is not on one line. Formatters split cast( from bool, across a newline, so a per-line pattern never sees them together: return cast ( bool , await self . _tool_confirmation (...), ) grep -n 'cast(bool' returns nothing here. I had to look at a window of lines rather than at single lines. What I got wrong Two things, and the second is the embarrassing one. I first recorded the sites as function_tool.py:206 and mcp_tool.py:474 . Those lines read return bool(self._require_confirmation) , which is the safe branch. The expression that matters is a few lines above each of them. what I reported what actually matters function_tool.py :206 :202-205 mcp_tool.py :474 :470-473 the code there return bool(...) , the safe branch the multi-line cast I recorded, and reported, the location of the code that was fine. The reason I landed there is that my tool did find those functions, and it found them for a reason I never checked. A coercion signal had matched bool(...) on the safe branch. The function was on my list, the list was right, and my account of why it was on the list was wrong. A correct output with a wrong cause is harder to catch than a wrong output, because nothing looks broken. The same tool was also printing a banner that named two active signals while three were running. I fixed that by printing the signal set the run actually used. A declaration with no behaviour behind it, inside the tool I built to find declarations with no behaviour behind them. What I did not check Whether any caller in adk-python actually passes something that resolves to None . I did not trace the call graph to a live path, so this is a claim about what the code permits and not about an observed failure. cast is not the defect. A cast over a value that has already been checked is fine and common. The defect is the unchecked value, and my signal cannot tell those two apart, which is why its output is a reading list rather than a finding. I have not measured how common this spelling is across the ecosystem. One repository, one commit, two sites. Repository: crates/gx-witness is the part of the project that exists because a claim about a value is not the same as evidence about it. Runnable reproductions for every framework named above, offline and pinned to a version: https://github.com/mahirhir/unanswered-approval

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mahirhir/castbool-x-is-a-promise-to-the-type-checker-at-runtime-it-is-the-identity-function-3d0e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
