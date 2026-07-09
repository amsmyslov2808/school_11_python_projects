all_in_str = input("введите все числа через пробел: ")

# numbers_as_array = all_in_str.split(";")
numbers_as_array = list(map(int, all_in_str.split()))

# for i in range(len(numbers_as_array)):
#     numbers_as_array[i] = int(numbers_as_array[i])

print(numbers_as_array)
