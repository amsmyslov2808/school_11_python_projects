import requests

url = "https://ccmessangeritog1.onrender.com/send_message"
message_init = "Привет"

for i in range(100):
    message = message_init + str(i)
    response = requests.post(
        url, data={"message": message}, cookies={"username": "Rayman208"}
    )
    print(i + 1, response.status_code)
