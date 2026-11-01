from dataclasses import dataclass
import requests


# Храним только те поля персонажа, которые нужны для вывода.
@dataclass
class Character:
    name: str
    status: str
    species: str
    gender: str
    origin_name: str
    image: str


# Словари переводят значения API на русский язык.
STATUS_RU = {
    "Alive": "Живой",
    "Dead": "Мёртвый",
    "unknown": "Неизвестно",
}

SPECIES_RU = {
    "Human": "Человек",
    "Alien": "Пришелец",
    "Humanoid": "Гуманоид",
    "Robot": "Робот",
    "Animal": "Животное",
    "Mythological Creature": "Мифическое существо",
    "Poopybutthole": "Пупибатхол",
    "Cronenberg": "Кроненберг",
    "Disease": "Болезнь",
    "unknown": "Неизвестно",
}

GENDER_RU = {
    "Male": "Мужской",
    "Female": "Женский",
    "Genderless": "Бесполый",
    "unknown": "Неизвестно",
}


# Запрашивает персонажа по ID и возвращает его данные в объекте Character.
def get_character_info_by_id(character_id: int) -> Character:

    url = f"https://rickandmortyapi.com/api/character/{character_id}"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    # Превращаем JSON-ответ в словарь Python.
    data = response.json()

    # Родной мир находится во вложенном объекте origin.
    return Character(
        name=data["name"],
        status=data["status"],
        species=data["species"],
        gender=data["gender"],
        origin_name=data["origin"]["name"],
        image=data["image"],
    )


# Формирует описание персонажа, переводя статус, вид и пол на русский язык.
def character_to_pritty_str(character: Character) -> str:
    # Если перевода нет, оставляем исходное значение из API.
    status_ru = STATUS_RU.get(character.status, character.status)
    species_ru = SPECIES_RU.get(character.species, character.species)
    gender_ru = GENDER_RU.get(character.gender, character.gender)

    return (
        f"Имя: {character.name}\n"
        f"Статус: {status_ru}\n"
        f"Вид: {species_ru}\n"
        f"Пол: {gender_ru}\n"
        f"Родной мир: {character.origin_name}\n"
        f"Изображение: {character.image}"
    )


# После каждого вывода снова запрашиваем ID следующего персонажа.
while True:
    character_id = int(input("введите ИД персонажа мульта Рик и Морти от 1 до 826: "))

    print()
    print(character_to_pritty_str(get_character_info_by_id(character_id)))
    print("\n\n")
