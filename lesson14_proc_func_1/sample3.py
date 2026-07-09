import random


def add_elem_to_end(elem, arr):
    arr.append(elem)


# def random_array(arr, count_elems):
#     for _ in range(count_elems):
#         arr.append(random.randint(1, 100))


def create_array():
    return [3, 4, 5, 6, 23, 23, 23, 23, 54, 56, 67]


arr = create_array()
count_elems = 5

# random_array(arr, count_elems)

print(f"MAIN {arr}")

add_elem_to_end(999, arr)

print(f"MAIN {arr}")
