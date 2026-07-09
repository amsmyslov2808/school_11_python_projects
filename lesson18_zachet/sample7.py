age = int(input("age: "))

if age >= 0 and age < 7:
    print("go to детский сад")
elif age >= 7 and age < 18:
    print("go to школа")
elif age >= 18 and age <= 25:
    print("go to университет")
else:
    print("неизвестный науке возраст")
