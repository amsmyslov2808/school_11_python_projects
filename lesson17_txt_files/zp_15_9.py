all_text = ""

with open("test.txt", "r", encoding="utf-8") as file:
    all_text = file.read()

print(len(all_text) - all_text.count("\n"))
