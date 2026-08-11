from product import Product
from datetime import date
from console_helper import *
from products_functions import *

products: list[Product] = []

# Создаем список из 10 моковых продуктов с динамическим ID
mock_products = [
    Product(
        id=get_next_product_id(),
        icon="🧥",
        name="Куртка зимняя оверсайз",
        category="Одежда",
        price=4500,
        rating=4.7,
        amount=120,
        release_date=date(2025, 10, 15),
    ),
    Product(
        id=get_next_product_id(),
        icon="👟",
        name="Кроссовки спортивные",
        category="Обувь",
        price=3200,
        rating=4.5,
        amount=85,
        release_date=date(2026, 3, 20),
    ),
    Product(
        id=get_next_product_id(),
        icon="🎒",
        name="Рюкзак городской",
        category="Аксессуары",
        price=1800,
        rating=4.8,
        amount=200,
        release_date=date(2026, 1, 10),
    ),
    Product(
        id=get_next_product_id(),
        icon="💄",
        name="Матовая помада для губ",
        category="Косметика",
        price=450,
        rating=4.6,
        amount=450,
        release_date=date(2026, 5, 5),
    ),
    Product(
        id=get_next_product_id(),
        icon="🎧",
        name="Беспроводные наушники",
        category="Электроника",
        price=2900,
        rating=4.3,
        amount=60,
        release_date=date(2025, 12, 1),
    ),
    Product(
        id=get_next_product_id(),
        icon="🧴",
        name="Увлажняющий крем для лица",
        category="Косметика",
        price=650,
        rating=4.9,
        amount=310,
        release_date=date(2026, 4, 18),
    ),
    Product(
        id=get_next_product_id(),
        icon="🕯️",
        name="Свеча ароматическая",
        category="Дом и уют",
        price=550,
        rating=4.7,
        amount=140,
        release_date=date(2026, 6, 12),
    ),
    Product(
        id=get_next_product_id(),
        icon="📱",
        name="Чехол для смартфона",
        category="Электроника",
        price=350,
        rating=4.4,
        amount=500,
        release_date=date(2026, 7, 1),
    ),
    Product(
        id=get_next_product_id(),
        icon="👕",
        name="Футболка базовая хлопковая",
        category="Одежда",
        price=890,
        rating=4.8,
        amount=350,
        release_date=date(2026, 2, 28),
    ),
    Product(
        id=get_next_product_id(),
        icon="🥤",
        name="Термокружка из стали",
        category="Дом и уют",
        price=1100,
        rating=4.6,
        amount=95,
        release_date=date(2025, 11, 23),
    ),
]

# Добавляем все продукты в список
for prod in mock_products:
    add_product_to_list(products, prod)


def print_all_products():
    pass


def print_main_menu():

    pass


def work_with_buyer_menu():
    pass


def auth_is_administrator():
    pass


def work_with_administrator_menu():
    pass


is_run = True

while is_run == True:
    print_all_products()

    print_main_menu()
    choose_action_main_menu = input_int("Выберите пункт меню: ", 0, 5)

    if choose_action_main_menu == 1:
        work_with_buyer_menu()
    elif choose_action_main_menu == 2:
        if auth_is_administrator() == True:
            work_with_administrator_menu()
        else:
            print("Ошибка ввода пароля администратора")
    elif choose_action_main_menu == 0:
        is_run = False
