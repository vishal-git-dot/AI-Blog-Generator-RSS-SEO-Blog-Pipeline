---
title: "Building a Name Numerology Calculator in Python: Chaldean vs Pythagorean, With Tests"
slug: "building-a-name-numerology-calculator-in-python-chaldean-vs-pythagorean-with-tests"
author: "NumsExpert"
source: "devto_python"
published: "Fri, 13 Nov 2026 23:06:39 +0000"
description: "Name numerology turns the letters of a name into numbers. Two letter-value systems dominate: Pythagorean (1–9 repeating) and Chaldean (1–8, based on sound vi..."
keywords: "total, name, pythagorean, chaldean, letter, calculator, letters, value"
generated: "2026-11-13T23:25:16.989142"
---

# Building a Name Numerology Calculator in Python: Chaldean vs Pythagorean, With Tests

## Overview

Name numerology turns the letters of a name into numbers. Two letter-value systems dominate: Pythagorean (1–9 repeating) and Chaldean (1–8, based on sound vibration). The same name gives different totals under each system, which is exactly what makes this a good small calculator project — the rules are simple, the edge cases are real, and the arithmetic is easy to test. This post builds a dependency-free Python calculator for the three classic numbers — Destiny (all letters), Soul Urge (vowels only), Personality (consonants only) — and tests it against hand-checked examples. The letter tables PYTHAGOREAN = { "A" : 1 , "B" : 2 , "C" : 3 , "D" : 4 , "E" : 5 , "F" : 6 , "G" : 7 , "H" : 8 , "I" : 9 , "J" : 1 , "K" : 2 , "L" : 3 , "M" : 4 , "N" : 5 , "O" : 6 , "P" : 7 , "Q" : 8 , "R" : 9 , "S" : 1 , "T" : 2 , "U" : 3 , "V" : 4 , "W" : 5 , "X" : 6 , "Y" : 7 , "Z" : 8 , } CHALDEAN = { "A" : 1 , "B" : 2 , "C" : 3 , "D" : 4 , "E" : 5 , "F" : 8 , "G" : 3 , "H" : 5 , "I" : 1 , "J" : 1 , "K" : 2 , "L" : 3 , "M" : 4 , "N" : 5 , "O" : 7 , "P" : 8 , "Q" : 1 , "R" : 2 , "S" : 3 , "T" : 4 , "U" : 6 , "V" : 6 , "W" : 6 , "X" : 5 , "Y" : 1 , "Z" : 7 , } Reduction and master numbers Totals reduce to a single digit by summing digits — except master numbers 11, 22 and 33, which standard practice keeps as-is: MASTER_NUMBERS = ( 11 , 22 , 33 ) def reduce_number ( total , keep_masters = True ) : while total > 9 : if keep_masters and total in MASTER_NUMBERS : return total total = sum ( int ( digit ) for digit in str ( total ) ) return total The letter Y The fiddly edge case. The most common textbook rule: Y counts as a vowel only when a word has no other vowel (A, E, I, O, U); otherwise it is a consonant. So in "LYN", Y is the vowel; in "MARY", A is the vowel and Y is a consonant. State the rule explicitly in your code — different traditions differ, and silent assumptions are how calculators disagree. Putting it together VOWELS = set ( "AEIOU" ) def calculate ( name , system = "pythagorean" ) : table = { "pythagorean" : PYTHAGOREAN , "chaldean" : CHALDEAN } [ system ] destiny = soul = personality = 0 for word in name . upper ( ) . split ( ) : letters = [ ch for ch in word if ch . isalpha ( ) ] for letter in letters : value = table [ letter ] destiny += value is_vowel = letter in VOWELS or ( letter == "Y" and not any ( ch in VOWELS for ch in letters ) ) if is_vowel : soul += value else : personality += value return ( reduce_number ( destiny ) , reduce_number ( soul ) , reduce_number ( personality ) , ) Verified example: MICHAEL Hand-checked, and covered by the test suite: System Destiny Soul Urge Personality Pythagorean 33 (total 33) 6 (total 15) 9 (total 18) Chaldean 22 (total 22) 7 (total 7) 6 (total 15) Pythagorean: M4 + I9 + C3 + H8 + A1 + E5 + L3 = 33, a master number, so it stays 33. Chaldean: M4 + I1 + C3 + H5 + A1 + E5 + L3 = 22, also kept. Same name, different systems, different answers — which is why any calculator must say which system it used. Tests worth writing At minimum: master-number preservation (11/22/33 kept, 38 → 11 kept), the MICHAEL totals above in both systems, the Y rule in both directions ("LYN" vs "MARY"), and case/whitespace handling. If those pass, the calculator agrees with hand calculation on every name I checked. If you want to check your own addition without running code, the free calculator at namenumerologycal.com runs both systems side by side. Name numerology is a reflection tool from a symbolic tradition, not a prediction or a diagnosis — the code just does the arithmetic honestly.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nums-expert/building-a-name-numerology-calculator-in-python-chaldean-vs-pythagorean-with-tests-2ed0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
