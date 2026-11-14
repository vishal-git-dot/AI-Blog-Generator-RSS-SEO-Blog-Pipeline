---
title: "Our AI assistant can write to exactly one table. Postgres enforces it, not our code"
slug: "our-ai-assistant-can-write-to-exactly-one-table-postgres-enforces-it-not-our-code"
author: "Googleer"
source: "devto_ai"
published: "Sat, 14 Nov 2026 13:05:58 +0000"
description: "We build Reperline , a small system that tracks construction schedules, budgets and contracts. It also connects to Claude through MCP (Model Context Protocol..."
keywords: "can, one, only, function, policies, our, table, postgres"
generated: "2026-11-14T13:16:27.352776"
---

# Our AI assistant can write to exactly one table. Postgres enforces it, not our code

## Overview

We build Reperline , a small system that tracks construction schedules, budgets and contracts. It also connects to Claude through MCP (Model Context Protocol), so a project manager can ask "which milestones are late?" or upload an invoice and have Claude prepare the entry. That second part is where it gets uncomfortable. Budget data is money. We did not want "the AI only proposes changes" to be a promise made by application code that one refactor could break. We wanted the database to make it impossible. This post is how we set that up in Postgres, and the one default that quietly undid part of it. Two database roles, two very different grants The web app and the MCP server connect as different Postgres roles. Neither has BYPASSRLS . app_rw is the web app. It reads and writes, filtered by row level security. app_mcp is the MCP server. It can SELECT (RLS still applies) and it can INSERT into one table: pending_changes . grant insert on pending_changes to app_mcp ; create policy pending_changes_mcp_ins on pending_changes for insert to app_mcp with check ( org_id = current_org_id ( ) and status = 'pending' and source = 'claude' ) ; There is no UPDATE or DELETE grant for app_mcp anywhere. So even if a tool handler had a bug, or a prompt talked the model into trying, the worst it can do is file a row that says "pending, from Claude" in its own organisation. A person approves or rejects it in an inbox. The function that applies it, apply_pending_change , is executable by app_rw only and is SECURITY INVOKER on purpose: it runs with the approver's own row level security, so a person can only approve a change they would be allowed to make themselves. The default that undid it: EXECUTE is granted to PUBLIC Some writes in our system go through functions, for example applying an imported schedule. In an early migration we wrote, roughly: revoke execute on function apply_schedule_import ( uuid ) from app_mcp ; It did nothing. In Postgres a new function is executable by PUBLIC by default, and every role is a member of PUBLIC . Revoking from app_mcp removes a grant that app_mcp never had on its own; the PUBLIC grant still lets it in. The fix was the next migration: revoke all on function schedule_import_diff ( uuid ) , apply_schedule_import ( uuid ) from public ; grant execute on function schedule_import_diff ( uuid ) , apply_schedule_import ( uuid ) to app_rw ; Since then, sensitive functions are revoked from public and granted to the one role that needs them. If you rely on roles to limit an AI agent (or anything else), check functions as well as tables. has_function_privilege('app_mcp', 'apply_schedule_import(uuid)', 'execute') is a quick test to put in CI. Permissions as data, checked once per statement Our roles are configurable per organisation, so policies cannot list role names. A permission is an (area, read or write) pair, and policies call has_perm(area, mode) , a SECURITY DEFINER function. One small detail mattered: we wrap it in a scalar subquery. using ( ( select has_perm ( 'budget' , 'r' ) ) ) Written bare, the planner may call the function for every row. As (select ...) it does not depend on the row, so Postgres evaluates it once per statement as an init plan. RESTRICTIVE policies for rules that must always hold Postgres combines ordinary (permissive) policies with OR. That is right for "owner or finance may read", and wrong for rules that must apply on top of everything, like "only the projects you were given" or "a trial that ended is read only". Those are RESTRICTIVE policies, which are combined with AND. We generate them per table: create policy budget_lines_proj on budget_lines as restrictive for all to app_rw , app_mcp using ( < project is visible > ) with check ( < project is visible > ) ; create policy budget_lines_w_ins on budget_lines as restrictive for insert to app_rw , app_mcp with check ( org_writable ( current_org_id ( ) ) ) ; A new permissive policy added later cannot widen access past them, which is exactly what you want from a rule like "read only after the trial". A test that finds new tables by itself The weak spot of RLS is the table someone adds next month and forgets to protect. Our isolation test does not keep a list. It reads the catalogue for every table and view with an org_id column, creates two organisations, and checks, as both app_rw and app_mcp , that a user of A cannot read, update, delete or insert anything of B. A new table is covered the moment it exists, and fails the test run if its policies are missing. What the database cannot do Grants and policies decide who can change what. They cannot decide whether Claude's proposal is right. An invoice read wrongly is still a wrong proposal; it just cannot reach the books without a person looking at it. The inbox is where the real control happens, and the database only guarantees that nobody can skip it. If you are connecting an LLM to data that matters, our one piece of advice: give it its own database role, list exactly what that role may write, and test it the way an attacker would, including functions.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/appwebseo/our-ai-assistant-can-write-to-exactly-one-table-postgres-enforces-it-not-our-code-4pp7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
