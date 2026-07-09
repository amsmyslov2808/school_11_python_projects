# Константы состояний
STATE_START = 1
STATE_MAIN_MENU = 2
STATE_PRODUCTS_MENU = 3
STATE_BOOKING_TABLE = 4
STATE_READ_COMMENTS = 5
STATE_EXIT = 0

global_current_state = STATE_START


# Функции обработки состояний
def process_state_start():
    global global_current_state

    print("Добро пожаловать в наш ресторан. Здесь вы можете.....")

    input("Для продолжения нажмите <Enter>")

    global_current_state = STATE_MAIN_MENU


def process_state_main_menu():
    global global_current_state

    print("Вы в главном меню. пожалуйста выберете что вы хотите")
    print("1) Изучить меню ресторана")
    print("2) Забронировать столик")
    print("3) Почитать отзывы")
    print("0) Выйти из программы")

    choose = int(input("Ввведите номер выбранного вами варианта: "))

    if choose == 1:
        global_current_state = STATE_PRODUCTS_MENU
    elif choose == 2:
        global_current_state = STATE_BOOKING_TABLE
    elif choose == 3:
        global_current_state = STATE_READ_COMMENTS
    elif choose == 0:
        global_current_state = STATE_EXIT


def process_state_products_menu():
    pass


def process_state_booking_table():
    pass


def process_state_read_comments():
    pass


def process_state_exit():
    print("Спасибо что пользовались системой нашего ресторана")


# Главный цикл программы
is_run = True

while is_run == True:
    if global_current_state == STATE_START:
        process_state_start()
    elif global_current_state == STATE_MAIN_MENU:
        process_state_main_menu()
    elif global_current_state == STATE_PRODUCTS_MENU:
        process_state_products_menu()
    elif global_current_state == STATE_BOOKING_TABLE:
        process_state_booking_table()
    elif global_current_state == STATE_READ_COMMENTS:
        process_state_read_comments()
    elif global_current_state == STATE_EXIT:
        process_state_exit()
        is_run = False
