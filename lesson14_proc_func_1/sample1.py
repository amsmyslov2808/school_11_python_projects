def input_int(message, left_side, right_side):
    is_correct_input = False
    value = 0

    while is_correct_input == False:
        try:
            value = int(input(message))
            if value >= left_side and value <= right_side:
                is_correct_input = True
            else:
                print(f"Ошибка. Число вышло за границы от {left_side} до {right_side}.")
        except:
            print("Ошибка. Вы ввели НЕ число.")

    return value


def get_sum(a, b):
    return a + b


def print_summa(summa):
    print(f"summa = {summa}")


a = input_int("a: ", 1, 1000)
b = input_int("b: ", 1, 1000)

summa = get_sum(a, b)

print_summa(summa)
