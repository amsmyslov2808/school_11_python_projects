from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class Product:
    """Хранит данные об одной товарной позиции."""

    icon: str
    release_date: date
    name: str
    category: str
    price: int
    rating: float
    amount: int
    # ID назначается после ввода данных, поэтому у нового товара он может отсутствовать.
    id: int | None = None

    def convert_date_to_str(self) -> str:
        """Возвращает дату выпуска в удобном для человека виде: ДД.ММ.ГГГГ."""
        return self.release_date.strftime("%d.%m.%Y")
