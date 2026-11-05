import telebot
from telebot import types

bot = telebot.TeleBot("9276925819:AAFoz8bo5NRanS72N6VMdLIM0m2k_wx2rqI")

# Ссылка на картинку, которую отправляем пользователю.
photo_url = "https://www.python.org/static/community_logos/python-logo.png"


@bot.message_handler(commands=["start"])
def process_command_start(message: types.Message):
    chat_id = message.chat.id

    # Рабочий вариант: картинка с подписью.
    bot.send_photo(chat_id, photo_url, caption="Привет! Это логотип Python 🐍")

    # Вариант без подписи: убери # у следующей строки,
    # а строку bot.send_photo выше закомментируй.
    # bot.send_photo(chat_id, photo_url)


print("Бот запущен")
bot.infinity_polling()
