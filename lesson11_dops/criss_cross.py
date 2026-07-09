import random

repeat_answer = "y"

while repeat_answer == "y":

    CRISS_SYMBOL = "X"
    CROSS_SYMBOL = "O"
    EMPTY_CELL = "."

    SIZE_FIELD = 3

    PLAYER_X = "Игрок X"
    PLAYER_O = "Игрок O"
    DRAW = "Ничья"

    field = []

    current_player = ""
    winner_player = ""

    current_symbol = ""

    current_round = 0
    filled_cells = 0

    for i in range(SIZE_FIELD):
        field.append([])
        for j in range(SIZE_FIELD):
            field[i].append(EMPTY_CELL)

    if random.randint(1, 1000) <= 500:
        current_player = PLAYER_X
        current_symbol = CRISS_SYMBOL
    else:
        current_player = PLAYER_O
        current_symbol = CROSS_SYMBOL

    print()
    print(f"Первым ходит {current_player}")
    print()

    is_playing = True

    while is_playing == True:
        current_round += 1
        print(f"Раунд {current_round}")

        print()
        print("-" * 20)
        print()

        for i in range(SIZE_FIELD):
            for j in range(SIZE_FIELD):
                if j < SIZE_FIELD - 1:
                    print(f" {field[i][j]} │", end="")
                else:
                    print(f" {field[i][j]}", end="")
            print()
            if i < SIZE_FIELD - 1:
                print("───┼───┼───")

        print()
        print("-" * 20)
        print()

        print(f"Сейчас ходит {current_player}")

        is_correct_input = False

        while is_correct_input == False:
            try:
                i_symbol = int((input("Введите номер строки (1-3): "))) - 1
                j_symbol = int((input("Введите номер столбца (1-3): "))) - 1

                if (
                    i_symbol >= 0
                    and i_symbol <= SIZE_FIELD - 1
                    and j_symbol >= 0
                    and j_symbol <= SIZE_FIELD - 1
                ):
                    if field[i_symbol][j_symbol] == EMPTY_CELL:
                        is_correct_input = True
                    else:
                        print("Ошибка. Клетка уже заполнена.")
                else:
                    print("Ошибка. Вы ввели клетку за пределами поля.")
            except:
                print("Ошибка. Вы ввели не число.")

        field[i_symbol][j_symbol] = current_symbol
        filled_cells += 1

        print()
        print("*" * 20)
        print()

        if current_player == PLAYER_X:
            current_player = PLAYER_O
            current_symbol = CROSS_SYMBOL

        elif current_player == PLAYER_O:
            current_player = PLAYER_X
            current_symbol = CRISS_SYMBOL

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
            is_playing = False
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
            is_playing = False
        elif filled_cells == 9:
            winner_player = DRAW
            is_playing = False

    print()
    print("-" * 20)
    print()

    for i in range(SIZE_FIELD):
        for j in range(SIZE_FIELD):
            if j < SIZE_FIELD - 1:
                print(f" {field[i][j]} │", end="")
            else:
                print(f" {field[i][j]}", end="")
        print()
        if i < SIZE_FIELD - 1:
            print("───┼───┼───")

    print()
    print("-" * 20)
    print()

    if winner_player != DRAW:
        print(f"Игра окончена. Победил {winner_player}")
    else:
        print(f"Игра окончена. {winner_player}")

    print()
    print("=" * 20)
    print()

    repeat_answer = input("Хотите сыграть ещё раз? (y - да / n - нет): ")


print()
print("Спасибо за игру. (c) by Rayman208")
