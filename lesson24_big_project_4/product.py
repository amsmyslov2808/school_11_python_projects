# dataclass автоматически создаёт служебный код класса, например конструктор __init__.
from dataclasses import dataclass

# Тип date нужен для хранения даты выпуска товара.
from datetime import date


# slots=True запрещает случайно добавлять объекту неизвестные поля с опечатками.
@dataclass(slots=True)
class Product:
    """Карточка одного товара — как одна заполненная строка в таблице магазина."""

    # Двоеточие после имени поля указывает, данные какого типа здесь ожидаются.
    icon: str
    release_date: date
    name: str
    category: str
    price: int
    rating: float
    amount: int
    # Новый товар может ещё не иметь номера, поэтому кроме int разрешено значение None.
    id: int | None = None

    def release_date_to_str(self) -> str:
        """Возвращает дату выпуска в удобном для человека виде: ДД.ММ.ГГГГ."""
        # self — конкретный товар, у которого был вызван этот метод.
        return self.release_date.strftime("%d.%m.%Y")
