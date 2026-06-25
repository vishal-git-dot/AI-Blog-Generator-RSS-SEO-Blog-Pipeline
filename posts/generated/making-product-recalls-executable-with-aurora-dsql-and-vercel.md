---
title: "Making product recalls executable with Aurora DSQL and Vercel"
slug: "making-product-recalls-executable-with-aurora-dsql-and-vercel"
author: "Ujwal Vanjare"
source: "devto_webdev"
published: "Thu, 25 Jun 2026 03:53:41 +0000"
description: "Live demo: https://safestate.vercel.app , code: https://github.com/usv240/safestate A product recall today is basically a notice. It lives on a webpage, or a..."
keywords: "dsql, recall, vercel, write, product, safestate, recalled, where"
generated: "2026-06-25T04:05:12.294092"
---

# Making product recalls executable with Aurora DSQL and Vercel

## Overview

Live demo: https://safestate.vercel.app , code: https://github.com/usv240/safestate A product recall today is basically a notice. It lives on a webpage, or a PDF, or an email that somebody is supposed to read. Say the problem out loud and it gets uncomfortable fast. A recalled crib can be listed and sold to another family, and nobody in that sale ever sees the recall. Reselling recalled goods is actually illegal, and recalled infant products have killed kids. I spent this hackathon building something to close that gap. I called it SafeState, and the idea is small: make the recall do something. When a second-hand item is listed or sold, the marketplace checks SafeState first, and recalled units get blocked right at checkout. It is precise down to the serial number, so safe units still sell. It runs on the stack this hackathon is about. A Next.js front end on Vercel, with Amazon Aurora DSQL behind it. Why DSQL is the whole point here The promise SafeState has to keep is this: the moment a recall lands in any region, no marketplace anywhere should ever read that product as "safe" again. That is a strong consistency problem, not a nice-to-have. If there is any window where a recalled product still looks safe, that is exactly when it gets sold. An eventually consistent store or a nightly sync leaves that window open. DSQL's active-active, multi-region setup with strong consistency is what closes it. I set up a real peered cluster across us-east-1 and us-east-2, with us-west-2 as the witness. Write a recall through one region's endpoint and you can read it back from the other region right away. There is a page in the app that lets you run that yourself. The one trick that makes it work DSQL runs on snapshot isolation (PostgreSQL REPEATABLE READ) with optimistic concurrency. It catches write-write conflicts at commit time. Snapshot isolation will not protect you from write skew, so I had to design around that. To guarantee that a recall and a sale of the same product actually collide, I make both of them write the same row. Every model has one safety_guard row that holds its status and an epoch number. // authorize-transfer, simplified. The AUTHORIZED path touches the SAME guard // row a concurrent recall writes, so DSQL is forced to detect the conflict. await client . query ( " BEGIN " ); await client . query ( " SELECT epoch FROM safety_guard WHERE model_id = $1 FOR UPDATE " , [ modelId ]); // ...evaluate every active directive against THIS unit's serial... // if it is covered, return BLOCKED. otherwise: await client . query ( " INSERT INTO ownership_transfers (...) VALUES (...) " ); await client . query ( " UPDATE product_instances SET current_owner_id = $1 WHERE id = $2 " , [ buyer , id ]); await client . query ( " UPDATE safety_guard SET updated_at = now() WHERE model_id = $1 " , [ modelId ]); // the conflict-forcing write await client . query ( " COMMIT " ); // the loser throws SQLSTATE 40001 / OC000 here If the recall commits first, the sale's COMMIT throws SQLSTATE 40001 ( OC000 ). A small wrapper catches it, backs off with some jitter, and runs the whole transaction again. The second time around it reads the recalled state and returns BLOCKED. So there is no version of events where a recalled product slips through as safe. const RETRYABLE = new Set ([ " 40001 " , " OC000 " , " OC001 " ]); // retry the WHOLE transaction on conflict, backoff plus jitter, max 3 attempts The Vercel side Route handlers talk to DSQL over the normal Postgres protocol, but auth is a short-lived IAM token minted per connection with @aws-sdk/dsql-signer . There is no database password sitting in an env var anywhere. A Vercel Cron job pulls real recalls from the public CPSC API once a day. And Claude reads messy second-hand listings, the kind a person actually writes ("used baby sleeper, works fine"), and figures out which recall they match, with a confidence score. The uncertain ones go to a review queue instead of being auto-blocked. One thing that cost me an hour. Vercel functions run on Lambda, and Lambda reserves AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY and AWS_REGION . You cannot set those as env vars. So I pass the DSQL credentials under different names and hand them to the signer directly. const creds = process . env . SAFESTATE_AWS_ACCESS_KEY_ID ? { accessKeyId : process . env . SAFESTATE_AWS_ACCESS_KEY_ID , secretAccessKey : process . env . SAFESTATE_AWS_SECRET_ACCESS_KEY } : undefined ; // local dev falls back to the default AWS provider chain const signer = new DsqlSigner ( creds ? { hostname , region , credentials : creds } : { hostname , region }); A few things that helped If you build on DSQL, pick a problem where being correct under concurrency is the actual product, not a side detail. That is where it earns its keep. Make your conflicting operations write the same row so OCC has something to catch. And write the retry-on-40001 wrapper before anything else, because you will lean on it constantly. Recalls should stop being PDFs and start being decisions. Aurora DSQL and Vercel got me there over a weekend. Live: https://safestate.vercel.app , code: https://github.com/usv240/safestate I built this for the H0: Hack the Zero Stack hackathon. #H0Hackathon

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujwal240/making-product-recalls-executable-with-aurora-dsql-and-vercel-2nja

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
