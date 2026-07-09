# import sys

# sys.setrecursionlimit(5000)


def print_10_hello(i):
    print(f"{i} - hello - down ⬇ ")
    i += 1

    if i < 10:
        print_10_hello(i)

    print(f"{i} - hello - up ⬆ ")


print_10_hello(0)

# i = 0

# while i < 10:
#     print(f"{i} - hello")
#     i += 1
