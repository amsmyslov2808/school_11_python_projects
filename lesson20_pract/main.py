from car import Car
from cars_functions import *

cars: list[Car] = []

fill_cars_mock_data(cars)

is_run = True

while is_run == True:

    print("Меню:")
    print("1. Вывести машину по ИД")
    print("2. Добавить новую машину")
    print("3. Обновить машину по ИД")
    print("4. Удалить машину по ИД")
    print("0. Выйти из программы")

    choose_action = int(input("Введите номер выбранного пункта меню: "))

    if choose_action == 1:
        pass
    elif choose_action == 2:
        pass
    elif choose_action == 3:
        pass
    elif choose_action == 4:
        pass
    elif choose_action == 0:
        is_run = False

    print("=" * 50)
    input("Для продолжения нажмите <Enter>")
    print("\n" * 10)
