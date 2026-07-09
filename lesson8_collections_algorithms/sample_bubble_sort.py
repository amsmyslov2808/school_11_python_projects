import random

count_prices = 5
prices = []

for _ in range(count_prices):
    prices.append(random.randint(100, 1000))

print(prices)

# sort
temp = 0
is_sort = False
offset = 0

while is_sort == False:
    is_sort = True

    for i in range(count_prices - 1 - offset):
        if prices[i + 1] < prices[i]:
            temp = prices[i]
            prices[i] = prices[i + 1]
            prices[i + 1] = temp

            is_sort = False

    offset += 1

print(prices)
