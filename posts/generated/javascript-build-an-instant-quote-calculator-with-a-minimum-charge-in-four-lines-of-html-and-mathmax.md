---
title: "JavaScript: Build an Instant Quote Calculator With a Minimum Charge in Four Lines of HTML and Math.max"
slug: "javascript-build-an-instant-quote-calculator-with-a-minimum-charge-in-four-lines-of-html-and-mathmax"
author: "Robert Breen"
source: "devto_webdev"
published: "Tue, 24 Nov 2026 22:00:00 +0000"
description: "A small office-cleaning business gets the same enquiry every day: "How much for our office?" Then an email back asking for the size, then a reply with a pric..."
keywords: "quote, you, minimum, number, price, const, result, button"
generated: "2026-11-24T22:10:49.161786"
---

# JavaScript: Build an Instant Quote Calculator With a Minimum Charge in Four Lines of HTML and Math.max

## Overview

A small office-cleaning business gets the same enquiry every day: "How much for our office?" Then an email back asking for the size, then a reply with a price a day later, by which time half the people have asked someone else. The pricing rule is simple: 12 cents a square foot, never less than $150. That rule fits in one line of JavaScript, and the whole calculator fits on one page. This post builds it in JSFiddle , the free code playground, with no account needed. What you build 2,000 square feet gives Estimate: $240.00 800 square feet gives Estimate: $150.00 (the minimum) Change the rate or the minimum and every quote follows. Step 1: The form (HTML panel) Four lines: a heading, a number box, a button and an empty paragraph for the result. <h3> Office cleaning quote </h3> <input id = "sqft" type = "number" placeholder = "Square feet" > <button id = "quote-btn" > Get my quote </button> <p id = "result" ></p> The id values matter. They're how JavaScript finds each element. JSFiddle often adds closing tags for you as you type. If you end up with a doubled </h3> or a stray > , delete it. Click Run at the top. The Result panel shows the form. The button does nothing yet. Step 2: The price rule (JavaScript panel) Put the two numbers your price depends on at the top, as constants: const RATE = 0.12 ; // dollars per square foot const MINIMUM = 150 ; // smallest job we take Everything after // is a note for people; the browser ignores it. Now a function that prices a job: function quote ( sqft ) { return Math . max ( sqft * RATE , MINIMUM ) ; } Math.max returns the bigger of its arguments. For 2,000 square feet, 2000 * 0.12 is 240, which beats 150, so you get 240. For 800 square feet, 800 * 0.12 is 96, which loses to 150, so you get 150. No if statement needed; the minimum charge is built into one expression. Step 3: Connect the button Three lines find the page parts by their ids: const button = document . querySelector ( '#quote-btn' ) ; const box = document . querySelector ( '#sqft' ) ; const result = document . querySelector ( '#result' ) ; Then, when the button is clicked: read the box, price it, and write the estimate with two decimals. button . onclick = function ( ) { const price = quote ( Number ( box . value ) ) ; result . textContent = 'Estimate: $' + price . toFixed ( 2 ) ; } ; Two details: box.value is always a string , even in a number input. Number(...) turns it into a number before the multiplication. toFixed(2) turns 240 into "240.00" and 150 into "150.00" , so a price always shows cents. Point at the JavaScript panel and a small tidy icon appears at its top right. Click it and JSFiddle indents the code. Nothing changes in how it works; it's just easier to read. Step 4: Test both paths Click Run , then in the Result panel: Type 2000 and click Get my quote . You should see Estimate: $240.00 . Select the number, type 800 , and click Get my quote again. You should see Estimate: $150.00 . Always test one case on each side of the minimum. If the small office comes out at $96.00 , Math.max isn't in the path; if every quote is $150.00 , the box value probably isn't reaching quote() as a number. The full JavaScript const RATE = 0.12 ; // dollars per square foot const MINIMUM = 150 ; // smallest job we take function quote ( sqft ) { return Math . max ( sqft * RATE , MINIMUM ) ; } const button = document . querySelector ( '#quote-btn' ) ; const box = document . querySelector ( '#sqft' ) ; const result = document . querySelector ( '#result' ) ; button . onclick = function ( ) { const price = quote ( Number ( box . value ) ) ; result . textContent = 'Estimate: $' + price . toFixed ( 2 ) ; } ; Why this shape works Keeping the rule in one small function pays off as the pricing changes: The price lives in two constants. If the rate goes to 14 cents, you change RATE and nothing else. Nobody has to hunt through the click handler for a magic number. quote() knows nothing about the page. It takes a number and returns a number. You can test it in the browser console with quote(2000) and quote(800) without touching the form at all. The click handler only does wiring. Read the input, call the rule, write the output. If you later add a second input (say, visits per week), the handler grows by one line and the rule stays readable. That separation is the difference between a calculator you can maintain and one you're afraid to edit. Checklist [ ] Four HTML lines with ids sqft , quote-btn and result [ ] RATE and MINIMUM as constants at the top, so a price change is a one-line edit [ ] Math.max(sqft * RATE, MINIMUM) for the minimum charge [ ] Number(box.value) before doing math on the input [ ] toFixed(2) on the displayed price [ ] Tested above the minimum (2,000 → $240.00) and below it (800 → $150.00) The same HTML and JavaScript can go on a real website: whoever manages the site can paste both into a page. Practice it If you'd like to type it line by line with each step checked (13 steps, about 12 minutes, free), the interactive version is here: JavaScript: An Instant Quote Calculator for Your Website .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/robert_breen_d96e41ecd765/javascript-build-an-instant-quote-calculator-with-a-minimum-charge-in-four-lines-of-html-and-jd4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
