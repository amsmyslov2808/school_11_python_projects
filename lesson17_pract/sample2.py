prices = []
count_prices = 0

with open("prices.txt", "r", encoding="utf-8") as file_in:
    count_prices = int(file_in.readline())

    for _ in range(count_prices):
        prices.append(int(file_in.readline()))

prices[0] = 1111
prices.append(298374)
prices.append(29234)
prices[2] *= 2
prices.pop(0)

with open("prices.txt", "w", encoding="utf-8") as file_out:
    file_out.write(str(len(prices)) + "\n")

    for price in prices:
        file_out.write(str(price) + "\n")
