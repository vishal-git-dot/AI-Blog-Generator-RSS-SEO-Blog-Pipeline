---
title: "JWKS and `kid` Explained: How to Find the Key That Signed Your Token (and Spot a Leaked Private Key)"
slug: "jwks-and-kid-explained-how-to-find-the-key-that-signed-your-token-and-spot-a-leaked-private-key"
author: "Avada Labs"
source: "devto_webdev"
published: "Sat, 21 Nov 2026 18:48:29 +0000"
description: "A practical guide to reading a jwks.json file, matching the right key, and checking it is safe to publish. Your API receives a token signed by an identity pr..."
keywords: "key, kid, jwks, keys, you, json, public, rsa"
generated: "2026-11-21T18:56:47.822288"
---

# JWKS and `kid` Explained: How to Find the Key That Signed Your Token (and Spot a Leaked Private Key)

## Overview

A practical guide to reading a jwks.json file, matching the right key, and checking it is safe to publish. Your API receives a token signed by an identity provider. To verify it, you need the provider's public key. But which one? Providers rotate keys, and a single endpoint can publish several at once. The answer is a small JSON document called a JWKS, and a header field called kid. JWK and JWKS in one minute A JSON Web Key (JWK) is a standard JSON representation of one cryptographic key, defined in RFC 7517. A JSON Web Key Set (JWKS) is simply a JSON object with a keys array holding several JWKs. Identity providers publish a JWKS at a public URL, commonly /.well-known/jwks.json, or at the address listed as jwks_uri in their OpenID Connect discovery document. Your API downloads it and uses it to verify signatures. A minimal entry for an RSA public key looks like this (the modulus is shortened here): { "keys": [ { "kty": "RSA", "kid": "key-2026-01", "use": "sig", "alg": "RS256", "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78...", "e": "AQAB" } ] } The fields you will see most: kty: key type (RSA, EC, oct). kid: the key ID, used to pick the right key. use: intended use, sig for signatures or enc for encryption. alg: the algorithm the key is meant for, such as RS256. n and e: the RSA public modulus and exponent. For EC keys you see crv, x and y instead. How kid picks the right key The token's header contains a kid too. Verification is a lookup: Decode the token header and read kid. Find the JWK in keys with the same kid. Build a public key from it and verify the signature. In Node.js, the matching step is one line: const jwk = jwks.keys.find((k) => k.kid === header.kid); if (!jwk) throw new Error( No matching key for kid: ${header.kid} ); Never assume the first key in the list is the right one. A JWKS can hold several keys while a provider rotates, and the order is not a contract. Caching, rotation and the "unknown kid" case Fetching the JWKS on every request is slow and fragile, so apps cache it. Caching creates one subtle rule you should follow: Cache the key set for a reasonable time. When you see a kid you do not recognize, refresh the cache once and retry, because the provider may have just rotated. If it still does not match, reject the token. Do not retry in a loop. Auth0's documentation describes the same pattern: on a failed verification, invalidate the cache and fetch new keys, then try only one more time. During a rotation, a well-behaved provider publishes the new key before it starts signing with it, and keeps the old key published until old tokens have expired. That overlap is exactly why kid exists. Five things to check in any JWKS Whether it is yours or a provider's, open it and look for these: Private key material. A public JWKS must contain only public parameters. If you see d, p, q, dp, dq or qi on an RSA key (or d on an EC key), the private key has been published. Treat it as compromised and rotate immediately. Symmetric keys (kty: "oct"). A shared secret should never appear in a public set. If it does, anyone can forge tokens. Missing kid. Without it, verifiers cannot select a key during rotation. Duplicate kid values. Two keys with the same ID make key selection ambiguous. Weak RSA keys. A modulus under 2048 bits is outdated. Use 2048 or more. Also check that alg and kty agree (an RS256 key must be RSA, an ES256 key must be EC on the P-256 curve), and that use and key_ops do not contradict each other. Inspecting a JWKS without sending it anywhere You can download the file with curl and read it, but large keys are hard to read by eye: curl -s https://example.com/.well-known/jwks.json Paste the JSON into the JWKS Viewer . It parses the key set in your browser and shows each key's type, size, kid and algorithm, and flags problems such as private fields, symmetric keys, missing or duplicate kid values and weak RSA sizes. It computes the RFC 7638 thumbprint of each key (a stable fingerprint you can use as a key ID) and can export a public key as PEM. It does not fetch URLs: you paste the JSON, so nothing is sent to a server. If you do not want to trust any tool with a sensitive set, the same checks are a few lines of code: const PRIVATE = ['d', 'p', 'q', 'dp', 'dq', 'qi', 'oth', 'k']; for (const key of jwks.keys) { const leaked = PRIVATE.filter((f) => f in key); if (leaked.length) console.error( kid ${key.kid}: private fields ${leaked.join(', ')} ); } (The k field holds the secret of an oct key, so it belongs on the list.) Putting it together A JWKS is a list of public keys, found at jwks_uri. kid in the token header tells you which key to use. Cache the set, and refresh once on an unknown kid. Audit the set: no private fields, no symmetric keys, every key has a unique kid, RSA at least 2048 bits. To go further on the rotation side, see How to Rotate JWT Signing Secrets Without Logging Everyone Out . How does your team test key rotation before it happens in production? I would like to compare notes.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/avadalabs/jwks-and-kid-explained-how-to-find-the-key-that-signed-your-token-and-spot-a-leaked-private-key-2ioj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
