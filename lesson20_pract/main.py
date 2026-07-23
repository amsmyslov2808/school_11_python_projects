from car import Car
from cars_functions import *

cars: list[Car] = []

fill_cars_mock_data(cars)

is_run = True

while is_run == True:

    print("Список машин:")
    print_all_cars(cars)

    print("Меню:")
    print("1. Вывести машину по ИД")
    print("2. Добавить новую машину")
    print("3. Обновить машину по ИД")
    print("4. Удалить машину по ИД")
    print("0. Выйти из программы")

    choose_action = int(input("Введите номер выбранного пункта меню: "))

    if choose_action == 1:
        id = int(input("Введите ИД машины: "))

        found_car = get_car_by_id(cars, id)

        if found_car != None:
            print_one_car(found_car)
        else:
            print(f"Машина с ИД = {id} не найдена")
    elif choose_action == 2:
        new_car = input_car_data()
        new_car.id = get_next_car_id()

        add_new_car(cars, new_car)

        print("Машина успешно добавлена")
    elif choose_action == 3:
        id = int(input("Введите ИД машины: "))
        car = input_car_data()

        car.id = id

        is_updated = update_car_by_id(cars, car)

        if is_updated == True:
            print("Успешно обновлено")
        else:
            print(f"Машина с ИД = {id} не найдена")

    elif choose_action == 4:
        id = int(input("Введите ИД машины: "))

        is_deleted = delete_car_by_id(cars, id)

        if is_deleted == True:
            print("Успешно удалено")
        else:
            print(f"Машина с ИД = {id} не найдена")
    elif choose_action == 0:
        is_run = False

    print("." * 50)
    input("Для продолжения нажмите <Enter>")
    print("\n" * 10)
