---
title: "Ship a Restart-Safe Upload CLI That Survives an Expired Resume URL"
slug: "ship-a-restart-safe-upload-cli-that-survives-an-expired-resume-url"
author: "Sam Rivera"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 03:18:45 +0000"
description: "My upload CLI looked restart-safe until I tested two failures together: the process crashed at 63%, and the signed resume URL expired before restart. The che..."
keywords: "remote, upload, checkpoint, file, offset, restart, url, expired"
generated: "2026-07-20T03:39:19.783823"
---

# Ship a Restart-Safe Upload CLI That Survives an Expired Resume URL

## Overview

My upload CLI looked restart-safe until I tested two failures together: the process crashed at 63%, and the signed resume URL expired before restart. The checkpoint needs identity, not credentials: { "file" : "release.tar.gz" , "fingerprint" : "sha256:..." , "uploadId" : "up_123" , "localOffset" : 66060288 , "updatedAt" : "2026-07-19T12:00:00Z" } Do not persist the signed URL. On restart, exchange the durable upload ID for fresh authorization, query the server offset, then reconcile: const remote = await headUpload ( freshUrl ); if ( remote > file . size ) throw new Error ( " invalid remote offset " ); if ( remote !== checkpoint . localOffset ) { await saveCheckpoint ({ ... checkpoint , localOffset : remote }); } await sendFrom ( file , remote , freshUrl ); The server offset wins because a crash can occur after bytes are accepted but before the local checkpoint is renamed. Save checkpoints through write-to-temp plus atomic rename so a partial JSON file cannot destroy recovery. My fixture matrix includes: Failure Expected behavior crash after remote commit rewind/advance to remote offset expired URL refresh without creating a second upload changed local file stop on fingerprint mismatch missing remote upload ask before starting over checkpoint write interrupted retain previous valid checkpoint The tus resumable upload protocol specifies offset discovery and conflict handling that are useful even if the service uses a smaller custom protocol. The key idea is explicit reconciliation, not assuming client memory is authoritative. I also shipped upload status , upload forget , and an exportable checkpoint directory. Recovery is a user-facing feature; if users cannot inspect or remove state, “resumable” becomes hidden lock-in.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rivera123/ship-a-restart-safe-upload-cli-that-survives-an-expired-resume-url-182m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
