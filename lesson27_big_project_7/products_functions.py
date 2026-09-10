from product import Product
from datetime import date, datetime
from console_helper import *

SEARCH_BY_PART_NAME = 1
SEARCH_BY_CATEGORY = 2
SEARCH_BY_PRICE = 3


# Храним последний выданный ID, чтобы новые товары не получали уже занятые ID.
global_product_id = 0


def set_start_product_id(product_id: int):
    # После загрузки продолжаем нумерацию с сохранённого значения.
    global global_product_id
    global_product_id = product_id


def get_next_product_id() -> int:
    # Увеличиваем счётчик перед выдачей очередного ID.
    global global_product_id

    global_product_id += 1

    return global_product_id


def input_product_data() -> Product:
    # Последовательно считываем и проверяем все пользовательские поля товара.
    icon = input_str("Вставьте иконку товара (одно эмодзи): ", 1, 10)
    release_date = input_date(
        "Введите дату производства в формет ДД.ММ.ГГГГ: ",
        date(2026, 1, 1),
        date.today(),
    )
    name = input_str("Введите название товара (от 1 до 25 символов): ", 1, 25)
    category = input_str("Введите категорию товара (от 1 до 20 символов): ", 1, 20)
    price = input_int("Введите цену товара (от 1 до 10 000 000 руб.): ", 1, 10_000_000)
    rating = input_float("Введите рейтинг товара (от 1 до 5, можно дробный): ", 1, 5)
    amount = input_int(
        "Введите количество товара на складе (от 1 до 10 000 ед.): ", 1, 10_000
    )

    # ID здесь не задаётся: его назначает код добавления товара в каталог.
    return Product(
        icon=icon,
        release_date=release_date,
        name=name,
        category=category,
        price=price,
        rating=rating,
        amount=amount,
    )


def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
    # Последовательно просматриваем товары до первого совпадения ID.
    for product in products:
        if product.id == search_id:
            # Возвращаем сам объект, чтобы вызывающий код мог его изменить.
            return product

    # Отсутствие результата обозначаем значением None.
    return None


def add_product_to_list(products: list[Product], product: Product):
    # Добавляем переданный объект в конец общего каталога.
    products.append(product)


def update_product_by_id(products: list[Product], product: Product) -> bool:
    # Ищем существующий объект по ID новой версии товара.
    find_product = get_product_by_id(products, product.id)

    # Нельзя обновить товар, которого нет в каталоге.
    if find_product == None:
        return False

    # Меняем поля найденного объекта, сохраняя его место в списке.
    find_product.icon = product.icon
    find_product.release_date = product.release_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    find_product.amount = product.amount

    # Сообщаем вызывающему коду об успешном обновлении.
    return True


def delete_product_by_id(products: list[Product], search_id: int) -> bool:
    # Сначала получаем объект, который соответствует переданному ID.
    find_product = get_product_by_id(products, search_id)

    # Возвращаем False, если товар с таким ID отсутствует.
    if find_product == None:
        return False

    # Удаляем найденный объект из исходного списка.
    products.remove(find_product)

    return True


def print_table_products_header():
    # Фиксированная ширина полей выравнивает названия столбцов таблицы.
    print(
        f"{'ИД':<5}"
        f"{'Иконка':<15}"
        f"{'Дата выпуска':<20}"
        f"{'Название':<35}"
        f"{'Категория':<20}"
        f"{'Цена(руб.)':<12}"
        f"{'Рейтинг':<10}"
        f"{'Количество':<12}"
    )


def print_single_product(product: Product):
    # Значения используют ту же ширину, что и соответствующие заголовки.
    print(
        f"{product.id:<5}"
        f"{product.icon:<15}"
        f"{product.convert_date_to_str():<20}"
        f"{product.name:<35}"
        f"{product.category:<20}"
        f"{product.price:<12}"
        f"{product.rating:<10}"
        f"{product.amount:<12}"
    )


def print_all_products(products: list[Product]):
    # Заголовок нужен как для заполненной, так и для пустой таблицы.
    print_table_products_header()

    # Печатаем товары построчно либо сообщаем, что каталог пуст.
    if len(products) > 0:
        for product in products:
            print_single_product(product)
    else:
        print("Список товаров пуст")


def sort_products_by_type_sort(products: list[Product], action, is_reverse=False):
    # sort меняет исходный список, поэтому новый список возвращать не нужно.
    products.sort(key=action, reverse=is_reverse)


def find_products_by_type_search(products: list[Product], func_filter) -> list[Product]:
    # В новый список попадают только товары, прошедшие переданную проверку.
    return [product for product in products if func_filter(product) == True]


def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:
    # Ищем товар, остаток которого требуется уменьшить.
    find_product = get_product_by_id(products, search_id)

    # Покупка невозможна, если указан неизвестный ID.
    if find_product == None:
        return False

    # Не разрешаем купить больше единиц, чем имеется на складе.
    if find_product.amount < request_amount:
        return False

    # Списываем купленное количество с текущего остатка.
    find_product.amount -= request_amount

    return True


def load_products_from_txt_file(filename: str) -> list[Product]:
    # Любая ошибка чтения или разбора файла считается ошибкой загрузки.
    try:
        # UTF-8 нужен для корректного чтения русских названий и эмодзи.
        with open(filename, "r", encoding="utf-8") as file_in:
            # Формируем новый каталог независимо от текущего списка товаров.
            products = []

            # Первые две строки файла: число товаров и последний выданный ID.
            count_products = int(file_in.readline())
            set_start_product_id(int(file_in.readline()))

            for _ in range(count_products):
                # Каждый товар занимает в файле восемь строк в порядке полей Product.
                products.append(
                    Product(
                        id=int(file_in.readline()),
                        icon=file_in.readline().strip(),
                        release_date=datetime.strptime(
                            file_in.readline().strip(), "%d.%m.%Y"
                        ).date(),
                        name=file_in.readline().strip(),
                        category=file_in.readline().strip(),
                        price=int(file_in.readline()),
                        rating=float(file_in.readline()),
                        amount=int(file_in.readline()),
                    )
                )

            # Возвращаем полностью восстановленный список товаров.
            return products
    except:
        # None позволяет меню отличить ошибку от успешно загруженного пустого списка.
        return None


def save_products_to_txt_file(products: list[Product], filename: str) -> bool:
    # Сохраняем данные в служебном формате с возможностью последующей загрузки.
    try:
        # Режим w создаёт новый файл или заменяет содержимое существующего.
        with open(filename, "w", encoding="utf-8") as file_out:
            # Служебные строки нужны, чтобы загрузчик восстановил список и счётчик ID.
            file_out.write(f"{len(products)}\n")
            file_out.write(f"{global_product_id}\n")

            # Поля каждого товара записываются по одному на строку.
            for product in products:
                file_out.write(
                    f"{product.id}\n"
                    f"{product.icon}\n"
                    f"{product.convert_date_to_str()}\n"
                    f"{product.name}\n"
                    f"{product.category}\n"
                    f"{product.price}\n"
                    f"{product.rating}\n"
                    f"{product.amount}\n"
                )

        # Успешное завершение блока with означает, что файл записан и закрыт.
        return True
    except:
        # Меню получит False и покажет пользователю сообщение об ошибке.
        return False


def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:
    # Создаём человекочитаемый отчёт, не предназначенный для обратной загрузки.
    try:
        with open(filename, "w", encoding="utf-8") as file_out:
            # Сначала записываем название отчёта и заголовки таблицы.
            file_out.write("Список товаров магазина NeDikayaMalina\n\n")

            file_out.write(
                f"{'ИД':<5}"
                f"{'Иконка':<15}"
                f"{'Дата выпуска':<20}"
                f"{'Название':<35}"
                f"{'Категория':<20}"
                f"{'Цена(руб.)':<12}"
                f"{'Рейтинг':<10}"
                f"{'Количество':<12}"
                "\n"
            )

            # Каждый товар занимает одну выровненную строку таблицы.
            if len(products) > 0:
                for product in products:
                    file_out.write(
                        f"{product.id:<5}"
                        f"{product.icon:<15}"
                        f"{product.convert_date_to_str():<20}"
                        f"{product.name:<35}"
                        f"{product.category:<20}"
                        f"{product.price:<12}"
                        f"{product.rating:<10}"
                        f"{product.amount:<12}"
                        "\n"
                    )
            else:
                # Пустой каталог явно отмечаем в итоговом файле.
                file_out.write("Список товаров пуст")

        # Сообщаем меню, что отчёт успешно записан.
        return True
    except:
        # Ошибки создания или записи файла превращаем в понятный результат False.
        return False
