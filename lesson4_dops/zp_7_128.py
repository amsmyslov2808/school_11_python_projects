number = int(input("введите число: "))
sum_del = 0

i = 1
right_side = number // 2

while i <= right_side:
    if number % i == 0:
        sum_del += i
    i += 1

if number == sum_del:
    print(f"число {number} совершенное")
else:
    print(f"число {number} НЕ совершенное")
