from datetime import datetime

from src.parser.cleaner import clean_html
from src.utils.slug import create_slug


BAD_PATTERNS = [
    "<think>",
    "</think>",
    "the user wants me to",
    "let me think",
    "i need to rewrite",
    "complete rewrite",
    "first person",
    "minimum 1500 words"
]


def is_garbage(title, summary):

    text = (
        title + " " + summary
    ).lower()

    return any(
        pattern in text
        for pattern in BAD_PATTERNS
    )


def extract_article(entry, source_name):

    title = getattr(entry, "title", "")
    link = getattr(entry, "link", "")
    published = getattr(entry, "published", "")
    summary = getattr(entry, "summary", "")
    author = getattr(entry, "author", "Unknown")

    clean_summary = clean_html(summary)

    if is_garbage(
        title,
        clean_summary
    ):
        return None

    return {
        "title": title,
        "slug": create_slug(title),
        "link": link,
        "author": author,
        "source": source_name,
        "published": published,
        "summary": clean_summary,
        "fetched_at": datetime.utcnow().isoformat()
    }
