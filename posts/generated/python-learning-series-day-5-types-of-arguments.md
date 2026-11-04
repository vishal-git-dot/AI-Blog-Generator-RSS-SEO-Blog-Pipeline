---
title: "Python learning series | Day-5 Types of arguments"
slug: "python-learning-series-day-5-types-of-arguments"
author: "Ajay"
source: "devto_python"
published: "Wed, 04 Nov 2026 05:20:49 +0000"
description: "What is arguments? Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma(,..."
keywords: "arguments, name, positional, keyword, greet, print, def, add"
generated: "2026-11-04T05:43:20.841995"
---

# Python learning series | Day-5 Types of arguments

## Overview

What is arguments? Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma(,). Types of arguments in python Positional Arguments Keyword Arguments Default Arguments Arbitrary / Variable-Length Arguments 1) Positional Arguments These are the arguments to be passed in exact order in which the parameter are defined. def greet ( name , age ): print ( f " hello { name } ,Are you { age } year old " ) greet ( " Ajay " , 20 ) 2) Keyword Arguments We can pass arguments with explicitly stating the parameter name followed with value(name = value), the order of arguments doesn't matters. -The keyword name must match the parameter name def greet ( name , age ): print ( f " hello { name } ,Are you { age } year old " ) greet ( age = 20 , name = " Ajay " ) 3) Default Arguments You can assign fallback values to parameters in the function definition(declaration). If the caller skips providing a value for that argument, the predefined default value is used. Default arugments must always be placed after the non-default arugments in the function definition. def greet ( name = " ajay " , message ): print ( f " Hello { name } , { message } ! " ) greet ( " harry " ) greet ( " harry " , " Goodbye " ) 4) Arbitrary / Variable-Length Arguments When you do not know beforehand how many arguments a user might pass, you use variable-length arguments: • *args (Arbitrary Positional Arguments): Prefixed with a single asterisk, it collects extra positional arguments into a tuple. • **kwargs (Arbitrary Keyword Arguments): Prefixed with a double asterisk, it collects extra keyword arguments into a dictionary. def dynamic_function ( * args , ** kwargs ): print ( " Positional tuple: " , args ) print ( " Keyword dictionary: " , kwargs ) dynamic_function ( 1 , 2 , 3 , status = " active " , role = " admin " ) # Output: # Positional tuple: (1, 2, 3) # Keyword dictionary: {'status': 'active', 'role': 'admin'} 4) Special boundries : Positional-Only, Keywords- Only (/) and (*)strictly enforce how the arguments are suppied to the function Positional-Only(/) ---> Arguments before (/) must be passed as positional arguments not a keyword arguments. def add ( a , b , / , c ): print ( a + b + c ) add ( 20 , 30 , c = 20 ) #valid add ( a = 20 , 30 , c = 30 ) #invalid Keyword-Only(*) ---> Arguments before (*) must be passed as keyword arguments not a positional arguments. def add ( a , b , * , c ): print ( a + b + c ) add ( a = 20 , 30 , c = 30 ) #invalid add ( 20 , 30 , c = 20 ) #invalid

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ajay_056/python-learning-series-day-5-types-of-arguments-4ajn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
