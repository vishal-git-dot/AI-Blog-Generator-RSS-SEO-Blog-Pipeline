---
title: "Two details worth checking in a paginated ASP.NET Core CRUD"
slug: "two-details-worth-checking-in-a-paginated-aspnet-core-crud"
author: "Dayer Arturo López Piña"
source: "devto_webdev"
published: "Sat, 31 Oct 2026 20:57:58 +0000"
description: "This article was prepared with AI assistance and is based on a local ASP.NET Core and SQL Server demo. The examples are excerpts, not a complete application ..."
keywords: "application, query, not, when, email, page, sql, pagination"
generated: "2026-10-31T21:15:20.727310"
---

# Two details worth checking in a paginated ASP.NET Core CRUD

## Overview

This article was prepared with AI assistance and is based on a local ASP.NET Core and SQL Server demo. The examples are excerpts, not a complete application or a production-readiness claim. A customer CRUD can look complete when creating, editing, and deleting work from the UI. Two less visible details deserve a closer look: what happens when sort values are equal, and what happens when two requests try to create the same email address. 1. Give pagination a fully specified order The demo keeps query execution in an EF Core repository. The application service bounds the page size before passing the query to it: var size = Math . Clamp ( query . PageSize , 1 , 100 ); var q = query with { Page = Math . Clamp ( query . Page , 1 , int . MaxValue / size ), PageSize = size }; The upper page bound keeps the subsequent integer offset calculation from overflowing. Clamping is a contract choice: an API could reject invalid inputs instead, provided that behavior is documented for its callers. In the repository, each supported ordering includes the unique ID as a second key. For example: data = data . OrderBy ( x => x . Name ). ThenBy ( x => x . Id ); var total = await data . CountAsync ( ct ); var items = await data . Skip (( query . Page - 1 ) * query . PageSize ) . Take ( query . PageSize ) . ToListAsync ( ct ); Sorting only by name leaves the relative order of customers with the same name unspecified. Adding the ID gives those ties an explicit order. This does not make offset pagination a consistent snapshot. Inserts and deletes between page requests can still shift records. Count and item queries are separate database operations too, so concurrent writes can make their results disagree. The example does not solve either issue; those requirements would need a separate design decision. 2. A duplicate check does not enforce uniqueness The application checks whether an email already exists before saving. That gives the common duplicate case a useful response, but two requests can both pass the check before either commits. The database therefore also has a unique index on Email. Infrastructure translates SQL Server's uniqueness errors into an exception defined by Application: try { await db . SaveChangesAsync ( ct ); } catch ( DbUpdateException ex ) when ( ex . InnerException is SqlException { Number : 2601 or 2627 }) { throw new DuplicateEmailException ( ex ); } Application handles that exception, and the API returns HTTP 409 for the duplicate email case. Application does not need to reference SqlException or EF Core. There is an important limit in this small implementation: the translation assumes a uniqueness failure during this save means a duplicate email. If another unique constraint is added, that assumption must be revisited to avoid reporting the wrong error. What was checked, and what remains open The recorded local SQL Server test submitted ten concurrent creates with the same email. It returned one 201 and nine 409 responses. The HTTP smoke test also covered CRUD, filters, sorting, and pagination. These are results from a previous local verification, not an independent installation or a complete correctness proof. The project separates domain entities, application services and interfaces, infrastructure implementations, and API composition. That separation makes the SQL-specific translation easy to locate. It does not remove the need to test the behavior against SQL Server. For a small business application, when would you move from offset pagination to keyset pagination? And how do you identify the exact violated constraint when a repository has several unique keys?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dayer_arturolpezpia_a/two-details-worth-checking-in-a-paginated-aspnet-core-crud-2p5l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
