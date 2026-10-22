---
title: "Four .pub files, one run: what REVIEW and FAILED actually look like"
slug: "four-pub-files-one-run-what-review-and-failed-actually-look-like"
author: "alapha888"
source: "devto_python"
published: "Thu, 22 Oct 2026 20:51:32 +0000"
description: "Microsoft removed Publisher from Microsoft 365 on October 1, 2026, and support for the perpetual version ended October 13, 2026. The files, of course, are st..."
keywords: "file, pub, not, failed, review, files, what, pubaudit"
generated: "2026-10-22T21:22:57.091039"
---

# Four .pub files, one run: what REVIEW and FAILED actually look like

## Overview

Microsoft removed Publisher from Microsoft 365 on October 1, 2026, and support for the perpetual version ended October 13, 2026. The files, of course, are still there. My earlier posts covered the rescue checklist and why batch conversion is not the hard part — verification is. This post is one concrete run, end to end, on a set of files whose expected verdicts were written down before the run took place. The run happened on October 19, 2026, with PubAudit ( pubaudit.py ) and LibreOffice 24.2.7.2, on copies of the files in a scratch folder. The originals were not modified — PubAudit never writes to its inputs — and nothing in this example deletes anything. The four files These are the smoke-test fixtures of the Windows edition of PubAudit, kept in that project's test corpus with their provenance and expected verdicts pinned in advance: File Size (bytes) What it actually is MSPublisher2013-Sample.pub 98,304 A real Publisher 2013 file (from the PRONOM research corpus). Image-heavy. fdo59355-1.pub 10,752 A real Publisher file from LibreOffice's own libmspub test corpus. corrupt-ole.pub 2,048 Derived locally: the first 2,048 bytes of fdo59355-1.pub — a valid OLE2 header with a truncated body. fake-renamed.pub 48 One line of plain text saved with a .pub name. No OLE2 header. The verdicts pinned for this set before any run are: REVIEW , REVIEW , FAILED , FAILED . The set is deliberately built to contain no easy OK — its job is to exercise the two piles people find confusing. The run and the report it wrote python3 pubaudit.py /path/to/folder # Done: 0 OK, 2 REVIEW, 2 FAILED The CSV report, row for row: File Status Pages Text chars Note (shortened) MSPublisher2013-Sample.pub REVIEW 1 7 PDF produced but little/no extractable text — check it visually before deleting the .pub . fdo59355-1.pub REVIEW 2 16 PDF produced but little/no extractable text — check it visually before deleting the .pub . corrupt-ole.pub FAILED — — No PDF produced. Converter said: rc=0, no PDF produced; "source file could not be loaded". fake-renamed.pub FAILED — — Not a real Publisher file (missing OLE2 header). All four verdicts match the pinned expectations. The page counts also match what the fixture documentation says these files convert to (one page and two pages respectively) — a small cross-check that the PDFs are the right documents, not just some output. Reading the four rows The two REVIEW rows are successes with homework attached. Both real files converted: a PDF exists for each, with the expected page count. They land in REVIEW rather than OK for one stated reason — the extractable text (7 and 16 characters) is under PubAudit's 20-character floor for a clean OK . That is what image-heavy flyers look like to a text check: the content is in the pictures, not in a text layer. REVIEW here is not a suspicion that conversion failed; it is the report declining to verify what it cannot read. The next step is a visual check, and both originals stay exactly where they are until someone has done it. fake-renamed.pub is the first FAILED shape. At 48 bytes of plain text, it fails the eight-byte OLE2 header check before the converter ever sees it — the note says so in those words. Re-running will never change this row. The file is not a damaged Publisher file; it is a text file wearing the wrong name, to be kept or discarded as what it actually is. corrupt-ole.pub is the second FAILED shape, and the instructive one. It passes the header check (its first 2,048 bytes are a genuine Publisher file's), the converter runs — and exits with code 0 while producing no PDF at all. A tool that trusted the exit code would report this file as converted. The row is FAILED because PubAudit checks that the output file exists, not what the converter claimed. Where the run ends Nothing was deleted, and nothing in this report licenses a deletion yet. The two REVIEW originals wait for eyes; the two FAILED originals are kept — for the renamed text file because it was never a Publisher file, for the truncated file because a better copy or a future converter is its only remaining route, and "unrecoverable for now" is a legitimate end state. The same four verdicts are what the Windows edition's engine is pinned to produce on this set. Two independent implementations agreeing on the awkward files — not just the easy ones — is the consistency this fixture set exists to check. What this example does not show No OK row (the fixture set excludes one on purpose; the repository README records a separate seven-file verification run in which five real flyers all came out OK ). No timeout, no missing-converter environment failure, and no large archive. And a four-file run proves nothing about your archive: it shows what the two non- OK verdicts look like when each is earned, so the first real report you read has a reference point. Tool PubAudit is free and MIT-licensed. It converts a folder of .pub files locally via LibreOffice and writes a report classifying every file as OK , REVIEW , or FAILED : Repo: https://github.com/alapha888/pubaudit This worked example in the repo, with links to the per-pile guides: https://github.com/alapha888/pubaudit/blob/main/docs/worked-example-four-files.md Windows edition (graphical app, no command line), $29 one-time: https://alapha888.gumroad.com/l/lvodxo One rule to keep in view throughout: do not delete any original .pub until its replacement PDF has been verified, not just produced.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alapha888/four-pub-files-one-run-what-review-and-failed-actually-look-like-h7g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
