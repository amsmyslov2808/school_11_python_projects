import telebot
from telebot import types

import random

# 8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA

# @math_game_2026_bot

# Общая переменная хранит сумму последнего созданного примера.
right_answer = 0

bot = telebot.TeleBot("8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA")


# Создаёт пример на сложение и показывает четыре кнопки с вариантами ответа.
@bot.message_handler(commands=["start"])
def process_command_start(message):
    # Изменяем переменную уровня модуля, а не создаём локальную.
    global right_answer

    chat_id = message.chat.id
    output_text = ""

    # Генерируем слагаемые и запоминаем правильную сумму.
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    right_answer = a + b

    output_text = f"Решите пример {a} + {b} = ?"

    # Заготавливаем четыре случайных варианта, затем один заменяем верным.
    answers = []
    for _ in range(4):
        answers.append(random.randint(1, 10))

    # Помещаем верный ответ на случайную позицию среди четырёх вариантов.
    right_answer_index = random.randint(0, 3)
    answers[right_answer_index] = right_answer

    inline_keyboard = types.InlineKeyboardMarkup()

    # Пока у всех кнопок одинаковые данные, а обработчик ответов ещё не добавлен.
    inline_keyboard.add(types.InlineKeyboardButton(str(answers[0]), callback_data="1"))
    inline_keyboard.add(types.InlineKeyboardButton(str(answers[1]), callback_data="1"))
    inline_keyboard.add(types.InlineKeyboardButton(str(answers[2]), callback_data="1"))
    inline_keyboard.add(types.InlineKeyboardButton(str(answers[3]), callback_data="1"))

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


# Запускаем получение сообщений и передаём их зарегистрированным обработчикам.
print("Бот запущен")
bot.infinity_polling()
