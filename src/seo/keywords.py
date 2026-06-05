import re
from collections import Counter


STOP_WORDS = {
    "the", "a", "an", "and", "or", "to",
    "of", "for", "with", "in", "on",
    "is", "are", "was", "were", "be",
    "this", "that", "it", "as", "at",
    "by", "from", "into", "about"
}


def generate_keywords(text, limit=8):

    words = re.findall(
        r'\b[a-zA-Z]{3,}\b',
        text.lower()
    )

    words = [
        word
        for word in words
        if word not in STOP_WORDS
    ]

    counts = Counter(words)

    return [
        word
        for word, count in counts.most_common(limit)
    ]