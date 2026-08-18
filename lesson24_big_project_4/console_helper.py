# Из модуля datetime берём два инструмента для работы с датами:
# date хранит дату, а datetime умеет превращать введённый текст в дату.
from datetime import date, datetime


def input_int(message: str, min_val: int, max_val: int) -> int:
    """Запрашивает целое число, пока пользователь не введёт допустимое значение."""
    # Этот флаг похож на зелёный сигнал: цикл остановится, когда ввод станет верным.
    is_correct_input = False
    # Начальное значение нужно, чтобы переменная существовала до начала цикла.
    input_int = 0

    # Пока правильного ответа нет, снова просим пользователя ввести число.
    while is_correct_input == False:
        try:
            # input() возвращает строку, а int() пытается превратить её в целое число.
            input_int = int(input(message))

            # Проверяем, попало ли число в разрешённый промежуток.
            if input_int < min_val or input_int > max_val:
                print(
                    f"Ошибка ввода. Введённое число должно быть от {min_val} до {max_val}"
                )
            else:
                # Значение подходит — разрешаем циклу закончиться.
                is_correct_input = True
        except:
            # Сюда программа попадёт, если строку нельзя превратить в целое число.
            print(f"Ошибка ввода. Вы ввели не целое число")

    # Отдаём проверенное число той части программы, которая вызвала функцию.
    return input_int


def input_float(message: str, min_val: float, max_val: float) -> float:
    """Запрашивает число, которое может содержать дробную часть."""
    is_correct_input = False
    # Несмотря на имя input_int, ниже переменная может хранить и дробное число.
    input_int = 0

    while is_correct_input == False:
        try:
            # float() понимает, например, строку "4.5" и превращает её в число 4.5.
            input_int = float(input(message))

            # Не принимаем значение, если оно меньше минимума или больше максимума.
            if input_int < min_val or input_int > max_val:
                print(
                    f"Ошибка ввода. Введённое число должно быть от {min_val} до {max_val}"
                )
            else:
                is_correct_input = True
        except:
            # Этот блок выполняется, если пользователь ввёл не число.
            print(f"Ошибка ввода. Вы ввели не целое число")

    return input_int


def input_str(message: str, min_len: int, max_len: int) -> str:
    """Запрашивает текст нужной длины."""
    is_correct_input = False
    input_str = ""

    while is_correct_input == False:
        # Здесь преобразование не требуется: input() уже возвращает строку.
        input_str = input(message)

        # len() считает количество символов, включая пробелы.
        if len(input_str) < min_len or len(input_str) > max_len:
            print(
                f"Ошибка ввода. Введённая строка по длине должна быть от {min_len} до {max_len} сиволов"
            )
        else:
            is_correct_input = True

    return input_str


def input_date(message: str, min_date: date, max_date: date) -> date:
    """Запрашивает дату в формате ДД.ММ.ГГГГ и проверяет её границы."""
    is_correct_input = False
    # Сегодняшняя дата служит безопасным начальным значением.
    input_date = date.today()

    while is_correct_input == False:
        try:
            # strptime работает как переводчик: превращает текст вроде 25.08.2026 в дату.
            # Шаблон %d.%m.%Y означает «день.месяц.год».
            input_date = datetime.strptime(input(message), "%d.%m.%Y").date()

            # Дата должна находиться внутри указанного промежутка, включая его края.
            if input_date < min_date or input_date > max_date:
                print(
                    f"Ошибка ввода. Введённая дата должна быть от {min_date.strftime('%d.%m.%Y')} до {max_date.strftime('%d.%m.%Y')}"
                )
            else:
                is_correct_input = True
        except:
            # Например, 40.15.2026 не является настоящей датой и вызовет ошибку.
            print(f"Ошибка ввода. Вы ввели дату не в формате ДД.ММ.ГГГГ")

    return input_date
