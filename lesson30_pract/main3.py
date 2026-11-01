import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass


# Одна запись связывает текст цитаты с её автором.
@dataclass
class Quote:
    text: str
    author: str


# Извлекает текст и автора из каждой карточки цитаты и возвращает список Quote.
def get_quotes():
    # Загружаем HTML и останавливаемся, если сервер вернул ошибку HTTP.
    response = requests.get("https://quotes.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")

    # Каждый блок quote содержит и текст, и автора одной цитаты.
    quotes = html_page.find_all("div", class_="quote")

    clear_quotes = []

    # Ищем внутри отдельной карточки, чтобы не перепутать авторов.
    for quote in quotes:
        # Удаляем разметку и внешние кавычки из текста цитаты.
        text = (
            quote.find("span", class_="text")
            .get_text()
            .replace("“", "")
            .replace("”", "")
        )

        author = quote.find("small", class_="author").get_text()

        clear_quotes.append(Quote(text, author))

    return clear_quotes


# Запускаем сбор данных и выводим результат в консоль.
quotes = get_quotes()
print(quotes)
