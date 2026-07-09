import random

CRISS_SYMBOL = "X"
CROSS_SYMBOL = "O"
EMPTY_CELL = "."

SIZE_FIELD = 3

PLAYER_X = "Игрок X"
PLAYER_O = "Игрок O"
DRAW = "Ничья"


def create_and_fill_field(field):
    for i in range(SIZE_FIELD):
        field.append([])
        for j in range(SIZE_FIELD):
            field[i].append(EMPTY_CELL)


def get_first_step_player():
    current_player = ""
    current_symbol = ""

    if random.randint(1, 1000) <= 500:
        current_player = PLAYER_X
        current_symbol = CRISS_SYMBOL
    else:
        current_player = PLAYER_O
        current_symbol = CROSS_SYMBOL

    return current_player, current_symbol


def print_first_step_player(current_player):
    print()
    print(f"Первым ходит {current_player}")
    print()


def print_current_step_player(current_player):
    print(f"Сейчас ходит {current_player}")


def print_devider(sign_devider):
    print()
    print(sign_devider * 20)
    print()


def print_and_change_current_round(current_round):
    current_round += 1
    print(f"Раунд {current_round}")

    return current_round


def print_game_field(field):
    for i in range(SIZE_FIELD):
        for j in range(SIZE_FIELD):
            if j < SIZE_FIELD - 1:
                print(f" {field[i][j]} │", end="")
            else:
                print(f" {field[i][j]}", end="")
        print()
        if i < SIZE_FIELD - 1:
            print("───┼───┼───")


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


def is_empty_cell(field, i_symbol, j_symbol):
    return field[i_symbol][j_symbol] == EMPTY_CELL


def change_current_player(current_player):
    current_symbol = ""

    if current_player == PLAYER_X:
        current_player = PLAYER_O
        current_symbol = CROSS_SYMBOL
    elif current_player == PLAYER_O:
        current_player = PLAYER_X
        current_symbol = CRISS_SYMBOL

    return current_player, current_symbol


def inc_filled_cells(filled_cells):
    return filled_cells + 1


def fill_cell(field, i_symbol, j_symbol, current_symbol):
    field[i_symbol][j_symbol] = current_symbol


def get_winner(field, filled_cells):
    winner_player = ""

    if (
        field[0][0] == CRISS_SYMBOL
        and field[0][1] == CRISS_SYMBOL
        and field[0][2] == CRISS_SYMBOL
        or field[1][0] == CRISS_SYMBOL
        and field[1][1] == CRISS_SYMBOL
        and field[1][2] == CRISS_SYMBOL
        or field[2][0] == CRISS_SYMBOL
        and field[2][1] == CRISS_SYMBOL
        and field[2][2] == CRISS_SYMBOL
        or field[0][0] == CRISS_SYMBOL
        and field[1][0] == CRISS_SYMBOL
        and field[2][0] == CRISS_SYMBOL
        or field[0][1] == CRISS_SYMBOL
        and field[1][1] == CRISS_SYMBOL
        and field[2][1] == CRISS_SYMBOL
        or field[0][2] == CRISS_SYMBOL
        and field[1][2] == CRISS_SYMBOL
        and field[2][2] == CRISS_SYMBOL
        or field[0][0] == CRISS_SYMBOL
        and field[1][1] == CRISS_SYMBOL
        and field[2][2] == CRISS_SYMBOL
        or field[0][2] == CRISS_SYMBOL
        and field[1][1] == CRISS_SYMBOL
        and field[2][0] == CRISS_SYMBOL
    ):
        winner_player = PLAYER_X
    elif (
        field[0][0] == CROSS_SYMBOL
        and field[0][1] == CROSS_SYMBOL
        and field[0][2] == CROSS_SYMBOL
        or field[1][0] == CROSS_SYMBOL
        and field[1][1] == CROSS_SYMBOL
        and field[1][2] == CROSS_SYMBOL
        or field[2][0] == CROSS_SYMBOL
        and field[2][1] == CROSS_SYMBOL
        and field[2][2] == CROSS_SYMBOL
        or field[0][0] == CROSS_SYMBOL
        and field[1][0] == CROSS_SYMBOL
        and field[2][0] == CROSS_SYMBOL
        or field[0][1] == CROSS_SYMBOL
        and field[1][1] == CROSS_SYMBOL
        and field[2][1] == CROSS_SYMBOL
        or field[0][2] == CROSS_SYMBOL
        and field[1][2] == CROSS_SYMBOL
        and field[2][2] == CROSS_SYMBOL
        or field[0][0] == CROSS_SYMBOL
        and field[1][1] == CROSS_SYMBOL
        and field[2][2] == CROSS_SYMBOL
        or field[0][2] == CROSS_SYMBOL
        and field[1][1] == CROSS_SYMBOL
        and field[2][0] == CROSS_SYMBOL
    ):
        winner_player = PLAYER_O
    elif filled_cells == 9:
        winner_player = DRAW

    return winner_player


def print_winner(winner_player):
    if winner_player != DRAW:
        print(f"Игра окончена. Победил {winner_player}")
    else:
        print(f"Игра окончена. {winner_player}")


def get_repeat_answer():
    return input("Хотите сыграть ещё раз? (y - да / n - нет): ")


def print_thank_phrase():
    print()
    print("Спасибо за игру. (c) by Rayman208")


# def create_arr(count):
#     return [0] * count

# arr = create_arr(10)


repeat_answer = "y"

while repeat_answer == "y":

    field = []

    current_player = ""
    winner_player = ""

    current_symbol = ""

    current_round = 0
    filled_cells = 0

    create_and_fill_field(field)

    current_player, current_symbol = get_first_step_player()

    print_first_step_player(current_player)

    is_playing = True

    while is_playing == True:
        current_round = print_and_change_current_round(current_round)

        print_devider("-")
        print_game_field(field)
        print_devider("-")

        print_current_step_player(current_player)

        is_correct_input = False
        while is_correct_input == False:
            i_symbol = input_int("Введите номер строки (1-3): ", 1, 3) - 1
            j_symbol = input_int("Введите номер столбца (1-3): ", 1, 3) - 1

            is_correct_input = is_empty_cell(field, i_symbol, j_symbol)

            if is_correct_input == False:
                print("Ошибка. Клетка уже заполнена.")

        fill_cell(field, i_symbol, j_symbol, current_symbol)

        filled_cells = inc_filled_cells(filled_cells)

        print_devider("*")

        current_player, current_symbol = change_current_player(current_player)

        winner_player = get_winner(field, filled_cells)

        if winner_player != "":
            is_playing = False

    print_devider("-")
    print_game_field(field)
    print_devider("-")

    print_winner(winner_player)

    print_devider("=")

    repeat_answer = get_repeat_answer()


print_thank_phrase()
