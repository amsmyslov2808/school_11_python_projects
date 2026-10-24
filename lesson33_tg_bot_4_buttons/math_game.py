import telebot
from telebot import types

import random

# 8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA

# @math_game_2026_bot

right_answer = 0

bot = telebot.TeleBot("8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA")


@bot.message_handler(commands=["start"])
def process_command_start(message):
    global right_answer

    chat_id = message.chat.id
    output_text = ""

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    right_answer = a + b

    output_text = f"Решите пример {a} + {b} = ?"

    answers = []
    for _ in range(4):
        answers.append(random.randint(1, 10))

    right_answer_index = random.randint(0, 3)
    answers[right_answer_index] = right_answer

    inline_keyboard = types.InlineKeyboardMarkup()

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


print("Бот запущен")
bot.infinity_polling()
