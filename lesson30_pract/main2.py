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

    quotes_text = html_page.find_all("span", class_="text")
    quotes_author = html_page.find_all("small", class_="author")

    count_quotes = len(quotes_text)

    clear_quotes = []

    for i in range(count_quotes):
        clear_quotes.append(
            Quote(
                quotes_text[i].get_text().replace("“", "").replace("”", ""),
                quotes_author[i].get_text(),
            )
        )

    return clear_quotes


quotes = get_quotes()
print(quotes)
