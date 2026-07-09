users_countries = ["Россия", "россия", "рОссия", "РоссиЯ"]

print(users_countries[0].lower())

count_from_russia = 0

for i in range(len(users_countries)):
    if users_countries[i].lower() == "Россия".lower():
        count_from_russia += 1

print(f"count from russia = {count_from_russia}")

print(users_countries)
