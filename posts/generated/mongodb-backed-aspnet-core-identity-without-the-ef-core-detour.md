---
title: "MongoDB-backed ASP.NET Core Identity, without the EF Core detour"
slug: "mongodb-backed-aspnet-core-identity-without-the-ef-core-detour"
author: "Michael Jordan"
source: "devto_webdev"
published: "Wed, 24 Jun 2026 19:42:41 +0000"
description: "If you're already running MongoDB and you reach for ASP.NET Core Identity, the official story points you at Entity Framework Core. That's a fine answer if yo..."
keywords: "you, identity, store, mongo, guid, index, mongodb, core"
generated: "2026-06-24T19:54:11.166189"
---

# MongoDB-backed ASP.NET Core Identity, without the EF Core detour

## Overview

If you're already running MongoDB and you reach for ASP.NET Core Identity, the official story points you at Entity Framework Core. That's a fine answer if you have a relational database. If you don't, you end up bolting a second data access stack onto an app that has exactly one store. You don't need it. AspNetCoreIdentity.MongoDriver is a store provider that talks to Mongo through the official MongoDB.Driver directly — no EF Core, no SQL, no second persistence model. It implements the Identity store interfaces, ships a UserStore and RoleStore , and wires up UserManager / RoleManager the way you already expect. The 15-line version Register the provider in Program.cs : builder . Services . AddIdentityMongoDbProvider < MongoUser < Guid >, MongoRole < Guid >, Guid >( identity => { identity . User . RequireUniqueEmail = true ; }, mongo => { mongo . ConnectionString = builder . Configuration . GetConnectionString ( "MongoDb" )!; }); A connection string like mongodb://localhost:27017/Identity creates an Identity database and stores the collections there. That's the whole setup. Now inject the managers wherever you need them: public class AccountController ( UserManager < MongoUser < Guid >> userManager ) : Controller { // ... } They're registered as scoped services — let the container manage their lifetime. Don't call BuildServiceProvider() yourself, and don't cache the managers in long-lived objects. Your key type is yours The MongoUser and MongoRole classes are generic, so the primary key isn't forced to be a Guid . Want string keys? Use MongoUser<string> . If you use string keys and don't assign an Id on create, the store generates an ObjectId-style string for you. If you do go with Guid , register the serializer once before the code above so Mongo stores them in the standard representation: BsonSerializer . RegisterSerializer ( new GuidSerializer ( GuidRepresentation . Standard )); Migrations that survive a rolling deploy Here's the part that usually bites people who hand-roll a Mongo store. On the first store operation — not during service registration — the library: applies any pending schema migrations, guarded by a distributed lock so that if several app instances boot at once, the migrations apply exactly once; and creates its indexes: a unique index on NormalizedUserName , an index on NormalizedEmail , a compound index on Logins.LoginProvider / Logins.ProviderKey , and a unique index on the role NormalizedName . That distributed lock matters the moment you run more than one instance. Two pods starting simultaneously won't race each other into a half-applied schema. Because the NormalizedUserName index enforces real uniqueness, index creation will fail if your existing data already contains duplicate user names — clean those up before you upgrade. If you'd rather own these concerns yourself, set mongo.DisableIndexCreation = true and/or mongo.DisableAutoMigrations = true . And if you want the work done at startup instead of on first request, resolve MongoIdentityInitializer and await EnsureInitializedAsync() . It won't silently clobber concurrent writes Updates and deletes use optimistic concurrency through Identity's ConcurrencyStamp . If the document changed since you loaded your copy, the operation returns a ConcurrencyFailure instead of overwriting the other write. Reload, reapply, retry — the normal Identity dance. One honest limitation options.Stores.ProtectPersonalData is not supported. The store doesn't encrypt personal data at rest, and rather than letting you flip that switch and quietly store unprotected data anyway, enabling it throws at runtime. If you need encryption-at-rest for PII, handle it at a different layer. Try it dotnet add package AspNetCoreIdentity.MongoDriver Package: https://www.nuget.org/packages/AspNetCoreIdentity.MongoDriver Source: https://github.com/lxman/AspNetCoreIdentity.MongoDriver If you're on Mongo and Identity, this is the short path. Issues and PRs welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/michael_jordan_87eaf96f24/mongodb-backed-aspnet-core-identity-without-the-ef-core-detour-848

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
