---
title: "The "Transfer Counted as an Expense" Bug That Breaks Almost Every Budgeting App"
slug: "the-transfer-counted-as-an-expense-bug-that-breaks-almost-every-budgeting-app"
author: "Muhammad Arslan"
source: "devto_webdev"
published: "Sun, 09 Aug 2026 18:22:15 +0000"
description: "Move ₨15,000 from your bank account to a digital wallet. Nothing was earned. Nothing was spent. Your net worth is identical to a second ago. Open almost any ..."
keywords: "transfer, transaction, string, account, app, ledger, model, amount"
generated: "2026-08-09T18:49:27.363203"
---

# The "Transfer Counted as an Expense" Bug That Breaks Almost Every Budgeting App

## Overview

Move ₨15,000 from your bank account to a digital wallet. Nothing was earned. Nothing was spent. Your net worth is identical to a second ago. Open almost any budgeting app afterward and it'll cheerfully tell you that you just "spent" ₨15,000. I hit this constantly while building Danapani , a multi-ledger personal finance app, and it turned out to be a genuinely interesting data-modeling problem — not just a UI bug. Here's how the transaction model actually works under the hood. The naive model (and why it breaks) The obvious first pass at a finance schema: model Transaction { id String @id @default(uuid()) accountId String type TransactionType // INCOME | EXPENSE amount Decimal } Every transaction either adds to a balance or subtracts from it. Simple — until a user has more than one account. The moment money moves between their own accounts, this model has no way to express "this isn't real income or a real expense, it's the same money in a different place." So it gets recorded as an EXPENSE on the source account, and your monthly spending chart is now wrong. The fix: a TRANSFER type with two linked legs Instead of forcing a transfer through the income/expense lens, Danapani treats it as a first-class type with two rows sharing a group ID: model Transaction { id String @id @default(uuid()) userId String accountId String transferToId String? type TransactionType // INCOME | EXPENSE | TRANSFER amount Decimal transferGroupId String? relatedTransactionId String? // ... } A single transfer becomes two Transaction rows, created atomically: await prisma . $transaction ( async ( tx ) => { const source = await tx . account . findUniqueOrThrow ({ where : { id : sourceId } }); if ( source . balance < amount ) throw new Error ( " Insufficient funds " ); const groupId = crypto . randomUUID (); const outbound = await tx . transaction . create ({ data : { accountId : sourceId , type : " TRANSFER " , amount : - amount , transferGroupId : groupId }, }); const inbound = await tx . transaction . create ({ data : { accountId : destinationId , type : " TRANSFER " , amount , transferGroupId : groupId , relatedTransactionId : outbound . id , }, }); await tx . account . update ({ where : { id : sourceId }, data : { balance : { decrement : amount } } }); await tx . account . update ({ where : { id : destinationId }, data : { balance : { increment : amount } } }); }); Two consequences fall out of this for free: Reporting is correct by construction. Income/expense charts simply filter WHERE type != 'TRANSFER' — no special-casing needed downstream. Deletes and edits stay consistent. Delete one leg, and the handler looks up relatedTransactionId and reverts both account balances together, instead of leaving an orphaned half-transfer. The whole prisma.$transaction() block matters here — without it, a crash between the two balance updates leaves one account short and the other over, and now the user's money has silently duplicated or vanished. Wrapping it means either both legs commit or neither does. Isolating a user's own books from each other The second problem: a single person can have very different reasons to track money — personal spending, freelance client income, a small side business — and mixing them in one view makes monthly reports meaningless. Danapani solves this with a Ledger model that transactions optionally tag into: model Ledger { id String @id @default(uuid()) userId String name String // "Personal", "Freelance USD", "Business" } A transfer between a Meezan-style bank account and a wallet, tagged to the same ledger, nets to zero on that ledger's report. Money moved between ledgers (say, paying yourself from the business ledger into personal) is still just a transfer — same mechanism, just crossing a ledger boundary instead of an account boundary. Multi-tenant isolation with Postgres Row-Level Security None of this matters if user A can query user B's transactions. Rather than repeating WHERE userId = ? in every single query by hand (and inevitably forgetting it somewhere), the isolation is enforced at the database layer: ALTER TABLE "Transaction" ENABLE ROW LEVEL SECURITY ; CREATE POLICY user_isolation ON "Transaction" USING ( user_id = current_setting ( 'app.current_user_id' ):: uuid ); Every request sets app.current_user_id from the verified JWT before running any query. Even a bug that forgets a WHERE clause in application code can't leak another user's rows — Postgres itself refuses to return them. For a finance app specifically, I wanted that guarantee to not depend on every future engineer (including future me) remembering to scope every query correctly. Stack, if you're curious Next.js 15 (App Router) · TypeScript · Prisma · PostgreSQL · Redux Toolkit + RTK Query on the frontend, hitting the same prisma.$transaction() pattern above for every mutation that touches more than one row. Try it / poke holes in it Danapani is live and free at danapani.app if you want to see the transfer/ledger model in action. I'd genuinely like feedback from other people who've built financial or multi-tenant systems — particularly if you've solved the double-entry problem differently, or found a hole in the RLS approach above.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/marslanmustafa/the-transfer-counted-as-an-expense-bug-that-breaks-almost-every-budgeting-app-524p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
