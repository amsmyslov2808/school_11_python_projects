from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Product:
    # Поля описывают одну товарную позицию и её остаток на складе.
    icon: str
    release_date: date
    name: str
    category: str
    price: int
    rating: float
    amount: int

    # До добавления в каталог товар может ещё не иметь ID.
    id: int | None = None

    def convert_date_to_str(self) -> str:
        # В таком же формате дата показывается в таблице и хранится в файле.
        return self.release_date.strftime("%d.%m.%Y")
