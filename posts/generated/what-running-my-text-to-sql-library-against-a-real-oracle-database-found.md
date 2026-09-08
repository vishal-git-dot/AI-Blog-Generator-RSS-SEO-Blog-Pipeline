---
title: "What running my text-to-SQL library against a real Oracle database found"
slug: "what-running-my-text-to-sql-library-against-a-real-oracle-database-found"
author: "Ashish sinha"
source: "devto_python"
published: "Tue, 08 Sep 2026 20:46:12 +0000"
description: "A few weeks ago I published schemagate, a library that picks the handful of tables a text-to-SQL model needs and filters them by who's asking. Two people in ..."
keywords: "what, oracle, database, not, one, schemagate, now, because"
generated: "2026-09-08T20:58:09.572560"
---

# What running my text-to-SQL library against a real Oracle database found

## Overview

A few weeks ago I published schemagate, a library that picks the handful of tables a text-to-SQL model needs and filters them by who's asking. Two people in the comments asked for column-level restriction and an audit record of what was selected. Both are in now — restrict_column() and Selection.to_dict() . This post is about something less comfortable: what happened when I finally pointed it at a real database instead of my test fixtures. The library had 445 passing tests and a README that said Oracle support was "not yet run against a live instance". That phrasing was honest and I was relaxed about it, because reflection goes through SQLAlchemy's dialect-agnostic Inspector and there is no vendor SQL anywhere. What could a live run possibly find? Five things. Here they are in order of how much they embarrassed me. 1. Reflection returned 1,493 objects ADMIN on an Autonomous Database sees APEX, ORDS, OML, ODI and the whole OCI service layer. The user's own tables were a few dozen of those. Nothing was broken exactly — it just made the catalog useless. Oracle records this in ALL_USERS.ORACLE_MAINTAINED , so that's the filter now. 2. VECTOR columns came back as NULL SQLAlchemy reports a type it has no class for as NULL and warns. On Oracle that covers XMLTYPE, JSON, object types and — on 23ai/26ai — VECTOR. So the DDL going into the prompt said NULL where it should have said VECTOR(512, FLOAT32) . Recovered from the data dictionary now. 3. The driver handed back JSON already decoded OracleStore reads a CLOB CHECK (IS JSON) column and called json.loads on it. python-oracledb 4 returns a dict. TypeError , in four of fifteen store tests, on a code path that had 26 static tests pinning its SQL. 4. The one that actually mattered I added the Oracle service-schema filter from finding 1, and put public on the list — because PUBLIC is a pseudo-schema on Oracle. On PostgreSQL, public is the user's entire database. So for four releases, every PostgreSQL user who upgraded got a catalog of zero objects. No error, no warning, no exception. bootstrap() returned an empty catalog and selection returned nothing, and it looked exactly like a library that didn't understand your schema. I only found it because someone asked me to make sure Postgres worked, and instead of trusting my own README I installed PostgreSQL 16 and ran the certification script. It failed 7 of 10 checks. The one-line fix is boring. The structural fix isn't: internal-schema detection now lives behind a per-dialect hook, applies only to the dialect that defines it, and there's a test that fails if a cross-dialect list ever reappears. One engine's tidy-up should never be able to empty another engine's catalog. 5. And then the stack that could never apply I ship a Terraform stack so people can stand this up on OCI in one click. I had reviewed it carefully, twice, and fixed real bugs in it by reading. Then I finally ran it in a real tenancy. terraform plan was clean: ten resources, no warnings. The apply provisioned the database, then died: 400-InvalidParameter: Internet Gateway target cannot be used together with Service Gateway target for All Services in the same routing table I had added that service gateway myself, in an earlier review pass, because an Autonomous Database access-control list naming a VCN only works when traffic arrives through one. What I could not see by reading is that OCI refuses to have it in the same route table as the internet gateway the VM needs to install anything. Not a plan error — the plan cannot know. Only the API knows. Every one-click deploy since that "fix" would have failed at exactly that point. The button was live in my README the whole time. What I'd take from this "It goes through an abstraction layer so it must be portable" is a hypothesis, not a property. So is "I read it carefully and it looks right." Every one of these bugs lived below the abstraction or below the plan: in what the driver returns, in what the dictionary calls a type, in what a schema name means, in what the API will accept. None were reachable from SQLite, which is what all 445 tests ran on. And none were reachable from reading. If you maintain something that claims to work on a database or an infrastructure you have not run it against, that claim is a to-do item, not a feature. Reviewing is not running. There is now a script in the repo that stands the whole thing up in your own tenancy, checks the running machine rather than the plan, and tears it down again — because the next person to say "it looks right" will be me. schemagate 0.1.7 is on PyPI, certified live on Oracle 26ai and PostgreSQL 16. Apache-2.0. pip install schemagate schemagate demo "salary by employee" https://github.com/ashishsinha1602/schemagate

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ashish_sinha_5241c7673d93/what-running-my-text-to-sql-library-against-a-real-oracle-database-found-1gab

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
