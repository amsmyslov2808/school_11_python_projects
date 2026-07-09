# 1 вариант
# def print_stars(count_rows, count_cols):
#     for _ in range(count_rows):
#         for _ in range(count_cols):
#             print("*", end="")
#         print()


# 2 вариант
# def print_stars(count_rows, count_cols):
#     for _ in range(count_rows):
#         print("*" * count_cols)


# 3 вариант
def print_row(count_stars):
    print("* " * count_stars)


def print_stars(count_rows, count_cols):
    for _ in range(count_rows):
        print_row(count_cols)


print_stars(3, 10)
