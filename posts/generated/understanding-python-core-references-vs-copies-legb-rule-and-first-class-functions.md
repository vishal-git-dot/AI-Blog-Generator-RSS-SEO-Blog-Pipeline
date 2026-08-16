---
title: "Understanding Python Core: References vs. Copies, LEGB Rule, and First-Class Functions"
slug: "understanding-python-core-references-vs-copies-legb-rule-and-first-class-functions"
author: "Deepika Pusala"
source: "devto_python"
published: "Sun, 16 Aug 2026 12:42:13 +0000"
description: "1. Variable References vs. Copies In Python, variables do not hold values directly. They hold references (memory addresses) to objects. Understanding this is..."
keywords: "functions, copy, original, print, output, return, new, def"
generated: "2026-08-16T12:49:10.503038"
---

# Understanding Python Core: References vs. Copies, LEGB Rule, and First-Class Functions

## Overview

1. Variable References vs. Copies In Python, variables do not hold values directly. They hold references (memory addresses) to objects. Understanding this is crucial to avoid bugs when duplicating data. Reference: [ List A ] -------------> [ Data ] Shallow: [ List B ] -------------> [ New Container ] ---> (Shares Internal Data) Deep: [ List C ] -------------> [ New Container ] ---> (New Internal Data) Variable References Assignment ( a = b ) does not create a new object. Both variables point to the exact same memory address. Modifying a mutable object through one variable alters it for both. list_a = [ 1 , 2 , 3 ] list_b = list_a # Shared reference list_b . append ( 4 ) print ( list_a ) # Output: [1, 2, 3, 4] Shallow Copy Creates a new outer object container. Inserts references to the same inner elements. Changes to nested mutable elements affect both the original and the copy. Created using copy.copy() or slicing [:] . import copy original = [[ 1 , 2 ], [ 3 , 4 ]] shallow = copy . copy ( original ) # Modifying the outer list doesn't affect the copy original . append ([ 5 , 6 ]) # Modifying a nested list affects BOTH original [ 0 ]. append ( 99 ) print ( original ) # Output: [[1, 2, 99], [3, 4], [5, 6]] print ( shallow ) # Output: [[1, 2, 99], [3, 4]] Deep Copy Creates a new outer object container. Recursively copies all inner objects found in the original. Fully disconnects the new object from the original. Created using copy.deepcopy() . import copy original = [[ 1 , 2 ], [ 3 , 4 ]] deep = copy . deepcopy ( original ) original [ 0 ]. append ( 99 ) print ( original ) # Output: [[1, 2, 99], [3, 4]] print ( deep ) # Output: [[1, 2], [3, 4]] -> Entirely unaffected 2. The LEGB Scoping Rule Python searches for variable names in a strict, sequential order defined by the LEGB acronym. It looks from the innermost scope outward. L (Local): Names assigned inside the current function ( def or lambda ). E (Enclosing): Names in the local scope of any outer enclosing functions (relevant for nested functions and closures). G (Global): Names assigned at the top level of a module file, or declared global within a function. B (Built-in): Preloaded Python names like print() , len() , and ValueError . If Python cannot find a variable name after checking all four scopes, it raises a NameError . 3. First-Class Functions Python treats functions as "first-class citizens." This means functions behave just like any other data type, such as integers, floats, or strings. Assign Functions to Variables You can reference a function without executing it by omitting the parentheses. def greet ( name ): return f " Hello, { name } ! " say_hi = greet # Assigning function to a variable print ( say_hi ( " Alice " )) # Output: Hello, Alice! Pass Functions as Arguments Functions can accept other functions as parameters (often called higher-order functions). def formal_greet ( name ): return f " Good day, { name } . " def person_processor ( func , name ): return func ( name ) print ( person_processor ( formal_greet , " Bob " )) # Output: Good day, Bob. Return Functions from Functions A function can generate and return a brand-new function dynamic wrapper. def multiplier ( factor ): def multiply_by ( num ): return num * factor return multiply_by double = multiplier ( 2 ) print ( double ( 5 )) # Output: 10 Store Functions in Collections You can organize functions inside lists, dicts, or tuples for clean execution pipelines. def step_one ( x ): return x + 1 def step_two ( x ): return x * 2 pipeline = [ step_one , step_two ] value = 5 for func in pipeline : value = func ( value ) print ( value ) # Output: 12 ((5 + 1) * 2)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/deepika_pusala/understanding-python-core-references-vs-copies-legb-rule-and-first-class-functions-4717

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
