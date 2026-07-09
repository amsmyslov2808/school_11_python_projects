import random

salaries = []

# salaries.append(123)
# salaries.append(343)
# salaries.append(324)

# print(salaries[0])
# print(salaries[1])

for _ in range(10):
    salaries.append(random.randint(1, 100))

print(salaries)

salaries.insert(1, 999)
# salaries.pop(0)
# salaries[0] = 999

print(salaries)

# count_chet = 0

# for i in range(len(salaries)):
#     if salaries[i] % 2 == 0:
#         print(f"{salaries[i]} ", end="")
#         count_chet += 1

# print(f"\ncount_chet = {count_chet}\n")

# count_ne_chet = 0

# for i in range(len(salaries)):
#     if salaries[i] % 2 != 0:
#         print(f"{salaries[i]} ", end="")
#         count_ne_chet += 1

# print(f"\ncount_ne_chet = {count_ne_chet}")
