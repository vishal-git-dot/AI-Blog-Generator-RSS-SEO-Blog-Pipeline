from src.seo.keywords import (
    generate_keywords
)


def generate_description(text):

    text = text.strip()

    if len(text) <= 160:
        return text

    return text[:157] + "..."


def build_seo_data(article):

    content = article["summary"]

    keywords = generate_keywords(
        article["title"] + " " + content
    )

    return {

        "keywords": keywords,

        "description":
        generate_description(
            content
        )
    }