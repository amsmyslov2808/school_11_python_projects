import random

array = []
count_elems = 14
sum_elems_less_20 = 0

for i in range(count_elems):
    array.append(random.randint(1, 100))

print(array)

for i in range(count_elems):
    if array[i] <= 20:
        sum_elems_less_20 += array[i]
