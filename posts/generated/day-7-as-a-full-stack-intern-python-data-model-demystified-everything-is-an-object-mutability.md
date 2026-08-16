---
title: "Day 7 as a Full Stack Intern: Python Data Model Demystified: Everything-Is-An-Object & Mutability"
slug: "day-7-as-a-full-stack-intern-python-data-model-demystified-everything-is-an-object-mutability"
author: "Deepika Pusala"
source: "devto_python"
published: "Sun, 16 Aug 2026 12:31:28 +0000"
description: "In Python's "everything-is-an-object" data model , every piece of data is an object stored in memory. This includes numbers, strings, lists, functions, and e..."
keywords: "object, immutable, mutable, data, memory, python, address, place"
generated: "2026-08-16T12:49:10.504285"
---

# Day 7 as a Full Stack Intern: Python Data Model Demystified: Everything-Is-An-Object & Mutability

## Overview

In Python's "everything-is-an-object" data model , every piece of data is an object stored in memory. This includes numbers, strings, lists, functions, and even classes themselves. Every Python object has three unchangeable properties: Identity : The unique memory address of the object (checked via id() ). Type : The class/category of the object (checked via type() ). Value : The actual data stored inside the object. An object's type dictates whether its value can be changed in place (mutable) or if it is completely unchangeable once created (immutable). 📊 Quick Reference Table Data Type Mutability Memory Behavior On Modification Can Be Used As Dict Key? list Mutable Modifies the original object in place. No (unhashable) dict Mutable Modifies the original object in place. No (unhashable) set Mutable Modifies the original object in place. No (unhashable) tuple Immutable Throws an error; must create a brand-new object. Yes (if items are immutable) str Immutable Throws an error; must create a brand-new object. Yes int / float Immutable Reallocates variables to a new memory address. Yes 🔄 Mutable Types ( list , dict , set ) Mutable objects can alter their values directly at their existing memory address. Behavior : When you append to a list or update a dictionary, the object's id() stays exactly the same. Code Example : my_list = [ 1 , 2 , 3 ] print ( id ( my_list )) # Output: 140312981206408 (Example address) my_list . append ( 4 ) print ( id ( my_list )) # Output: 140312981206408 (Same address, object modified in place) Side-Effect Risk : If two variables point to the same mutable object, changing one changes both. a = [ 1 , 2 ] b = a b . append ( 3 ) print ( a ) # Output: [1, 2, 3] - 'a' was unintentionally changed! 🔒 Immutable Types ( tuple , str , int ) Immutable objects can never change their internal value once they are written to memory. Behavior : If you perform an operation that seems to alter an immutable variable, Python leaves the original object alone and creates an entirely new object elsewhere in memory. Code Example : my_str = " Hello " print ( id ( my_str )) # Output: 140312985552112 my_str += " World " print ( id ( my_str )) # Output: 140312985558944 (Different address; a new string was created) The Tuple Nuance : A tuple is immutable, meaning you cannot add, remove, or swap its elements. However, if a tuple contains a mutable object (like a list), that nested list can still be mutated in place. my_tuple = ([ 1 , 2 ], 3 ) my_tuple [ 0 ]. append ( 9 ) # This works! The tuple still points to the same list object. 🧠 Variable Assignment vs Function Passing Variables are Labels : Variables in Python are not boxes that hold data; they are simply text labels bound to objects. Pass-by-Object-Reference : When passing arguments to a function, Python passes the reference to the object. Modifying a mutable argument inside a function alters the original data outside the function. Reassigning an immutable argument inside a function just points the local variable name to a new object, leaving the outside data untouched.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/deepika_pusala/day-7-as-a-full-stack-intern-python-data-model-demystified-everything-is-an-object-mutability-llb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
