---
title: "XTK: A Symbolic Expression Toolkit for Term Rewriting"
slug: "xtk-a-symbolic-expression-toolkit-for-term-rewriting"
author: "Alex Towell"
source: "devto_python"
published: "Sun, 07 Jun 2026 03:41:13 +0000"
description: "XTK (Expression Toolkit) is a Python library for symbolic computation through rule-based term rewriting. You define pattern-skeleton pairs, and the engine re..."
keywords: "xtk, rules, rewrite, expression, result, engine, expr, rule"
generated: "2026-06-07T04:26:51.963130"
---

# XTK: A Symbolic Expression Toolkit for Term Rewriting

## Overview

XTK (Expression Toolkit) is a Python library for symbolic computation through rule-based term rewriting. You define pattern-skeleton pairs, and the engine rewrites expressions by matching and substituting until it reaches a normal form. I built this because I kept wanting a lightweight term rewriting system that wasn't Mathematica. Something I could embed in other projects, extend with custom rules, and use from the command line. Quick Start The fastest way to try it is the interactive REPL: pip install xpression-tk python3 -m xtk.cli xtk> ( + 2 3 ) xtk> /rewrite Rewritten: 5 xtk> ( define square ( lambda ( x ) ( * x x ))) xtk> ( square 4 ) xtk> /rewrite Rewritten: 16 Core Concepts S-Expressions XTK uses S-expressions as its primary representation. If you've used Lisp, this is familiar: ( + 1 2 ) ; Addition ( * x ( + y 1 )) ; Nested expressions ( lambda ( x ) x ) ; Lambda abstraction Infix Notation For people who'd rather not count parentheses, there's infix support: xtk> /infix 2 + 3 * 4 S-expr: ( + 2 ( * 3 4 )) xtk> /infix ( x + y ) * ( x - y ) S-expr: ( * ( + x y ) ( - x y )) Rewrite Rules Rules are [pattern, skeleton] pairs. Pattern variables bind to subexpressions, and skeleton references substitute them back: from xtk import rewriter # Define rules: x + 0 => x, x * 0 => 0 rules = [ [[ ' + ' , [ ' ? ' , ' x ' ], 0 ], [ ' : ' , ' x ' ]], # x + 0 => x [[ ' * ' , [ ' ? ' , ' x ' ], 0 ], 0 ], # x * 0 => 0 ] # Create rewriter and apply rewrite = rewriter ( rules ) result = rewrite ([ ' + ' , ' a ' , 0 ]) # => 'a' result = rewrite ([ ' * ' , [ ' + ' , ' a ' , ' b ' ], 0 ]) # => 0 Pattern syntax: ['?', 'x'] matches any expression, binding it to x [':', 'x'] references the matched binding in the skeleton Built-in Rewrite Rules XTK ships with standard algebraic simplification rules: ; Arithmetic ( + x 0 ) → x ( * x 1 ) → x ( * x 0 ) → 0 ( - x x ) → 0 ; Boolean ( and true x ) → x ( or false x ) → x ( not ( not x )) → x ; Lambda calculus (( lambda ( x ) body ) arg ) → body [ x := arg ] Step-by-Step Tracing This is where it gets useful for teaching. You can watch the rewriting steps: xtk> ( * ( + 1 2 ) ( - 5 5 )) xtk> /trace Step 1 : ( * ( + 1 2 ) ( - 5 5 )) Rule: ( + a b ) → eval Result: ( * 3 ( - 5 5 )) Step 2 : ( * 3 ( - 5 5 )) Rule: ( - a a ) → 0 Result: ( * 3 0 ) Step 3 : ( * 3 0 ) Rule: ( * x 0 ) → 0 Result: 0 Final: 0 REPL Commands /help Show all commands /rewrite Apply rewrite rules /step Single rewrite step /trace Show rewrite trace /rules List active rules /load file.xtk Load rule definitions /infix expr Parse infix to S-expr /tree Show expression tree /quit Exit REPL Python API from xtk import Expression , RuleSet , Engine # Create engine with standard rules engine = Engine . with_standard_rules () # Parse and rewrite expr = Expression . parse ( " (* (+ 1 2) (+ 3 4)) " ) result = engine . rewrite ( expr ) print ( result ) # 21 # Custom rules rules = RuleSet ([ Rule . parse ( " (square ?x) → (* ?x ?x) " ), Rule . parse ( " (cube ?x) → (* ?x ?x ?x) " ), ]) engine . add_rules ( rules ) expr = Expression . parse ( " (+ (square 3) (cube 2)) " ) result = engine . rewrite ( expr ) print ( result ) # 17 Expression Visualization The REPL renders expression trees in ASCII: xtk> (* (+ a b) (- c d)) xtk> /tree * / \ + - / \ / \ a b c d Use Cases Computer algebra : Symbolic differentiation, integration Compiler optimization : Peephole optimization rules Theorem proving : Automated reasoning steps DSL implementation : Custom language semantics via rewrite rules Education : Teaching term rewriting and lambda calculus Installation pip install xpression-tk Resources PyPI : pypi.org/project/xpression-tk/ GitHub : github.com/queelius/xtk

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/queelius/xtk-a-symbolic-expression-toolkit-for-term-rewriting-cei

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
