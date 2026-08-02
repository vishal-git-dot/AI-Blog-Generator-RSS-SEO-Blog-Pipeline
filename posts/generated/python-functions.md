---
title: "Python Functions"
slug: "python-functions"
author: "vidhya murali"
source: "devto_python"
published: "Sun, 02 Aug 2026 19:15:48 +0000"
description: "Python functions are reusable blocks of code used to perform a specific task. They help organize programs into smaller sections and execute the same logic wh..."
keywords: "function, print, arguments, def, value, return, functions, values"
generated: "2026-08-02T19:18:04.964349"
---

# Python Functions

## Overview

Python functions are reusable blocks of code used to perform a specific task. They help organize programs into smaller sections and execute the same logic whenever needed by calling the function. Defining a Function A function can be defined using def keyword. Below is the syntax to define a function: Here, we define a function using def that prints a welcome message when called. def show(): print("Hello welcome to my blog") Calling a Function After creating a function, call it by using the name of the functions followed by parenthesis containing parameters of that particular function. def show(): print("Hello welcome to my blog") show() Function Arguments Arguments are values passed to a function when it is called. They allow functions to receive input data and perform operations using those values. Syntax : def function_name(arguments): # function body return value def function_name(arguments): defines a function with optional arguments. # function body contains the statements to be executed. return value returns a result from the function. If no return statement is used, it returns None by default. Example: In this example, function checks whether the number passed as an argument is even or odd. def evenOdd(x): if (x % 2 == 0): return "Even" else: return "Odd" print(evenOdd(2)) print(evenOdd(5)) Types of Function Arguments Python supports different types of arguments that can be passed during a function call. Default argument : Default argument use a predefined value when no value is passed during the function call. def myFun(x, y=12): print("x: ", x) print("y: ", y) myFun(3) Explanation : y=12 sets a default value for parameter y and myFun(3) passes only one argument. Since y is not provided, it uses the default value 12. Keyword Arguments : pass values using parameter names, so argument order does not matter. def student(fname, lname): print(fname, lname) student(fname='vidhya', lname='murali') student(lname='Murali', fname='Prem') Explanation : fname and lname are passed using parameter names and arguments can be provided in any order. Positional Arguments: values are assigned to parameters based on their order in the function call. def nameAge(name, age): print("Hi, I am", name) print("My age is ", age) print("Case-1:") nameAge("vidhya", 22) print("Case-2:") nameAge(15, "prem") Explanation : In Case-1, values match the correct parameters. In Case-2, values are swapped because the order changed. Arbitrary Arguments : allow functions to accept multiple values. This is done using two special symbols: *args collects extra positional arguments as a tuple. **kwargs collects extra keyword arguments as a dictionary. def myFun(*args, **kwargs): print("Non-Keyword Arguments (*args):") for arg in args: print(arg) print("Keyword Arguments (**kwargs):") for key, value in kwargs.items(): print(f"{key} == {value}") myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks') Explanation : *args stores extra positional arguments. **kwargs stores extra keyword arguments. loop prints all positional and keyword values separately. Function within Functions A function defined inside another function is called an inner function (or nested function). It is used to organize related logic and access variables from the outer function. def f1(): s = 'Happy Learning' def f2(): print(s) f2() f1() Return Statement Return is used to end a function and send a value back to the caller. It can return any data type, multiple values (packed into a tuple), or None if no value is given. Syntax return [expression] Parameters : expression is the value returned by the function. If no value is returned, it returns None by default def sq_value(num): return num**2 print(sq_value(2)) print(sq_value(-4)) Explanation : sq_value(num) accepts a number as input. num**2 calculates the square of the number. return sends the result back to the caller. Pass by Reference and Pass by Value Variables refer to objects . Function behavior depends on whether the object is mutable or immutable. Mutable objects like lists can be modified inside functions. Immutable objects like integers and strings remain unchanged. def myFun(x): x[0] = 20 b = [10, 11, 12, 13] myFun(b) print(b) def myFun2(x): x = 20 a = 10 myFun2(a) print(a) Explanation : myFun(x) modifies the first element of the list and lists are mutable, so the original list changes. myFun2(x) assigns a new value to x. Integers are immutable, so the original value of a remains unchanged. Note: Python uses pass-by-object-reference, where functions receive references to objects instead of actual copies. Reference : https://www.geeksforgeeks.org/python/python-functions/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vidhya_murali_5aabe7784bd/python-functions-2iki

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
