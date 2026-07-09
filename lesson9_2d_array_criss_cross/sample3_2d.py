arr2d = []
rows_count = 5
cols_count = 5

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        # if i == j:
        # if i >= j:
        # if i <= j:
        # if i + j == rows_count - 1:
        # if i + j >= rows_count - 1:
        # if i + j <= rows_count - 1:
        # if (i + j) % 2 == 0:
        # if i % 2 == 0:
        # if j % 2 == 0:
        # if i == rows_count // 2 or j == cols_count // 2:
        # if i == rows_count // 2 and j == cols_count // 2:
        # if i == j or i + j == rows_count - 1:
        # if i >= j and i + j >= rows_count - 1 or i <= j and i + j <= rows_count - 1:
        if not (i > j and i + j > rows_count - 1 or i < j and i + j < rows_count - 1):
            arr2d[i].append(1)
        else:
            arr2d[i].append(0)

for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()

summa = 0
for i in range(rows_count):
    for j in range(cols_count):
        if j % 2 == 0:
            summa += arr2d[i][j]
