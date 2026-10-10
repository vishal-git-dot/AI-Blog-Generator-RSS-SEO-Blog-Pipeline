---
title: "What the first digits of a card number tell you (BIN basics for developers)"
slug: "what-the-first-digits-of-a-card-number-tell-you-bin-basics-for-developers"
author: "ZikCards"
source: "devto_webdev"
published: "Sat, 10 Oct 2026 11:56:57 +0000"
description: "If you have ever built a checkout form, you have probably shown a Visa or Mastercard logo as the user types. That logo comes from the first few digits of the..."
keywords: "number, you, digits, card, return, bin, test, what"
generated: "2026-10-10T12:13:29.604491"
---

# What the first digits of a card number tell you (BIN basics for developers)

## Overview

If you have ever built a checkout form, you have probably shown a Visa or Mastercard logo as the user types. That logo comes from the first few digits of the card number: the BIN , or Bank Identification Number. This post covers what a BIN tells you, how to detect the brand and validate a number in a few lines of JavaScript, and what you are allowed to keep. What a BIN is The first 6 to 8 digits of a card number identify the institution that issued it. The standard (ISO/IEC 7812) calls it the IIN, Issuer Identification Number; the payments industry still says BIN. Since 2022, Visa and Mastercard allocate 8-digit BINs , so code that assumes exactly 6 digits will slowly get less accurate. A BIN lookup can tell you: Network : Visa, Mastercard, American Express, Discover, JCB, UnionPay Issuer : the bank or card programme Country where the card was issued Type : credit, debit or prepaid Level : for example classic, gold, business What it can't tell you: the cardholder, the balance, or whether a payment will succeed. Detecting the brand The first digit narrows it down; a few more settle it. The common ranges: Network Starts with Length Visa 4 16 (also 13, 19) Mastercard 51–55, 2221–2720 16 American Express 34, 37 15 Discover 6011, 644–649, 65 16–19 JCB 3528–3589 16–19 UnionPay 62 16–19 Diners Club 36, 300–305 14–19 Ranges overlap in places, so check the most specific prefix first: function cardBrand ( number ) { const n = number . replace ( / \D /g , '' ); const p = ( len ) => Number ( n . slice ( 0 , len )); if ( /^3 [ 47 ] / . test ( n )) return ' amex ' ; if ( /^ ( 36|30 [ 0-5 ]) / . test ( n )) return ' diners ' ; if ( p ( 4 ) >= 3528 && p ( 4 ) <= 3589 ) return ' jcb ' ; if ( /^ ( 6011|64 [ 4-9 ] |65 ) / . test ( n )) return ' discover ' ; if ( /^62/ . test ( n )) return ' unionpay ' ; if ( /^5 [ 1-5 ] / . test ( n ) || ( p ( 4 ) >= 2221 && p ( 4 ) <= 2720 )) return ' mastercard ' ; if ( /^4/ . test ( n )) return ' visa ' ; return ' unknown ' ; } This is enough for a logo. For anything that matters (fraud rules, routing, telling credit from debit), use a BIN database, because the type and country can't be read from the digits alone. Catching typos with the Luhn check The last digit of a card number is a check digit. The Luhn algorithm catches any single mistyped digit and most swapped neighbours, so you can tell the user before the payment provider does: function luhnValid ( number ) { const digits = number . replace ( / \D /g , '' ); if ( digits . length < 12 || digits . length > 19 ) return false ; let sum = 0 ; let double = false ; for ( let i = digits . length - 1 ; i >= 0 ; i -- ) { let d = Number ( digits [ i ]); if ( double ) { d *= 2 ; if ( d > 9 ) d -= 9 ; } sum += d ; double = ! double ; } return sum % 10 === 0 ; } luhnValid ( ' 4242 4242 4242 4242 ' ); // true (a well-known test number) luhnValid ( ' 4242 4242 4242 4241 ' ); // false A number that passes Luhn is only well-formed . It says nothing about whether the card exists. What you may store Under PCI DSS you must never store the CVV, and you shouldn't keep the full card number unless you are set up to protect it. The BIN and the last four digits are the usual "safe" pair for receipts, support and fraud rules. Check the PCI Security Standards Council's current truncation guidance for how many leading digits are allowed now that BINs are 8 digits long. If you take payments through a hosted field or iframe (Stripe Elements and similar), the full number never reaches your server at all. That is the simplest way to stay out of most of PCI's scope. Testing without real cards Payment providers publish test numbers that pass Luhn and trigger specific results (approved, declined, 3D Secure challenge). Use those in development and CI, never a real card. Tools if you just need an answer I work on ZikCards, and we keep a few free tools for exactly these questions. No sign-up: BIN lookup : network, issuer, country and type for the first digits Card brand checker : which network a number belongs to Test card numbers : sandbox numbers by provider What's the oddest card-number edge case you've hit in a checkout form?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zikcards/what-the-first-digits-of-a-card-number-tell-you-bin-basics-for-developers-4g18

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
