msg = input("Введите сообщение: ").lower()

roots = ["хуй", "пизд", "сука", "бля", "еб", "ёб"]

for root in roots:
    msg = msg.replace(root, "***")

print("Результат:", msg)
