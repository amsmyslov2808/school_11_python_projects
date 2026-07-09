import math


def is_simple(number):
    result = True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            result = False
            break

    return result


for number in range(100, 999 + 1):
    if is_simple(number) == True:
        print(number)
