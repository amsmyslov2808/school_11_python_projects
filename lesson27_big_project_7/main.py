from product import Product
from console_helper import *

from buyer_menu import *
from administrator_menu import *
from main_menu import *

products: list[Product] = []

is_run = True

while is_run == True:
    print_products(products)

    print_main_menu()
    choosen_action = input_int("Выберите пункт меню: ", 0, 2)

    if choosen_action == 1:
        work_with_buyer_menu(products)
    elif choosen_action == 2:

        if auth_is_administrator() == True:
            print("Пароль успешно введён")
            work_with_administrator_menu(products)
        else:
            print("Ошибка ввода пароля администратора")
    elif choosen_action == 0:
        is_run = False
