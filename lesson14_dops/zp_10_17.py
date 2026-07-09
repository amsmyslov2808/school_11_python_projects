def get_factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


result = (2 * get_factorial(5) + 3 * get_factorial(8)) / (
    get_factorial(6) + get_factorial(4)
)

print(f"result = {result:.2f}")
