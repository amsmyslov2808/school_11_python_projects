from product import Product

# from products_functions import add_to_end, print_all
from products_functions import *

# import product
# import products_functions

products: list[Product] = []

add_to_end(
    products,
    Product(
        photo="💻",
        title="Игровой ноутбук Storm X",
        description="Мощный ноутбук с видеокартой последнего поколения, RGB-подсветкой и экраном 144 Гц.",
        rating=Decimal("4.9"),
        price=124990,
        comments=[
            "Тянет все современные игры на ультра-настройках.",
            "Охлаждение шумновато под нагрузкой, но со своей задачей справляется.",
            "Экран просто пушка, цвета очень сочные!",
        ],
    ),
)

add_to_end(
    products,
    Product(
        photo="📱",
        title="Смартфон Horizon Pro",
        description="Флагманский смартфон с камерой 108 Мп, безрамочным OLED-экраном и поддержкой быстрой зарядки.",
        rating=Decimal("4.7"),
        price=69990,
        comments=[
            "Камера делает потрясающие снимки ночью.",
            "Заряжается до 100% всего за полчаса.",
            "В комплекте нет блока питания, только кабель.",
        ],
    ),
)

print_all(products)
