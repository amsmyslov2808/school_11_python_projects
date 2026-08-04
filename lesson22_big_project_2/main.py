def print_main_menu():
    pass


def work_with_buyer_menu():
    pass


def auth_is_administrator():
    pass


def work_with_administrator_menu():
    pass


is_run = True

while is_run == True:
    print_main_menu()
    choose_action_main_menu = int(input())

    if choose_action_main_menu == 1:
        work_with_buyer_menu()
    elif choose_action_main_menu == 2:
        if auth_is_administrator() == True:
            work_with_administrator_menu()
        else:
            print("Ошибка ввода пароля администратора")
    elif choose_action_main_menu == 0:
        is_run = False

# kjlsbfkljsd
# setsdklmfnsdlkj
