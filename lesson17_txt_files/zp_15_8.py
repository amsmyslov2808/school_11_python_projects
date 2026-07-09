all_lines = []

with open("test.txt", "r", encoding="utf-8") as file:
    all_lines = file.readlines()

print(len(all_lines))
