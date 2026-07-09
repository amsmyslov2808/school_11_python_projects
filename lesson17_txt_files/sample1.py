# file = open("test.txt", "w")
# a = 111

# file.write(str(111) + "\n")
# file.write(f"{a}")

# file.close()


file = open("test.txt", "r")

file_lines = file.readlines()

file.close()

for i in range(len(file_lines)):
    file_lines[i] = file_lines[i].strip()

file_lines.pop()

file = open("test.txt", "w")

for line in file_lines:
    file.write(line + "\n")

# file.writelines(file_lines)

file.close()
