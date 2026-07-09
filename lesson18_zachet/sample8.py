# import math
# from math import sin, cos

n = 283
sum_n_digits = 0

while n > 0:
    last_digit = n % 10
    sum_n_digits += last_digit
    n = n // 10

print(sum_n_digits)


a = 5
b = 10
temp = a
a = b
b = temp
