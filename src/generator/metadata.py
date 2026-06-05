from datetime import datetime

from src.seo.optimizer import (
    build_seo_data
)


def create_metadata(article):

    seo = build_seo_data(
        article
    )

    return {

        "title":
        article["title"],

        "slug":
        article["slug"],

        "author":
        article["author"],

        "source":
        article["source"],

        "published":
        article["published"],

        "description":
        seo["description"],

        "keywords":
        seo["keywords"],

        "generated":
        datetime.utcnow().isoformat()
    }