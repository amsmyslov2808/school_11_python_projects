left_side = 1
right_side = 100
user_number = 0

is_correct_input = False

while is_correct_input == False:
    user_number = int(input(f"введите от {left_side} до {right_side}: "))

    if user_number >= left_side and user_number <= right_side:
        is_correct_input = True
    else:
        print(f"Ошибка ввода. Границы должны быть от {left_side} до {right_side}")

print(f"вы ввели {user_number}")
