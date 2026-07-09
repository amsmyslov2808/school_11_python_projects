# arr2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import random

arr2d = []

rows_count = 3
cols_count = 4

i1 = j1 = i2 = j2 = -1

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        arr2d[i].append(random.randint(1, 10))


for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()

i1 = int(input("введите строку первого элемента: "))
j1 = int(input("введите столбец первого элемента: "))

i2 = int(input("введите строку второго элемента: "))
j2 = int(input("введите столбец второго элемента: "))

summa = arr2d[i1][j1] + arr2d[i2][j2]

print(summa)
