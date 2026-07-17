arr = [2, 435, 345, 1]

# min_number = arr[0]

# for number in arr:
#     if number < min_number:
#         min_number = number

min_number = arr[0]
index_min_number = 0

for i in range(len(arr)):
    if arr[i] < min_number:
        min_number = arr[i]
        index_min_number = i

# for number in arr:
#     if number < min_number:
#         min_number = number

print(arr)

print(min_number)

print(index_min_number)
