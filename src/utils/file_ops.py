import json
from pathlib import Path


def ensure_directory(path: str):

    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


def write_file(path: str, content: str):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


def read_json(path: str):

    if not Path(path).exists():
        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def write_json(path: str, data):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )