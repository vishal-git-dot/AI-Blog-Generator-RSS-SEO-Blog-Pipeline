---
title: "How AIClaw 3.7.7 Separates File Previews from Recorded Change Reviews"
slug: "how-aiclaw-377-separates-file-previews-from-recorded-change-reviews"
author: "chowyu"
source: "devto_webdev"
published: "Tue, 13 Oct 2026 00:06:17 +0000"
description: "A generated file is useful only if you can inspect it. A chat can say that a SQL query was updated or a report was saved, but switching to another applicatio..."
keywords: "file, not, recorded, preview, panel, read, markdown, line"
generated: "2026-10-13T00:25:36.278321"
---

# How AIClaw 3.7.7 Separates File Previews from Recorded Change Reviews

## Overview

A generated file is useful only if you can inspect it. A chat can say that a SQL query was updated or a report was saved, but switching to another application interrupts the review—and opening the current file does not necessarily show what the agent changed. AIClaw v3.7.7 , released on October 12, adds an in-app file preview and a separate view of recorded modifications. At the time of writing, v3.7.9 is the latest public release. The behavior described here shipped in v3.7.7; it is not an unreleased proposal. The important distinction is between reading a file now and reviewing the snapshots recorded when a tool changed it . Open the result beside the conversation Clicking a supported file card opens a read-only panel beside the chat. Text, SQL, Markdown, and common source-code formats get line numbers, content copying, and syntax highlighting where a loaded grammar is available. Markdown has rendered and source views. On narrower windows, the preview overlays the main content instead of squeezing both panes indefinitely. For example, an agent might return a query such as: SELECT id , email FROM users WHERE active = 1 ; You can read that query in context without launching an editor. This is inspection, not editing: the panel does not save changes. Unsupported formats, including Office documents, retain the existing system-open behavior. The format map selects languages from explicit extensions and a small set of recognized filenames. The highlighter uses an explicit language rather than auto-detection. Unavailable grammars and large inputs fall back to escaped plain text. A recorded diff is not a Git diff The work panel's file-change entries open the same preview panel in comparison mode. You can choose a side-by-side or unified view, or read the recorded before and after snapshots. Removed and added lines carry separate line numbers. Suppose a tool changed a query from selecting only an ID to selecting an ID and email. The comparison shows that recorded transition even if somebody subsequently edits the file on disk. That is also its boundary: the recorded after snapshot is not a claim about the current disk contents . The panel displays a reminder of this distinction. It does not compare against Git HEAD, inspect staged changes, or provide a general repository-review view. The diff helper performs a line comparison. When the product of the two line counts exceeds 250,000, it uses replacement blocks instead of allocating a large comparison matrix. The panel limits displayed differences to 3,000 lines, so very large changes may need an external editor for complete review. Reading local files needs a host boundary The renderer requests a preview through Electron IPC with both the path and the owning session ID. The host resolves relative paths using that session's working directory, rather than whichever workspace happens to be selected later. The reader checks protected locations for both the requested path and its canonical target. It checks that the opened descriptor refers to a regular file, bounds the read, and rejects NUL bytes or invalid UTF-8. Disk-text previews have a 512 KiB limit. Displayed source content is also bounded by size and line count. These checks protect the preview path; they are not a general sandbox for every filesystem operation. The comparison view uses recorded snapshots instead of rereading the file. There is a separate UI race to handle. If a read finishes after the user switches chats or opens another file, the store ignores the stale result. A delayed response should not reopen another conversation's preview. Markdown remains a document, not an execution surface Local Markdown previews reuse the existing Markdown parser and sanitizer, with image tags and inline style attributes forbidden in the preview renderer . Embedded images are not automatically fetched. Relative file references resolve from the document's directory. This is not a browser for arbitrary HTML applications, nor does recognizing an MDX extension execute MDX components. What the tests establish The reader tests cover supported formats, protected paths and symlink aliases, oversized and invalid text, and special-file refusal. Diff tests check line numbering and paired replacement rows. The desktop workflow smoke test exercises the real Vue/preload interface with fixture host responses, including Markdown/source switching, SQL comparisons, and late-read isolation. That validates those UI and bridge cases; it does not prove every language grammar or every operating system's file-opening behavior. The v3.7.7 release notes report 259 renderer/helper tests and 86 work-panel UI checks passing as part of the full local check. These are suite totals, not preview-only counts. Its release CI also succeeded. The same notes record an unrelated live transcription timeout and a successful targeted retry; the fixture-based preview checks should not be confused with live-model validation. Keeping current-file inspection and recorded-change review visibly separate makes the result easier to assess without implying that a historical snapshot is the current state of the workspace. This article was generated by an AI agent and checked against public AIClaw source, release notes, and the release CI result.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chowyu12/how-aiclaw-377-separates-file-previews-from-recorded-change-reviews-l7o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
