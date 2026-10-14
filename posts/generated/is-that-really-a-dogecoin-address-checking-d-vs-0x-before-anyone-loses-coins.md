---
title: "Is that really a Dogecoin address? Checking D... vs 0x... before anyone loses coins"
slug: "is-that-really-a-dogecoin-address-checking-d-vs-0x-before-anyone-loses-coins"
author: "Bardo Lindqvist"
source: "devto_python"
published: "Wed, 14 Oct 2026 16:39:01 +0000"
description: "I nearly lost 500 DOGE to a dropdown. A casino cashier listed Dogecoin twice, once as the native coin and once as a BEP-20 token on BNB Smart Chain, and the ..."
keywords: "address, doge, dogecoin, one, native, what, chain, first"
generated: "2026-10-14T16:54:47.639675"
---

# Is that really a Dogecoin address? Checking D... vs 0x... before anyone loses coins

## Overview

I nearly lost 500 DOGE to a dropdown. A casino cashier listed Dogecoin twice, once as the native coin and once as a BEP-20 token on BNB Smart Chain, and the BEP-20 option came first. I copied the address it gave me, pasted it into my wallet and only then saw the 0x at the start. I stopped before sending. Plenty of people don't. I spent eight years testing payment flows, and this one's a classic edge case: two things with the same name and different rails. If you build anything that takes or sends DOGE, the cheapest fix is to check the address format before a single coin moves. Here's how, with nothing but the Python standard library. Two families of "DOGE" addresses Starts with What it is Format D Native Dogecoin, pay-to-public-key-hash Base58Check, version byte 0x1E , 34 characters 9 or A Native Dogecoin, pay-to-script-hash Base58Check, version byte 0x16 0x An EVM address (BNB Smart Chain, Ethereum…), where a token borrows the DOGE ticker 0x + 40 hex characters A native Dogecoin wallet won't send to a 0x address, and coins sent the other way land on a chain the receiving service may never look at. The first character tells you which world you're in, but the first character alone isn't validation: typos and truncated pastes start with D too. Base58Check in a few lines A native address is 25 bytes encoded in Base58: one version byte, a 20-byte hash, and a 4-byte checksum, which is the first four bytes of a double SHA-256 of the first 21. Decode, split, recompute, compare. import hashlib import re ALPHABET = " 123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz " DOGE_VERSIONS = { 0x1E : " P2PKH " , 0x16 : " P2SH " } # mainnet: D... and 9.../A... EVM_RE = re . compile ( r " ^0x[0-9a-fA-F]{40}$ " ) def b58decode ( s : str ) -> bytes : n = 0 for ch in s : i = ALPHABET . find ( ch ) if i < 0 : raise ValueError ( f " not base58: { ch !r} " ) n = n * 58 + i raw = n . to_bytes (( n . bit_length () + 7 ) // 8 , " big " ) pad = len ( s ) - len ( s . lstrip ( " 1 " )) return b " \x00 " * pad + raw def classify ( address : str ) -> str : address = address . strip () if EVM_RE . match ( address ): return " evm " # BEP-20 / ERC-20 style: not a Dogecoin address try : data = b58decode ( address ) except ValueError : return " invalid " if len ( data ) != 25 : return " invalid " payload , checksum = data [: - 4 ], data [ - 4 :] if hashlib . sha256 ( hashlib . sha256 ( payload ). digest ()). digest ()[: 4 ] != checksum : return " invalid " kind = DOGE_VERSIONS . get ( payload [ 0 ]) return f " doge- { kind . lower () } " if kind else " invalid " classify returns one of four answers: doge-p2pkh , doge-p2sh , evm or invalid . A Bitcoin legacy address passes the checksum but has version byte 0x00 , so it comes back invalid , which is what you'd want in a DOGE field. What to test The edge cases I'd put in any test suite for this field: a real D… address, and the same address with one character changed (checksum must fail) a 9… or A… script address 0x followed by 40 hex characters (must be flagged, not rejected silently) a Bitcoin address, a Litecoin address, an empty string, a string with spaces around it the characters Base58 leaves out on purpose: 0 , O , I , l What to do with the answer Validation is half the job. The other half is what the person at the screen sees: evm in a DOGE field: say so in words. "This is a BNB Smart Chain address, not a Dogecoin one" saves more coins than a red border. Two networks for one ticker: default to the native chain, label the other one with its chain name, not just "DOGE". No memo field for native DOGE. If your form shows one for Dogecoin, people will assume something's wrong. They'll be right. Show the first and last characters back after paste, so people compare what they meant with what they copied. None of this needs a node or an API call. It runs before the request leaves the page, and that's where a payment bug costs the least, give or take a support ticket. I test crypto casino cashiers the way I used to test checkouts. The write-ups are at dogecasino.best, and the raw numbers are on GitHub .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bardolindqvist/is-that-really-a-dogecoin-address-checking-d-vs-0x-before-anyone-loses-coins-2a5k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
