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
    # Состояния и временные данные хранятся в памяти и исчезают при перезапуске.
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


# Каждый этап определяет, какой ввод сейчас ожидается от пользователя.
class RegistrationStates(StatesGroup):
    input_name = State()
    input_age = State()
    choose_gender = State()
    confirmation = State()


# Начинает регистрацию заново и запрашивает имя участника.
@bot.message_handler(commands=["start"])
def process_command_start(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    output_text = "Добро пожаловать на регистрацию на концерт группы ХаХаХа\nВведите своё имя (от 2 до 30 символов):"

    # /start сбрасывает предыдущую анкету и начинает регистрацию заново.
    state.delete()
    state.set(RegistrationStates.input_name)

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Проверяет длину имени, сохраняет его и переходит к вводу возраста.
@bot.message_handler(state=RegistrationStates.input_name, content_types=["text"])
def process_state_input_name(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    name = message.text.strip()
    output_text = ""

    # При ошибке остаёмся на текущем этапе и ждём повторный ввод.
    if len(name) < 2 or len(name) > 30:
        output_text = "Ошибка ввода имени. Имя должно быть от 2 до 30 символов"

        bot.send_message(
            chat_id, output_text, message_thread_id=message.message_thread_id
        )
        return

    # Сохраняем имя между сообщениями и переходим к запросу возраста.
    state.add_data(name=name)
    state.set(RegistrationStates.input_age)

    output_text = (
        "Ваше имя успешно сохранено\nТеперь введите Ваш возраст от 13 до 100 лет: "
    )

    bot.send_message(chat_id, output_text, message_thread_id=message.message_thread_id)


# Проверяет возраст, сохраняет его и предлагает кнопки выбора пола.
@bot.message_handler(state=RegistrationStates.input_age, content_types=["text"])
def process_state_input_age(message: types.Message, state: StateContext):
    chat_id = message.chat.id
    age_as_str = message.text.strip()
    output_text = ""

    # Проверяем отдельно преобразование в число и допустимый возраст.
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

    # Кнопки передают выбранный пол через callback_data.
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


# Сохраняет выбранный пол и показывает заполненную анкету для подтверждения.
@bot.callback_query_handler(state=RegistrationStates.choose_gender)
def process_state_choose_gender(call: types.CallbackQuery, state: StateContext):
    chat_id = call.message.chat.id
    output_text = ""

    bot.answer_callback_query(call.id)

    state.add_data(gender=call.data)

    name = ""
    age = 0
    gender = ""

    # Читаем данные, накопленные на предыдущих этапах регистрации.
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

    # Кнопки подтверждения передают решение пользователя: Accept или Error.
    inline_keyboard.add(
        types.InlineKeyboardButton("Всё корректно", callback_data="Accept")
    )
    inline_keyboard.add(
        types.InlineKeyboardButton("Есть ошибки", callback_data="Error"),
    )

    # Следующее нажатие должно подтвердить или отменить введённые данные.
    # Обработчик подтверждения в этой учебной версии ещё не добавлен.
    state.set(RegistrationStates.confirmation)

    bot.send_message(
        chat_id,
        output_text,
        message_thread_id=call.message.message_thread_id,
        reply_markup=inline_keyboard,
    )


# Фильтр выбирает обработчик по состоянию, middleware передаёт в него StateContext.
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

# Запускаем получение сообщений и передаём их зарегистрированным обработчикам.
print("Бот запущен")
bot.infinity_polling()
