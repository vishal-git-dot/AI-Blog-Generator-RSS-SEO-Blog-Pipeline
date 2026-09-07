---
title: "Building invite flows that don't have race conditions in SvelteKit + Postgres"
slug: "building-invite-flows-that-dont-have-race-conditions-in-sveltekit-postgres"
author: "VerdantStack"
source: "devto_webdev"
published: "Mon, 07 Sep 2026 03:46:18 +0000"
description: "Most invite-link implementations look correct in development and break in production. The edge cases aren't exotic — they're the normal concurrency you get w..."
keywords: "invite, const, invites, count, await, orgid, token, delete"
generated: "2026-09-07T03:57:33.583386"
---

# Building invite flows that don't have race conditions in SvelteKit + Postgres

## Overview

Most invite-link implementations look correct in development and break in production. The edge cases aren't exotic — they're the normal concurrency you get when two people click the same link, or when someone clicks an expired token, or when a seat limit is hit between the check and the insert. Here's how I built an invite flow that handles all of them, using SvelteKit, Postgres, and Drizzle ORM. The flow looks simple Owner creates invite → single-use link sent → recipient clicks → membership created → done Five steps. But each step has failure modes that compound. Edge case 1: token reuse The link gets shared (Slack, email forward, clipboard accident). Two people click it within seconds. The fix: hash the token before storing it in the database. The plaintext token only exists in the URL. When someone clicks, you hash the token from the URL, look up the hash, and delete it atomically — not "check if exists, then delete." // Wrong: TOCTOU race condition const invite = await db . select (). from ( invites ) . where ( eq ( invites . tokenHash , tokenHash )); if ( ! invite ) return fail ( 400 , { message : ' Invalid invite ' }); if ( invite . expiresAtMs < Date . now ()) return fail ( 400 , { message : ' Expired ' }); await db . delete ( invites ). where ( eq ( invites . id , invite . id )); // ^^^ Another request can slip in between the select and delete // Right: single atomic operation const [ claimed ] = await db . transaction ( async ( tx ) => { const [ row ] = await tx . delete ( invites ) . where ( and ( eq ( invites . tokenHash , tokenHash ), gt ( invites . expiresAtMs , Date . now ()), )) . returning (); if ( ! row ) return [ null ]; const [ membership ] = await tx . insert ( memberships ) . values ({ orgId : row . orgId , userId , role : ' member ' , createdAtMs : Date . now () }) . returning (); return [ membership ]; }); if ( ! claimed ) return fail ( 400 , { message : ' Invalid or expired invite ' }); Delete-first, insert-second, one transaction. If two requests arrive simultaneously, one wins the delete and the other gets null . Edge case 2: seat limits The org has 5 seats and 5 members. A 6th invite link was created before the limit was hit. Now someone clicks it. The fix: check the seat count inside the same transaction that creates the membership — not before, not after. // Inside the same transaction as the token claim: const [{ count }] = await tx . select ({ count : count () }) . from ( memberships ) . where ( eq ( memberships . orgId , orgId )); const org = await tx . select (). from ( organizations ) . where ( eq ( organizations . id , orgId )); if ( count >= org . seatLimit ) { // Don't delete the invite — let someone else try later if a seat opens throw new Error ( ' SEAT_LIMIT_REACHED ' ); } The seat check and the membership insert happen atomically. No gap for a second click to slip through. Edge case 3: invite creation also needs protection What if the owner creates 10 invites when they only have 2 seats left? Each invite is "valid" at creation time, but 8 of them will fail at claim time. Two approaches: Count active (unclaimed) invites + existing members vs. seat limit at invite creation time. Reject early. Let anyone create invites, enforce at claim time. Simpler, but the UX is worse (people get a link that doesn't work). I went with option 1 — it's a few extra lines and catches the problem where it's cheap to catch: const activeInvites = await db . select ({ count : count () }) . from ( invites ) . where ( eq ( invites . orgId , orgId )); const members = await db . select ({ count : count () }) . from ( memberships ) . where ( eq ( memberships . orgId , orgId )); if ( activeInvites [ 0 ]. count + members [ 0 ]. count >= org . seatLimit ) { return fail ( 400 , { message : ' No seats available ' }); } Edge case 4: the token itself Don't use sequential IDs or predictable strings. Generate a cryptographically random token, hash it with scrypt (not SHA-256 — scrypt is slower by design, which makes brute-force harder), and store only the hash. import { randomBytes , scrypt , timingSafeEqual } from ' node:crypto ' ; import { promisify } from ' node:util ' ; const scryptAsync = promisify ( scrypt ); async function createInviteToken () { const raw = randomBytes ( 32 ). toString ( ' base64url ' ); const salt = randomBytes ( 16 ); const derived = await scryptAsync ( raw , salt , 64 ); const tokenHash = ` ${ salt . toString ( ' hex ' )} : ${ Buffer . from ( derived ). toString ( ' hex ' )} ` ; return { raw , tokenHash }; // raw goes in the URL, tokenHash goes in the DB } What I packaged I built this pattern (plus RBAC, seat billing, and audit logging) into a tested SvelteKit + Postgres starter. 194 automated tests against a real Postgres database, including the exact race-condition scenarios above. Live demo: postgres-starter.verdantstack-site.pages.dev — seeded with two users (owner + member), resets daily. Try creating an invite and claiming it. Source on GitHub: verdantstack/sveltekit-postgres-starter Pricing: $79 early bird → $129 standard. One license, unlimited projects, lifetime updates, 30-day refund.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/verdantstack/building-invite-flows-that-dont-have-race-conditions-in-sveltekit-postgres-241o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
