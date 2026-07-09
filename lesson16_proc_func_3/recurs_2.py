# 5! = 1 * 2 * 3 * 4 * 5


def get_fact(n):
    if n == 1:
        return 1
    else:
        return n * get_fact(n - 1)


result = get_fact(5)

print(f"5! = {result}")

# result = 1
# i = 1

# while i <= 5:
#     result *= i
#     i += 1

# print(f"5! = {result}")


def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))


print(A(2, 2))
