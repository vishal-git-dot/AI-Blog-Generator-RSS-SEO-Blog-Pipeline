---
title: "Rich Text: Edit Blocks on the Page, Plus Framework-Agnostic Rendering"
slug: "rich-text-edit-blocks-on-the-page-plus-framework-agnostic-rendering"
author: "Tony Spiro"
source: "devto_webdev"
published: "Wed, 17 Jun 2026 19:56:11 +0000"
description: "When we launched the rich-text metafield, reusable Content Blocks were global: edit a block in settings and every instance updates. That is exactly what you ..."
keywords: "block, text, blocks, html, rich, content, instance, react"
generated: "2026-06-17T20:21:04.205024"
---

# Rich Text: Edit Blocks on the Page, Plus Framework-Agnostic Rendering

## Overview

When we launched the rich-text metafield, reusable Content Blocks were global: edit a block in settings and every instance updates. That is exactly what you want for a shared CTA or footer. But sometimes you want to drop in a block as a starting point and tweak that one instance, like a callout with copy unique to a single article, without changing it everywhere else. Now you can. This release adds editable blocks in the editor and a framework-agnostic HTML renderer for developers, two of the most requested follow-ups since launch. What's New Edit a block on the page. Every block now has an "Edit on page" action. Insert a reusable block, then detach this one instance to edit its content inline. The saved block and all its other instances stay untouched. Synced or per-instance, clearly labeled. Each block shows whether it is Synced (resolved from the saved block, updates everywhere) or Edit on page (content lives inline, unique to this page). "Reset to synced" discards the on-page edits and reconnects the instance, with a confirmation so it never happens by surprise. The right editor for the content. A detached block opens the same editor its type uses: the full rich-text editor for rich text, a code editor for HTML, and a plain text area for plain text. Render anywhere, not just React. The new renderToHtml function turns a rich-text value into a plain HTML string with no React dependency. Use it in Vue, Svelte, Astro, server templates, or any non-React stack. Import it from the @cosmicjs/rich-text/html entry point. Backward compatible. Existing content and synced blocks work exactly as before. No migration, and the stored format is unchanged for synced references. Why This Matters Reusable blocks and one-off, editable blocks solve different problems, and good content tooling needs both. A global block keeps shared content consistent. An editable instance lets a writer adapt a pattern (a callout, a pull quote, a stat highlight) to a single piece without leaving the post or creating a separate Object to link to. On the developer side, rich-text was already stored as portable Markdown with tokens you resolve at render time. The missing piece for non-React teams was a simple way to get an HTML string. renderToHtml closes that gap while keeping the same control-first model: you decide the markup for every block and embed. How It Works In the editor, insert a block from the / slash menu as usual. To customize a single instance, click Edit on page on the block. It detaches from the saved block and becomes editable right there in your content. Synced instances keep tracking the saved block. To undo a detach, click Reset to synced and confirm. For non-React front ends, render the value to an HTML string: import { createBucketClient } from ' @cosmicjs/sdk ' import { renderToHtml } from ' @cosmicjs/rich-text/html ' const cosmic = createBucketClient ({ bucketSlug : ' your-bucket ' , readKey : ' your-read-key ' , }) const { object } = await cosmic . objects . findOne ({ type : ' posts ' , slug : ' hello-world ' }) . props ( ' slug,title,metadata ' ) const { blocks } = await cosmic . blocks . find () // A single HTML string, blocks and prose resolved const html = renderToHtml ( object . metadata . content , { blocks }) You can customize the markup for each block with blockWrapper , and resolve inline Object embeds to your own HTML with resolveObjectHtml . React apps keep using the RichText component and renderRichText as before. Packages & Resources @cosmicjs/rich-text (v0.2.0): adds the framework-agnostic renderToHtml renderer via the new @cosmicjs/rich-text/html entry point (no React dependency), and renders editable, per-instance blocks. Docs : Rich text and blocks, including the new "Render to an HTML string (no React)" section. Read the full post on the Cosmic blog .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tonyspiro/rich-text-edit-blocks-on-the-page-plus-framework-agnostic-rendering-4dlk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
