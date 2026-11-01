import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass


# Объединяем текст и автора одной цитаты в отдельный объект.
@dataclass
class Quote:
    text: str
    author: str


# Собирает цитаты и авторов с первой страницы в список объектов Quote.
def get_quotes():
    # Загружаем HTML и останавливаемся, если сервер вернул ошибку HTTP.
    response = requests.get("https://quotes.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")

    # Списки текстов и авторов идут в том же порядке, что и на странице.
    quotes_text = html_page.find_all("span", class_="text")
    quotes_author = html_page.find_all("small", class_="author")

    count_quotes = len(quotes_text)

    clear_quotes = []

    # По одинаковому индексу связываем цитату с её автором.
    for i in range(count_quotes):
        clear_quotes.append(
            Quote(
                quotes_text[i].get_text().replace("“", "").replace("”", ""),
                quotes_author[i].get_text(),
            )
        )

    return clear_quotes


# Запускаем сбор данных и выводим результат в консоль.
quotes = get_quotes()
print(quotes)
