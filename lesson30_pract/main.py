import requests
from bs4 import BeautifulSoup


# Загружает первую страницу цитат и возвращает список их текстов без кавычек.
def get_quotes():
    response = requests.get("https://quotes.toscrape.com/", timeout=10)
    # При ошибке HTTP прерываем работу, чтобы не разбирать страницу ошибки.
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")
    # Выбираем только элементы с текстом цитат, без авторов и тегов.
    quotes = html_page.find_all("span", class_="text")

    # Извлекаем текст и убираем декоративные кавычки сайта.
    clear_quotes = [
        quote.get_text().replace("“", "").replace("”", "") for quote in quotes
    ]

    return clear_quotes


# Запускаем сбор данных и выводим результат в консоль.
quotes = get_quotes()
print(quotes)
