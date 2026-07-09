import random

arr2d = []

rows_count = 11
cols_count = 4

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        arr2d[i].append(random.randint(20, 35))


for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()


# summa = arr2d[4][0] + arr2d[4][1] + arr2d[4][2] + arr2d[4][3]
summa = 0

for j in range(cols_count):
    summa += arr2d[4][j]

# for i in range(rows_count):
#     summa += arr2d[i][5]

print(summa)
