from product import Product
from datetime import date
from console_helper import *

SEARCH_BY_PART_NAME = 1
SEARCH_BY_CATEGORY = 2
SEARCH_BY_PRICE = 3


global_product_id = 0


def set_start_product_id(product_id: int):

    global global_product_id
    global_product_id = product_id


def get_next_product_id() -> int:

    global global_product_id

    global_product_id += 1

    return global_product_id


def input_product_data() -> Product:

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

    for product in products:
        if product.id == search_id:

            return product

    return None


def add_product_to_list(products: list[Product], product: Product):

    products.append(product)


def update_product_by_id(products: list[Product], product: Product) -> bool:

    find_product = get_product_by_id(products, product.id)

    if find_product == None:
        return False

    find_product.icon = product.icon
    find_product.release_date = product.release_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    find_product.amount = product.amount

    return True


def delete_product_by_id(products: list[Product], search_id: int) -> bool:

    find_product = get_product_by_id(products, search_id)

    if find_product == None:
        return False

    products.remove(find_product)

    return True


def print_table_products_header():

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

    print_table_products_header()

    if len(products) > 0:
        for product in products:
            print_single_product(product)
    else:
        print("Список товаров пуст")


def sort_products_by_type_sort(products: list[Product], action, is_reverse=False):
    products.sort(key=action, reverse=is_reverse)


def find_products_by_type_search(products: list[Product], func_filter) -> list[Product]:
    return [product for product in products if func_filter(product) == True]


def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:

    find_product = get_product_by_id(products, search_id)

    if find_product == None:
        return False

    if find_product.amount < request_amount:
        return False

    find_product.amount -= request_amount

    return True


def load_products_from_txt_file(filename: str) -> list[Product]:

    try:

        with open(filename, "r", encoding="utf-8") as file_in:

            products = []

            count_products = int(file_in.readline())

            set_start_product_id(int(file_in.readline()))

            for _ in range(count_products):

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

            return products
    except:

        return None


def save_products_to_txt_file(products: list[Product], filename: str) -> bool:

    try:

        with open(filename, "w", encoding="utf-8") as file_out:

            file_out.write(f"{len(products)}\n")

            if len(products) > 0:

                file_out.write(f"{global_product_id}\n")
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
            else:

                file_out.write("Список товаров пуст")

        return True
    except:

        return False


def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:

    try:

        with open(filename, "w", encoding="utf-8") as file_out:

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

                file_out.write("Список товаров пуст")

        return True
    except:

        return False
