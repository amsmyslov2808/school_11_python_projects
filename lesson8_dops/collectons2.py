import random

salaries = []
salaries_count = 10

for _ in range(salaries_count):
    salaries.append(random.randint(30, 150))

print(salaries)

sum_salaries = 0

for i in range(salaries_count):
    sum_salaries += salaries[i]

print(f"sum salaries = {sum_salaries}")

avg_salaries = sum_salaries / salaries_count

print(f"avg salaries = {avg_salaries:.2f}")

# is_sort = False
# temp = 0
# offset = 0

# while is_sort == False:
#     is_sort = True

#     for i in range(salaries_count - 1 - offset):
#         if salaries[i + 1] < salaries[i]:
#             temp = salaries[i]
#             salaries[i] = salaries[i + 1]
#             salaries[i + 1] = temp

#             is_sort = False

#     offset += 1

# index_min_elem = 0
# min_elem = 0
# temp = 0

# for i in range(salaries_count - 1):
#     index_min_elem = i
#     min_elem = salaries[i]

#     for j in range(i + 1, salaries_count):
#         if salaries[j] < min_elem:
#             min_elem = salaries[j]
#             index_min_elem = j

#     temp = salaries[i]
#     salaries[i] = salaries[index_min_elem]
#     salaries[index_min_elem] = temp

# salaries.sort(reverse=True)

print(salaries)
