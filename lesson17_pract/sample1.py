text = ""

with open("input.txt", "r", encoding="utf-8") as file_in:
    text = file_in.read()

with open("output.txt", "w", encoding="utf-8") as file_out:
    for letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        percent_letter_in_text = text.count(letter) / len(text) * 100

        file_out.write(
            f"количество букв {letter} в тексте = {percent_letter_in_text:.2f}%\n"
        )
