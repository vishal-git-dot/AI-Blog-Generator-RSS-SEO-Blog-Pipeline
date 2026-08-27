---
title: "Why Auto-Generated JSON Schemas Fail in Production: 5 Draft-07 vs 2020-12 Traps"
slug: "why-auto-generated-json-schemas-fail-in-production-5-draft-07-vs-2020-12-traps"
author: "Rasika Dangamuwa"
source: "devto_webdev"
published: "Thu, 27 Aug 2026 22:01:27 +0000"
description: "Every API team reaches a point where hand-writing validation schemas becomes unsustainable. The obvious shortcut is piping sample JSON payloads through an au..."
keywords: "schema, draft, type, json, schemas, number, validation, false"
generated: "2026-08-27T22:04:47.422926"
---

# Why Auto-Generated JSON Schemas Fail in Production: 5 Draft-07 vs 2020-12 Traps

## Overview

Every API team reaches a point where hand-writing validation schemas becomes unsustainable. The obvious shortcut is piping sample JSON payloads through an auto-schema generator or inferring contracts from API responses. You test the generated schema locally, wire it into your validator (like Ajv or Python's jsonschema ), and deploy. Then edge cases strike. Valid requests get rejected with 422 Unprocessable Entity errors, polymorphic endpoints fail schema compilation, or malformed data passes through unnoticed. Auto-generated schemas frequently fail because they treat JSON as static data rather than a dynamic contract. Here are 5 subtle JSON Schema traps between Draft-07 and Draft 2020-12 that cause production validation failures. 1. The Positional Tuple Trap: items vs. prefixItems If your API returns fixed-length coordinate pairs (e.g. [40.7128, -74.0060] ), Draft-07 validated positional types using an array of schemas in items : { "$schema" : "http://json-schema.org/draft-07/schema#" , "type" : "array" , "items" : [{ "type" : "number" }, { "type" : "number" }], "additionalItems" : false } In Draft 2020-12 , items can only be a single schema object for remaining elements. Positional tuple validation moved to prefixItems : { "$schema" : "https://json-schema.org/draft/2020-12/schema" , "type" : "array" , "prefixItems" : [{ "type" : "number" }, { "type" : "number" }], "items" : false } Passing a Draft-07 tuple schema into a Draft 2020-12 validator without updating keywords causes compilation errors or allows arbitrary arrays to pass validation. 2. Composition Collapse: additionalProperties vs. unevaluatedProperties When composing modular schemas with allOf , developers often add additionalProperties: false to sub-schemas: { "allOf" : [ { "$ref" : "#/$defs/BaseEntity" }, { "type" : "object" , "properties" : { "email" : { "type" : "string" } }, "additionalProperties" : false } ] } additionalProperties is locally scoped . It only evaluates properties declared inside its own sub-schema object. It has zero awareness of properties defined in sibling branches of allOf or referenced schemas. Because BaseEntity defines id in a separate branch, the local additionalProperties: false rejects valid payloads containing id as unexpected properties. Fix: In Draft 2020-12, use unevaluatedProperties: false at the top level. It dynamically tracks evaluated keys across all allOf branches and $ref targets. 3. The null vs. Optional Field Dilemma When inferring a schema from sample payloads containing {"avatar_url": null} , naive generators often emit: { "properties" : { "avatar_url" : { "type" : "null" } }, "required" : [ "avatar_url" ] } This causes two distinct issues: Type Locking: When a user passes "avatar_url": "https://example.com/pic.png" , validation fails because only literal null is allowed. Presence vs. Nullability: Optional fields and nullable fields are distinct concepts. If a field is optional, omit it from required . If it can be null , use union typing type: ["string", "null"] . When generating schemas from live API payloads or drafting contracts, using an interactive tool like the Nutilz JSON Schema Generator lets you toggle between Draft-07 and Draft 2020-12 specifications, inspect required field inference, and test sample payloads immediately against both drafts. 4. Integer vs. Number Ambiguity The JSON specification (RFC 8259) defines only one generic "number" data type. However, JSON Schema distinguishes between type: "number" (any real number) and type: "integer" (whole numbers). If an auto-generator samples an e-commerce payload where a product price is round ( { "price": 100 } ), it infers "price": { "type": "integer" } . When a fractional price ( 100.50 ) arrives in production, validation rejects the payload. Unless a field is strictly a discrete counter or integer ID, monetary values and rates should always be specified as type: "number" . 5. $defs vs. definitions References In Draft-07, reusable sub-schemas lived in the definitions map: { "$schema" : "http://json-schema.org/draft-07/schema#" , "definitions" : { "UserRole" : { "type" : "string" , "enum" : [ "admin" , "editor" ] } }, "properties" : { "role" : { "$ref" : "#/definitions/UserRole" } } } In Draft 2020-12, the standardized keyword is $defs : { "$schema" : "https://json-schema.org/draft/2020-12/schema" , "$defs" : { "UserRole" : { "type" : "string" , "enum" : [ "admin" , "editor" ] } }, "properties" : { "role" : { "$ref" : "#/$defs/UserRole" } } } Strict Draft 2020-12 engines treat definitions as an unindexed custom key, causing $ref: "#/definitions/..." resolution to fail at runtime. Summary Checklist Before deploying an inferred schema to production: Verify Draft Version: Explicitly define $schema to avoid validator fallback guesswork. Audit Array Validation: Use prefixItems for fixed tuples in Draft 2020-12, and items for lists. Handle Composition: Prefer unevaluatedProperties: false over additionalProperties: false with allOf . Relax Numeric Fields: Use type: "number" for any values that might accept floats. Separate Nullability: Do not mark nullable fields as required unless the key must exist in every payload. Whether you are defining strict validation for webhook ingress or generating OpenAPI contracts from microservices, understanding these specification differences prevents silent data corruption and unexpected 422 errors. For generating or testing schemas with Draft-07 and Draft 2020-12 compatibility, you can use the Nutilz JSON Schema Generator .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rasika_dangamuwa_ed1074fe/why-auto-generated-json-schemas-fail-in-production-5-draft-07-vs-2020-12-traps-j4d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
