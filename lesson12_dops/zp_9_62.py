text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

max_percent = 0
max_letter = ""

for letter_code in range(ord("a"), ord("z") + 1):
    letter = chr(letter_code)

    percent = text.count(letter) / len(text) * 100

    if percent > max_percent:
        max_percent = percent
        max_letter = letter

    print(f"{letter} - {percent:.2f}")

print(f"\n\n{max_letter} - {max_percent:.2f}")

# percent = text.count("o") / len(text) * 100

# print(f"{percent:.2f}")
