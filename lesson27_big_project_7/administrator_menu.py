from product import Product
from console_helper import *
from products_functions import *


def auth_is_administrator():

    password = input_str(
        "Введите пароль Администратора для входа в Меню Администратора: ", 4, 16
    )
    return password == "12345"


def work_with_administrator_menu(products: list[Product]):

    is_run = True
    while is_run == True:
        print("Меню Администратора:")
        print("1. Найти товар по ID")
        print("2. Добавить новый товар")
        print("3. Изменить товар по ID")
        print("4. Удалить товар по ID")
        print("5. Загрузить товары из текстового файла")
        print("6. Сохранить товары в текстовый файл")
        print("7. Сохранить товары в текстовый файл для печати")
        print("0. В Главное меню")

        choosen_action = input_int("Выберите пункт меню: ", 0, 7)

        if choosen_action == 1:
            search_id = input_int("Введите ID товара для поиска: ", 1, 2_000_000_000)
            found_product = get_product_by_id(products, search_id)

            if found_product == None:
                print(f"Продукт с ID {search_id} не найден")
            else:
                print_table_products_header()
                print_single_product(found_product)
        elif choosen_action == 2:

            print("Введите данные нового продукта")

            new_product = input_product_data()

            new_product.id = get_next_product_id()

            add_product_to_list(products, new_product)

            print("Товар успешно добавлен")
        elif choosen_action == 3:

            update_id = input_int(
                "Введите ID товара для обновления: ", 1, 2_000_000_000
            )
            found_product = get_product_by_id(products, update_id)

            if found_product == None:
                print(f"Продукт с ID {update_id} не найден")
            else:

                print("Введите новые данные для продукта ")

                update_product = input_product_data()

                update_product.id = update_id

                update_product_by_id(products, update_product)

                print("Продукт успешно обновлён")

        elif choosen_action == 4:

            delete_id = input_int("Введите ID товара для удаления: ", 1, 2_000_000_000)

            is_deleted = delete_product_by_id(products, delete_id)

            if is_deleted == False:
                print(f"Продукт с ID {delete_id} не найден")
            else:
                print("Продукт успешно удалён")
        elif choosen_action == 5:

            filename = input_str("Введите имя файла для загрузки: ", 4, 100)

            load_products = load_products_from_txt_file(filename)

            if load_products == None:
                print("Ошибка загрузки файла")
            else:
                products.clear()
                products.extend(load_products)

                print("Файл успешно загружен")

        elif choosen_action == 6:

            filename = input_str("Введите имя файла для сохранения: ", 4, 100)

            is_saved = save_products_to_txt_file(products, filename)

            if is_saved == False:
                print("Ошибка сохранения файла")
            else:
                print("Файл успешно сохранён")
        elif choosen_action == 7:

            filename = input_str("Введите имя файла для сохранения: ", 4, 100)

            is_saved = save_products_to_txt_file_for_print(products, filename)

            if is_saved == False:
                print("Ошибка сохранения файла")
            else:
                print("Файл успешно сохранён")

        elif choosen_action == 0:

            is_run = False

        wait_enter()
