from pathlib import Path
import json


POST_DIR = Path(
    "posts/generated"
)


def parse_frontmatter(content):

    if not content.startswith("---"):
        return {}

    parts = content.split("---")

    if len(parts) < 3:
        return {}

    meta_lines = parts[1].splitlines()

    metadata = {}

    for line in meta_lines:

        if ":" not in line:
            continue

        key, value = line.split(
            ":",
            1
        )

        metadata[
            key.strip()
        ] = value.strip().replace(
            '"',
            ''
        )

    return metadata


def build_post_index():

    posts = []

    if not POST_DIR.exists():
        return posts

    for file in POST_DIR.glob(
        "*.md"
    ):

        content = file.read_text(
            encoding="utf-8"
        )

        metadata = parse_frontmatter(
            content
        )

        metadata["file"] = (
            file.name
        )

        posts.append(
            metadata
        )

    return posts


def save_post_index():

    posts = build_post_index()

    with open(
        "website/data/posts.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            posts,
            file,
            indent=4,
            ensure_ascii=False
        )

    return len(posts)