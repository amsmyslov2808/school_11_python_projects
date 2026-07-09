import random

team_name = input("введите название футбольной команды: ")
print(len(team_name))
print(f"{team_name} - это чемпион")

k = random.randint(0, len(team_name) - 1)
print(f"{team_name[k]}")
