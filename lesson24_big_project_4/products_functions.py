# Импортируем описание товара, инструменты дат и функции безопасного ввода.
from product import Product
from datetime import date
from console_helper import *

# Это общий счётчик выданных ID. Сначала ещё не создано ни одного товара.
global_product_id = 0


def get_next_product_id() -> int:
    """Увеличивает общий счётчик и возвращает новый уникальный ID."""
    # global сообщает Python, что мы изменяем переменную за пределами функции.
    global global_product_id

    # Каждый новый номер на один больше предыдущего: 1, 2, 3 и так далее.
    global_product_id += 1

    return global_product_id


def input_product_data() -> Product:
    """Собирает данные о товаре из консоли и создаёт объект Product."""
    # Каждая функция ввода сама повторяет вопрос, пока ответ не пройдёт проверку.
    icon = input_str("Вставьте иконку товара: ", 1, 1)
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
    # Собираем отдельные ответы в одну карточку товара.
    # ID здесь не задаётся: у нового объекта он пока будет равен None.
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
    """Ищет товар по ID; возвращает товар или None, если совпадения нет."""
    # Перебираем карточки по очереди, словно просматриваем строки таблицы.
    for product in products:
        if product.id == search_id:
            # Совпадение найдено — дальше искать уже не нужно.
            return product

    # Цикл закончился без совпадения.
    return None


def add_product_to_list(products: list[Product], product: Product):
    """Добавляет карточку товара в конец списка."""
    products.append(product)


def update_product_by_id(products: list[Product], product: Product) -> bool:
    """Заменяет данные товара с таким же ID и сообщает, получилось ли это."""
    find_product = get_product_by_id(products, product.id)

    # None означает, что обновлять нечего.
    if find_product == None:
        return False

    # Обновляем поля найденной карточки, но сохраняем её прежний ID.
    find_product.icon = product.icon
    find_product.release_date = product.release_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    find_product.amount = product.amount

    # True — условный ответ «операция прошла успешно».
    return True


def delete_product_by_id(products: list[Product], search_id: int) -> bool:
    """Удаляет товар с нужным ID и возвращает результат операции."""
    find_product = get_product_by_id(products, search_id)

    if find_product == None:
        return False

    # remove() удаляет из списка именно найденный объект.
    products.remove(find_product)

    return True


def print_table_products_header():
    """Печатает названия столбцов таблицы товаров."""
    # В записи :<5 число задаёт ширину столбца, а знак < выравнивает текст влево.
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
    """Печатает одну карточку товара как строку таблицы."""
    # Одинаковая ширина полей помогает значениям стоять под своими заголовками.
    print(
        f"{product.id:<5}"
        f"{product.icon:<15}"
        f"{product.release_date_to_str():<20}"
        f"{product.name:<35}"
        f"{product.category:<20}"
        f"{product.price:<12}"
        f"{product.rating:<10}"
        f"{product.amount:<12}"
    )


def print_all_products(products: list[Product]):
    """Печатает заголовок и все товары либо сообщение о пустом списке."""
    print_table_products_header()

    # Если длина больше нуля, в списке есть хотя бы один товар.
    if len(products) > 0:
        for product in products:
            print_single_product(product)
    else:
        print("Список товаров пуст")


def sort_products_by_type_sort(products: list[Product], type_sort: int):
    """В будущем будет сортировать товары выбранным способом."""
    # pass — временная заглушка: Python ничего не делает и идёт дальше.
    pass


def find_products_by_type_parameter(
    products: list[Product], type_parameter: int, parameter: str
) -> list[Product]:
    """В будущем будет находить товары по выбранному параметру."""
    pass


def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:
    """В будущем будет оформлять покупку указанного количества товара."""
    pass


def load_products_from_txt_file(filename: str) -> list[Product]:
    """В будущем будет загружать список товаров из текстового файла."""
    pass


def save_products_to_txt_file(products: list[Product], filename: str) -> bool:
    """В будущем будет сохранять товары в текстовый файл."""
    pass


def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:
    """В будущем будет сохранять товары в удобном для печати виде."""
    pass
