# sqlite3 — встроенный модуль Python для работы с базами данных SQLite.
# База SQLite хранится в обычном файле и не требует отдельного сервера.
import sqlite3
from dataclasses import dataclass


# dataclass автоматически создаёт конструктор __init__ и представление __repr__.
# Благодаря этому Tour удобно создавать из данных таблицы и выводить через print.
@dataclass
class Tour:
    # Аннотации описывают ожидаемые типы полей, но сами по себе не проверяют их.
    id: int  # Идентификатор записи в таблице tours.
    title: str  # Название тура.
    country: str  # Страна путешествия.
    days: int  # Продолжительность тура в днях.
    price: int  # Стоимость тура.


def get_connection():
    # Относительный путь отсчитывается от текущей рабочей папки программы,
    # а не обязательно от папки этого Python-файла. Если файла нет, SQLite
    # создаст его, но таблицу tours нужно создать отдельно.
    connection = sqlite3.connect("vokrug_sveta.db")
    # По умолчанию строки результата — кортежи. sqlite3.Row позволяет также
    # обращаться к значениям по именам столбцов и преобразовывать строку в dict.
    connection.row_factory = sqlite3.Row
    return connection


def get_all_tours() -> list[Tour]:
    # Контекстный менеджер соединения управляет транзакцией: при успешном
    # выходе фиксирует изменения, а при исключении откатывает их.
    # Само соединение SQLite конструкция with автоматически не закрывает.
    with get_connection() as connection:
        # execute выполняет запрос, а fetchall собирает все найденные строки
        # в список. SELECT * выбирает все столбцы таблицы tours.
        tours = connection.execute("SELECT * FROM tours").fetchall()

    # Для каждой строки создаём словарь вида {"id": ..., "title": ..., ...}.
    # Оператор ** передаёт его элементы как именованные аргументы Tour.
    # Имена столбцов должны совпадать с именами полей класса.
    return [Tour(**dict(tour)) for tour in tours]


def insert_new_tour(tour: Tour):
    # Добавляем данные объекта в таблицу. Поле tour.id не используется:
    # значение id должна назначить база согласно схеме таблицы.
    with get_connection() as connection:
        # Знаки ? — параметры запроса. Значения передаются отдельно, поэтому
        # sqlite3 корректно обрабатывает кавычки и не принимает данные за SQL.
        # Порядок значений в кортеже соответствует порядку столбцов INSERT.
        connection.execute(
            """
            INSERT INTO tours (title, country, days, price)
            VALUES (?,?,?,?)
            """,
            (tour.title, tour.country, tour.days, tour.price),
        )


def update_tour_by_id(tour: Tour, id: int):
    # Объект tour содержит новые данные, а отдельный аргумент id определяет,
    # какую запись изменить. Значение tour.id в этом запросе не используется.
    with get_connection() as connection:
        # SET перечисляет обновляемые поля, WHERE ограничивает выбор записью
        # с нужным id. Без WHERE запрос изменил бы все строки таблицы.
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
        # DELETE удаляет строки, удовлетворяющие условию WHERE.
        # Если такого id нет, запрос просто не удалит ни одной строки.
        connection.execute(
            """
            DELETE FROM tours
            WHERE id=?
            """,
            # Запятая обязательна: (id,) — кортеж из одного элемента,
            # тогда как (id) — просто значение id в скобках.
            (id,),
        )


# Далее идут примеры использования функций. Этот код выполняется сразу
# при запуске файла и при его импорте: защиты if __name__ == "__main__" нет.
# Активный вызов удаляет тур с id=1; изменение фиксируется при выходе из with.
delete_tour_by_id(1)

# Пример обновления: данные Tour заменят поля записи с id=1.
# update_tour_by_id(Tour(0, "Солнечный", "Россия", 21, 35000), 1)

# Пример добавления: id=0 здесь условный, функция не передаёт его в базу.
# insert_new_tour(
#     Tour(id=0, title="Орловский заповедник", country="Россия", days=3, price=5700)
# )

# Получаем текущее содержимое таблицы уже после удаления записи.
tours = get_all_tours()

for tour in tours:
    # Для dataclass print выводит имя класса и значения всех его полей.
    print(tour)
    # Альтернативный формат: вывести только название и стоимость тура.
    # print(f"{tour.title} {tour.price}")
