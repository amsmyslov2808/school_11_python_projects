count_days = int(input("введите кол-во наблюдаемых дней: "))
i = 0

current_length = 0
max_length = 0

while i < count_days:
    i += 1
    current_temp = int(input(f"введите температуру {i} дня: "))

    if current_temp > 0:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length

        current_length = 0

if current_length > max_length:
    max_length = current_length

print(f"сама длинная оттепель = {max_length} дней")
