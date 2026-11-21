import sqlite3
from dataclasses import dataclass


@dataclass
class Tour:
    id: int
    title: str
    country: str
    days: int
    price: int


def get_connection():
    connection = sqlite3.connect("vokrug_sveta.db")
    connection.row_factory = sqlite3.Row
    return connection


def get_all_tours() -> list[Tour]:
    with get_connection() as connection:
        tours = connection.execute("SELECT * FROM tours").fetchall()

    return [Tour(**dict(tour)) for tour in tours]


def insert_new_tour(tour: Tour):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO tours (title, country, days, price)
            VALUES (?,?,?,?)
            """,
            (tour.title, tour.country, tour.days, tour.price),
        )


insert_new_tour(
    Tour(id=0, title="Орловский заповедник", country="Россия", days=3, price=5700)
)

tours = get_all_tours()

for tour in tours:
    print(tour)
    # print(f"{tour.title} {tour.price}")
