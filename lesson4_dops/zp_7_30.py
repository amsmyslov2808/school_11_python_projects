i = 0
count_total_people = 0
current_birth_year = 0
count_people_before_1985 = 0
count_people_after_1990 = 0

count_total_people = int(input("введите кол-во людей в группе: "))

while i < count_total_people:
    i += 1
    current_birth_year = int(input(f"введите год рождения {i} человека: "))

    if current_birth_year < 1985:
        count_people_before_1985 += 1
    elif current_birth_year > 1990:
        count_people_after_1990 += 1

print(f"кол-во людей родившихся до 1985 = {count_people_before_1985}")
print(f"кол-во людей родившихся после 1990 = {count_people_after_1990}")
