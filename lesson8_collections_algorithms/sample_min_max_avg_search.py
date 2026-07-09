import random

count_marks = 25
marks = []

for _ in range(count_marks):
    marks.append(random.randint(2, 5))

print(marks)

# algorithms
max_mark = marks[0]
min_mark = marks[0]

for i in range(count_marks):
    if marks[i] < min_mark:
        min_mark = marks[i]

for i in range(count_marks):
    if marks[i] > max_mark:
        max_mark = marks[i]

sum_marks = 0
for i in range(count_marks):
    sum_marks += marks[i]
avg_mark = sum_marks / count_marks

count_min_marks = 0
for i in range(count_marks):
    if marks[i] == min_mark:
        count_min_marks += 1

count_max_marks = 0
for i in range(count_marks):
    if marks[i] == max_mark:
        count_max_marks += 1

count_marks_ge_avg = 0
for i in range(count_marks):
    if marks[i] >= avg_mark:
        count_marks_ge_avg += 1

count_marks_l_avg = 0
for i in range(count_marks):
    if marks[i] < avg_mark:
        count_marks_l_avg += 1

print(f"максимальная оценка = {max_mark}")
print(f"минимальная оценка = {min_mark}")
print(f"средняя оценка = {avg_mark:.2f}")

print(f"кол-во учеников с минимальной оценкой = {count_min_marks}")
print(f"кол-во учеников с максимальной оценкой = {count_max_marks}")
print(f"кол-во учеников с оценкой ниже средней = {count_marks_l_avg}")
print(f"кол-во учеников с оценкой выше или равной средней = {count_marks_ge_avg}")
