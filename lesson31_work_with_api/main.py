import requests

from datetime import datetime

WEATHER_CODE_RU = {
    0: "Ясно",
    1: "Преимущественно ясно",
    2: "Переменная облачность",
    3: "Пасмурно",
    45: "Туман",
    48: "Изморозь",
    51: "Слабая морось",
    53: "Умеренная морось",
    55: "Сильная морось",
    56: "Слабая ледяная морось",
    57: "Сильная ледяная морось",
    61: "Слабый дождь",
    63: "Умеренный дождь",
    65: "Сильный дождь",
    66: "Слабый ледяной дождь",
    67: "Сильный ледяной дождь",
    71: "Слабый снегопад",
    73: "Умеренный снегопад",
    75: "Сильный снегопад",
    77: "Снежная крупа",
    80: "Слабые ливни",
    81: "Умеренные ливни",
    82: "Сильные ливни",
    85: "Слабые снежные ливни",
    86: "Сильные снежные ливни",
    95: "Гроза",
    96: "Гроза со слабым градом",
    97: "Сильная гроза",
    99: "Гроза с сильным градом",
}


def get_weather(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
        "timezone": "Europe/Moscow",
    }

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast", params=params, timeout=10
    )
    response.raise_for_status()

    data = response.json()
    return data["current"]


city = "Брянск"
latitude = 53.27096
longitude = 34.32143

city_weather = get_weather(latitude, longitude)


normalize_datetime = datetime.strptime(city_weather["time"], "%Y-%m-%dT%H:%M").strftime(
    "%d.%m.%Y"
)
temperature = city_weather["temperature_2m"]

weather_condition = WEATHER_CODE_RU[int(city_weather["weather_code"])]

print("Погода в городе:", city)

print(f"Время по Москве: {normalize_datetime}")

print(f"Температура: {temperature} °C")

print(f"Погодные условия: {weather_condition}")
