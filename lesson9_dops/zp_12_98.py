import random

arr2d = []

rows_count = 12
cols_count = 4

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        arr2d[i].append(random.randint(1, 6))


for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()

# count_people_in_floor = []
# summa = 0

# for i in range(rows_count):
#     summa = 0
#     for j in range(cols_count):
#         summa += arr2d[i][j]
#     count_people_in_floor.append(summa)

# min_people = min(count_people_in_floor)
# min_people_index = count_people_in_floor.index(min_people)

# print(f"минимальное число людей = {min_people} проживает на этаже {min_people_index+1}")


min_people = 1000
min_people_index = -1
summa = 0

for i in range(rows_count):
    summa = 0
    for j in range(cols_count):
        summa += arr2d[i][j]
    if summa < min_people:
        min_people = summa
        min_people_index = i


print(f"минимальное число людей = {min_people} проживает на этаже {min_people_index+1}")
