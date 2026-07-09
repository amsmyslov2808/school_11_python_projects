import sys

symbol = input("введите любой символ с клавиатуры: ")

if len(symbol) == 0:
    print("Ошибка ввода. Вы ввели пустую строку. Программа будет закрыта.")
    sys.exit()

if len(symbol) > 1:
    print("Ошибка ввода. Вы ввели слишком много символов. Программа будет закрыта.")
    sys.exit()


if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("это английская буква")
    if symbol >= "a" and symbol <= "z":
        print("маленькая")
    else:
        print("большая")

elif symbol >= "0" and symbol <= "9":
    print("это цифра")
    if ord(symbol) % 2 == 0:
        print("чётная")
    else:
        print("НЕчётная")

else:
    print("это неизвестный символ")
