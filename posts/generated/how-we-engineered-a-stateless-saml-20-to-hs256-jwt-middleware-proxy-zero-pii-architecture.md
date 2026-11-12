---
title: "How We Engineered a Stateless SAML 2.0 to HS256 JWT Middleware Proxy (Zero-PII Architecture)"
slug: "how-we-engineered-a-stateless-saml-20-to-hs256-jwt-middleware-proxy-zero-pii-architecture"
author: "KyoRox"
source: "devto_webdev"
published: "Thu, 12 Nov 2026 00:13:28 +0000"
description: "Enterprise customers require OASIS SAML 2.0 Single Sign-On (SSO) via Identity Providers like Okta, Microsoft Entra ID (Azure AD), Google Workspace, JumpCloud..."
keywords: "kyorox, saml, user, com, buffer, jwt, xml, mau"
generated: "2026-11-12T00:20:19.772139"
---

# How We Engineered a Stateless SAML 2.0 to HS256 JWT Middleware Proxy (Zero-PII Architecture)

## Overview

Enterprise customers require OASIS SAML 2.0 Single Sign-On (SSO) via Identity Providers like Okta, Microsoft Entra ID (Azure AD), Google Workspace, JumpCloud, and PingIdentity before signing annual B2B contracts. However, engineering teams building modern JWT-based web applications face two major bottlenecks when implementing SAML 2.0: Fragile XML Cryptography & Security Debt: Parsing SAML 2.0 XML assertions directly inside an application backend introduces XML External Entity (XXE) injection vectors, XML Signature Wrapping (XSW) vulnerabilities, canonicalization mismatches, and X.509 certificate rotation maintenance. Punitive Per-User (MAU) & Per-Connection Pricing: Legacy identity brokers charge $125+/month per single SAML connection or impose steep Monthly Active User (MAU) taxes while persisting end-user Personally Identifiable Information (PII) in third-party databases. To solve both problems at the architectural level, we built KyoRox — a 100% Stateless Volatile RAM SAML 2.0 to HS256 JWT Middleware Proxy . Core Architectural Design Instead of acting as a heavyweight user database, KyoRox operates strictly as a deterministic cryptographic translation proxy at sso.kyorox.com : 1. 100% Volatile RAM Execution ( 0 Bytes End-User PII on Disk) When an Identity Provider posts a signed SAML 2.0 XML response to the KyoRox Assertion Consumer Service (ACS) endpoint: The XML payload is parsed and verified strictly in volatile memory ( < 12ms median latency). Normalized attributes ( sub , email , firstName , lastName , groups , idp , tenantId ) are packed into an HS256 JSON Web Token signed with the tenant's secret. Immediately after the HTTP 302 redirect handoff back to the customer's application callback URL, the memory buffer is garbage-collected. Zero bytes of end-user PII are ever written to PostgreSQL or disk logs. 2. Defense-in-Depth Cryptographic Verification Pinned X.509 RSA-SHA256 Validation: Strict cryptographic verification against the tenant's pinned Identity Provider certificate with DTD/XXE parsing disabled at the parser level. 300-Second Atomic Nonce Replay Lock: Every SAML AssertionID is hashed and locked in volatile memory for 300 seconds ( SET NX EX 300 ), neutralizing Man-in-the-Middle (MitM) assertion replay attacks. FIPS-197 AES-256-GCM Vault Encryption: Tenant JWT signing secrets are encrypted at rest using a unique 96-bit Initialization Vector (IV) and 128-bit Authentication Tag. Verifying the Returning HS256 JWT in Node.js (Zero Dependencies) Applications integrate with KyoRox using standard HTTP redirects and verify the returning token using native node:crypto (or Python's hmac / hashlib ) without installing bloated third-party SDKs: const crypto = require ( 'node:crypto' ) ; function verifyKyoRoxJwt ( token , clientSecret , expectedTenantId ) { const parts = ( token || '' ) . split ( '.' ) ; if ( parts . length !== 3 ) throw new Error ( 'Malformed JWT structure.' ) ; const [ headerB64 , payloadB64 , signatureB64 ] = parts ; const header = JSON . parse ( Buffer . from ( headerB64 , 'base64url' ) . toString ( 'utf8' ) ) ; if ( header . alg !== 'HS256' ) throw new Error ( 'Expected HS256 algorithm.' ) ; const expectedSig = crypto . createHmac ( 'sha256' , clientSecret ) . update ( `${headerB64}.${payloadB64}` ) . digest ( 'base64url' ) ; if ( Buffer . byteLength ( signatureB64 ) !== Buffer . byteLength ( expectedSig ) || ! crypto . timingSafeEqual ( Buffer . from ( signatureB64 ) , Buffer . from ( expectedSig ) ) ) { throw new Error ( 'Invalid KyoRox HMAC-SHA256 signature.' ) ; } const claims = JSON . parse ( Buffer . from ( payloadB64 , 'base64url' ) . toString ( 'utf8' ) ) ; if ( claims . exp && Math . floor ( Date . now ( ) / 1000 ) >= claims . exp ) { throw new Error ( 'Expired SSO token.' ) ; } if ( expectedTenantId && claims . tenantId !== expectedTenantId ) { throw new Error ( 'Tenant UUID mismatch.' ) ; } return claims ; } Predictable Flat-Rate B2B Comparison ( $0 MAU Tax ) Capability KyoRox WorkOS Legacy CIAM (Auth0 / Okta) Starting Price $39/mo flat (Starter: 1 IdP) $125/mo per connection High base + MAU scaling tiers Multi-IdP Growth Tier $139/mo flat (Up to 5 IdPs) $625/mo (5 connections) Enterprise contract required Unlimited Enterprise Tier $349/mo flat (Unlimited IdPs) Custom / $1,000s+/mo Custom annual contract Monthly Active User (MAU) Fees $0 (Unlimited Users) Included per connection Expensive MAU overage tiers End-User PII Stored on Disk 0 Bytes (Volatile RAM Only) Stored in vendor database Stored in vendor database Official Resources & Open-Source Reference Code Platform & Interactive SAML Simulator: https://kyorox.com 6-IdP Integration Documentation: https://kyorox.com/docs Trust & Security Center: https://kyorox.com/trust GitHub Organization (Node.js & Python Verifiers): https://github.com/Kyorox-official LinkedIn: https://www.linkedin.com/company/kyorox Trustpilot Reviews: https://www.trustpilot.com/review/kyorox.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kyorox/how-we-engineered-a-stateless-saml-20-to-hs256-jwt-middleware-proxy-zero-pii-architecture-g91

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
