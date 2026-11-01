import requests
from dataclasses import dataclass
from datetime import datetime

EUR = "eur"
USD = "usd"


# Дата публикации и курс одной единицы валюты в рублях.
@dataclass
class RateData:
    date: str
    rate: float


# Получает курс выбранной валюты к рублю и возвращает его вместе с датой публикации.
def get_vatule_rub(valute: str):
    # Код валюты подставляется в адрес запроса, рубль — валюта результата.
    url = f"https://api.frankfurter.dev/v2/rate/{valute}/rub"

    response = requests.get(url, timeout=10)
    # Не продолжаем разбор данных, если сервер вернул ошибку HTTP.
    response.raise_for_status()

    data = response.json()

    # Приводим дату API к привычному формату день.месяц.год.
    return RateData(
        date=datetime.strptime(data["date"], "%Y-%m-%d").strftime("%d.%m.%Y"),
        rate=data["rate"],
    )
