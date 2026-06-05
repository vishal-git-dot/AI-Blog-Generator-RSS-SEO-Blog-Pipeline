from src.rss.feeds import load_feed_config
from src.rss.fetcher import fetch_feed
from src.parser.extractor import extract_article

from src.utils.logger import log


def collect_articles():

    config = load_feed_config()

    feeds = config["feeds"]

    settings = config["settings"]

    max_per_feed = settings[
        "max_articles_per_feed"
    ]

    all_articles = []

    seen_links = set()

    for feed in feeds:

        feed_name = feed["name"]

        feed_url = feed["url"]

        log(
            f"Fetching {feed_name}"
        )

        entries = fetch_feed(
            feed_url
        )

        count = 0

        for entry in entries:

            if count >= max_per_feed:
                break

            article = extract_article(
                entry,
                feed_name
            )

            if not article["title"]:
                continue

            if article["link"] in seen_links:
                continue

            seen_links.add(
                article["link"]
            )

            all_articles.append(
                article
            )

            count += 1

    limit = settings[
        "max_total_articles"
    ]

    return all_articles[:limit]