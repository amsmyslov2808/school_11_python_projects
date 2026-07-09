import random

array = []
count_elems = 0
required_index = 0

count_elems = random.randint(5, 15)

for _ in range(count_elems):
    array.append(random.randint(1, 100))

# for i in range(count_elems):
#     current_value = int(input(f"введите {i+1} из {count_elems} значение: "))
#     array.append(current_value)

# print(array)

for i in range(count_elems):
    # print(f"{array[i]} ", end="")
    print(f"element index {i} - {array[i]}")

is_correct_input = False

while is_correct_input == False:
    required_index = int(
        input(
            f"ввведите требуемый индекс элемента для вывода (от 0 до {count_elems-1}): "
        )
    )

    if required_index >= 0 and required_index <= count_elems - 1:
        is_correct_input = True
    else:
        print("такого индексе в массиве нет")

print(array[required_index])
