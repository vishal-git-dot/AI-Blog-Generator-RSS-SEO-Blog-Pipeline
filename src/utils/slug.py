import re


def create_slug(text: str) -> str:

    text = text.lower()

    text = re.sub(
        r'[^a-z0-9\s-]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        '-',
        text
    )

    text = re.sub(
        r'-+',
        '-',
        text
    )

    return text.strip('-')