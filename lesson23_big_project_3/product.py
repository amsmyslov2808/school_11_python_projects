from dataclasses import dataclass

from datetime import date


@dataclass(slots=True)
class Product:
    icon: str
    release_date: date
    name: str
    category: str
    price: int
    rating: float
    amount: int
    id: int | None = None

    def release_date_to_str(self) -> str:
        return self.release_date.strftime("%d.%m.%Y")
