# @cubes_randoms_bot

import telebot
import random

# Возможные результаты броска кубика событий
adventure_events = [
    "Внезапная стычка",
    "Находка/Клад",
    "Природная аномалия",
    "Случайная встреча",
    "Ловушка или препятствие",
    "Удача/Благословение",
]


# Создание бота с помощью токена от BotFather
bot = telebot.TeleBot("8608472443:AAEgXYrAJbPzqghVwJWerWunGGhcukdcbKU")


# Обработчик всех текстовых сообщений
@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):
    # Получаем текст сообщения и ID чата, откуда оно пришло
    input_text = message.text
    chat_id = message.chat.id
    output_text = ""

    # В группе к команде добавляется имя бота после символа @
    if input_text in ["/start", "/start@cubes_randoms_bot"]:
        output_text = "Добро пожаловать в бота генератора стандартных кубиков на 6 граней и кубиков событий. Введите /cube1 или /cube2 или /cube3 чтобы бросить 1, 2 или 3 кубика на 6 граней соответственно. Введите /cube_events чтобы бросить кубик событий."

    # Бросок одного обычного шестигранного кубика
    elif input_text in ["/cube1", "/cube1@cubes_randoms_bot"]:
        number1 = random.randint(1, 6)
        output_text = f"На кубике выпало: {number1}"

    # Для нескольких кубиков создаём отдельное случайное число для каждого
    elif input_text in ["/cube2", "/cube2@cubes_randoms_bot"]:
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        output_text = f"На кубике 1 выпало: {number1}"
        output_text += "\n"
        output_text += f"На кубике 2 выпало: {number2}"

    # Бросок трёх кубиков выполняется по тому же принципу
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
        # Выбираем одно случайное событие из списка
        output_text = f"На кубике выпало событие: {random.choice(adventure_events)}"

    else:
        # Ответ на любой текст, который не совпал с командами выше
        output_text = "Команда не распознана для начала работы с ботом введите /start"

    # Отправляем ответ в ту же тему группового чата
    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


print("Бот запущен")
# Запускаем постоянное получение новых сообщений
bot.infinity_polling()
