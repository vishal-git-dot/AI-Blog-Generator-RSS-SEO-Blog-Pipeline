import feedparser

from src.utils.logger import log


def fetch_feed(feed_url: str):

    try:

        parsed = feedparser.parse(feed_url)

        if parsed.bozo:
            log(
                f"Feed warning: {feed_url}"
            )

        return parsed.entries

    except Exception as error:

        log(
            f"Feed fetch failed: {feed_url}"
        )

        log(
            str(error)
        )

        return []