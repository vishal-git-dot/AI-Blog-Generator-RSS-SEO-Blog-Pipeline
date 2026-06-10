---
title: "JWT Decoding: Reading Tokens Without a Library"
slug: "jwt-decoding-reading-tokens-without-a-library"
author: "Snappy Tools"
source: "devto_webdev"
published: "Wed, 10 Jun 2026 10:08:50 +0000"
description: "JSON Web Tokens (JWTs) are everywhere: authentication headers, session cookies, API keys. When debugging, you often need to see what is inside a token — expi..."
keywords: "token, payload, jwt, claims, json, tokens, signature, string"
generated: "2026-06-10T10:13:09.116956"
---

# JWT Decoding: Reading Tokens Without a Library

## Overview

JSON Web Tokens (JWTs) are everywhere: authentication headers, session cookies, API keys. When debugging, you often need to see what is inside a token — expiry time, user ID, permissions, issuer. You do not need a library for this. JWTs are Base64-encoded JSON, and you can decode them in one line. What a JWT actually contains A JWT has three parts, separated by dots: header.payload.signature Each part is Base64url-encoded. The header identifies the algorithm used to sign the token. The payload contains the claims — data the token asserts. The signature is a cryptographic hash that verifies the token has not been tampered with. Typical decoded header: { "alg" : "HS256" , "typ" : "JWT" } Typical decoded payload: { "sub" : "user_12345" , "email" : "user@example.com" , "iat" : 1717200000 , "exp" : 1717286400 , "roles" : [ "user" , "admin" ] } Decoding without a library The payload is just Base64url-encoded JSON. You can decode it in any language: JavaScript (browser or Node.js): function decodeJwt ( token ) { const payload = token . split ( ' . ' )[ 1 ]; // Base64url → Base64 → JSON const base64 = payload . replace ( /-/g , ' + ' ). replace ( /_/g , ' / ' ); return JSON . parse ( atob ( base64 )); } Python: import base64 , json def decode_jwt ( token ): payload = token . split ( ' . ' )[ 1 ] # Add padding if needed padding = 4 - len ( payload ) % 4 payload += ' = ' * ( padding % 4 ) return json . loads ( base64 . urlsafe_b64decode ( payload )) Go: import ( "encoding/base64" "encoding/json" "strings" ) func decodeJwt ( token string ) ( map [ string ] interface {}, error ) { parts := strings . Split ( token , "." ) payload , err := base64 . RawURLEncoding . DecodeString ( parts [ 1 ]) if err != nil { return nil , err } var claims map [ string ] interface {} json . Unmarshal ( payload , & claims ) return claims , nil } Note: decoding the payload gives you the data, but it does not verify the signature. Never trust the claims in a JWT until the signature is verified with the correct secret or public key. What the claims mean Common JWT claims (registered in RFC 7519): Claim Name Type Meaning iss Issuer string Who created the token sub Subject string Who the token refers to (usually user ID) aud Audience string/array Who the token is intended for exp Expiry Unix timestamp When the token expires iat Issued at Unix timestamp When the token was created nbf Not before Unix timestamp Earliest time the token is valid jti JWT ID string Unique identifier for this token The exp and iat values are Unix timestamps (seconds since 1970-01-01 UTC). To convert them to a readable date, use a Unix timestamp converter . Verifying vs. decoding Decoding is read-only. Any client can decode a JWT — the payload is not encrypted, just encoded. If your application needs to act on the claims (check user roles, validate session), it must verify the signature first. For HS256 tokens, verification requires the shared secret. For RS256 tokens (common in OAuth 2.0 and OIDC), verification uses the public key from the server's JWKS endpoint. In Node.js: const jwt = require ( ' jsonwebtoken ' ); const decoded = jwt . verify ( token , process . env . JWT_SECRET ); // throws if signature is invalid or token is expired Never skip verification in production. A decoded-but-unverified JWT can be forged — the server must check that the signature matches. Debugging JWT issues Common problems and how to diagnose them: "Token expired" — decode the payload and check exp . Convert the Unix timestamp: if exp is in the past, the token is expired. Check whether the clock on your server is in sync (NTP drift can cause token rejections even for freshly issued tokens). "Invalid audience" — check aud in the payload. It must match what your application expects. Some providers issue tokens for one service that other services refuse. "Signature verification failed" — the token was signed with a different key, or the token body was modified after signing. Check that your application is using the correct key or JWKS endpoint. Unexpected claims — decode and inspect the full payload. Sometimes tokens contain custom claims (namespaced like https://myapp.com/roles ) that are not obvious from the standard field names. Quick token inspection For debugging during development, the JWT Decoder on SnappyTools gives you a formatted view of the header and payload with timestamps converted to readable dates. Paste the token and see all claims instantly — nothing is sent to any server. Dealing with a JWT in production debugging? Decode it instantly here — completely client-side, safe to use with real tokens.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/snappy_tools/jwt-decoding-reading-tokens-without-a-library-1o2j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
