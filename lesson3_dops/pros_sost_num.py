import math

number = 8
count_delit = 0
i = 2

sqrt_number = math.sqrt(number)
# while i <= number - 1:
while i <= sqrt_number:
    if number % i == 0:
        count_delit += 1
        break
    i += 1


if count_delit == 0:
    print("prost")
else:
    print("sost")
