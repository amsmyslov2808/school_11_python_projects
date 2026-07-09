# i = 1

# while i <= 10:
#     print(i)
#     i += 1


# for i in range(1, 11 + 1, 2):
#     print(i)

# for i in range(10, 0 - 1, -1):
#     print(i)

# number = int(input("введите число для определения простое оно или составное: "))
# is_complex = False

# for i in range(2, number):
#     if number % i == 0:
#         is_complex = True
#         break

# if is_complex == True:
#     print("число составное")
# else:
#     print("число простое")

for i in range(1, 25 + 1):
    if i == 5 or i == 7 or i == 11:
        continue

    print(i)
