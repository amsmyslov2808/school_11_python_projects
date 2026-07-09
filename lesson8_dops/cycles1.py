a = 5
arr = []

arr.append(5)
arr.append(65)
arr.append(76)

print(arr[0])

arr[0] = 999
print(arr[0])

print("--------")
print(arr[0])
print(arr[1])
print(arr[2])

print("--------")
i = 0
while i < 3:
    print(arr[i])
    i += 1

print("--------")

for i in range(3):
    print(arr[i])
