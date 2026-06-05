import sys
from pathlib import Path

# ==================================================
# Add repository root to Python path
# ==================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ==================================================
# Imports
# ==================================================

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

# ==================================================
# Setup Directories
# ==================================================

def setup_directories():

    directories = [
        "posts",
        "posts/generated",
        "website",
        "website/data",
        "logs"
    ]

    for directory in directories:
        ensure_directory(directory)

# ==================================================
# Main Pipeline
# ==================================================

def main():

    log("Starting RSS Blog Pipeline...")

    setup_directories()

    try:

        articles = collect_articles()

        write_json(
            "website/data/raw_articles.json",
            articles
        )

        log(
            f"Collected {len(articles)} articles"
        )

    except Exception as error:

        log(
            f"RSS collection failed: {error}"
        )

        raise

    generated = 0

    for article in articles:

        try:

            save_markdown(article)

            generated += 1

        except Exception as error:

            log(
                f"Failed to generate article: "
                f"{article.get('title', 'Unknown')}"
            )

            log(str(error))

    indexed = save_post_index()

    log(
        f"Generated {generated} markdown posts"
    )

    log(
        f"Indexed {indexed} posts"
    )

    log(
        "Pipeline completed successfully"
    )

# ==================================================
# Entry Point
# ==================================================

if __name__ == "__main__":
    main()
