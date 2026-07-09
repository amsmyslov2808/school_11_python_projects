rainfall = []
count_days = 31
total_sum = 0


for i in range(count_days):
    rainfall[i] = int(input(f"input rainfall for {i+1} day: "))

print(rainfall)

for i in range(count_days):
    total_sum += rainfall[i]

print(total_sum)
