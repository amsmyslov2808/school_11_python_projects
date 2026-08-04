from product import Product
from datetime import date

global_product_id = 0


def get_next_product_id() -> int:
    global global_product_id

    global_product_id += 1

    return get_product_by_id


def input_product_data() -> Product:
    pass


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
    pass


def print_single_product(product: Product):
    pass


def print_all_products(products: list[Product]):
    for product in products:
        print_single_product(product)


def sort_products_by_type_sort(products: list[Product], type_sort: int):
    pass


def find_products_by_type_parameter(
    products: list[Product], type_parameter: int, parameter: str
) -> list[Product]:
    pass


def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:
    pass


def load_products_from_txt_file(filename: str) -> list[Product]:
    pass


def save_products_to_txt_file(products: list[Product], filename: str) -> bool:
    pass


def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:
    pass
