import random

ALIVE_SHIP = "K"
DEAD_SHIP = "X"
MISS_CELL = "O"
EMPTY_CELL = "."

USER_PLAYER = "игрок 😊"
COMP_PLAYER = "компьютер 🤖"


def input_int(message, left_side, right_side):
    is_correct_input = False
    value = 0

    while is_correct_input == False:
        try:
            value = int(input(message))
            if value >= left_side and value <= right_side:
                is_correct_input = True
            else:
                print(
                    f"Ошибка. Значение вышло за границы от {left_side} до {right_side}."
                )
        except:
            print("Ошибка. Вы ввели НЕ число.")

    return value


def create_empty_field(field, size_field):
    for i in range(size_field):
        field.append([])
        for j in range(size_field):
            field[i].append(EMPTY_CELL)


def place_alive_ships(field, size_field, count_alive_ships):
    for _ in range(count_alive_ships):
        i_ship = 0
        j_ship = 0
        is_correct_place = False

        while is_correct_place == False:
            i_ship = random.randint(0, size_field - 1)
            j_ship = random.randint(0, size_field - 1)

            if field[i_ship][j_ship] == EMPTY_CELL:
                is_correct_place = True

        field[i_ship][j_ship] = ALIVE_SHIP


def get_first_step_player():
    current_player = ""

    if random.randint(1, 1000) <= 500:
        current_player = USER_PLAYER
        print()
        print("Первым ходит игрок 😊")
    else:
        current_player = COMP_PLAYER
        print()
        print("Первым ходит компьютер 🤖")

    return current_player


def print_devider(sign_devider):
    print()
    print(sign_devider * 20)
    print()


def print_open_field(field, size_field, message):
    print(message)
    for i in range(size_field):
        for j in range(size_field):
            print(f"{field[i][j]:2}", end="")
        print()


def print_closed_field(field, size_field, message):
    print(message)
    for i in range(size_field):
        for j in range(size_field):
            if field[i][j] == ALIVE_SHIP:
                print(f"{EMPTY_CELL:2}", end="")
            else:
                print(f"{field[i][j]:2}", end="")
        print()


def print_and_change_current_round(current_round):
    current_round += 1
    print(f"Раунд {current_round}")

    return current_round


def is_correct_shoot(field, i_shoot, j_shoot):
    return (
        field[i_shoot][j_shoot] == ALIVE_SHIP or field[i_shoot][j_shoot] == EMPTY_CELL
    )


def wait_enter():
    print()
    input("Для продолжения нажмите клавишу <Enter>")


def get_winner(user_count_alive_ships, comp_count_alive_ships):
    winner_player = ""

    if user_count_alive_ships == 0:
        winner_player = COMP_PLAYER
    elif comp_count_alive_ships == 0:
        winner_player = USER_PLAYER

    return winner_player


repeat_answer = "y"

while repeat_answer == "y":

    user_count_alive_ships = 0
    comp_count_alive_ships = 0

    user_field = []
    comp_field = []

    current_player = ""
    winner_player = ""

    size_field = input_int("Введите размеры игрового поля (от 3 до 10): ", 3, 10)
    user_count_alive_ships = comp_count_alive_ships = size_field

    create_empty_field(user_field, size_field)
    create_empty_field(comp_field, size_field)

    place_alive_ships(user_field, size_field, user_count_alive_ships)
    place_alive_ships(comp_field, size_field, comp_count_alive_ships)

    current_player = get_first_step_player()

    is_playing = True
    current_round = 0

    print_devider("*")

    while is_playing == True:
        current_round = print_and_change_current_round(current_round)

        print_devider("=")

        print_open_field(user_field, size_field, "Поле игрока 😊:")

        print_devider("-")

        print_closed_field(comp_field, size_field, "Поле компьютера 🤖:")

        print_devider("=")

        if current_player == USER_PLAYER:
            print("Ход игрока 😊:")

            is_correct_input = False

            while is_correct_input == False:
                i_shoot = (
                    input_int("Введите номер строки для выстрела: ", 1, size_field) - 1
                )

                j_shoot = (
                    input_int("Введите номер столбца для выстрела: ", 1, size_field) - 1
                )

                is_correct_input = is_correct_shoot(comp_field, i_shoot, j_shoot)

                if is_correct_input == False:
                    print("Ошибка. Вы уже стреляли в эту клетку.")

            if comp_field[i_shoot][j_shoot] == ALIVE_SHIP:
                comp_field[i_shoot][j_shoot] = DEAD_SHIP
                comp_count_alive_ships -= 1
                print()
                print("Поздравляем. Вы попали в корабль. 🍾")

            elif comp_field[i_shoot][j_shoot] == EMPTY_CELL:
                comp_field[i_shoot][j_shoot] = MISS_CELL
                current_player = COMP_PLAYER
                print()
                print("К сожалению вы промахнулись. 😭")

        elif current_player == COMP_PLAYER:
            print("Ход компьютера 🤖:")

            wait_enter()

            is_correct_input = False

            while is_correct_input == False:
                i_shoot = random.randint(0, size_field - 1)
                j_shoot = random.randint(0, size_field - 1)

                is_correct_input = is_correct_shoot(user_field, i_shoot, j_shoot)

            print()
            print(f"Комп выстрелил по координатам ({i_shoot+1}; {j_shoot+1})")

            if user_field[i_shoot][j_shoot] == ALIVE_SHIP:
                user_field[i_shoot][j_shoot] = DEAD_SHIP
                user_count_alive_ships -= 1
                print()
                print("К сожалению компьютер попал в корабль игрока. 😭")

            elif user_field[i_shoot][j_shoot] == EMPTY_CELL:
                user_field[i_shoot][j_shoot] = MISS_CELL
                current_player = USER_PLAYER
                print()
                print("Урааа!! Компьютер промахнулся. 🍾")

        winner_player = get_winner(user_count_alive_ships, comp_count_alive_ships)

        if winner_player != "":
            is_playing = False

        wait_enter()

        print_devider("*")

    print(f"Игра окончена. Победил {winner_player}")

    print_devider("=")

    print_open_field(user_field, size_field, "Поле игрока 😊:")
    print_devider("-")
    print_open_field(comp_field, size_field, "Поле компьютера 🤖:")

    print_devider("=")

    repeat_answer = input("Хотите сыграть ещё раз? (y - да / n - нет): ")
