str11 = ["h", "e", "l", "l", "o"]
str22 = "hello"  # [104, 101, 108, 108, 111]

# str22 = str22[:2] + "X" + str22[2:]
# print(str22)

str22 = str22[0:1] + str22[2 : len(str22)]
print(str22)

# str22 += "!!!"

# print(str22)

# for i in range(len(str22)):
#     if str22[i] >= "l":
#         print(str22[i], end="")

# str22[0] = "x"
# print(str22)

# str33 = "x" + str22[1:]
# print(str33)
