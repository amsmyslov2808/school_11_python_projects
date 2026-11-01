# 8929579040:AAFhY5t15eu0uF-zuoaGDj9TXRLCqAk9-qU

# @lesson33_tg_bot_4_buttons_bot

import telebot

bot = telebot.TeleBot("8929579040:AAFhY5t15eu0uF-zuoaGDj9TXRLCqAk9-qU")


# Подтверждает получение /start; специальные команды должны идти до общих обработчиков.
@bot.message_handler(commands=["start"])
def process_command_start(message):
    chat_id = message.chat.id
    output_text = "бот получил команду start"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Подтверждает получение /clear; в этом примере команда только отправляет текст.
@bot.message_handler(commands=["clear"])
def process_command_clear(message):
    chat_id = message.chat.id
    output_text = "бот получил команду clear"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Подтверждает получение /add; добавление данных в этом примере не реализовано.
@bot.message_handler(commands=["add"])
def process_command_add(message):
    chat_id = message.chat.id
    output_text = "бот получил команду add"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Сообщает о неизвестной команде, начинающейся с /.
@bot.message_handler(func=lambda message: message.text.startswith("/"))
def process_command_unknown(message):
    chat_id = message.chat.id
    output_text = "неизвестная Команда"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Для остальных сообщений отправляет подсказку о команде /start.
@bot.message_handler(func=lambda message: True)
def process_text_common(message):
    chat_id = message.chat.id
    output_text = "неизвестный текст - нажмите /start для начала работы бота"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Запускаем получение сообщений и передаём их зарегистрированным обработчикам.
print("Бот запущен")
bot.infinity_polling()
