import random

salaries = []
count_workers = 5
count_months = 12

for i in range(count_workers):
    salaries.append([])
    for j in range(count_months):
        salaries[i].append(random.randint(50, 150))

for i in range(count_workers):
    for j in range(count_months):
        print(f"{salaries[i][j]:<5} ", end="")
    print()
