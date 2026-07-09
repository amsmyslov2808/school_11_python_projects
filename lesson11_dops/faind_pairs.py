import random

carta = [
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
]
hisla = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]
STOLBU = 10
STROKU = 2
i_ship = 0
parra = 10
naideno_parr = 0
col = 0
print("привет! ты должен собрать одинаковые карты 🃏")
for i in range(STROKU):
    for j in range(STOLBU):
        print(carta[i][j], end=" ")
    print()
    print()
for y in range(STOLBU):
    is_correct_rand = False
    while is_correct_rand == False:
        is_correct_rand = True
        i_ship = random.randint(0, STROKU - 1)
        j_ship = random.randint(0, STOLBU - 1)
        if hisla[i_ship][j_ship] != ".":
            is_correct_rand = False
    hisla[i_ship][j_ship] = y

for y in range(STOLBU):
    is_correct_rand = False
    while is_correct_rand == False:
        is_correct_rand = True
        i_ship = random.randint(0, STROKU - 1)
        j_ship = random.randint(0, STOLBU - 1)
        if hisla[i_ship][j_ship] != ".":
            is_correct_rand = False
    hisla[i_ship][j_ship] = y


while naideno_parr < parra:
    is_correct_player = False
    while is_correct_player == False:
        is_correct_player = True
        print("введите кординаты для 1⃣  карты  ")
        i_shoot = int(input("Введите номер строки для открытия : ")) - 1
        j_shoot = int(input("Введите номер столбца для открытия: ")) - 1
        if carta[i_shoot][j_shoot] == "✅ ":
            print("эта карта уже открыта")
            is_correct_player = False

    carta[i_shoot][j_shoot] = hisla[i_shoot][j_shoot]

    for i in range(STROKU):
        for j in range(STOLBU):
            print(carta[i][j], end=" ")
        print()
        print()

    is_correct_player = False
    while is_correct_player == False:
        is_correct_player = True
        print("введите кординаты для 2⃣  карты ")
        i_shoot2 = int(input("Введите номер строки для открытия: ")) - 1
        j_shoot2 = int(input("Введите номер столбца для открытия: ")) - 1
        if carta[i_shoot2][j_shoot2] == "✅ ":
            print("эта карта уже открыта")
            is_correct_player = False
        elif i_shoot2 == i_shoot and j_shoot2 == j_shoot:
            print("ты ввёл теже кординаты")
            is_correct_player = False

    carta[i_shoot2][j_shoot2] = hisla[i_shoot2][j_shoot2]

    for i in range(STROKU):
        for j in range(STOLBU):
            print(carta[i][j], end=" ")
        print()
        print()

    if carta[i_shoot][j_shoot] == carta[i_shoot2][j_shoot2]:
        col += 1
        naideno_parr += 1
        print("урраааа ты нашёл карту 🔥 ")
        print()
        print("===" * 20)
        print()
        carta[i_shoot][j_shoot] = "✅ "
        carta[i_shoot2][j_shoot2] = "✅ "
    else:
        col += 1
        print("ты не угодал карту 😭")
        print()
        print("===" * 20)
        print()
        carta[i_shoot][j_shoot] = "⬛ "
        carta[i_shoot2][j_shoot2] = "⬛ "

    for i in range(STROKU):
        for j in range(STOLBU):
            print(carta[i][j], end=" ")
        print()
        print()


print("поздровляю ты выйграл ✨")
print(f"тебе потребовалось {col} ходов для выйгрыша 🤩")
