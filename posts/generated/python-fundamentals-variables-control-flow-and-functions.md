---
title: "Python Fundamentals: Variables, Control Flow, and Functions"
slug: "python-fundamentals-variables-control-flow-and-functions"
author: "abiud kipngetich"
source: "devto_python"
published: "Fri, 11 Sep 2026 10:46:06 +0000"
description: "1. Variables and Naming Conventions A variable is a name bound to a value in memory. Python is dynamically typed, so you don't declare a type, the type is in..."
keywords: "print, name, variable, age, range, return, def, input"
generated: "2026-09-11T10:58:00.563104"
---

# Python Fundamentals: Variables, Control Flow, and Functions

## Overview

1. Variables and Naming Conventions A variable is a name bound to a value in memory. Python is dynamically typed, so you don't declare a type, the type is inferred from the value assigned . age = 25 price = 19 Snake_case Python's official style guide (PEP 8) recommends snake_case for variable and functions names: lowercase words separated by underscores. first_name = "Jonah" total_price = 50 Constants are typically written in ALL_CAPS : PI = 3.14159 2. input() and f-strings input() pauses execution and reads a line of text from the user as a string name = input("What is your name? ") age = int(input("what is your age? ")) # convert to int explicitly f-strings(formatted string literals) let you embed expressions directly inside a string using {} name = " Bud " age = 30 print ( f " { name } is { age } years old. " 3. Operators and Conditionals Operator-Meaning == equal to != not equal to >,< greater/less than >=,<= greater/less than or equal if, elif, else score = 82 if score >= 90 : grade = " A " elif score >= 80 : grade = " B " elif score >= 70 : grade = " C " else : grade = " F " print ( grade ) # B Logical operators and, or, not combine or invert boolean conditions. temperature = 55 is_sunny = True if temperature > 50 and is_sunny : print ( " Great beach day " ) if temperature < 30 or temperature > 70 : print ( " Extreme weather " ) if not is_sunny : print ( " Bring an umbrella " ) 4. Loops for loop Iterates over a sequence (list, string, range, etc.) fruits = [ " apple " , " banana " , " cherry " ] for fruit in fruits : print ( fruit ) range() Generates a sequence of numbers, commonly used with for . for i in range ( 5 ): # 0, 1, 2, 3, 4 print ( i ) for i in range ( 2 , 10 , 2 ): # _start, stop, step -> 2,4,6,8_ print ( i ) while loop Repeats as long as a condition is true. count = 0 while count < 5 : print ( count ) count += 1 while True An infinite loop that must be broken out of explicitly, useful for menus or input validation. while True : answer = input ( " Type ' quit ' to exit: " if answer == " quit " : break Accumulators A pattern where a variable collects a running total or result across loop iterations. total = 0 for number in [ 10 , 20 , 30 ]: total += number print ( total ) # 60 # Accumulating into a list squares = [] for n in range ( 5 ): squares . append ( n ** 2 ) print ( squares ) # [0, 1, 4, 9, 16] 5. break and continue break exits the loop immediately. continue skips to the next iteration. for n in range ( 10 ): if n == 5 : break # stop entirely once n hits 5 print ( n ) for n in range ( 10 ): if n % 2 == 0 : continue # skip even numbers print ( n ) 6. enumerate() Gives you both the index and the value while looping, cleaner than manually tracking a counter. colors = [ " red " , " green " , " blue " ] for index , color in enumerate ( colors ): print ( index , color ) # 0 red # 1 green # 2 blue for index , color in enumerate ( colors , start = 1 ): print ( f " { index } . { color } " ) 7. Functions and return Functions bundle reusable logic under a name. return sends a value back to the caller and ends the function. def square ( x ): return x ** 2 result = square ( 4 ) v print ( result ) # 16 def greet ( name ): return f " Hello, { name } ! " def add_and_multiply ( a , b , factor ): total = ( a + b ) * factor return total Afunction without an explicit return returns None 8. Parameters, Arguments, and Scope Parameters are the names listed in a function's definition. Arguments are the actual values passed in when calling it. def introduce ( name , age ): # name, age are parameters print ( f " { name } is { age } " ) introduce ( " Sam " , 22 ) # "Sam", 22 are arguments Functions can have default parameter values and keyword arguments: def power ( base , exponent = 2 ): return base ** exponent print ( power ( 5 )) # 25 (uses default exponent) print ( power ( 5 , 3 )) # 125 print ( power ( base = 2 , exponent = 10 )) # 1024 Local vs global variables A local variable is defined inside a function and only exists there. A global variable is defined at the top level of a script and accessible everywhere (read access by default). counter = 0 # global variable def increment (): local_value = 1 # local variable, disappears after the function runs print ( local_value ) increment () # print(local_value) # Error: local_value doesn't exist here def modify_global () global counter # explicitly declare intent to modify the global modify_global () print ( counter ) # 1 Without the global keyword, assigning to a variable inside a function creates a new local variable instead of modifying the outer one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abudkip/python-fundamentals-variables-control-flow-and-functions-56h8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
