def print_n_hello(n):
    print(f"{n} - hello")

    if n > 0:
        print_n_hello(n - 1)

    print(f"return {n}")


print_n_hello(10)
