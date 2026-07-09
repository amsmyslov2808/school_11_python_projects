number = 9384313
count_3 = 0

while number != 0:
    last_digit = number % 10
    # number = number // 10
    number //= 10

    if last_digit == 3:
        count_3 += 1

    print(f"last_digit = {last_digit}")

print(f"count_3 = {count_3}")
