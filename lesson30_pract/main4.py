import requests
from bs4 import BeautifulSoup


# Загружает результаты поиска кукол и возвращает названия найденных товаров.
def get_dolls():
    # User-Agent представляет запрос как запрос от браузера.
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
        "https://market.yandex.ru/search?text=кукла",
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")

    # Находим карточки товаров по служебному атрибуту HTML.
    dolls = html_page.find_all(
        "article",
        attrs={"data-autotest-id": "product-snippet"},
    )

    clear_dolls = []

    for doll in dolls:
        # Из каждой карточки берём только заголовок товара.
        title = doll.find("h3")

        clear_dolls.append(title.get_text())

    return clear_dolls


# Запускаем сбор данных и выводим результат в консоль.
dolls = get_dolls()
print(dolls)
