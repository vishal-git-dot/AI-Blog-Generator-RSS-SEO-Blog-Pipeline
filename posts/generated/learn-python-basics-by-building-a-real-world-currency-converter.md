---
title: "Learn Python Basics by Building a Real-World Currency Converter"
slug: "learn-python-basics-by-building-a-real-world-currency-converter"
author: "JARED ARITO"
source: "devto_python"
published: "Tue, 29 Sep 2026 21:14:01 +0000"
description: "Learn Python Basics by Building a Real-World Currency Converter As the global tech ecosystem grows, understanding how to manipulate real-world data like fina..."
keywords: "kes, rate, print, usd, input, python, exchange, our"
generated: "2026-09-29T22:04:59.850571"
---

# Learn Python Basics by Building a Real-World Currency Converter

## Overview

Learn Python Basics by Building a Real-World Currency Converter As the global tech ecosystem grows, understanding how to manipulate real-world data like finances is a fantastic practical skill. If you are learning Python, the best way to make concepts stick is by building small, functional projects. In this beginner-friendly tutorial, we will build a Python program that converts Kenyan Shillings (KES) to US Dollars (USD). Prerequisites To follow along, you only need: A basic Python environment (like VS Code or an online compiler). 5 minutes of free time. Step 1: Setting Up the Exchange Rate Every currency converter needs a base rate to calculate the math. In programming, we store pieces of information that might change inside variables. Let's create a variable to hold our exchange rate. For this tutorial, we will use a baseline market rate of 129.50 KES per Dollar. # Define the exchange rate constant (1 USD to KES) usd_to_kes_rate = 129.50 print ( f " System initialized. Current Base Rate: 1 USD = { usd_to_kes_rate } KES " ) Step 2: Getting Input from the User To make our converter dynamic, we cannot hardcode the money amount. We need to ask the user how much money they want to convert. Python handles this elegantly using the built-in input() function. However, there is a catch: the input() function reads everything as plain text (a string). Because financial amounts require decimals for cents, we must wrap our input in the float() function to convert that text into a decimal number. # Prompt the user for input and convert it to a floating-point decimal kes_amount_input = input ( " Enter the amount in Kenyan Shillings (KES): " ) kes_amount = float ( kes_amount_input ) print ( f " Processing conversion for: KES { kes_amount : , } " ) Step 3: Doing the Math & Displaying the Result Now that we have our mathematical decimal, the logic is simple: we divide the user's Kenyan Shillings by our exchange rate variable. Finally, we print the output using an f-string . The format tracker :.2f is used to ensure our final USD amount is neatly rounded to exactly two decimal places, matching standard currency formats. # Calculate the USD value usd_amount = kes_amount / usd_to_kes_rate # Display the output clearly using visual anchors print ( " = " * 40 ) print ( f " SUCCESS: KES { kes_amount : ,. 2 f } converts to $ { usd_amount : ,. 2 f } USD " ) print ( " = " * 40 ) The Complete Script Here is the complete, uninterrupted script. You can copy and paste this directly into a .py file or a Jupyter cell in VS Code to see it run smoothly from start to finish: # 1. Define the exchange rate usd_to_kes_rate = 129.50 # 2. Get user input kes_amount_input = input ( " Enter the amount in Kenyan Shillings (KES): " ) kes_amount = float ( kes_amount_input ) # 3. Process the conversion usd_amount = kes_amount / usd_to_kes_rate # 4. Output the result print ( " = " * 40 ) print ( f " SUCCESS: KES { kes_amount : ,. 2 f } converts to \$ { usd_amount : ,. 2 f } USD " ) print ( " = " * 40 ) Conclusion & Your Challenge Congratulations! You just built a functional financial script in Python and mastered variables, inputs, data type conversion, and f-strings. Your Challenge: To take your learning further, try modifying this code to do the reverse script. Can you write a block that asks the user for an amount in USD and multiplies it by the exchange rate to output KES ? Share your solution in the comments below!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jared_arito_80a802c5fbbc0/learn-python-basics-by-building-a-real-world-currency-converter-5a5d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
