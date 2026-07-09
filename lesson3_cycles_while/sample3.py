import math

number = -1

while number < 0:
    number = int(input("введи число (>=0) для вычисления из него квадратного корня: "))

    if number < 0:
        print(
            "вы ввели число <0 из такого числа корень вычислить невозможно. введите число ещё раз\n"
        )

result = math.sqrt(number)

print(f"квадратный корень из {number} = {result:.2f}")
