import requests
from bs4 import BeautifulSoup


# Возвращает полные названия книг с первой страницы каталога.
def get_titles():
    # Получаем HTML каталога и проверяем успешность запроса.
    response = requests.get("https://books.toscrape.com/", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")
    # Ограничиваем поиск карточками книг, исключая остальную страницу.
    books = html_page.find_all("article", class_="product_pod")

    books_titles = []

    for book in books:
        # В атрибуте title хранится полное название, даже если ссылка сокращена.
        title = book.find("h3").find("a")["title"]
        books_titles.append(title)

    return books_titles


# Запускаем сбор данных и выводим результат в консоль.
print(get_titles())
