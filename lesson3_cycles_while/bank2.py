money = 1000
percent = 10

finish_money = 10000
year = 0

while money < finish_money:
    money = money + (money * percent / 100)
    year += 1

    print(f"текущий год = {year} текущий вклад = {money:.2f}")

print(f"после {year} лет вклад = {money:.2f}")
