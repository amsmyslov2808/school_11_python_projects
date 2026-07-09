money = 1000
percent = 10
year = 5

current_year = 0

while current_year < year:
    current_year += 1
    money = money + (money * percent / 100)

    print(f"текущий год = {current_year} текущий вклад = {money:.2f}")

print(f"после {year} лет вклад = {money:.2f}")
