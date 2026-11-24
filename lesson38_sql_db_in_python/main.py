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


def update_tour_by_id(tour: Tour, id: int):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE tours SET
            title = ?, 
            country = ?,
            days = ?,
            price = ?
            WHERE id=?
            """,
            (tour.title, tour.country, tour.days, tour.price, id),
        )


def delete_tour_by_id(id: int):
    with get_connection() as connection:
        connection.execute(
            """
            DELETE FROM tours
            WHERE id=?
            """,
            (id,),
        )


delete_tour_by_id(1)

# update_tour_by_id(Tour(0, "Солнечный", "Россия", 21, 35000), 1)

# insert_new_tour(
#     Tour(id=0, title="Орловский заповедник", country="Россия", days=3, price=5700)
# )

tours = get_all_tours()

for tour in tours:
    print(tour)
    # print(f"{tour.title} {tour.price}")
