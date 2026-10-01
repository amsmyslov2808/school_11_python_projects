import requests
from bs4 import BeautifulSoup


def get_titles():
    response = requests.get("https://books.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")
    books = html_page.find_all("article", class_="product_pod")

    books_titles = []

    for book in books:
        title = book.find("h3").find("a")["title"]
        books_titles.append(title)

    return books_titles


print(get_titles())
