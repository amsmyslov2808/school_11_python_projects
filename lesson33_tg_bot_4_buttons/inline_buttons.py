import telebot
from telebot import types

bot = telebot.TeleBot("8929579040:AAFhY5t15eu0uF-zuoaGDj9TXRLCqAk9-qU")


# По команде /start отправляет сообщение с прикреплёнными inline-кнопками.
@bot.message_handler(commands=["start"])
def process_command_start(message):
    chat_id = message.chat.id
    output_text = "бот получил команду start"

    # Inline-кнопки прикрепляются к конкретному сообщению.
    inline_keyboard = types.InlineKeyboardMarkup()

    # callback_data передаётся боту при нажатии, текст кнопки видит пользователь.
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


# Обрабатывает нажатие hide_keyboard и отправляет ответ о получении кнопки.
@bot.callback_query_handler(func=lambda call: call.data == "hide_keyboard")
def process_inline_button_hide_keyboard(call):
    # Убираем индикатор ожидания на нажатой кнопке.
    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id
    # Пока обработчик лишь отвечает сообщением; клавиатуру он не удаляет.
    output_text = "поймали кнопку Скрыть кнопки"

    bot.send_message(
        chat_id, output_text, message_thread_id=call.message.message_thread_id
    )


# Запускаем получение сообщений и передаём их зарегистрированным обработчикам.
print("Бот запущен")
bot.infinity_polling()
