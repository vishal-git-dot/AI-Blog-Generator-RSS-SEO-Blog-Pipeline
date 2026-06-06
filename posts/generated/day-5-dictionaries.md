---
title: "🏷️ DAY 5: Dictionaries"
slug: "day-5-dictionaries"
author: "Bonface Thuo"
source: "devto_python"
published: "Sat, 06 Jun 2026 19:23:32 +0000"
description: "Welcome back, Pythonistas! 🚀 For the last two days, we’ve been using indices like 0, 1, and 2 to grab items out of our lists and tuples. But let’s be real—if..."
keywords: "character, you, key, value, out, dictionary, data, anya"
generated: "2026-06-06T19:40:03.722471"
---

# 🏷️ DAY 5: Dictionaries

## Overview

Welcome back, Pythonistas! 🚀 For the last two days, we’ve been using indices like 0, 1, and 2 to grab items out of our lists and tuples. But let’s be real—if you’re building an RPG game and want to find a character's "stamina", nobody wants to guess whether that's stored at index 4 or index 7. Today, we are throwing numerical indices out the window and upgrading to custom labels. Imagine a massive chest of drawers where you get to write the labels on the outside yourself. Enter Dictionaries! 🏷️📖 📖 What is a Dictionary? In Python, a Dictionary is a collection of key-value pairs. Instead of looking up items by a number, you look them up using a unique word (the Key) to get the data attached to it (the Value). To make a dictionary, we use curly braces {}, and we separate keys and values with a colon : # Creating our character's stat sheet 🎮 character = { " name " : " Anya " , " role " : " Mage " , " level " : 14 , " is_premium " : True } print ( character ) 🔍 Reading data with Custom Labels To pull data out, you use the exact same square bracket setup we used for lists, but instead of a number, you pass in the exact string key: # Checking Anya's role print ( character [ " role " ]) # Prints: Mage # Checking Anya's level print ( character [ " level " ]) # Prints: 14 ⚠️ Tantrum Alert: Python keys are case-sensitive! If you try to look up character["Role"] with a capital R, Python will throw a KeyError and pretend it has never seen that data in its life. 🛠️ Modifying the Chest of Drawers Dictionaries are completely mutable (flexible). You can change values, add new drawers, or rip drawers out completely. # 1. Updating a value (Anya leveled up! 🎉) character [ " level " ] = 15 # 2. Adding a brand new key-value pair character [ " weapon " ] = " Crystal Staff " # 3. Deleting a key-value pair 🗑️ del character [ " is_premium " ] print ( character ) # Output: {'name': 'Anya', 'role': 'Mage', 'level': 15, 'weapon': 'Crystal Staff'} 🚀 Today's Challenge 🏆 Create a dictionary called my_car with the keys: brand, model, and year. Print out the model of your car. Update the year to a newer one (or change it to a hovercar from the future 🚀). Add a new key called color and give it a value. Drop your custom dictionary in the comments below! Tomorrow, we are finishing our core data structures by looking at Sets—the ultimate bouncers of the Python world! 🎟️

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alpha3020/day-5-dictionaries-1nm4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
