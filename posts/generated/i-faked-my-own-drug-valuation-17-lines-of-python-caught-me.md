---
title: "I Faked My Own Drug Valuation. 17 Lines of Python Caught Me."
slug: "i-faked-my-own-drug-valuation-17-lines-of-python-caught-me"
author: "Raymond Chang"
source: "devto_python"
published: "Tue, 24 Nov 2026 21:49:05 +0000"
description: "I build a drug valuation app called Somota. This week I tried to cheat on my own numbers, on camera, to see whether the app would catch me. Video: https://yo..."
keywords: "fingerprint, receipt, signature, caught, json, valuation, app, somota"
generated: "2026-11-24T22:10:49.160305"
---

# I Faked My Own Drug Valuation. 17 Lines of Python Caught Me.

## Overview

I build a drug valuation app called Somota. This week I tried to cheat on my own numbers, on camera, to see whether the app would catch me. Video: https://youtu.be/_qJZJFU8xTo The setup In a drug licensing deal, a valuation is usually a big spreadsheet that gets emailed between two companies, bankers and lawyers. Months later somebody asks which version everybody agreed on, and nobody can prove it. So every valuation in Somota is now signed as a receipt: Take every input (odds of success, costs, sales, discount rate) and serialize it as canonical JSON: sorted keys, no spaces. Hash it with SHA-256. That is the fingerprint. Sign the fingerprint with an Ed25519 key that never leaves my machine. Put the previous receipt's fingerprint inside the new one, so the receipts form a chain. What I tried Changed the odds of success from 10.8% to 30%. Caught. The fingerprint no longer matches, and Verify shows which field moved. Changed one character of the signature. Caught. The signature no longer verifies against my public key. Renamed receipt #2 so it vanished from the chain. Caught. Receipt #3 still points at the missing fingerprint. Deleted the newest receipt. Not caught. Nothing points at the newest receipt yet, so the chain still looks complete. That is a real hole, and the next thing I'm building (anchoring the latest fingerprint somewhere public) is meant to close it. The checker The other side of a deal shouldn't have to trust my software. This is the whole independent checker. It doesn't import anything from my app: # Check one Somota receipt without the Somota app. Usage: python check_receipt.py 1 import json , hashlib , sys from cryptography . hazmat . primitives . serialization import load_pem_public_key folder = sys . argv [ 2 ] if len ( sys . argv ) > 2 else "receipts" rec = json . load ( open ( f "{folder}/receipt_{int(sys.argv[1]):04d}.json" , encoding = "utf-8" ) ) body = { k : rec [ k ] for k in ( "n" , "issued_at" , "prev_hash" , "payload" ) } canon = json . dumps ( body , sort_keys = True , separators = ( "," , ":" ) , ensure_ascii = False ) . encode ( "utf-8" ) fingerprint = hashlib . sha256 ( canon ) . hexdigest ( ) print ( "Fingerprint matches:" , fingerprint == rec [ "hash" ] ) key = load_pem_public_key ( open ( f "{folder}/desk_public_key.pem" , "rb" ) . read ( ) ) try : key . verify ( bytes . fromhex ( rec [ "signature" ] ) , bytes . fromhex ( fingerprint ) ) print ( "Signature OK" ) except Exception : print ( "Signature FAILED" ) On a clean receipt it prints True and Signature OK . After I changed 10.8% to 30% it printed False and Signature FAILED . Note that it verifies the signature against the fingerprint it rebuilt itself, not against the hash field stored in the file. If you check against the stored field, a tampered file can still pass the signature step. What a receipt can't do If I sign garbage, the receipt just proves I signed garbage. It says nothing about where the inputs came from. It only answers one question: is this still the exact file that was signed? The harder problem is letting a buyer check my numbers without seeing all my data. That needs a different kind of math, and I'm working on it separately. How does your team prove a number never changed after everyone agreed on it?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dr_delta234/i-faked-my-own-drug-valuation-17-lines-of-python-caught-me-3kph

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
