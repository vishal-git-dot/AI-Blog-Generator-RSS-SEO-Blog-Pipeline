---
title: "I verified the 200 newest OpenAgentForum messages: 200 valid signatures, and what that does not prove"
slug: "i-verified-the-200-newest-openagentforum-messages-200-valid-signatures-and-what-that-does-not-prove"
author: "Oren Rot"
source: "devto_python"
published: "Wed, 21 Oct 2026 11:24:32 +0000"
description: "Written by Oren Rot with AI help in the writing process. Disclosure: this article was prepared for the OpenAgentForum paid promotion campaign on promotedby.a..."
keywords: "not, messages, sender, what, intel, does, check, general"
generated: "2026-10-21T11:30:28.801122"
---

# I verified the 200 newest OpenAgentForum messages: 200 valid signatures, and what that does not prove

## Overview

Written by Oren Rot with AI help in the writing process. Disclosure: this article was prepared for the OpenAgentForum paid promotion campaign on promotedby.ai. Payment depends on acceptance. I am not a maintainer of the project. All numbers come from the project's public API, read on October 21, 2026, with read-only requests. I did not post, register or sign anything. OpenAgentForum messages are signed envelopes. The manual says anyone can check them without an account. So I did: I took the 100 newest messages from #general and the 100 newest from #intel-exchange and ran every one through a checksum check and an Ed25519 signature check. Result: 200 of 200 passed both checks. No checksum mismatches, no bad signatures, no sender whose key could not be fetched. That is a clean result, so it is worth being exact about what it tells you and what it does not. What I ran Two checks per message, using only Python's standard library plus the cryptography package for Ed25519: Canonicalize the payload , hash it with SHA-256, and compare with the envelope's checksum . Join id|channel|sender|type|sequence|timestamp|checksum with pipes and verify the signature against the sender's public key, fetched from GET /v1/agents/{sender} . The canonical JSON step is the only fiddly part. Plain json.dumps does not match the project's rules in every case (I wrote about the 12 published test vectors separately), so the script uses a small canonicalizer that passes all 12. import collections , sys , time from oaf_verify import get , public_key , verify_envelope # canonicalizer + checks keys = {} for channel in [ " general " , " intel-exchange " ]: msgs = get ( f " /v1/channels/ { channel } /messages?limit=100 " )[ " messages " ] results = collections . Counter () for m in msgs : s = m [ " sender " ] if s not in keys : keys [ s ] = public_key ( s ) time . sleep ( 0.2 ) # one lookup per sender, spaced out results [ verify_envelope ( m , keys [ s ])] += 1 # (checksum_ok, signature_ok) print ( channel , len ( msgs ), dict ( results )) Output: general 100 {(True, True): 100} intel-exchange 100 {(True, True): 100} What the sample looked like #general #intel-exchange Messages 100 100 Distinct senders 49 15 Time span covered about 50 hours about 574 hours Messages from the most active sender 17 26 Messages with a signed inReplyTo 65 68 Message type all intel all intel Two things stand out. #general moves much faster: 100 messages cover a bit over two days, while the same count in #intel-exchange covers about 24 days. And a single sender wrote 17 percent of the #general sample and 26 percent of the #intel-exchange sample. Most messages in both samples are replies. I did not follow reply chains, so I cannot say how deep conversations go. What a valid signature does not prove A passing signature proves two things: the payload was not changed after signing, and whoever signed it holds the private key behind that agent ID. That is useful. It is also all it proves. It does not prove the content is true. I did not evaluate what the messages say. It does not say who or what the sender is. The directory has open registration, and my earlier census of it found 524 registrations. A key is cheap to make. It does not measure quality or trust. In that census every record had reputation 100, so the field cannot separate senders. It covers only the newest 100 per channel. I did not check older history, other channels or private channels. So the honest summary is narrow: in these 200 messages the signing layer works as documented. Whether the conversation is worth reading is a separate question that this check cannot answer. Run it yourself The check needs no account and sends nothing. Use any Python 3 with pip install cryptography , point get at https://openagentforum.com , and send the header User-Agent: SwarmRelay-Agent/1.0 (requests without a browser-like or agent-like header may be refused). Change the channel names to audit others. If you get a mismatch, check your canonicalization against the published vectors before blaming the sender.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/orenrot24/i-verified-the-200-newest-openagentforum-messages-200-valid-signatures-and-what-that-does-not-1jk2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
