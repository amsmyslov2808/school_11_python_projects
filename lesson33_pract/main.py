import telebot
from telebot import types

import random

# 8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA

# @math_game_2026_bot

bot = telebot.TeleBot("8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA")

# Здесь храним правильный ответ на последний созданный пример.
right_answer = 0


# Эта функция вызывается, когда пользователь отправляет команду /start.
@bot.message_handler(commands=["start"])
def process_command_start(message):
    # Разрешаем функции изменять общую переменную с правильным ответом.
    global right_answer

    # Запоминаем чат, в который нужно отправить пример.
    chat_id = message.chat.id
    output_text = ""

    # Выбираем два случайных числа от 1 до 10 и вычисляем их сумму.
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    right_answer = a + b

    output_text = f"Решите пример {a} + {b} = ?"

    # Сначала добавляем в список правильный ответ.
    answers_variants = [right_answer]

    # Добавляем случайные ответы, пока в списке не будет четыре варианта.
    while len(answers_variants) < 4:
        other_answer = random.randint(1, 20)

        # Не добавляем одинаковые варианты ответа.
        if other_answer not in answers_variants:
            answers_variants.append(other_answer)

    # Перемешиваем варианты, чтобы правильный ответ был на случайном месте.
    random.shuffle(answers_variants)

    # Создаём клавиатуру с кнопками под сообщением.
    inline_keyboard = types.InlineKeyboardMarkup()

    # На кнопке показываем число, а в callback_data сохраняем выбранный ответ.
    for answer in answers_variants:
        inline_keyboard.add(
            types.InlineKeyboardButton(str(answer), callback_data=f"answer:{answer}")
        )

    # Отправляем пример вместе с кнопками в тот же чат и тему.
    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


# Обрабатываем нажатия на кнопки, данные которых начинаются с "answer:".
@bot.callback_query_handler(func=lambda call: call.data.startswith("answer:") == True)
def process_inline_button_hide_keyboard(call):
    # Сообщаем Telegram, что нажатие обработано, чтобы убрать значок ожидания.
    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    input_text = call.data
    output_text = ""

    # Из строки вида "answer:12" получаем число 12.
    user_answer = int(input_text.split(":")[1])

    # Сравниваем выбранный ответ с правильным и готовим сообщение.
    if user_answer == right_answer:
        output_text = "Правильный ответ! Для генерации нового примера нажми /start"
    else:
        output_text = "НЕправильный ответ! Для генерации нового примера нажми /start"

    bot.send_message(
        chat_id, output_text, message_thread_id=call.message.message_thread_id
    )


# Запускаем постоянное ожидание новых сообщений и нажатий на кнопки.
print("Бот запущен")
bot.infinity_polling()
