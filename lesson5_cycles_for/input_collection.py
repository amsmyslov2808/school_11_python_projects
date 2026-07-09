count_marks = 5
i = 0
current_mark = 0
sum_marks = 0
avg_marks = 0


while i < count_marks:
    i += 1

    current_mark = int(input(f"введите {i} оценку из {count_marks}: "))

    sum_marks += current_mark

avg_marks = sum_marks / count_marks

print(f"ваша средняя оценка = {avg_marks:.2f}")
