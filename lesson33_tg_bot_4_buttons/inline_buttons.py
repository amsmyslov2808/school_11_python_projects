import telebot
from telebot import types

bot = telebot.TeleBot("8929579040:AAFhY5t15eu0uF-zuoaGDj9TXRLCqAk9-qU")


@bot.message_handler(commands=["start"])
def process_command_start(message):
    chat_id = message.chat.id
    output_text = "бот получил команду start"

    inline_keyboard = types.InlineKeyboardMarkup()

    inline_keyboard.add(
        types.InlineKeyboardButton("Скрыть кнопки", callback_data="hide_keyboard")
    )
    inline_keyboard.add(
        types.InlineKeyboardButton("Привет", callback_data="hello"),
        types.InlineKeyboardButton("Кубик", callback_data="cubik"),
    )

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data == "hide_keyboard")
def process_inline_button_hide_keyboard(call):
    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    output_text = "поймали кнопку Скрыть кнопки"

    bot.send_message(
        chat_id, output_text, message_thread_id=call.message.message_thread_id
    )


print("Бот запущен")
bot.infinity_polling()
