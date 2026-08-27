---
title: "JSON to C# in Modern .NET: 5 Deserialization Traps with Records and System.Text.Json"
slug: "json-to-c-in-modern-net-5-deserialization-traps-with-records-and-systemtextjson"
author: "Rasika Dangamuwa"
source: "devto_webdev"
published: "Thu, 27 Aug 2026 21:31:39 +0000"
description: "Converting JSON payloads into strongly typed C# models is one of the most common tasks in .NET backend development. Whether integrating third-party webhooks,..."
keywords: "json, public, net, records, system, text, string, get"
generated: "2026-08-27T22:04:47.424091"
---

# JSON to C# in Modern .NET: 5 Deserialization Traps with Records and System.Text.Json

## Overview

Converting JSON payloads into strongly typed C# models is one of the most common tasks in .NET backend development. Whether integrating third-party webhooks, consuming microservice endpoints, or ingesting external telemetry, having well-structured Data Transfer Objects (DTOs) ensures compile-time safety and clean architecture. However, moving from dynamic JSON to static C# is rarely a 1:1 mapping. With modern .NET features like nullable reference types (NRT), positional records, source generators, and System.Text.Json , naive auto-generated classes frequently cause production runtime exceptions or silent data truncation. Here are five subtle deserialization traps every .NET engineer should guard against when converting JSON to C#. 1. Positional Records vs Missing JSON Properties C# positional records provide a concise syntax for immutable DTOs: public record UserDto ( string Id , string Email , string ? PhoneNumber ); When deserializing with System.Text.Json , positional records use the parameterized primary constructor. If the incoming JSON payload omits a non-nullable property like Email , .NET does not throw during instantiation; instead, it passes default ( null ) into the constructor. { "id" : "usr_8921" } Even though Email is declared as non-nullable string , user.Email becomes null at runtime without throwing a JsonException . Downstream code expecting non-null references will subsequently fail with an unhandled NullReferenceException . Solution: If fields are optional in upstream payloads, explicitly annotate them as nullable ( string? ) or define fallback defaults in your models. 2. Case Insensitivity vs Explicit [JsonPropertyName] Many teams enable case-insensitive matching globally: var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true }; While convenient, case-insensitive property matching introduces runtime overhead and ambiguity if an API returns conflicting casing (such as ID and id ). Furthermore, when using Native AOT compilation or .NET Source Generators ( JsonSourceGenerationOptions ), reflection-based matching is disabled or discouraged. When mapping snake_case or kebab-case APIs to idiomatic PascalCase C# properties, explicit mapping attributes eliminate runtime guessing: using System.Text.Json.Serialization ; public record OrderDto { [ JsonPropertyName ( "order_id" )] public required string OrderId { get ; init ; } [ JsonPropertyName ( "total_amount" )] public decimal TotalAmount { get ; init ; } } If you are generating models for large JSON schemas, tools like the browser-based Nutilz JSON to C# Converter can automatically output clean records with explicit [JsonPropertyName] annotations and chosen casing conventions client-side. 3. Timestamp Drift: DateTime vs DateTimeOffset Naive generators often map ISO 8601 strings to DateTime : // Unsafe: loses exact timezone offset public DateTime CreatedAt { get ; init ; } When System.Text.Json deserializes "2026-08-27T18:30:00+05:30" into a DateTime , it sets DateTimeKind.Unspecified unless configured otherwise. If you later convert it to UTC via .ToUniversalTime() , .NET assumes the timestamp was in the server's local timezone, corrupting the stored timestamp. // Safe: preserves UTC offset and fractional seconds [ JsonPropertyName ( "created_at" )] public DateTimeOffset CreatedAt { get ; init ; } Always use DateTimeOffset for API models representing instant points in time, or DateOnly for calendar dates. 4. Floating Point Precision Loss in Numeric IDs and Currency JSON treats all numbers uniformly. As a result, code generators frequently default fractional values to double or float : // Bug: binary floating-point representation causes rounding errors public double Price { get ; init ; } In financial calculations, 0.1 + 0.2 becomes 0.30000000000000004 in binary floating-point math. Always use decimal for monetary values. Similarly, large 64-bit integer identifiers (such as Snowflake IDs or Discord user IDs) exceed the safe 53-bit integer limit of JavaScript clients ( Number.MAX_SAFE_INTEGER ). Ensure large IDs are typed as long or string in your C# DTOs to avoid truncation. 5. Mutable Collections vs Immutable Read-Only Lists Defaulting collections to List<T> exposes internal state across layers: public class CartDto { public List < CartItemDto > Items { get ; set ; } = new (); } This allows consumers of your DTO to modify the collection in-place, bypassing domain invariants. In modern C#, prefer read-only interfaces or immutable collections with init-only setters: public record CartDto { [ JsonPropertyName ( "items" )] public IReadOnlyList < CartItemDto > Items { get ; init ; } = Array . Empty < CartItemDto >(); } System.Text.Json can deserialize directly into IReadOnlyList<T> , IReadOnlyCollection<T> , or ImmutableArray<T> without additional converters. Summary Generating C# classes from JSON saves hours of boilerplate, but taking generated code straight to production without checking nullability, timestamp formats, and numeric precision invites subtle bugs. Next time you need to scaffold strongly typed C# classes or positional records from JSON responses, try the free Nutilz JSON to C# utility to generate clean, customizable System.Text.Json or Newtonsoft models in your browser.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rasika_dangamuwa_ed1074fe/json-to-c-in-modern-net-5-deserialization-traps-with-records-and-systemtextjson-3ol9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
