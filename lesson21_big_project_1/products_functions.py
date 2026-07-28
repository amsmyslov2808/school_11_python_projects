from product import Product
from datetime import date

global_product_id = 0


def get_next_product_id() -> int:
    pass


def input_product_data() -> Product:
    pass


def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
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
