# Подключаем класс-карточку Product, тип даты и готовые функции из соседних файлов.
from product import Product
from datetime import date
from console_helper import *
from products_functions import *

# Это главная «полка» магазина: здесь будут храниться все товары программы.
# Запись list[Product] подсказывает, что список предназначен для объектов Product.
products: list[Product] = []

# Создаём десять тестовых товаров. Они нужны, чтобы программу можно было сразу
# запустить и проверить, не вводя все данные вручную.
mock_products = [
    # Каждый вызов Product(...) похож на заполнение одной карточки товара.
    # get_next_product_id() выдаёт следующий свободный номер.
    Product(
        id=get_next_product_id(),
        icon="🧥",
        name="Куртка зимняя оверсайз",
        category="Одежда",
        price=4500,
        rating=4.7,
        amount=120,
        release_date=date(2025, 10, 15),
    ),
    # Остальные карточки устроены так же, но содержат данные других товаров.
    Product(
        id=get_next_product_id(),
        icon="👟",
        name="Кроссовки спортивные",
        category="Обувь",
        price=3200,
        rating=4.5,
        amount=85,
        release_date=date(2026, 3, 20),
    ),
    Product(
        id=get_next_product_id(),
        icon="🎒",
        name="Рюкзак городской",
        category="Аксессуары",
        price=1800,
        rating=4.8,
        amount=200,
        release_date=date(2026, 1, 10),
    ),
    Product(
        id=get_next_product_id(),
        icon="💄",
        name="Матовая помада для губ",
        category="Косметика",
        price=450,
        rating=4.6,
        amount=450,
        release_date=date(2026, 5, 5),
    ),
    Product(
        id=get_next_product_id(),
        icon="🎧",
        name="Беспроводные наушники",
        category="Электроника",
        price=2900,
        rating=4.3,
        amount=60,
        release_date=date(2025, 12, 1),
    ),
    Product(
        id=get_next_product_id(),
        icon="🧴",
        name="Увлажняющий крем для лица",
        category="Косметика",
        price=650,
        rating=4.9,
        amount=310,
        release_date=date(2026, 4, 18),
    ),
    Product(
        id=get_next_product_id(),
        icon="🕯️",
        name="Свеча ароматическая",
        category="Дом и уют",
        price=550,
        rating=4.7,
        amount=140,
        release_date=date(2026, 6, 12),
    ),
    Product(
        id=get_next_product_id(),
        icon="📱",
        name="Чехол для смартфона",
        category="Электроника",
        price=350,
        rating=4.4,
        amount=500,
        release_date=date(2026, 7, 1),
    ),
    Product(
        id=get_next_product_id(),
        icon="👕",
        name="Футболка базовая хлопковая",
        category="Одежда",
        price=890,
        rating=4.8,
        amount=350,
        release_date=date(2026, 2, 28),
    ),
    Product(
        id=get_next_product_id(),
        icon="🥤",
        name="Термокружка из стали",
        category="Дом и уют",
        price=1100,
        rating=4.6,
        amount=95,
        release_date=date(2025, 11, 23),
    ),
]

# Перекладываем тестовые товары из временного списка в главный список магазина.
for prod in mock_products:
    add_product_to_list(products, prod)


def print_products():
    """Печатает название магазина, таблицу товаров и линию-разделитель."""
    print("Список товаров магазина NeDikayaMalina")
    print_all_products(products)
    # Умножение строки повторяет знак «=» 125 раз.
    print("=" * 125)


def print_main_menu():
    """Показывает пункты главного меню."""
    print("Главное меню:")
    print("1. Меню Покупателя")
    print("2. Меню Администратора")
    print("0. Выход")


def work_with_buyer_menu():
    """Показывает меню покупателя, пока пользователь не решит выйти из него."""
    # True означает, что меню должно продолжать работать.
    is_run_buyer_menu = True
    while is_run_buyer_menu == True:
        print("Меню Покупателя:")
        print("1. Найти товар по ID")
        print("2. Сортировать товары")
        print("3. Найти товары")
        print("4. Купить товар")
        print("5. Сохранить товары в текстовый файл для печати")
        print("0. В Главное меню")

        # input_int не пропустит текст или номер пункта вне диапазона от 0 до 7.
        # Выбранный пункт сохранён для будущей обработки команд этого меню.
        choose_action_buyer_menu = input_int("Выберите пункт меню: ", 0, 7)

        if choose_action_buyer_menu == 1:
            pass
        elif choose_action_buyer_menu == 2:
            pass
        elif choose_action_buyer_menu == 3:
            pass
        elif choose_action_buyer_menu == 4:
            pass
        elif choose_action_buyer_menu == 5:
            pass
        elif choose_action_buyer_menu == 0:
            is_run_buyer_menu = False

        print("\n\n")
        print("=" * 125)
        print("\n\nДля продолжения работы нажмите <Enter>\n\n")
        input()


def auth_is_administrator():
    """Проверяет пароль и возвращает True, если он правильный."""
    # Пароль должен содержать от 4 до 16 символов.
    password = input_str(
        "Введите пароль Администратора для входа в Меню Администратора: ", 4, 16
    )
    # Сравнение == само даёт True или False, поэтому отдельный if здесь не нужен.
    return password == "12345"  # todo вынести в отдельную константу


def work_with_administrator_menu():
    """Обрабатывает команды меню администратора."""
    # Флаг управляет повторным показом меню до команды возврата назад.
    is_run_administrator_menu = True
    # Меню повторяется после каждой команды, пока флаг остаётся равен True.
    while is_run_administrator_menu == True:
        print("Меню Администратора:")
        print("1. Найти товар по ID")
        print("2. Добавить новый товар")
        print("3. Изменить товар по ID")
        print("4. Удалить товар по ID")
        print("5. Загрузить товары из текстового файла")
        print("6. Сохранить товары в текстовый файл")
        print("7. Сохранить товары в текстовый файл для печати")
        print("0. В Главное меню")

        # Принимаем только номера существующих пунктов меню.
        choose_action_administrator_menu = input_int("Выберите пункт меню: ", 0, 7)

        # В зависимости от выбранного номера выполняется только одна ветка.
        if choose_action_administrator_menu == 1:
            # Запрашиваем ID и пробуем найти карточку с таким номером.
            search_id = input_int("Введите ID товара для поиска: ", 1, 1_000_000)
            found_product = get_product_by_id(products, search_id)

            # None можно представить как пустую коробку: товара внутри нет.
            if found_product == None:
                print(f"Продукт с ID {search_id} не найден")
            else:
                # Если товар найден, сначала печатаем шапку таблицы, затем его строку.
                print_table_products_header()
                print_single_product(found_product)
        elif choose_action_administrator_menu == 2:
            # Собираем данные, присваиваем свободный ID и добавляем новую карточку.
            print("Введите данные нового продукта")

            new_product = input_product_data()

            new_product.id = get_next_product_id()

            add_product_to_list(products, new_product)

            print("Товар успешно добавлен")
        elif choose_action_administrator_menu == 3:
            # Сначала убеждаемся, что товар для изменения существует.
            update_id = input_int("Введите ID товара для обновления: ", 1, 1_000_000)
            found_product = get_product_by_id(products, update_id)

            if found_product == None:
                print(f"Продукт с ID {update_id} не найден")
            else:
                # Новые данные вводятся отдельно, а старый ID сохраняется.
                print("Введите новые данные для продукта ")

                update_product = input_product_data()

                update_product.id = update_id

                update_product_by_id(products, update_product)

                print("Продукт успешно обновлён")

        elif choose_action_administrator_menu == 4:
            # Функция удаления возвращает результат, чтобы показать подходящее сообщение.
            delete_id = input_int("Введите ID товара для удаления: ", 1, 1_000_000)

            is_deleted = delete_product_by_id(products, delete_id)

            if is_deleted == False:
                print(f"Продукт с ID {delete_id} не найден")
            else:
                print("Продукт успешно удалён")
        elif choose_action_administrator_menu == 5:
            # Загрузка из файла будет добавлена позднее.
            pass
        elif choose_action_administrator_menu == 6:
            # Записываем полный набор данных товаров в указанный файл.
            filename = input_str("Введите имя файла для сохранения: ", 4, 100)

            is_saved = save_products_to_txt_file(products, filename)

            if is_saved == False:
                print("Ошибка сохранения файла")
            else:
                print("Файл успешно сохранён")
        elif choose_action_administrator_menu == 7:
            # Создаём печатную версию списка в виде отформатированной таблицы.
            filename = input_str("Введите имя файла для сохранения: ", 4, 100)

            is_saved = save_products_to_txt_file_for_print(products, filename)

            if is_saved == False:
                print("Ошибка сохранения файла")
            else:
                print("Файл успешно сохранён")

        elif choose_action_administrator_menu == 0:
            # Меняем флаг на False — на следующей проверке цикл завершится.
            is_run_administrator_menu = False

        print("\n\n")
        print("=" * 125)
        print("\n\nДля продолжения работы нажмите <Enter>\n\n")
        input()


# Главный переключатель всей программы.
is_run = True

# Этот цикл можно представить как двигатель программы: пока он включён,
# пользователь видит товары и главное меню.
while is_run == True:
    # Перед выбором действия показываем актуальный список товаров.
    print_products()

    # Получаем команду верхнего уровня: покупатель, администратор или выход.
    print_main_menu()
    choose_action_main_menu = input_int("Выберите пункт меню: ", 0, 2)

    # Направляем пользователя в нужную часть программы по номеру пункта.
    if choose_action_main_menu == 1:
        work_with_buyer_menu()
    elif choose_action_main_menu == 2:
        # В меню администратора можно попасть только после проверки пароля.
        if auth_is_administrator() == True:
            print("Пароль успешно введён")
            work_with_administrator_menu()
        else:
            print("Ошибка ввода пароля администратора")
    elif choose_action_main_menu == 0:
        # False выключает главный цикл и завершает программу.
        is_run = False
