from product import Product
from console_helper import *
from products_functions import *


def print_products(products: list[Product]):
    print("Список товаров магазина NeDikayaMalina")
    print_all_products(products)
    print_devider("=", 125)


def print_main_menu():
    print("Главное меню:")
    print("1. Меню Покупателя")
    print("2. Меню Администратора")
    print("0. Выход")
