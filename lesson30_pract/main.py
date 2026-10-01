import requests
from bs4 import BeautifulSoup


def get_quotes():
    response = requests.get("https://quotes.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")
    quotes = html_page.find_all("span", class_="text")

    clear_quotes = [
        quote.get_text().replace("“", "").replace("”", "") for quote in quotes
    ]

    return clear_quotes


quotes = get_quotes()
print(quotes)
