from dataclasses import dataclass
import requests


@dataclass
class Character:
    name: str
    status: str
    species: str
    gender: str
    origin_name: str
    image: str


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


def get_character_info_by_id(character_id: int) -> Character:

    url = f"https://rickandmortyapi.com/api/character/{character_id}"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    return Character(
        name=data["name"],
        status=data["status"],
        species=data["species"],
        gender=data["gender"],
        origin_name=data["origin"]["name"],
        image=data["image"],
    )


def character_to_pritty_str(character: Character) -> str:
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


while True:
    character_id = int(input("введите ИД персонажа мульта Рик и Морти от 1 до 826: "))

    print()
    print(character_to_pritty_str(get_character_info_by_id(character_id)))
    print("\n\n")
