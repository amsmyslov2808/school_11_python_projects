import random

arr2d = []
n = 3
m = 4

for i in range(n):
    arr2d.append([])
    for j in range(m):
        arr2d[i].append(random.randint(10, 99))

for i in range(n):
    for j in range(m):
        print(f"{arr2d[i][j]:<4}", end="")
    print()

summa = 0
for j in range(m):
    summa += arr2d[0][j]

print(f"сумма первой строки = {summa}")

summa = 0
for i in range(n):
    summa += arr2d[i][0]

print(f"сумма первого стролбца = {summa}")

max_elem = arr2d[0][0]
max_elem_i = 0
max_elem_j = 0

for i in range(n):
    for j in range(m):
        if arr2d[i][j] > max_elem:
            max_elem = arr2d[i][j]
            max_elem_i = i
            max_elem_j = j

print(
    f"максимальный элемент лежит по индексам ({max_elem_i};{max_elem_j}) и имеет значение {max_elem}"
)
