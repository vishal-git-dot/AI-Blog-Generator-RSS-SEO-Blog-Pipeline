from pathlib import Path

from src.utils.logger import log

from src.utils.file_ops import (
    ensure_directory,
    write_json
)

from src.rss.aggregator import (
    collect_articles
)

from src.generator.markdown_builder import (
    save_markdown
)

from src.generator.post_index import (
    save_post_index
)


def setup_directories():

    directories = [

        "posts",

        "posts/generated",

        "website",

        "website/data",

        "logs"
    ]

    for directory in directories:

        ensure_directory(
            directory
        )


def main():

    log(
        "Starting pipeline..."
    )

    setup_directories()

    articles = collect_articles()

    write_json(
        "website/data/raw_articles.json",
        articles
    )

    generated = 0

    for article in articles:

        save_markdown(
            article
        )

        generated += 1

    indexed = save_post_index()

    Path(
        "website/data/posts.json"
    ).touch(
        exist_ok=True
    )

    log(
        f"Generated {generated} posts"
    )

    log(
        f"Indexed {indexed} posts"
    )

    log(
        "Phase 3 complete"
    )


if __name__ == "__main__":
    main()