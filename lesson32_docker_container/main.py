import telebot

from api import *

# @valute_itpark32_bot
bot = telebot.TeleBot("8708759320:AAGNAYjS3b6vE9-aPYG9Voa4OC8GuJOrlLY")


def get_valute_courses_as_str():
    eur_data = get_vatule_rub(EUR)
    usd_data = get_vatule_rub(USD)

    return (
        f"СУПЕР НОВЫЕ Валютные данные:\n\n"
        f"Курс доллара по отношению к рублю за {usd_data.date} = {usd_data.rate} руб.\n\n"
        f"Курс евро по отношению к рублю за {eur_data.date} = {eur_data.rate} руб."
    )


@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):
    input_text = message.text
    chat_id = message.chat.id
    output_text = ""

    if input_text == "/start":
        output_text = "Данный бот позволяет получить свежий курс рубля по отношению к доллару и евро. Для получения данных о курсе введите /course"
    elif input_text == "/course":
        output_text = get_valute_courses_as_str()
    else:
        output_text = "Команда не распознана. Пожалуйста введите /start"

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


print("Бот запущен")
bot.infinity_polling()
