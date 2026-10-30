import telebot

from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage

from dataclasses import dataclass

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
    start_await = State()


registarations = []


@dataclass
class Registration:
    name: str
    age: int
    gender: str


@bot.message_handler(commands=["start"])
def process_command_start(message: types.Message, state: StateContext):
    chat_id = message.chat.id

    output_text = "Добро пожаловать на регистрацию на концерт группы ХаХаХа\nВведите своё имя (от 2 до 30 символов):"

    state.delete()
    state.set(RegistrationStates.input_name)

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


@bot.message_handler(commands=["cancel"])
def process_command_cancel(message: types.Message, state: StateContext):
    chat_id = message.chat.id

    output_text = "Ваша регистрация успешно прервана.\n\nПожалуйста введите /start для новой регистрации."

    state.delete()
    state.set(RegistrationStates.start_await)

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

    output_text = (
        "Ваше имя успешно сохранено\nТеперь введите Ваш возраст от 13 до 100 лет: "
    )

    state.add_data(name=name)
    state.set(RegistrationStates.input_age)

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

    output_text = "Ваш возраст успешно сохранен\nТеперь выберите Ваш пол: "

    inline_keyboard = types.InlineKeyboardMarkup()

    inline_keyboard.add(types.InlineKeyboardButton("Мужской", callback_data="Мужской"))
    inline_keyboard.add(
        types.InlineKeyboardButton("Женский", callback_data="Женский"),
    )

    state.add_data(age=age)
    state.set(RegistrationStates.choose_gender)

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=message.message_thread_id,
        reply_markup=inline_keyboard,
    )


@bot.callback_query_handler(state=RegistrationStates.choose_gender)
def process_state_choose_gender(call: types.CallbackQuery, state: StateContext):
    chat_id = call.message.chat.id
    output_text = ""

    bot.answer_callback_query(call.id)

    state.add_data(gender=call.data)

    with state.data() as data:
        name = data["name"]
        age = data["age"]
        gender = data["gender"]

    output_text = (
        f"Проверьте правильность введённых данных\n\n" + f"Имя: {name}\n"
        f"Возраст: {age}\n"
        f"Пол: {gender}"
    )

    inline_keyboard = types.InlineKeyboardMarkup()

    inline_keyboard.add(
        types.InlineKeyboardButton("Всё корректно", callback_data="Accept")
    )
    inline_keyboard.add(
        types.InlineKeyboardButton("Есть ошибки", callback_data="Error"),
    )

    state.set(RegistrationStates.confirmation)

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=call.message.message_thread_id,
        reply_markup=inline_keyboard,
    )


@bot.callback_query_handler(state=RegistrationStates.confirmation)
def process_state_confirmation(call: types.CallbackQuery, state: StateContext):
    chat_id = call.message.chat.id
    output_text = ""

    bot.answer_callback_query(call.id)

    if call.data == "Accept":

        with state.data() as data:
            registaration = Registration(
                name=data["name"], age=data["age"], gender=data["gender"]
            )

        registarations.append(registaration)

        output_text = "Ваши данные успешно сохранены. Для регистраниции новых участников введите /start"

    elif call.data == "Error":

        output_text = "Сохранение отменено. Для повторной регистраниции введите /start"

    state.delete()
    state.set(RegistrationStates.start_await)

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=call.message.message_thread_id,
    )


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("Бот запущен")
bot.infinity_polling()
