arr2d = []
n = 5
m = 5

for i in range(n):
    arr2d.append([])
    for j in range(m):
        if j >= i:
            arr2d[i].append(1)
        else:
            arr2d[i].append(0)

for i in range(n):
    for j in range(m):
        print(f"{arr2d[i][j]:<4}", end="")
    print()
