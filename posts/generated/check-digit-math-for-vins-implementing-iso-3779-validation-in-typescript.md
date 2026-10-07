---
title: "Check Digit Math for VINs: Implementing ISO 3779 Validation in TypeScript"
slug: "check-digit-math-for-vins-implementing-iso-3779-validation-in-typescript"
author: "Vin Lookup"
source: "devto_webdev"
published: "Wed, 07 Oct 2026 05:16:46 +0000"
description: "A 17-character string that "looks like a VIN" is not necessarily a VIN. For vehicles built for the North American market, position 9 is a check digit: a sing..."
keywords: "vin, check, digit, character, string, position, const, value"
generated: "2026-10-07T05:20:33.233360"
---

# Check Digit Math for VINs: Implementing ISO 3779 Validation in TypeScript

## Overview

A 17-character string that "looks like a VIN" is not necessarily a VIN. For vehicles built for the North American market, position 9 is a check digit: a single character computed from the other 16. If you validate it, you catch most typos, transpositions, and copy-paste garbage before you ever hit a decoding API. This post walks through the math (as described in ISO 3779 and the US 49 CFR 565 rules), then gives a compact TypeScript implementation and the pitfalls I keep seeing in production code. Step 0: normalize and reject illegal characters A modern VIN has exactly 17 characters drawn from digits and uppercase letters, excluding I, O and Q . Those three are banned because they are too easily confused with 1 and 0. Before doing any math: Trim whitespace and uppercase the input. Reject anything that isn't 17 characters. Reject I, O, Q outright rather than "helpfully" converting them. Silently mapping O to 0 hides real data-entry errors and can turn a wrong VIN into a valid-looking one. Step 1: transliterate letters to numbers Each character gets a numeric value. Digits are themselves. Letters follow this table: Letter Value Letter Value Letter Value A 1 J 1 S 2 B 2 K 2 T 3 C 3 L 3 U 4 D 4 M 4 V 5 E 5 N 5 W 6 F 6 P 7 X 7 G 7 R 9 Y 8 H 8 Z 9 Notice the gaps: there's no I, O or Q, and S starts at 2 rather than 1. The pattern comes from old EBCDIC-style groupings, which is why it's easy to get wrong if you try to derive it with arithmetic. Hard-code the table. Step 2: apply position weights Each of the 17 positions has a weight: Position: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 Weight: 8 7 6 5 4 3 2 10 0 9 8 7 6 5 4 3 2 Position 9 has weight 0 because it is the check digit; it doesn't contribute to its own calculation. Multiply each transliterated value by its weight and add everything up. Step 3: mod 11 Take the sum modulo 11. The result is 0 through 10. If it's 10, the check digit is the letter X ; otherwise it's the digit itself. Compare it to the character at position 9. Worked example with the commonly cited test VIN 1M8GDM9AXKP042788 : Values: 1,4,8,7,4,4,9,1,(X),2,7,0,4,2,7,8,8 Weighted sum = 351 351 mod 11 = 10, so the check digit is X, and position 9 is X. Valid. The TypeScript const TRANSLIT : Record < string , number > = { A : 1 , B : 2 , C : 3 , D : 4 , E : 5 , F : 6 , G : 7 , H : 8 , J : 1 , K : 2 , L : 3 , M : 4 , N : 5 , P : 7 , R : 9 , S : 2 , T : 3 , U : 4 , V : 5 , W : 6 , X : 7 , Y : 8 , Z : 9 , }; const WEIGHTS = [ 8 , 7 , 6 , 5 , 4 , 3 , 2 , 10 , 0 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 ]; const VIN_RE = /^ [ A-HJ-NPR-Z0-9 ]{17} $/ ; export type VinCheck = | { ok : true ; vin : string } | { ok : false ; vin : string ; reason : string }; export function validateVin ( input : string ): VinCheck { const vin = input . trim (). toUpperCase (); if ( vin . length !== 17 ) return { ok : false , vin , reason : " length " }; if ( ! VIN_RE . test ( vin )) return { ok : false , vin , reason : " illegal character (I, O, Q or symbol) " }; let sum = 0 ; for ( let i = 0 ; i < 17 ; i ++ ) { const ch = vin [ i ]; const value = / \d / . test ( ch ) ? Number ( ch ) : TRANSLIT [ ch ]; sum += value * WEIGHTS [ i ]; } const rem = sum % 11 ; const expected = rem === 10 ? " X " : String ( rem ); return vin [ 8 ] === expected ? { ok : true , vin } : { ok : false , vin , reason : `check digit: expected ${ expected } , got ${ vin [ 8 ]} ` }; } It's dependency-free, runs in the browser or Node, and is cheap enough to run on every keystroke. Common pitfalls 1. Treating a failed check as "fake VIN." The check digit is mandatory for North American vehicles (model year 1981+). Many European and Asian market vehicles don't use it, and position 9 can be any character. If your users may enter non-NA VINs, show a soft warning instead of a hard block. 2. Pre-1981 vehicles. Before the 17-character standard, VINs varied in length and format. Don't run this algorithm on them at all. 3. Auto-correcting I/O/Q. Tempting, but it masks errors. Ask the user to re-check the plate instead. 4. Forgetting X. Code that only accepts digits at position 9 rejects roughly 1 in 11 valid VINs. 5. Assuming a valid check digit means a real car. The check digit only proves internal consistency. A random string has about a 1-in-11 chance of passing. You still need a decode (WMI, model year, plant) or registry lookup to know the vehicle exists. 6. Lowercase input and stray whitespace. Normalize first; people paste VINs from PDFs with trailing spaces and zero-width characters. Consider stripping \u200B too. 7. Testing only happy paths. Add tests for a single transposed pair (e.g. swap positions 12 and 13). The weights are designed so most adjacent swaps change the sum, and your test should confirm your implementation catches them. Where this fits in a pipeline A sensible order for user-entered VINs: Normalize. Regex for length and alphabet. Check digit (hard fail for NA markets, soft warning elsewhere). Only then call a decoder such as NHTSA vPIC or your own service. This saves API quota and gives users instant feedback with a specific message ("character 9 doesn't match, check for a typo") instead of a vague "VIN not found." Disclosure: I maintain VIN Lookup , a free VIN decoder that runs this same validation before decoding. The snippet above is free to use in your own projects.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vin_lookup_8dbd4710f77e9e/check-digit-math-for-vins-implementing-iso-3779-validation-in-typescript-2m2e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
