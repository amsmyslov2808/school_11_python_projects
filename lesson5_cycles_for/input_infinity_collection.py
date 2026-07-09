current_temp = 0
is_warm_day = True
sum_temps = 0
day_number = 0
avg_temp = 0


while is_warm_day == True:
    day_number += 1
    current_temp = int(
        input(f"введите температуру {day_number} дня (для выхода напишите 0): ")
    )

    if current_temp > 0:
        sum_temps += current_temp
    else:
        is_warm_day = False
        day_number -= 1

avg_temp = sum_temps / day_number

print(f"Всего было {day_number} тёплых дней. Средня температура = {avg_temp:.2f}")
