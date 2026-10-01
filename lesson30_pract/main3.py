import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass


@dataclass
class Quote:
    text: str
    author: str


def get_quotes():
    response = requests.get("https://quotes.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")

    quotes = html_page.find_all("div", class_="quote")

    clear_quotes = []

    for quote in quotes:
        text = (
            quote.find("span", class_="text")
            .get_text()
            .replace("“", "")
            .replace("”", "")
        )

        author = quote.find("small", class_="author").get_text()

        clear_quotes.append(Quote(text, author))

    return clear_quotes


quotes = get_quotes()
print(quotes)
