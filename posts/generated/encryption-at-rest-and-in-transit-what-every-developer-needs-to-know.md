---
title: "Encryption at rest and in transit: what every developer needs to know"
slug: "encryption-at-rest-and-in-transit-what-every-developer-needs-to-know"
author: "Rizwan Saleem"
source: "devto_webdev"
published: "Sat, 06 Jun 2026 03:50:20 +0000"
description: "Encryption at rest and in transit: what every developer needs to know Encryption is the foundation of data security. Encryption in transit protects data as i..."
keywords: "encryption, data, rest, protects, key, transit, tls, like"
generated: "2026-06-06T04:00:30.107403"
---

# Encryption at rest and in transit: what every developer needs to know

## Overview

Encryption at rest and in transit: what every developer needs to know Encryption is the foundation of data security. Encryption in transit protects data as it travels across networks. Encryption at rest protects data when it's stored on disk. Both are essential for protecting sensitive information. Encryption in transit uses TLS to protect data between clients and servers, and between services. Enforce TLS 1.2 or 1.3 for all communications. Disable older, insecure versions like TLS 1.0 and 1.1. Use strong cipher suites and modern key exchange algorithms. mTLS extends TLS to mutual authentication. Both the client and server present certificates, so each side verifies the other's identity. mTLS is the standard for service-to-service communication in zero trust architectures. Service meshes like Istio implement mTLS transparently. Encryption at rest protects data that isn't actively being transmitted. Most cloud providers encrypt data at rest by default S3, EBS, RDS, and DynamoDB all support encryption. Enable it. For data you manage yourself, encrypt disks with LUKS or use filesystem-level encryption. Database encryption protects sensitive columns within a row. Use column-level encryption for highly sensitive data like PII, payment information, and health records. PostgreSQL supports pgcrypto for column encryption. Key management is the hardest part of encryption. Use a dedicated key management service like AWS KMS, GCP Cloud KMS, HashiCorp Vault, or Azure Key Vault. Never store encryption keys in your application code or environment variables. Rotate keys regularly and audit key usage. Encryption is not a silver bullet. Encrypted data is still vulnerable to attacks that exploit the application itself SQL injection, access control flaws, and compromised credentials can all bypass encryption. Encryption protects against specific threats and complements access control. - Rizwan Saleem | https://rizwansaleem.co

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/therizwansaleem/encryption-at-rest-and-in-transit-what-every-developer-needs-to-know-4ie8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
