from dataclasses import dataclass
from decimal import Decimal


@dataclass(slots=True)
class Product:
    photo: str
    title: str
    description: str
    rating: Decimal
    price: int
    comments: list[str]
