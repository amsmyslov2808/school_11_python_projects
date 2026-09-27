# @cubes_randoms_bot

import telebot
import random

adventure_events = [
    "Внезапная стычка",
    "Находка/Клад",
    "Природная аномалия",
    "Случайная встреча",
    "Ловушка или препятствие",
    "Удача/Благословение",
]


bot = telebot.TeleBot("8608472443:AAEgXYrAJbPzqghVwJWerWunGGhcukdcbKU")


@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):
    input_text = message.text
    chat_id = message.chat.id
    output_text = ""

    if input_text in ["/start", "/start@cubes_randoms_bot"]:
        output_text = "Добро пожаловать в бота генератора стандартных кубиков на 6 граней и кубиков событий. Введите /cube1 или /cube2 или /cube3 чтобы бросить 1, 2 или 3 кубика на 6 граней соответственно. Введите /cube_events чтобы бросить кубик событий."

    elif input_text in ["/cube1", "/cube1@cubes_randoms_bot"]:
        number1 = random.randint(1, 6)
        output_text = f"На кубике выпало: {number1}"

    elif input_text in ["/cube2", "/cube2@cubes_randoms_bot"]:
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        output_text = f"На кубике 1 выпало: {number1}"
        output_text += "\n"
        output_text += f"На кубике 2 выпало: {number2}"

    elif input_text in ["/cube3", "/cube3@cubes_randoms_bot"]:
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        number3 = random.randint(1, 6)

        output_text = f"На кубике 1 выпало: {number1}"
        output_text += "\n"
        output_text += f"На кубике 2 выпало: {number2}"
        output_text += "\n"
        output_text += f"На кубике 3 выпало: {number3}"

    elif input_text in ["/cube_events", "/cube_events@cubes_randoms_bot"]:
        output_text = f"На кубике выпало событие: {random.choice(adventure_events)}"

    else:
        output_text = "Команда не распознана для начала работы с ботом введите /start"

    # bot.send_message(chat_id, output_text)
    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


print("Бот запущен")
bot.infinity_polling()
