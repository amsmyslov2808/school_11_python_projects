stage = 0
N = 100
distance_from_home = 0
total_distance = 0

while stage < N:
    stage += 1

    current_distance = 1 / stage

    if stage % 2 != 0:
        distance_from_home += current_distance
    else:
        distance_from_home -= current_distance

    total_distance += current_distance

print(f"дистанция от дома = {distance_from_home:.2f}")
print(f"общая дистанция = {total_distance:.2f}")
