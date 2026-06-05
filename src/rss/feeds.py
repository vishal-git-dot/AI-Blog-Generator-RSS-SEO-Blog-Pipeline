from pathlib import Path
import yaml


CONFIG_PATH = Path("config/feeds.yml")


def load_feed_config():

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            "config/feeds.yml not found"
        )

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)