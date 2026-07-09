array = []

array.append(123)  # 0
array.append(234)  # 1
array.append(456)  # 2
array.append(678)  # 3

array.extend([3, 54, 5, 546])

array.insert(1, 999)

print(array)

print(array[1])

array[0] = 999

print(array)

# xxx = array.pop(1)
# array.pop(1)
# print(xxx)

# del array[1]
del array[1:3]

print(array)
