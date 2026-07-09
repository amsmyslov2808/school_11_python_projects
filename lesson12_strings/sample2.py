# login_user_input = "rayman208 "
login_user_input = input("введите логин: ")
login_db = "rayman208"

login_user_input = login_user_input.strip()

if login_user_input == login_db:
    print("auth is correct")
else:
    print("error auth")
