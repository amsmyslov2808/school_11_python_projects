import random

array = []
count_elems = 10

for i in range(count_elems):
    array.append(random.randint(10))

for i in range(count_elems):
    if array[i] >= 0:
        # print(array[i])
        print(i)
