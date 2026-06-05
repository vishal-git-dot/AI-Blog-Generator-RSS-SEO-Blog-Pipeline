from datetime import datetime

from src.parser.cleaner import clean_html
from src.utils.slug import create_slug


def extract_article(entry, source_name):

    title = getattr(
        entry,
        "title",
        ""
    )

    link = getattr(
        entry,
        "link",
        ""
    )

    published = getattr(
        entry,
        "published",
        ""
    )

    summary = getattr(
        entry,
        "summary",
        ""
    )

    author = getattr(
        entry,
        "author",
        "Unknown"
    )

    clean_summary = clean_html(
        summary
    )

    article = {

        "title": title,

        "slug": create_slug(
            title
        ),

        "link": link,

        "author": author,

        "source": source_name,

        "published": published,

        "summary": clean_summary,

        "fetched_at": datetime.utcnow().isoformat()
    }

    return article