from product import Product
from datetime import date

global_product_id = 0


def get_next_product_id() -> int:
    pass


def input_product_data() -> Product:
    pass


def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
    pass


def add_product_to_list(products: list[Product], product: Product):
    pass


def update_product_by_id(products: list[Product], product: Product) -> bool:
    pass


def delete_product_by_id(products: list[Product], search_id: int) -> bool:
    pass


def print_table_products_header():
    pass


def print_single_product(product: Product):
    pass


def print_all_products(products: list[Product]):
    pass


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
