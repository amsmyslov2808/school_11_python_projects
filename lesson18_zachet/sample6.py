stroka = "hello"

for i in range(len(stroka) - 1, -1, -1):
    print(stroka[i], end="")

stroka = stroka.replace("l", "x")
print(stroka)
