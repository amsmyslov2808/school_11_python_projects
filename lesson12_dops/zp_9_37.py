word = "яблоко"

print(word[::-1])
print(word[3:] + word[:3])

part1 = ""
part2 = ""

center = len(word) // 2

for i in range(center):
    part1 += word[i + center]
    part2 += word[i]

print(part1 + part2)
