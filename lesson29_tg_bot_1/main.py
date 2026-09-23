# 8964071869:AAGyvHLoaB0GOUvO4hiioM-PsDA7_C3s530

# @pacan_citat_228_bot

import telebot
import random

bot = telebot.TeleBot("8964071869:AAGyvHLoaB0GOUvO4hiioM-PsDA7_C3s530")

quotes = [
    "Брат может не быть другом, но друг — всегда брат.",
    "Не важно, кто против тебя, важно, кто с тобой.",
    "Слабые ищут оправдания, сильные — возможности.",
    "Жизнь — это очередь за счастьем, но некоторые лезут без очереди.",
    "Лучше быть последним среди львов, чем первым среди шакалов.",
    "Упал — вставай, встал — нападай.",
    "Мои друзья не идеальны, но они настоящие.",
    "Своих надо ценить, а не оценивать.",
    "Слово пацана дороже золота.",
    "Не хвастайся силой, хвастайся верностью.",
    "Запомни: если тебе смотрят в спину, значит, ты впереди.",
    "Ошибайся, делай выводы, но никогда не сдавайся.",
    "Трудности делают нас сильнее, а верные друзья — непобедимыми.",
    "Делай как надо, и будь что будет.",
    "Глаза боятся, а руки делают. Особенно если рядом братва.",
]


@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):
    input_text = message.text
    chat_id = message.chat.id
    output_text = ""

    if input_text == "/start":
        output_text = "Это пацанский цитатник. Лучшие пацанские цитаты на каждый день. Для получения новой цитаты нажмите или введите /brat"
    elif input_text == "/brat":
        output_text = random.choice(quotes)
    else:
        output_text = "Команда не распознана. Пожалуйста введите /start"

    bot.send_message(chat_id, output_text)


print("Бот запущен")
bot.infinity_polling()
