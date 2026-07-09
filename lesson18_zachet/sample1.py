import random

arr = []

COUNT_ELEMS = 10

for _ in range(COUNT_ELEMS):
    arr.append(random.randint(50, 300))

# print(arr)
for i in range(COUNT_ELEMS):
    print(f"{arr[i]} ", end="")

print()

for i in range(COUNT_ELEMS):
    arr[i] = arr[i] * 2

for i in range(COUNT_ELEMS):
    print(f"{arr[i]} ", end="")

print()

arr.pop(1)
arr.pop(2)

COUNT_ELEMS -= 2

for i in range(COUNT_ELEMS):
    print(f"{arr[i]} ", end="")
