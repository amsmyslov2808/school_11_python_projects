COUNT_ROWS = 3
COUNT_COLS = 3

EMPTY_CELL = "."

field = []

for i in range(COUNT_ROWS):
    field.append([])

    for j in range(COUNT_COLS):
        field[i].append(EMPTY_CELL)

print(field)
