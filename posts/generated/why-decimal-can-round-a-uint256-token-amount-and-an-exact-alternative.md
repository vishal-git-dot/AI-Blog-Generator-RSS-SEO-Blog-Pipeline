---
title: "Why Decimal Can Round a UInt256 Token Amount, and an Exact Alternative"
slug: "why-decimal-can-round-a-uint256-token-amount-and-an-exact-alternative"
author: "BlockVectra"
source: "devto_python"
published: "Thu, 22 Oct 2026 03:45:28 +0000"
description: "The documented raw balance is a UInt256String: an unsigned integer string that can reach 78 digits. When you display one in Python, Decimal looks like the ob..."
keywords: "raw, decimal, string, context, decimals, integer, exact, scale"
generated: "2026-10-22T04:08:58.349640"
---

# Why Decimal Can Round a UInt256 Token Amount, and an Exact Alternative

## Overview

The documented raw balance is a UInt256String: an unsigned integer string that can reach 78 digits. When you display one in Python, Decimal looks like the obvious tool. The trap is subtle: building a Decimal from a string is exact, but arithmetic on it can round. Where the rounding happens Decimal(raw) keeps every digit, because construction ignores the context precision. Operations such as scaleb , normalize , multiplication, or division round their result to the context precision, which defaults to 28 significant digits. That holds even at scale 0, where you intend no change at all. The proof below takes the maximum UInt256 value and runs it through scaleb(0).normalize() with precision set to 28 inside localcontext() . The global context is not mutated. The result keeps the leading digits and replaces the rest with zeros, and nothing raises an error. This does not make Decimal the wrong tool. Decimal calculations need a context appropriate to the inputs and operations. For this display-only task, integer formatting avoids depending on that context. Exact integer formatting Python integers have arbitrary precision. int(raw) parses the string exactly, and divmod(value, 10 ** decimals) splits the whole and fractional parts with no rounding. The remainder is left-padded to decimals digits, trailing zeros are stripped, and the parts are joined. No Decimal context is involved in this formatting step. from decimal import Decimal , localcontext def to_display_amount ( raw : str , decimals : int | None ) -> str : if decimals is None : return raw # no decimals metadata: keep the raw integer value = int ( raw ) # parse the decimal string exactly whole , remainder = divmod ( value , 10 ** decimals ) fraction = str ( remainder ). rjust ( decimals , " 0 " ). rstrip ( " 0 " ) return f " { whole } . { fraction } " if fraction else str ( whole ) raw = " 115792089237316195423570985008687907853269984665640564039457584007913129639935 " with localcontext () as context : context . prec = 28 rounded = format ( Decimal ( raw ). scaleb ( 0 ). normalize (), " f " ) assert rounded != raw # Arithmetic rounded an exact Decimal input. assert to_display_amount ( raw , 0 ) == raw assert to_display_amount ( raw , None ) == raw # Raw units; the scale is still unknown. assert to_display_amount ( raw , 18 ) == " 115792089237316195423570985008687907853269984665640564039457.584007913129639935 " print ( " rounded: " , rounded ) print ( " exact: " , to_display_amount ( raw , 0 )) print ( " PASS: 4 offline assertions; no network requests " ) On Python 3.14.8 this exits with status 0, makes no network requests, and passes four assertions: the Decimal path differs from the input, scale 0 returns the exact string, None returns the raw string, and scale 18 yields the expected 18-digit fraction. Nullable scale The documented decimals value is an integer from 0 to 255, or null. When it is None , the formatter returns the raw integer string unchanged. That output is in raw units. It is not a scaled amount, and the scale is still unknown, so label it as raw instead of assuming 18. Limits The formatter assumes the input is already a valid unsigned integer string under the documented UInt256String format. It is a formatter, not a validator, so check input at your boundary first. The field definitions are in the wallet assets guide , and the standalone function is in this gist .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/blockvectra/why-decimal-can-round-a-uint256-token-amount-and-an-exact-alternative-10li

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
