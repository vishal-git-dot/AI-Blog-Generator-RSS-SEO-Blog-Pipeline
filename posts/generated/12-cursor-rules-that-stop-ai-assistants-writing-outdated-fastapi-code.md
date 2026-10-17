---
title: "12 Cursor rules that stop AI assistants writing outdated FastAPI code"
slug: "12-cursor-rules-that-stop-ai-assistants-writing-outdated-fastapi-code"
author: "RDJ"
source: "devto_python"
published: "Sat, 17 Oct 2026 03:45:24 +0000"
description: "AI coding assistants still reach for FastAPI patterns from a few years ago: .dict() , orm_mode , session.query() , HTTPException raised deep inside service c..."
keywords: "rules, code, never, app, cursor, fastapi, only, routers"
generated: "2026-10-17T03:51:06.688010"
---

# 12 Cursor rules that stop AI assistants writing outdated FastAPI code

## Overview

AI coding assistants still reach for FastAPI patterns from a few years ago: .dict() , orm_mode , session.query() , HTTPException raised deep inside service code, SQLite in tests. The code runs, but it isn't the code you'd write today. Cursor's project rules fix most of this. A rule is a small .mdc file in .cursor/rules/ with a glob, so it loads only when you edit matching files: --- description : " FastAPI routers, dependencies and Pydantic v2 schemas" globs : src/app/**/router.py,src/app/**/schemas.py,src/app/**/deps.py alwaysApply : false --- - One APIRouter(prefix="/<plural-resource>") per feature ... These are the 12 conventions that made the biggest difference for me. Routers and schemas Pydantic v2 APIs only. model_validate , model_dump , ConfigDict , field_validator . Never .dict() , parse_obj , orm_mode , class Config or the v1 validator decorator. Routers are thin and async. Parse, call a service, return a schema. No SQL or business rules in routers. Always declare response_model (or a return annotation) and an explicit status_code : 201 for create, 204 for delete. Schemas are named XCreate / XUpdate / XRead . Input models use ConfigDict(extra="forbid") so a sneaky "is_admin": true is rejected. Apply updates with model_dump(exclude_unset=True) . Database SQLAlchemy 2.0 style only. Mapped[...] , mapped_column() , select() . Never session.query() or declarative_base() . Services own the transaction with async with session.begin(): . Repositories never commit. Use async_sessionmaker(expire_on_commit=False) . Relationships default to lazy="raise" . Load explicitly with selectinload() or joinedload() , so there's no hidden IO in async code. Set MetaData(naming_convention=...) on your Base so Alembic constraint names are deterministic. Never edit a migration that's already applied. Errors, config and safety Services raise your own AppError subclasses, never HTTPException . One exception handler maps them to {"error": {"code": ..., "message": ...}} . Settings only through a cached get_settings() built on pydantic-settings. Never read os.environ elsewhere, and keep secrets as SecretStr . Never build SQL with f-strings. Use bound parameters or text(...).bindparams() . Tests pytest + pytest-asyncio + httpx.AsyncClient(transport=ASGITransport(app=app)) , against a real Postgres with a rollback per test. Clear app.dependency_overrides after each test. No SQLite stand-in. Using them Drop rules like these into .cursor/rules/ , one file per area, with globs that match your layout. For Claude Code, the same conventions work as a short CLAUDE.md at the repo root. Disclosure: I made a FastAPI rules pack with these conventions written out as 7 scoped .mdc files plus a CLAUDE.md , and I sell it for $12 at codebaserules.com . Two of the files are a free download , no email needed. Everything above works without buying anything. I'd like to hear which of these you'd change.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rdj/12-cursor-rules-that-stop-ai-assistants-writing-outdated-fastapi-code-1bc2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
