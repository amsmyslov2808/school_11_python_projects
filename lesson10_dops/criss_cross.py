import random

CRISS_SYMBOL = "X"
CROSS_SYMBOL = "O"
EMPTY_CELL = "."

SIZE_FIELD = 3

PLAYER_X = "player_x"
PLAYER_O = "player_o"
DRAW = "draw"

field = []

current_player = ""
winner_player = ""

current_round = 0
filled_cells = 0

for i in range(SIZE_FIELD):
    field.append([])
    for j in range(SIZE_FIELD):
        field[i].append(EMPTY_CELL)

if random.randint(1, 1000) <= 500:
    current_player = PLAYER_X
    print("Первым ходит X")
else:
    current_player = PLAYER_O
    print("Первым ходит О")

is_playing = True

while is_playing == True:
    current_round += 1

    print(f"Раунд {current_round}\n")

    for i in range(SIZE_FIELD):
        for j in range(SIZE_FIELD):
            print(f"{field[i][j]:2}", end="")
        print()

    if current_player == PLAYER_X:
        print("Сейчас ходит X")

        i_symbol = int((input("введите номер строки: "))) - 1
        j_symbol = int((input("введите номер столбца: "))) - 1

        field[i_symbol][j_symbol] = CRISS_SYMBOL
        filled_cells += 1

        current_player = PLAYER_O

    elif current_player == PLAYER_O:
        print("Сейчас ходит О")

        i_symbol = int((input("введите номер строки: "))) - 1
        j_symbol = int((input("введите номер столбца: "))) - 1

        field[i_symbol][j_symbol] = CROSS_SYMBOL

        current_player = PLAYER_X
        filled_cells += 1

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

print(f"Game is over. Winner {winner_player}")
