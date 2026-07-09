# arr2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rows_count = 3
# cols_count = 3

# for i in range(rows_count):
#     for j in range(cols_count):
#         print(f"{arr2d[i][j]} ", end="")
#     print()

# arr2d = [[1, 2, 3, 5], [4], [7, 8]]
# rows_count = 3
# # cols_count = 3

# for i in range(rows_count):
#     for j in range(len(arr2d[i])):
#         print(f"{arr2d[i][j]} ", end="")
#     print()

import random

arr2d = []
rows_count = 3
cols_count = 3

# for i in range(10):
#     arr2d.append(random.randint(1,100))

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        val = int(input("ddddd: "))
        arr2d[i].append(val)
        # arr2d[i].append(random.randint(1, 100))

for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()
