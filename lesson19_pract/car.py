from dataclasses import dataclass


@dataclass(slots=True)
class Car:
    brand: str
    model: str
    price: int
    photo_url: str
    id: int | None = None
