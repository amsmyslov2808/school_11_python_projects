import telebot
from telebot import types

import random

# 8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA

# @math_game_2026_bot

bot = telebot.TeleBot("8361193272:AAH2Vp3v_pjun5AjaO9017wnX7kW_sfZNpA")

right_answer = 0


@bot.message_handler(commands=["start"])
def process_command_start(message):
    global right_answer

    chat_id = message.chat.id
    output_text = ""

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    right_answer = a + b

    output_text = f"Решите пример {a} + {b} = ?"

    answers_variants = [right_answer]

    while len(answers_variants) < 4:
        other_answer = random.randint(1, 20)

        if other_answer not in answers_variants:
            answers_variants.append(other_answer)

    random.shuffle(answers_variants)

    inline_keyboard = types.InlineKeyboardMarkup()

    for answer in answers_variants:
        inline_keyboard.add(
            types.InlineKeyboardButton(str(answer), callback_data=f"answer:{answer}")
        )

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("answer:") == True)
def process_inline_button_hide_keyboard(call):
    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    input_text = call.data
    output_text = ""

    user_answer = int(input_text.split(":")[1])

    if user_answer == right_answer:
        output_text = "Правильный ответ! Для генерации нового примера нажми /start"
    else:
        output_text = "НЕправильный ответ! Для генерации нового примера нажми /start"

    bot.send_message(
        chat_id, output_text, message_thread_id=call.message.message_thread_id
    )


print("Бот запущен")
bot.infinity_polling()
