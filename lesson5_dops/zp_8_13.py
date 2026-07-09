import random

current_mark = 0
total_count_5 = 0
current_count_3 = 0

count_2_lesson_1 = 0
count_2_lesson_2 = 0
count_2_lesson_3 = 0

for i in range(1, 5 + 1):
    current_count_3 = 0

    print(f"ученик № {i:3d}: ", end="")
    for j in range(1, 3 + 1):
        current_mark = random.randint(2, 5)
        print(f"{current_mark:3d}", end="")

        if current_mark == 5:
            total_count_5 += 1

        if current_mark == 3:
            current_count_3 += 1

        if current_mark == 2 and j == 1:
            count_2_lesson_1 += 1

        if current_mark == 2 and j == 2:
            count_2_lesson_2 += 1

        if current_mark == 2 and j == 3:
            count_2_lesson_3 += 1

    print(f"\tкол-во троек у текущего ученика = {current_count_3}", end="")
    print()

print()

print(f"Общее кол-во оценок 5 = {total_count_5}")

print(f"Общее кол-во оценок 2 по первому предмету = {count_2_lesson_1}")
print(f"Общее кол-во оценок 2 по второму предмету = {count_2_lesson_2}")
print(f"Общее кол-во оценок 2 по третьему предмету = {count_2_lesson_3}")
