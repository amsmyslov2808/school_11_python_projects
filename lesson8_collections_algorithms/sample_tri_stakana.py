import random

count_items = 10
items = []

for _ in range(count_items):
    items.append(random.randint(1, 100))

print(items)

index1 = int(input("введите индекс 1-го элемента для замены: "))
index2 = int(input("введите индекс 2-го элемента для замены: "))

# algorithm

# temp = items[index1]
# items[index1] = items[index2]
# items[index2] = temp

# items[index1], items[index2] = items[index2], items[index1]

# items[index1] = items[index1] + items[index2]
# items[index2] = items[index1] - items[index2]
# items[index1] = items[index1] - items[index2]

print(items)
