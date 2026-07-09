import random

arr = []
# arr_count = int(input("arr_count: "))
arr_count = 10

for _ in range(arr_count):
    arr.append(random.randint(1, 100))

print(arr)
