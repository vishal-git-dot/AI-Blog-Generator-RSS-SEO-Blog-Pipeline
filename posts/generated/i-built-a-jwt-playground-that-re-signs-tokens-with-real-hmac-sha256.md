---
title: "I Built a JWT Playground That Re-signs Tokens With Real HMAC-SHA256"
slug: "i-built-a-jwt-playground-that-re-signs-tokens-with-real-hmac-sha256"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Thu, 25 Jun 2026 19:59:15 +0000"
description: "Most JWT explainers cheat. They show you header.payload.signature , point at the third part, and say "...and then the server verifies it." But they never run..."
keywords: "hmac, you, token, jwt, real, signature, key, playground"
generated: "2026-06-25T20:09:21.020457"
---

# I Built a JWT Playground That Re-signs Tokens With Real HMAC-SHA256

## Overview

Most JWT explainers cheat. They show you header.payload.signature , point at the third part, and say "...and then the server verifies it." But they never run the verification — so you never actually see what "tampered" or "expired" means in practice. So I built a JWT Playground that runs the real crypto in your browser, then animates how a Spring Security resource server validates the token. ▶ Live demo: https://dev48v.github.io/jwt-flow/ Source (zero dependencies): https://github.com/dev48v/jwt-flow Real HMAC, not faked The signing and verification use the Web Crypto API — actual HMAC-SHA256 : async function hmac ( signingInput , secret ) { const key = await crypto . subtle . importKey ( " raw " , new TextEncoder (). encode ( secret ), { name : " HMAC " , hash : " SHA-256 " }, false , [ " sign " ] ); const sig = await crypto . subtle . sign ( " HMAC " , key , new TextEncoder (). encode ( signingInput )); return base64url ( new Uint8Array ( sig )); } // token = base64url(header) + "." + base64url(payload) + "." + hmac(those two, secret) Because it's real, the demo behaves like the real thing: Edit the payload and re-sign → a new, valid signature is computed. Change one character of the token without re-signing → the verifier recomputes the HMAC, it no longer matches, and you get invalid signature . Change the secret → verification fails, exactly like a key mismatch. The thing most people miss: it's three separate gates A JWT being correctly signed does not mean the request is allowed. A Spring Security resource server runs three independent checks, and the demo lights each one up: BearerTokenAuthenticationFilter extracts the token from Authorization: Bearer … . JwtDecoder verifies the signature . Wrong signature → 401 . OAuth2TokenValidators check exp / nbf / iss / aud . A perfectly-signed but expired token → 401 . Authorization ( @PreAuthorize , scopes/roles) decides if the bearer may call this endpoint. Signed, unexpired, but missing the scope → 403 . That 401 vs 403 distinction trips people up constantly: 401 Unauthorized = "I don't believe who you are" (bad/expired/missing token). 403 Forbidden = "I know who you are, you're just not allowed to do this" (missing scope/role). The playground has a button for each failure so you can watch where exactly the request dies. Why a playground beats a diagram A static diagram shows the boxes. It can't show you that tampering breaks the signature check specifically, or that expiry is a different gate from authorization. Poking at a live token — breaking it on purpose and watching the 401 — is what makes it stick. It's one index.html , no build, no dependencies. Security note It only does symmetric HS256 so it can sign client-side for the demo. Real resource servers usually verify RS256 / ES256 with the issuer's public key via JWKS and never hold the signing key. Never paste a production token into any web page. If this made JWTs click, a star helps others find it: https://github.com/dev48v/jwt-flow

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-a-jwt-playground-that-re-signs-tokens-with-real-hmac-sha256-2hlh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
