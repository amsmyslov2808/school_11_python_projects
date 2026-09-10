from product import Product
from console_helper import *
from products_functions import *


def work_with_sort_products_sub_menu(products: list[Product]):

    print("Меню Сортировки:")
    print("1. По возрастанию цены")
    print("2. По убыванию цены")
    print("3. По возрастанию рейтинга")
    print("4. По убыванию рейтинга")
    print("5. По возрастанию даты выпуска")
    print("6. По убыванию даты выпуска")
    print("7. По возрастанию ID")
    print("8. По убыванию ID")

    choosen_action = input_int("Выберите пункт меню: ", 1, 8)

    if choosen_action == 1:
        sort_products_by_type_sort(products, lambda product: product.price)
    elif choosen_action == 2:
        sort_products_by_type_sort(products, lambda product: product.price, True)
    elif choosen_action == 3:
        sort_products_by_type_sort(products, lambda product: product.rating)
    elif choosen_action == 4:
        sort_products_by_type_sort(products, lambda product: product.rating, True)
    elif choosen_action == 5:
        sort_products_by_type_sort(products, lambda product: product.release_date)
    elif choosen_action == 6:
        sort_products_by_type_sort(products, lambda product: product.release_date, True)
    elif choosen_action == 7:
        sort_products_by_type_sort(products, lambda product: product.id)
    elif choosen_action == 8:
        sort_products_by_type_sort(products, lambda product: product.id, True)


def work_with_find_products_sub_menu(products: list[Product]):

    print("Меню Поиска:")
    print("1. По имени")
    print("2. По категории")
    print("3. По диапазону цены")

    choosen_action = input_int("Выберите пункт меню: ", 1, 3)

    finded_products = []

    if choosen_action == 1:
        name = input_str(
            "Введите название товара для поиска (от 1 до 25 символов): ", 1, 25
        )

        finded_products = find_products_by_type_search(
            products, lambda product: name.lower() in product.name.lower()
        )

    elif choosen_action == 2:
        category = input_str(
            "Введите категорию товара для поиска (от 1 до 20 символов): ", 1, 20
        )

        finded_products = find_products_by_type_search(
            products, lambda product: category.lower() in product.category.lower()
        )
    elif choosen_action == 3:
        min_price = input_int(
            "Введите минимальную цену товара для поиска (от 1 до 10 000 000 руб.): ",
            1,
            10_000_000,
        )

        max_price = input_int(
            f"Введите максимальную цену товара для поиска (от {min_price} до 10 000 000 руб.): ",
            min_price,
            10_000_000,
        )

        finded_products = find_products_by_type_search(
            products,
            lambda product: product.price >= min_price and product.price <= max_price,
        )

    print("Найденные товары")
    if len(finded_products) > 0:
        print_all_products(finded_products)
    else:
        print("Товары не найдены")


def work_with_buyer_menu(products: list[Product]):

    is_run = True
    while is_run == True:
        print("Меню Покупателя:")
        print("1. Найти товар по ID")
        print("2. Сортировать товары")
        print("3. Найти товары")
        print("4. Купить товар")
        print("5. Сохранить товары в текстовый файл для печати")
        print("0. В Главное меню")

        choosen_action = input_int("Выберите пункт меню: ", 0, 5)

        if choosen_action == 1:
            search_id = input_int("Введите ID товара для поиска: ", 1, 2_000_000_000)
            found_product = get_product_by_id(products, search_id)

            if found_product == None:
                print(f"Продукт с ID {search_id} не найден")
            else:
                print_table_products_header()
                print_single_product(found_product)
        elif choosen_action == 2:
            work_with_sort_products_sub_menu(products)
        elif choosen_action == 3:
            work_with_find_products_sub_menu(products)
        elif choosen_action == 4:
            search_id = input_int("Введите ID товара для покупки: ", 1, 2_000_000_000)
            request_amount = input_int(
                "Введите количество товара для покупки: ", 1, 10_000
            )
            is_bought = buy_product(products, search_id, request_amount)

            if is_bought == False:
                print(
                    "Ошибка покупки товара проверьте что Вы ввели верный ID товара и товара достаточно на складе"
                )
            else:
                print("Товар успешно куплен")
        elif choosen_action == 5:
            filename = input_str("Введите имя файла для сохранения: ", 4, 100)

            is_saved = save_products_to_txt_file_for_print(products, filename)

            if is_saved == False:
                print("Ошибка сохранения файла")
            else:
                print("Файл успешно сохранён")
        elif choosen_action == 0:
            is_run = False

        wait_enter()
