# for i in range(100, 0, -1):
#     print(i)

# stable_number = 5
# for i in range(1, 11):
#     result = stable_number * i

#     print(stable_number, "*", i, "=", result)

a1 = 4
an = 1000
d = 4
sum_numbers = 0

for i in range(a1, an + d, d):
    sum_numbers += i

print(sum_numbers)
