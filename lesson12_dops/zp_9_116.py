text = "АРГЕНТИНА МАНИТ НЕГРА"

text = text.replace(" ", "")

text_r = text[::-1]

if text == text_r:
    print("палиндром")
else:
    print("НЕ палиндром")
