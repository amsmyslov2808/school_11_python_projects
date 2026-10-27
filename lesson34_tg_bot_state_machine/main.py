import telebot

from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage

# 9276925819:AAFoz8bo5NRanS72N6VMdLIM0m2k_wx2rqI
# @registartion_27_10_bot

bot = telebot.TeleBot(
    "9276925819:AAFoz8bo5NRanS72N6VMdLIM0m2k_wx2rqI",
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


class RegistrationStates(StatesGroup):
    input_name = State()
    input_age = State()
    choose_gender = State()
    confirmation = State()


@bot.message_handler(commands=["start"])
def process_command_start(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    output_text = "Добро пожаловать на регистрацию на концерт группы ХаХаХа\nВведите своё имя (от 2 до 30 символов):"

    state.delete()
    state.set(RegistrationStates.input_name)

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


@bot.message_handler(state=RegistrationStates.input_name, content_types=["text"])
def process_state_input_name(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    name = message.text.strip()
    output_text = ""

    if len(name) < 2 or len(name) > 30:
        output_text = "Ошибка ввода имени. Имя должно быть от 2 до 30 символов"

        bot.send_message(
            chat_id, output_text, message_thread_id=message.message_thread_id
        )
        return

    state.add_data(name=name)
    state.set(RegistrationStates.input_age)

    output_text = (
        "Ваше имя успешно сохранено\nТеперь введите Ваш возраст от 13 до 100 лет: "
    )

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


@bot.message_handler(state=RegistrationStates.input_age, content_types=["text"])
def process_state_input_age(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    age_as_str = message.text.strip()
    output_text = ""

    try:
        age = int(age_as_str)

        if age < 13 or age > 100:
            output_text = "Ошибка ввода возвраста. Возраст должен быть от 13 до 100 лет"

            bot.send_message(
                chat_id, output_text, message_thread_id=message.message_thread_id
            )
            return
    except:
        output_text = "Ошибка ввода возвраста. Вы ввели НЕ число"

        bot.send_message(
            chat_id, output_text, message_thread_id=message.message_thread_id
        )

        return

    state.add_data(age=age)
    state.set(RegistrationStates.choose_gender)

    output_text = "Ваш возраст успешно сохранен\nТеперь выберите Ваш пол: "

    inline_keyboard = types.InlineKeyboardMarkup()

    inline_keyboard.add(types.InlineKeyboardButton("Мужской", callback_data="Мужской"))
    inline_keyboard.add(
        types.InlineKeyboardButton("Женский", callback_data="Женский"),
    )

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("Бот запущен")
bot.infinity_polling()
