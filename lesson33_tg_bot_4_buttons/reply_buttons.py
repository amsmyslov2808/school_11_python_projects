import telebot
from telebot import types

bot = telebot.TeleBot("8929579040:AAFhY5t15eu0uF-zuoaGDj9TXRLCqAk9-qU")


@bot.message_handler(commands=["start"])
def process_command_start(message):
    chat_id = message.chat.id
    output_text = "бот получил команду start"

    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    reply_keyboard.add(types.KeyboardButton("Скрыть кнопки"))
    reply_keyboard.add(types.KeyboardButton("Привет"), types.KeyboardButton("Кубик"))

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=reply_keyboard,
    )


@bot.message_handler(commands=["clear"])
def process_command_start(message):
    chat_id = message.chat.id
    output_text = "клавиатура скрыта"

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=types.ReplyKeyboardRemove(),
    )


@bot.message_handler(func=lambda message: message.text == "Скрыть кнопки")
def process_command_unknown(message):
    chat_id = message.chat.id
    output_text = "поймали кнопку Скрыть кнопки"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


print("Бот запущен")
bot.infinity_polling()
