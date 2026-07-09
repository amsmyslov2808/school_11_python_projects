import math


def get_length(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


# x1 = y1 = x2 = y2 = x3 = y3 = 0
# x1 = int(input("x1: "))

perimeter = get_length(1, 1, 3, 6) + get_length(3, 6, 7, 2) + get_length(1, 1, 7, 2)

print(f"perimeter = {perimeter:.2f}")

# perimeter = get_length(x1=1, y1=1, x2=3, y2=6)
# perimeter = get_length(x1=1, x2=3, y1=1, y2=6)
