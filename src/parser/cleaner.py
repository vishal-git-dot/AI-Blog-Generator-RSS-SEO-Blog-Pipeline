from bs4 import BeautifulSoup


def clean_html(content: str) -> str:

    if not content:
        return ""

    soup = BeautifulSoup(
        content,
        "html.parser"
    )

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    text = " ".join(
        text.split()
    )

    return text