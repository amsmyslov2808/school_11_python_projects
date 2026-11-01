import random
import requests
from bs4 import BeautifulSoup
import telebot

# 8911933491:AAGc-V8kEn-Lk6lZGU_CwDNKBYdSFmdmzYQ
# @bashorg_jokes_bot


# Загружает страницу башорг.рф и возвращает текст одной случайной цитаты.
def get_random_joke():
    # Загружаем страницу; timeout ограничивает ожидание ответа сервера.
    response = requests.get("https://башорг.рф/random", timeout=10)
    response.raise_for_status()

    html_page = BeautifulSoup(response.text, "html.parser")
    # Выбираем блоки цитат из разобранного HTML.
    quotes = html_page.find_all("div", class_="quote__body")

    # Сохраняем переносы строк, убирая HTML-теги и лишние пробелы по краям.
    clear_quotes = [quote.get_text("\n", strip=True) for quote in quotes]

    # На странице несколько цитат, поэтому выбираем одну случайную.
    return random.choice(clear_quotes)


bot = telebot.TeleBot("8911933491:AAGc-V8kEn-Lk6lZGU_CwDNKBYdSFmdmzYQ")


# Обрабатывает /start и /joke, а для неизвестного текста выводит подсказку.
@bot.message_handler(content_types=["text"], func=lambda message: True)
def process_all_text_messages(message):
    input_text = message.text
    chat_id = message.chat.id
    output_text = ""

    # /start показывает справку, /joke запрашивает новую цитату.
    if input_text == "/start":
        output_text = "Cлучайные шутки с башорг.рф. Для получения новой случайной шутки нажмите или введите /joke"

    elif input_text == "/joke":
        output_text = get_random_joke()

    else:
        output_text = "Команда не распознана. Пожалуйста введите /start"

    bot.send_message(chat_id, output_text)


# Запускаем получение сообщений и передаём их зарегистрированным обработчикам.
print("Бот запущен")

# Постоянно получаем новые сообщения от Telegram.
bot.infinity_polling()
