"""Операции с каталогом товаров."""

from product import Product
from datetime import date
from console_helper import *

# Числовые константы связывают пункт меню с конкретным способом сортировки.
# ASC (ascending) означает порядок по возрастанию, DESC (descending) — по убыванию.
SORT_BY_PRICE_ASC = 1
SORT_BY_PRICE_DESC = 2
SORT_BY_RATING_ASC = 3
SORT_BY_RATING_DESC = 4
SORT_BY_RELEASE_DATE_ASC = 5
SORT_BY_RELEASE_DATE_DESC = 6
SORT_BY_ID_ASC = 7
SORT_BY_ID_DESC = 8

# Эти константы аналогично обозначают разные режимы поиска.
SEARCH_BY_PART_NAME = 1
SEARCH_BY_CATEGORY = 2
SEARCH_BY_PRICE = 3


# Последний выданный ID; значение также восстанавливается из файла.
global_product_id = 0


def set_start_product_id(product_id: int):
    """Устанавливает значение счётчика ID после загрузки товаров из файла."""
    global global_product_id
    global_product_id = product_id


def get_next_product_id() -> int:
    """Увеличивает общий счётчик и возвращает новый уникальный ID."""
    global global_product_id

    global_product_id += 1

    return global_product_id


def input_product_data() -> Product:
    """Собирает данные о товаре из консоли и создаёт объект Product."""
    # Каждая функция ввода сама повторяет вопрос, пока ответ не пройдёт проверку.
    icon = input_str("Вставьте иконку товара: ", 1, 1)
    release_date = input_date(
        "Введите дату производства в формет ДД.ММ.ГГГГ: ",
        date(2026, 1, 1),
        date.today(),
    )
    name = input_str("Введите название товара (от 1 до 25 символов): ", 1, 25)
    category = input_str("Введите категорию товара (от 1 до 20 символов): ", 1, 20)
    price = input_int("Введите цену товара (от 1 до 10 000 000 руб.): ", 1, 10_000_000)
    rating = input_float("Введите рейтинг товара (от 1 до 5, можно дробный): ", 1, 5)
    amount = input_int(
        "Введите количество товара на складе (от 1 до 10 000 ед.): ", 1, 10_000
    )
    # Собираем отдельные ответы в одну карточку товара.
    # ID здесь не задаётся: у нового объекта он пока будет равен None.
    return Product(
        icon=icon,
        release_date=release_date,
        name=name,
        category=category,
        price=price,
        rating=rating,
        amount=amount,
    )


def get_product_by_id(products: list[Product], search_id: int) -> Product | None:
    """Ищет товар по ID; возвращает товар или None, если совпадения нет."""
    # Перебираем карточки по очереди, словно просматриваем строки таблицы.
    for product in products:
        if product.id == search_id:
            # Совпадение найдено — дальше искать уже не нужно.
            return product

    # Цикл закончился без совпадения.
    return None


def add_product_to_list(products: list[Product], product: Product):
    """Добавляет карточку товара в конец списка."""
    # append() сохраняет объект последней строкой списка.
    products.append(product)


def update_product_by_id(products: list[Product], product: Product) -> bool:
    """Заменяет данные товара с таким же ID и сообщает, получилось ли это."""
    find_product = get_product_by_id(products, product.id)

    # None означает, что обновлять нечего.
    if find_product == None:
        return False

    # Обновляем поля найденной карточки, но сохраняем её прежний ID.
    find_product.icon = product.icon
    find_product.release_date = product.release_date
    find_product.name = product.name
    find_product.category = product.category
    find_product.price = product.price
    find_product.rating = product.rating
    find_product.amount = product.amount

    # True — условный ответ «операция прошла успешно».
    return True


def delete_product_by_id(products: list[Product], search_id: int) -> bool:
    """Удаляет товар с нужным ID и возвращает результат операции."""
    find_product = get_product_by_id(products, search_id)

    if find_product == None:
        return False

    # remove() удаляет из списка именно найденный объект.
    products.remove(find_product)

    return True


def print_table_products_header():
    """Печатает названия столбцов таблицы товаров."""
    # В записи :<5 число задаёт ширину столбца, а знак < выравнивает текст влево.
    print(
        f"{'ИД':<5}"
        f"{'Иконка':<15}"
        f"{'Дата выпуска':<20}"
        f"{'Название':<35}"
        f"{'Категория':<20}"
        f"{'Цена(руб.)':<12}"
        f"{'Рейтинг':<10}"
        f"{'Количество':<12}"
    )


def print_single_product(product: Product):
    """Печатает одну карточку товара как строку таблицы."""
    # Одинаковая ширина полей помогает значениям стоять под своими заголовками.
    print(
        f"{product.id:<5}"
        f"{product.icon:<15}"
        f"{product.convert_date_to_str():<20}"
        f"{product.name:<35}"
        f"{product.category:<20}"
        f"{product.price:<12}"
        f"{product.rating:<10}"
        f"{product.amount:<12}"
    )


def print_all_products(products: list[Product]):
    """Печатает заголовок и все товары либо сообщение о пустом списке."""
    print_table_products_header()

    # Если длина больше нуля, в списке есть хотя бы один товар.
    if len(products) > 0:
        for product in products:
            print_single_product(product)
    else:
        print("Список товаров пуст")


def sort_products_by_type_sort(products: list[Product], type_sort: int):
    """Сортирует исходный список товаров выбранным способом методом пузырька.

    Функция меняет порядок элементов прямо в переданном списке и ничего не
    возвращает. На каждом проходе соседние товары сравниваются и при необходимости
    меняются местами. После полного прохода один элемент уже оказывается на своём
    месте, поэтому ``offset`` сокращает проверяемую часть списка.
    """
    # Для каждого type_sort выбирается поле сравнения и направление сортировки.
    if type_sort == SORT_BY_PRICE_ASC:
        # В конце первого прохода окажется самая большая цена, поэтому начинаем
        # без смещения, а после каждого прохода увеличиваем offset на единицу.
        offset = 0
        # temp временно хранит товар во время перестановки двух соседних объектов.
        temp = None
        # False означает, что сортировка ещё не подтверждена как завершённая.
        is_sort = False

        while is_sort == False:
            # Предполагаем, что список уже отсортирован. Любая перестановка ниже
            # снова установит False и заставит выполнить ещё один проход.
            is_sort = True

            # ``- 1`` нужен из-за обращения к i + 1, а offset исключает уже
            # отсортированный хвост списка из следующих проходов.
            for i in range(0, len(products) - 1 - offset):
                # Если правый товар дешевле левого, ставим его раньше.
                if products[i + 1].price < products[i].price:
                    # Классическая перестановка через третью временную переменную.
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    # Была перестановка — возможно, порядок ещё не окончательный.
                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_PRICE_DESC:
        # Та же пузырьковая сортировка, но более дорогие товары двигаются в начало.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                # Знак ``>`` задаёт убывание: большая цена должна стоять левее.
                if products[i + 1].price > products[i].price:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_RATING_ASC:
        # Сортировка рейтинга по возрастанию: от меньшей оценки к большей.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                # Здесь сравнивается rating, остальная схема алгоритма не меняется.
                if products[i + 1].rating < products[i].rating:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_RATING_DESC:
        # Сортировка рейтинга по убыванию: лучшие оценки окажутся первыми.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                # Больший рейтинг перемещается влево.
                if products[i + 1].rating > products[i].rating:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_RELEASE_DATE_ASC:
        # Объекты date поддерживают обычное сравнение: более ранняя дата меньше.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                # Более старые товары передвигаются к началу списка.
                if products[i + 1].release_date < products[i].release_date:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_RELEASE_DATE_DESC:
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                # Более поздние даты перемещаются к началу списка.
                if products[i + 1].release_date > products[i].release_date:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_ID_ASC:
        # Сортировка ID от меньшего к большему.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                if products[i + 1].id < products[i].id:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1
    elif type_sort == SORT_BY_ID_DESC:
        # Сортировка ID от большего к меньшему.
        offset = 0
        temp = None
        is_sort = False

        while is_sort == False:
            is_sort = True

            for i in range(0, len(products) - 1 - offset):
                if products[i + 1].id > products[i].id:
                    temp = products[i]
                    products[i] = products[i + 1]
                    products[i + 1] = temp

                    is_sort = False

            offset += 1


def find_products_by_type_search(
    products: list[Product], type_search: int, parameter: str
) -> list[Product]:
    """Возвращает товары, найденные выбранным способом поиска.

    Доступны поиск по части названия, по категории и по диапазону цены.
    Исходный список не изменяется.
    """
    if type_search == SEARCH_BY_PART_NAME:
        # Новый пустой список станет результатом функции.
        finded_products = []
        # strip() убирает случайные пробелы только по краям поискового запроса.
        parameter = parameter.strip()

        for product in products:
            # lower() с обеих сторон делает поиск нечувствительным к регистру:
            # запрос «поМАда» сможет найти товар «Матовая помада для губ».
            # Оператор in проверяет вхождение одной строки внутрь другой.
            if parameter.lower() in product.name.lower():
                finded_products.append(product)

        # Если совпадений нет, возвращается пустой список.
        return finded_products

    elif type_search == SEARCH_BY_CATEGORY:
        finded_products = []
        parameter = parameter.strip()

        for product in products:
            # Сравнение не зависит от регистра букв.
            if parameter.lower() in product.category.lower():
                finded_products.append(product)

        return finded_products

    elif type_search == SEARCH_BY_PRICE:
        finded_products = []
        parameter = parameter.strip()

        min_price = int(parameter.split("|")[0])
        max_price = int(parameter.split("|")[1])

        for product in products:
            if product.price >= min_price and product.price <= max_price:
                finded_products.append(product)

        # Если совпадений нет, возвращается пустой список.
        return finded_products

    # Неизвестный type_search приведёт к неявному возврату None.


def buy_product(products: list[Product], search_id: int, request_amount: int) -> bool:
    """Уменьшает остаток товара и возвращает True при успешной покупке.

    Покупка не состоится, если товар не найден или на складе недостаточно
    единиц; в этих случаях функция возвращает False.
    """
    find_product = get_product_by_id(products, search_id)

    if find_product == None:
        return False

    if find_product.amount < request_amount:
        return False

    find_product.amount -= request_amount

    return True


def load_products_from_txt_file(filename: str) -> list[Product]:
    """Загружает список товаров из служебного текстового файла.

    Формат файла построчный: сначала количество товаров и последнее выданное ID,
    затем для каждого товара идут восемь строк с его полями. При любой ошибке
    открытия, преобразования или структуры функция возвращает None.
    """
    try:
        # with автоматически закроет файл и при успехе, и при возникновении ошибки.
        with open(filename, "r", encoding="utf-8") as file_in:
            # Создаём новый список: загруженные товары не добавляются к старым.
            products = []
            # Первая строка говорит, сколько карточек нужно прочитать далее.
            count_products = int(file_in.readline())

            # Вторая строка восстанавливает счётчик, чтобы новые ID не повторялись.
            set_start_product_id(int(file_in.readline()))

            # Символ _ означает: номер итерации цикла здесь не используется.
            for _ in range(count_products):
                # Восемь последовательных строк превращаются в один объект Product.
                products.append(
                    Product(
                        # Числовые строки явно преобразуются в int или float.
                        id=int(file_in.readline()),
                        # strip() удаляет завершающий перевод строки ``\n``.
                        icon=file_in.readline().strip(),
                        # Формат совпадает с Product.convert_date_to_str().
                        release_date=datetime.strptime(
                            file_in.readline().strip(), "%d.%m.%Y"
                        ).date(),
                        name=file_in.readline().strip(),
                        category=file_in.readline().strip(),
                        price=int(file_in.readline()),
                        rating=float(file_in.readline()),
                        amount=int(file_in.readline()),
                    )
                )

            # Результат отдаётся только после чтения всех заявленных карточек.
            return products
    except:
        # Любая проблема считается общей ошибкой загрузки; вызывающее меню покажет
        # пользователю сообщение, проверив результат на None.
        return None


def save_products_to_txt_file(products: list[Product], filename: str) -> bool:
    """Сохраняет данные в служебном формате для последующей загрузки.

    В отличие от печатной таблицы, здесь каждое значение занимает отдельную
    строку. Непустой каталог можно прочитать функцией
    load_products_from_txt_file(); файл с пустым каталогом текущий загрузчик не поддерживает.
    """
    try:
        # Режим w создаёт новый файл или заменяет содержимое существующего.
        with open(filename, "w", encoding="utf-8") as file_out:
            # Первой строкой сохраняем число карточек: оно понадобится при загрузке.
            file_out.write(f"{len(products)}\n")

            if len(products) > 0:
                # Сохраняем счётчик ID до карточек, чтобы восстановить его при загрузке.
                file_out.write(f"{global_product_id}\n")
                for product in products:
                    # Каждое свойство занимает отдельную строку и читается обратно
                    # в точно таком же порядке функцией загрузки.
                    file_out.write(
                        f"{product.id}\n"
                        f"{product.icon}\n"
                        f"{product.convert_date_to_str()}\n"
                        f"{product.name}\n"
                        f"{product.category}\n"
                        f"{product.price}\n"
                        f"{product.rating}\n"
                        f"{product.amount}\n"
                    )
            else:
                # После числа 0 сохраняется текст. Текущая функция загрузки всё равно
                # ожидает во второй строке целый ID, поэтому такой файл обратно не загрузит.
                file_out.write("Список товаров пуст")

        # Файл успешно закрыт после выхода из with.
        return True
    except:
        # Любая ошибка открытия или записи означает, что сохранить файл не удалось.
        return False


def save_products_to_txt_file_for_print(products: list[Product], filename: str) -> bool:
    """Сохраняет список товаров в виде таблицы, удобной для чтения и печати.

    Это отдельный, человекочитаемый формат. Его нельзя передавать функции
    load_products_from_txt_file(), потому что расположение данных в нём другое.
    """
    try:
        # Открываем файл в кодировке UTF-8, чтобы корректно сохранить кириллицу и эмодзи.
        with open(filename, "w", encoding="utf-8") as file_out:
            # Добавляем название магазина перед таблицей.
            file_out.write("Список товаров магазина NeDikayaMalina\n\n")

            # Шапка использует ту же ширину столбцов, что и вывод в консоль.
            file_out.write(
                f"{'ИД':<5}"
                f"{'Иконка':<15}"
                f"{'Дата выпуска':<20}"
                f"{'Название':<35}"
                f"{'Категория':<20}"
                f"{'Цена(руб.)':<12}"
                f"{'Рейтинг':<10}"
                f"{'Количество':<12}"
                "\n"
            )

            if len(products) > 0:
                # Записываем по одной выровненной строке для каждой карточки.
                for product in products:
                    file_out.write(
                        f"{product.id:<5}"
                        f"{product.icon:<15}"
                        f"{product.convert_date_to_str():<20}"
                        f"{product.name:<35}"
                        f"{product.category:<20}"
                        f"{product.price:<12}"
                        f"{product.rating:<10}"
                        f"{product.amount:<12}"
                        "\n"
                    )
            else:
                # При отсутствии карточек оставляем под шапкой явное сообщение.
                file_out.write("Список товаров пуст")

        # Выход из блока with означает, что буфер записан и файл закрыт.
        return True
    except:
        # Возвращаем False, чтобы вызывающий код мог вывести сообщение об ошибке.
        return False
