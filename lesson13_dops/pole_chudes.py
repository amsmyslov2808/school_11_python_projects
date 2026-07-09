COMP_GENERATED_QUESTIONS = [
    "Какой фрукт обычно жёлтого цвета?",
    "Какое животное говорит мяу?",
    "Как называется столица России?",
    "Какой напиток делают из листьев чайного куста?",
    "Как называется планета, на которой мы живём?",
    "Какое время года идёт после зимы?",
    "Какой предмет нужен, чтобы писать?",
    "Как называется большой водоём с солёной водой?",
    "Какой день недели идёт после понедельника?",
    "Как называется дом для птиц?",
]

COMP_GENERATED_ANSWERS = [
    "банан",
    "кошка",
    "москва",
    "чай",
    "земля",
    "весна",
    "ручка",
    "море",
    "вторник",
    "гнездо",
]

CLOSED_LETTER = "*"

repeat_answer = "y"

while repeat_answer == "y":

    question = ""
    answer = ""
    guess_answer = ""

    input_type = int(
        input(
            "Выберите способ генерации вопроса и ответа (1 - ввести вручную, 2 - выбрать из готовых вариантов): "
        )
    )

    if input_type == 1:
        question = input("Введите свой вопрос: ")
        answer = input("Введите свой ответ: ")
    elif input_type == 2:
        for i in range(len(COMP_GENERATED_QUESTIONS)):
            print(f"Пара вопрос - ответ №{i+1}:")
            print(f"{COMP_GENERATED_QUESTIONS[i]} - {COMP_GENERATED_ANSWERS[i]}")
            print()

        pair_index = int(input("Введите номер выбранной пары вопрос - ответ: ")) - 1

        question = COMP_GENERATED_QUESTIONS[pair_index]
        answer = COMP_GENERATED_ANSWERS[pair_index]

    print("\n" * 50)

    guess_answer = CLOSED_LETTER * len(answer)

    is_run = True

    while is_run == True:
        print(f"Вопрос: {question}")
        # print(f"Отгаданное слово: {guess_answer}")

        print(f"Отгаданное слово: ", end="")
        for letter in guess_answer:
            print(f"{letter} ", end="")
        print()

        print()
        print("-" * 30)
        print()

        input_type = int(
            input(
                "Выберите способ текущего ввода (1 - ввести одну букву, 2 - ввести слово целиком): "
            )
        )

        if input_type == 1:
            input_letter = input("Введите одну предполагаемую букву: ")

            is_guess_letter = False

            for i in range(len(answer)):
                if input_letter == answer[i]:
                    guess_answer = (
                        guess_answer[:i] + input_letter + guess_answer[i + 1 :]
                    )
                    is_guess_letter = True

            if is_guess_letter == True:
                print("Поздравляем такая буква есть")
            else:
                print("К сожалению такой буквы нет")

        elif input_type == 2:
            input_word = input("Введите предполагаемое слово целиком: ")

            if input_word == answer:
                guess_answer = answer
                print("Поздравляем вы угалади всё слово целиком")
            else:
                print("К сожалению вы ввели неверное слово")

        print()
        print("=" * 30)
        print()

        if guess_answer == answer:
            is_run = False

    print(f"Поздравляем вы отгадали слово {answer}")

    print()
    print("=" * 30)
    print()

    repeat_answer = input("Хотите сыграть ещё раз? (y - да / n - нет): ")
