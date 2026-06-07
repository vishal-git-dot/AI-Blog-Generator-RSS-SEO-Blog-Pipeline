---
title: "PYTHON FUNCTION"
slug: "python-function"
author: "bhuvaneswari nandhagopal"
source: "devto_python"
published: "Sun, 07 Jun 2026 09:01:51 +0000"
description: "What is function in python? In Python, a function is a reusable block of code that performs a specific task. Functions help make programs more organized, rea..."
keywords: "print, def, hello, output, functions, function, name, arguments"
generated: "2026-06-07T09:24:56.816990"
---

# PYTHON FUNCTION

## Overview

What is function in python? In Python, a function is a reusable block of code that performs a specific task. Functions help make programs more organized, readable, and easier to maintain. Defining a Function You create a function using the def keyword def greet (): print ( " Hello, World! " ) Calling a Function greet() Output: Hello, World! a) Built-in Functions : Predefined in Python. Examples: print(), len(), type(), max(), min(), sum(). print ( len ( " Python " )) output: 6 b) User-defined Functions : Created by the programmer using the def keyword. def greet ( name ): return f " Hello, { name } ! " print ( greet ( " Bhuvana " )) output Hello, Bhuvana Functions without Parameters : def hello (): print ( " hello " ) hello () output hello Functions with Parameters : def add ( x , y ): total = x + y print ( total ) x = 10 y = 20 add ( x , y ) output 30 Positional Arguments : [TBD] Arguments are matched by position. def power ( base , exp ): return base ** exp print ( power ( 2 , 3 )) output 8 Keyword Arguments : Arguments are matched by name. print ( power ( exp = 3 , base = 2 )) output 8 Default Arguments : Parameters have default values. def greet ( name = " Guest " ): print ( f " Hello, { name } ! " ) greet () output Hello, Guest! Variable-length Arguments : *args → Non-keyword variable arguments (tuple) **kwargs → Keyword variable arguments (dict) def show_args ( * args , ** kwargs ): print ( args ) print ( kwargs ) show_args ( 1 , 2 , 3 , name = " Alice " , age = 25 ) output (1, 2, 3) {'name': 'Alice', 'age': 25} Functions that Return a Value def square ( x ): return x * x Explanation def → used to create a function square → function name x → input value x * x → multiply the number by itself return → gives back the result Functions that Do Not Return a Value def display ( msg ): print ( msg ) display ( " hello " ) output hello Lambda Functions (Anonymous functions) square = lambda x : x * x print ( square ( 5 )) output 25 Recursive Functions A function that calls itself. def factorial ( n ): return 1 if n == 0 else n * factorial ( n - 1 ) print ( factorial ( 5 )) This program finds the factorial of 5. What is factorial? multiply numbers from 5 to 1 5 × 4 × 3 × 2 × 1 = 120 output 120 Reference: https://www.bing.com/search?q=types+of+functions+in+python&gs_lcrp=EgRlZGdlKgcIBBBFGMIDMgcIABBFGLABMgcIARBFGMIDMgcIAhBFGMIDMgcIAxBFGMIDMgcIBBBFGMIDMgcIBRBFGMIDMgcIBhBFGMIDMgcIBxBFGMID0gEKNTIwNjI1ajBqN6gCCLACAQ&FORM=ANNTA1&PC=U531

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bhuvaneswari_nandhagopal_/python-function-2mie

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
