import random

count_workers = int(input("введите кол-во ваших сотрудников:  "))

salaries = []

for _ in range(count_workers):
    salaries.append(random.randint(50000, 150000))

for i in range(count_workers):
    print(f"Сотрудник № {i+1} зп - {salaries[i]} руб.")

print("===========")

print("сотрудники с зп больше 100 тыс. руб.")

for i in range(count_workers):
    if salaries[i] > 100_000:
        print(f"Сотрудник № {i+1} зп - {salaries[i]} руб.")

print("===========")

print("увеличить зп сотрудников на 10% у которох зп меньше 100 тыс. руб.")

for i in range(count_workers):
    if salaries[i] < 100_000:
        salaries[i] = salaries[i] + salaries[i] * 0.1

for i in range(count_workers):
    print(f"Сотрудник № {i+1} зп - {salaries[i]} руб.")
