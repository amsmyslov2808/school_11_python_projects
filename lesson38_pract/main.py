from tamagochi import Tamagochi

tamagochi = Tamagochi("Тузик")

while tamagochi.is_dead() == False:
    print()
    tamagochi.print_info()
    print()

    print("Выберите действие:")
    print("1. Поиграть")
    print("2. Покормить")
    print("3. Уложить спать")
    print("4. Сменить имя")
    print("0. Выйти из игры")
    choosen_action = int(input("Напишите номер действия: "))

    print()

    if choosen_action == 1:
        tamagochi.play()
    elif choosen_action == 2:
        tamagochi.feed()
    elif choosen_action == 3:
        tamagochi.sleep()
    elif choosen_action == 4:
        name = input("Введите новое имя питомца: ")
        tamagochi.set_name(name)
    elif choosen_action == 0:
        exit(0)

    print()
    print("Для продолжения нажмите клавишу <enter>")
    input()
