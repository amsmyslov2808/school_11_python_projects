login_user_input = input("введите логин привязанный к гугл почте: ")

if login_user_input.endswith("@gmail.com"):
    print("login is correct")
else:
    print("error login")
