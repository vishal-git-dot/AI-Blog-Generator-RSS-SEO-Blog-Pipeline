from pathlib import Path

from src.generator.metadata import (
    create_metadata
)

from src.utils.file_ops import (
    ensure_directory
)


POST_DIR = Path(
    "posts/generated"
)


def build_markdown(article):

    metadata = create_metadata(
        article
    )

    keywords = ", ".join(
        metadata["keywords"]
    )

    markdown = f"""---
title: "{metadata['title']}"
slug: "{metadata['slug']}"
author: "{metadata['author']}"
source: "{metadata['source']}"
published: "{metadata['published']}"
description: "{metadata['description']}"
keywords: "{keywords}"
generated: "{metadata['generated']}"
---

# {metadata['title']}

## Overview

{article['summary']}

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

{article['link']}

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
"""

    return markdown


def save_markdown(article):

    ensure_directory(
        POST_DIR
    )

    content = build_markdown(
        article
    )

    path = POST_DIR / (
        article["slug"] + ".md"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return str(path)