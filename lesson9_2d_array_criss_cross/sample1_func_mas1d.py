import random

arr = []
arr_count = 100

for _ in range(arr_count):
    arr.append(random.randint(1, 10))

print(arr)

print(f"min = {min(arr)}")
print(f"max = {max(arr)}")
print(f"sum = {sum(arr)}")
print(f"avg = {sum(arr)/len(arr)}")

arr.reverse()
print(f"index 5 = {len(arr)-arr.index(5)-1}")
arr.reverse()

# arr.reverse()
# arr.sort()
# arr.sort(reverse=True)
# print(arr)

# arr_sort = sorted(arr, reverse=True)

# print(arr)
# print(arr_sort)

# is_exist = False
# index_exist = -1
# find_elem = 5
# for i in range(len(arr)):
#     if arr[i] == find_elem:
#         index_exist = i
#         is_exist = True
#         break

# for i in range(len(arr) - 1, -1, -1):
#     if arr[i] == find_elem:
#         index_exist = i
#         is_exist = True
#         break

# print(is_exist)
# print(index_exist)


# val = 4

# if val % 2 == 0:
#     print("chet")
# else:
#     print("NE chet")
