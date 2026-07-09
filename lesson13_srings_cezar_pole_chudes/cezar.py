ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

original_text = ""
encryption_key = 0

encrypted_text = ""

original_text = input("Введите строку которую вы хотите зашифровать: ")
encryption_key = int(input("Введите ключ для шифрования от 1 до 1000000: "))

encryption_key = encryption_key % len(ALPHABET)

for symbol in original_text:
    original_index_in_alphabet = ALPHABET.find(symbol)

    if original_index_in_alphabet == -1:
        encrypted_text += symbol
    else:
        encrypted_index_in_alphabet = (
            original_index_in_alphabet + encryption_key
        ) % len(ALPHABET)

        encrypted_text += ALPHABET[encrypted_index_in_alphabet]

print(f"Зашифрованный текст: {encrypted_text}")

decrypted_text = ""
for symbol in encrypted_text:
    original_index_in_alphabet = ALPHABET.find(symbol)

    if original_index_in_alphabet == -1:
        decrypted_text += symbol
    else:
        decrypted_index_in_alphabet = original_index_in_alphabet - encryption_key
        decrypted_text += ALPHABET[decrypted_index_in_alphabet]

print(f"Расшифрованный текст: {decrypted_text}")
