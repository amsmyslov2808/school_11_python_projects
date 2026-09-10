from product import Product
from console_helper import *

from buyer_menu import *
from administrator_menu import *
from main_menu import *

# Один общий список передаётся во все меню и хранит текущее состояние магазина.
products: list[Product] = []

# Главный цикл работает до выбора пункта «Выход».
is_run = True

while is_run == True:
    # Перед меню всегда показываем актуальные остатки товаров.
    print_products(products)

    print_main_menu()
    choosen_action = input_int("Выберите пункт меню: ", 0, 2)

    # Передаём управление выбранному разделу программы.
    if choosen_action == 1:
        work_with_buyer_menu(products)
    elif choosen_action == 2:
        # Меню администратора доступно только после проверки пароля.
        if auth_is_administrator() == True:
            print("Пароль успешно введён")
            work_with_administrator_menu(products)
        else:
            print("Ошибка ввода пароля администратора")
    elif choosen_action == 0:
        # Изменение флага завершает главный цикл.
        is_run = False
