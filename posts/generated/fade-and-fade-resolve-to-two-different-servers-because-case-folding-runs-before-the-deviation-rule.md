---
title: "faß.de and FAẞ.DE Resolve to Two Different Servers, Because Case Folding Runs Before the Deviation Rule"
slug: "fade-and-fade-resolve-to-two-different-servers-because-case-folding-runs-before-the-deviation-rule"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 12:39:43 +0000"
description: "The rule most hand-rolled IDNA implementations get wrong is not a character. It is an order . 1 split on label separators 2 MAP each code point <- case foldi..."
keywords: "one, not, label, two, rule, punycode, character, three"
generated: "2026-08-23T12:50:17.232831"
---

# faß.de and FAẞ.DE Resolve to Two Different Servers, Because Case Folding Runs Before the Deviation Rule

## Overview

The rule most hand-rolled IDNA implementations get wrong is not a character. It is an order . 1 split on label separators 2 MAP each code point <- case folding lives here 3 apply the DEVIATION rule <- ß ς ZWJ ZWNJ get decided here 4 normalise to NFC 5 validate the label 6 punycode-encode U+1E9E LATIN CAPITAL LETTER SHARP S is mapped , and its mapping target is ss — two ASCII letters, not U+00DF. So by the time stage 3 goes looking for a deviation character, the uppercase spelling no longer holds one: faß.de -> xn--fa-hia.de the sharp s survives FAẞ.DE -> fass.de the sharp s became "ss" Faß.de -> xn--fa-hia.de lowercase again, back to the first answer Nothing in the IDNA switches changed between those lines — all three are nontransitional processing, the modern default, the mode that exists specifically to preserve ß. Node agrees with the page on all three. Same German word, two different servers, decided by the shift key, and the escape hatch IDNA2008 built for ß is only reachable from the lowercase spelling. No flag, no error, no warning. Type a domain and watch each stage: https://dev48.infy.uk/solve/day69-idna-punycode.html Three positional runners-up ab--cd INVALID "--" sits in the 3rd and 4th character positions a--bcd valid same two hyphens, one position to the left abc--de valid same two hyphens, one position to the right Identical characters; only the offset decides, because those slots are reserved so a future encoding could claim ??-- the way punycode claimed xn-- . Your browser switches that rule off along with the leading- and trailing-hyphen rules, so -ab.com parses and then fails in DNS instead. In a punycode label every hyphen is data except the last one, because the ASCII survivors are copied out first and any hyphens among them come with them. Write body.indexOf('-') instead of lastIndexOf and you get a decoder that is right on every single-word label anyone will paste into a test file: 0 wrong of 957 labels with no internal hyphen, and 500 wrong of 500 with one. And 1abc.example.com is legal while 1abc beside an Arabic-script sibling is not. RFC 5893 condition 1 wants every label of a Bidi domain to start with a strong character, and a digit is not one — so the label that gets refused did not change one byte. Its sibling did. What the measurement contradicted Four things. Three Bidi models failed to fit ICU, so the page stopped trying to emulate a browser and now implements RFC 5893 literally with the divergence measured : over an exhaustive sweep of 21,706 labels the RFC refuses 4,626 that the browser resolves — 21.3%, entirely one-directional, not a single label the RFC accepts and the browser rejects, and travelling through exactly two of the six conditions (3,676 via condition 1, 950 via condition 5). The closest relaxed fit still misses by 2,684. And my "99.4% of the mapping table is derivable" claim is actually 94.6% . The live sweep says 3,205 of 3,387 code points come back right from NFKC + toLowerCase , and the missing 182 are four named families rather than scattered exceptions — unassigned, format/separator, the 22 silently deleted, and a residue of 26 that no rule predicts. The residue is where ẞ→ss lives. 69 reference cases, 232 verifier assertions, 0 disagreements with ICU over 3,325 code points and 2,084 generated domains, 0 against Node's punycode over 60,000 ACE bodies. One file, inline CSS, and — unusually for this series — not a single external asset. Part of a from-scratch series — one tool a day, all client-side, dependency-free engine: https://dev48.infy.uk/solvefromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/fassde-and-fade-resolve-to-two-different-servers-because-case-folding-runs-before-the-deviation-11eo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
