import random

is_repeat = True

while is_repeat == True:
    comp_number = 0
    user_number = 0
    tries = 0
    level = 0
    left_side = 0
    right_side = 0

    print("выберите уровень сложности: ")
    print("1. лёгкий (от 1 до 10): ")
    print("2. средний (от 1 до 100): ")
    print("3. сложный (от 1 до 1000): ")

    level = int(input("введите номер уровня сложности: "))
    if level == 1:
        print("выбран лёгкий уровень сложности")
        left_side = 1
        right_side = 10
    elif level == 2:
        print("выбран средний уровень сложности")
        left_side = 1
        right_side = 100
    elif level == 3:
        print("выбран тяжёлый уровень сложности")
        left_side = 1
        right_side = 1000
    else:
        print("выбран невыносимый уровень сложности")
        left_side = 1
        right_side = 5000

    comp_number = random.randint(left_side, right_side)

    print(f"Я загадал число от {left_side} до {right_side}. Попробуй отгадай")

    while user_number != comp_number:
        is_correct_input = False
        tries += 1

        while is_correct_input == False:
            user_number = int(
                input(
                    f"попытка №{tries} - введи число от {left_side} до {right_side}: "
                )
            )

            if user_number == 9123:
                print(f"введен секретный ключ. загаданное число = {comp_number}")
            elif user_number >= left_side and user_number <= right_side:
                is_correct_input = True
            else:
                print(
                    f"ошибка ввода. вы вышли за границы отрезка от {left_side} до {right_side}"
                )

        if user_number < comp_number:
            print("введите число побольше")
            left_side = user_number
        elif user_number > comp_number:
            print("введите число поменьше")
            right_side = user_number

    print("поздравляем вы угадали загаданное число")
    print(f"вам понадобилось попыток: {tries}")

    # if 1 <= tries <= 3:
    if tries >= 1 and tries <= 3:
        print("вам тупо повезло")
    elif tries >= 4 and tries <= 7:
        print("вы гений")
    elif tries >= 8 and tries <= 11:
        print("неплохо")
    elif tries >= 12 and tries <= 15:
        print("тренируйся лучше")
    else:
        print("сочувствую")

    answer = input("Классно поиграли. Хочешь ещё раз? (y/n): ")

    if answer != "y":
        is_repeat = False
