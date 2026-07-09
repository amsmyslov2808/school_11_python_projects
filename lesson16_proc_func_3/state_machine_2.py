# Константы состояний
STATE_START = 1
STATE_MAIN_MENU = 2
STATE_PRODUCTS_MENU = 3
STATE_ORDER = 4
STATE_BOOKING_TABLE = 5
STATE_READ_COMMENTS = 6
STATE_EXIT = 0

global_current_state = STATE_START
global_order = []


# Данные ресторана
restaurant_name = "Теплая тарелка"

menu = [
    ["Салат с курицей и авокадо", 430],
    ["Томатный суп с базиликом", 350],
    ["Паста карбонара", 520],
    ["Куриный бургер с картофелем", 590],
    ["Пицца маргарита", 610],
    ["Лосось с рисом и овощами", 890],
    ["Чизкейк Нью-Йорк", 330],
    ["Лимонад домашний", 210],
]

comments = [
    "Анна: Заказывали пасту и лимонад. Привезли горячим, вкус как в ресторане.",
    "Илья: Бургер большой, картофель хрустящий. Курьер приехал на 10 минут раньше.",
    "Мария: Очень понравился томатный суп. Упаковка аккуратная, ничего не пролилось.",
    "Денис: Пицца простая, но сыр хороший и тесто тонкое. Закажу еще.",
    "Ольга: Лосось свежий, порция нормальная. Цена не самая низкая, но качество отличное.",
]


# Вспомогательные функции
def input_int(message, min_value, max_value):
    while True:
        text = input(message).strip()

        if text == "":
            print("Ошибка: нужно ввести число.")
            continue

        if text.isdigit() == False:
            print("Ошибка: вводите только цифры.")
            continue

        number = int(text)

        if number < min_value or number > max_value:
            print("Ошибка: выберите число от", min_value, "до", max_value)
            continue

        return number


def input_not_empty(message):
    while True:
        text = input(message).strip()

        if text == "":
            print("Ошибка: поле не может быть пустым.")
            continue

        return text


def input_phone(message):
    while True:
        phone = input(message).strip()
        good_symbols = True
        digits_count = 0

        for symbol in phone:
            if symbol.isdigit():
                digits_count = digits_count + 1
            elif symbol not in "+-() ":
                good_symbols = False

        if phone == "":
            print("Ошибка: телефон не может быть пустым.")
        elif good_symbols == False:
            print("Ошибка: в телефоне можно использовать цифры, пробелы, +, -, скобки.")
        elif digits_count < 10:
            print("Ошибка: в телефоне должно быть хотя бы 10 цифр.")
        else:
            return phone


def input_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer == "да" or answer == "д":
            return True
        elif answer == "нет" or answer == "н":
            return False
        else:
            print("Введите 'да' или 'нет'.")


def print_order():
    if len(global_order) == 0:
        print("Корзина пустая.")
        return

    total = 0

    print("Ваш заказ:")
    for i in range(len(global_order)):
        dish_number = global_order[i]
        dish = menu[dish_number]
        total = total + dish[1]
        print(str(i + 1) + ") " + dish[0] + " - " + str(dish[1]) + " руб.")

    print("Итого:", total, "руб.")


# Функции обработки состояний
def process_state_start():
    global global_current_state

    print("Добро пожаловать в ресторан '" + restaurant_name + "'!")
    print("Здесь можно посмотреть меню, собрать онлайн-заказ, забронировать столик")
    print("и прочитать отзывы гостей.")

    input("Для продолжения нажмите <Enter>")

    global_current_state = STATE_MAIN_MENU


def process_state_main_menu():
    global global_current_state

    print()
    print("Главное меню")
    print("1) Посмотреть меню ресторана")
    print("2) Собрать онлайн-заказ")
    print("3) Забронировать столик")
    print("4) Почитать отзывы")
    print("0) Выйти из программы")

    choose = input_int("Введите номер выбранного варианта: ", 0, 4)

    if choose == 1:
        global_current_state = STATE_PRODUCTS_MENU
    elif choose == 2:
        global_current_state = STATE_ORDER
    elif choose == 3:
        global_current_state = STATE_BOOKING_TABLE
    elif choose == 4:
        global_current_state = STATE_READ_COMMENTS
    elif choose == 0:
        global_current_state = STATE_EXIT


def process_state_products_menu():
    global global_current_state

    print()
    print("Меню ресторана")

    for i in range(len(menu)):
        dish = menu[i]
        print(str(i + 1) + ") " + dish[0] + " - " + str(dish[1]) + " руб.")

    print()
    print("1) Перейти к онлайн-заказу")
    print("0) Вернуться в главное меню")

    choose = input_int("Ваш выбор: ", 0, 1)

    if choose == 1:
        global_current_state = STATE_ORDER
    else:
        global_current_state = STATE_MAIN_MENU


def process_state_order():
    global global_current_state
    global global_order

    while True:
        show_order_number = len(menu) + 1
        clear_order_number = len(menu) + 2

        print()
        print("Онлайн-заказ")

        for i in range(len(menu)):
            dish = menu[i]
            print(str(i + 1) + ") " + dish[0] + " - " + str(dish[1]) + " руб.")

        print(str(show_order_number) + ") Показать корзину")
        print(str(clear_order_number) + ") Очистить корзину")
        print("0) Завершить заказ и вернуться в главное меню")

        choose = input_int("Выберите блюдо или действие: ", 0, clear_order_number)

        if choose >= 1 and choose <= len(menu):
            global_order.append(choose - 1)
            print("Добавлено:", menu[choose - 1][0])
        elif choose == show_order_number:
            print_order()
        elif choose == clear_order_number:
            if len(global_order) == 0:
                print("Корзина уже пустая.")
            else:
                clear = input_yes_no("Точно очистить корзину? ")
                if clear == True:
                    global_order = []
                    print("Корзина очищена.")
        elif choose == 0:
            if len(global_order) > 0:
                print_order()
                confirm = input_yes_no("Оформить заказ? ")

                if confirm == True:
                    name = input_not_empty("Ваше имя: ")
                    phone = input_phone("Ваш телефон: ")
                    address = input_not_empty("Адрес доставки: ")

                    print()
                    print("Заказ принят!")
                    print("Имя:", name)
                    print("Телефон:", phone)
                    print("Адрес:", address)
                    print("Ожидаемое время доставки: 45-60 минут.")

                    global_order = []
                else:
                    print("Заказ не оформлен. Корзина сохранена.")

            global_current_state = STATE_MAIN_MENU
            break


def process_state_booking_table():
    global global_current_state

    print()
    print("Бронирование столика")

    name = input_not_empty("Ваше имя: ")
    phone = input_phone("Ваш телефон: ")
    guests_count = input_int("Сколько будет гостей? ", 1, 12)
    day = input_int("На какое число месяца бронируем? ", 1, 31)
    hour = input_int("Во сколько часов? Ресторан работает с 10 до 22: ", 10, 22)

    print()
    print("Столик забронирован!")
    print("Гость:", name)
    print("Телефон:", phone)
    print("Количество гостей:", guests_count)
    print("Дата: " + str(day) + " число, " + str(hour) + ":00")
    print("Если планы изменятся, пожалуйста, позвоните в ресторан.")

    input("Нажмите <Enter>, чтобы вернуться в главное меню")
    global_current_state = STATE_MAIN_MENU


def process_state_read_comments():
    global global_current_state

    print()
    print("Отзывы гостей")

    for i in range(len(comments)):
        print(str(i + 1) + ") " + comments[i])

    input("Нажмите <Enter>, чтобы вернуться в главное меню")
    global_current_state = STATE_MAIN_MENU


def process_state_exit():
    print()
    print("Спасибо, что пользовались системой ресторана '" + restaurant_name + "'.")
    print("Хорошего дня!")


# Главный цикл программы
is_run = True

while is_run == True:
    if global_current_state == STATE_START:
        process_state_start()
    elif global_current_state == STATE_MAIN_MENU:
        process_state_main_menu()
    elif global_current_state == STATE_PRODUCTS_MENU:
        process_state_products_menu()
    elif global_current_state == STATE_ORDER:
        process_state_order()
    elif global_current_state == STATE_BOOKING_TABLE:
        process_state_booking_table()
    elif global_current_state == STATE_READ_COMMENTS:
        process_state_read_comments()
    elif global_current_state == STATE_EXIT:
        process_state_exit()
        is_run = False
