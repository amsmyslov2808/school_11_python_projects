import requests
from bs4 import BeautifulSoup


def get_dolls():
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(
        "https://market.yandex.ru/search?text=кукла",
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")

    dolls = html_page.find_all(
        "article",
        attrs={"data-autotest-id": "product-snippet"},
    )

    clear_dolls = []

    for doll in dolls:
        title = doll.find("h3")

        clear_dolls.append(title.get_text())

    return clear_dolls


dolls = get_dolls()
print(dolls)
