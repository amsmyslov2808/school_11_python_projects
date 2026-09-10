from datetime import date, datetime
import math


def input_int(message: str, min_val: int, max_val: int) -> int:
    # Повторяем ввод, пока пользователь не укажет целое число из диапазона.
    is_correct_input = False
    input_int = 0

    while is_correct_input == False:
        try:
            # Преобразование в int также проверяет, что введено целое число.
            input_int = int(input(message))

            # Значения за границами диапазона не принимаются.
            if input_int < min_val or input_int > max_val:
                print(
                    f"Ошибка ввода. Введённое число должно быть от {min_val} до {max_val}"
                )
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. Вы ввели не целое число")

    return input_int


def input_float(message: str, min_val: float, max_val: float) -> float:
    # Повторяем ввод, пока пользователь не укажет число из диапазона.
    is_correct_input = False
    value = 0

    while is_correct_input == False:
        try:
            value = float(input(message))

            # Бесконечность и NaN проходят float(), поэтому проверяем их отдельно.
            if not math.isfinite(value):
                print("Ошибка ввода. Число должно быть конечным")
            elif value < min_val or value > max_val:
                print(
                    f"Ошибка ввода. Введённое число должно быть от {min_val} до {max_val}"
                )
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. Вы ввели не целое число")

    return value


def input_str(message: str, min_len: int, max_len: int) -> str:
    # Принимаем только строку с допустимым количеством символов.
    is_correct_input = False
    input_str = ""

    while is_correct_input == False:
        input_str = input(message)

        if len(input_str) < min_len or len(input_str) > max_len:
            print(
                f"Ошибка ввода. Введённая строка по длине должна быть от {min_len} до {max_len} сиволов"
            )
        else:
            is_correct_input = True

    return input_str


def input_date(message: str, min_date: date, max_date: date) -> date:
    # Запрашиваем дату до получения корректного значения в заданном диапазоне.
    is_correct_input = False
    input_date = date.today()

    while is_correct_input == False:
        try:
            # strptime одновременно разбирает строку и проверяет календарную дату.
            input_date = datetime.strptime(input(message), "%d.%m.%Y").date()

            # Ограничиваем допустимый период переданными границами.
            if input_date < min_date or input_date > max_date:
                print(
                    f"Ошибка ввода. Введённая дата должна быть от {min_date.strftime('%d.%m.%Y')} до {max_date.strftime('%d.%m.%Y')}"
                )
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. Вы ввели дату не в формате ДД.ММ.ГГГГ")

    return input_date


def print_devider(devider: str, len_diveder: int):
    # Строим разделитель повторением переданного символа.
    print(devider * len_diveder)


def wait_enter():
    # Останавливаем меню, чтобы пользователь успел прочитать результат операции.
    print("\n\n")
    print_devider("=", 125)
    print("\n\nДля продолжения работы нажмите <Enter>\n\n")
    input()
