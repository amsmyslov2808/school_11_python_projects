count_in_lines = []

with open("test.txt", "r", encoding="utf-8") as file:
    for line in file:
        clear_line = line.strip()
        print(f"{clear_line} - {len(clear_line)}")

        count_in_lines.append(len(clear_line))

print(count_in_lines)

# all_text = ""

# with open("test.txt", "r", encoding="utf-8") as file:
#     all_text = file.read()


# all_clear_lines = all_text.splitlines()

# for line in all_clear_lines:
#     print(f"{line} - {len(line)}")
