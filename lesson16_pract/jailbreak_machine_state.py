# Константы состояний
STATE_START_GAME = 1
STATE_MAIN_MENU = 2
STATE_PRISON_START = 3
STATE_PRISON_MAIN_QUESTION = 4

STATE_PMQ_MEET = 41
STATE_PMQ_SEARCH = 42
STATE_PMQ_SEAT = 43

STATE_PMQ_M_PLAN1 = 411
STATE_PMQ_M_PLAN2 = 412
STATE_PMQ_M_PLAN3 = 413

STATE_PMQ_M_P1_NIGH = 4111
STATE_PMQ_M_P1_WORK = 4112
STATE_PMQ_M_P1_MONEY = 4113


# Глобальные переменные
lives = 3
score = 0
has_key = 0
has_plan = 0
has_lockpick = 0
guard_alert = 0
stage = 1
player_name = ""
dies = 0

# Глобальная переменная отвечает за текущее состояние
global_current_state = STATE_START_GAME


# Функции обработки состояний
def process_state_start_game():
    global global_current_state
    global player_name

    print(
        "Доброе утро зэк, сегодня твой первый день в тюрьме. Посмотрим сможешь ли ты сбежать или нет"
    )

    player_name = input("Как тя звать зэк? ")
    print(f"Чтож прибывший {player_name}, чтоб твое время тут тянулось вечно")

    global_current_state = STATE_MAIN_MENU


def process_state_main_menu():
    global global_current_state

    print("Список заключенного")
    print("1 - колличество жизней")
    print("2 - колличество полученых респектов")
    print("3 - колличество ключей")
    print("4 - колличество планов побега")
    print("5 - колличество отмычек")
    print("6 - уровень подозрения охраны")
    print("7 - текущий этап игры")
    print("8 - колличество смертей")
    print("9 - отправиться в тюремную камеру")

    change = int(input("введите один из пунктов списка "))

    if change == 1:
        print(f"у тя есть {lives} жизни")
    elif change == 2:
        print(f"твое колличество полученых респектов {score}")
    elif change == 3:
        print(f"у тя есть {has_key} ключа")
    elif change == 4:
        print(f"у тя есть {has_plan} планов побега")
    elif change == 5:
        print(f"у тя есть {has_lockpick} отмычек")
    elif change == 6:
        print(f"ты в жопе на {guard_alert} процентов")
    elif change == 7:
        print(f"ты сейчас на {stage}, ох еще далеко до побега")
    elif change == 8:
        print(f"ты умер {dies} раз")
    elif change == 9:
        print("добро пожаловать в тюрьму")
        global_current_state = STATE_PRISON_START


def process_state_prison_start():
    global global_current_state

    answer = input("Хочешь попробовать сбежать? ")
    if answer == "да":
        global_current_state = STATE_PRISON_MAIN_QUESTION


def process_state_prison_main_question():
    global global_current_state

    print(
        "Ты в одной камере с заключенным старой закалки который отсидел здесь кучу лет,что будешь делать?"
    )

    print("1 - познакомишься с сокамерником")
    print("2 - обыщешь комнату на наличие предметов")
    print("3 - будешь молча сидеть на своей койке")

    change = int(input("введите один из пунктов списка"))

    if change == 1:
        global_current_state = STATE_PMQ_MEET
    elif change == 2:
        global_current_state = STATE_PMQ_SEARCH
    elif change == 3:
        global_current_state = STATE_PMQ_SEAT


def process_state_pmq_meet():
    global global_current_state
    global score
    global stage

    print(
        "Поздравляю!Ты нашел себе нового друга,вы нашли много общего и теперь обдумываете план побега"
    )
    score += 20
    stage += 1
    print(f"Ваши респекты: {score}, теперь вы на {stage} этапе игры")

    print("1 план попробывать поискать что то в комнате пока сокамерник прикрывает")
    print("2 план стащить ложку со столовой")
    print("3 план попробовать отвлечь охранника и стащить у него ключ карту")

    change = int(input("выбери один из пунктов"))

    if change == 1:
        global_current_state = STATE_PMQ_M_PLAN1
    elif change == 2:
        global_current_state = STATE_PMQ_M_PLAN2
    elif change == 3:
        global_current_state = STATE_PMQ_M_PLAN3


def process_state_pmq_m_plan1():
    global global_current_state

    global score
    global stage
    global has_lockpick
    global guard_alert

    print(
        "ОГО!Вы нашли отмычку, благодаря тому что на шухере стоял ваш напарник вы успели спрятать найденную отмычку, но подозрение охраны выросло"
    )
    score += 15
    stage += 1
    has_lockpick += 1
    guard_alert += 30
    print(
        f"Ваши респекты {score}, найдееные вещи (отмычка), подозрение охраны {guard_alert}, теперь вы на {stage} этапе"
    )

    print("1 - дождаться ночи и сбежать из камеры а после и из тюрьмы")
    print(
        "2 - попробавать получить работу на кухне чтобы сбежать через ту дверь куда приносят продукты"
    )
    print(
        "3 - подкупить охранника с помощью денег знакомых с наружи чтоб вас ночью не запирали и помогли пройти по коридорам"
    )

    change = int(
        input("Выбери один из вариантов, сможешь ли ты сделать правильный выбор?")
    )

    if change == 1:
        global_current_state = STATE_PMQ_M_P1_NIGH
    elif change == 2:
        global_current_state = STATE_PMQ_M_P1_WORK
    elif change == 3:
        global_current_state = STATE_PMQ_M_P1_MONEY


def process_state_pmq_m_plan2():
    pass


def process_state_pmq_m_plan3():
    pass


def process_state_pmq_m_p1_nigh():
    global global_current_state

    global score
    global stage
    global has_lockpick
    global lives

    print(
        "Вы дошли до запасного выхода через медпункт, но ваша отмычка сломалась засчет чего вы создали кучу шума. Вы и ваш сокамерник отправляетесь в карцер на год."
    )

    score += 40
    stage += 1
    has_lockpick -= 1
    lives -= 1

    print(
        f"Ваш текущий результат: респекты {score}, найденные предметы (отмычка) {has_lockpick}, жизни {lives}"
    )

    print(
        "ПОЗДРРАВЛЯЕМ ВЫ СБЕЖАЛИ! Предлагаем сыграть снова и попытаться найти новую концовку"
    )

    global_current_state = STATE_MAIN_MENU


def process_state_pmq_m_p1_work():
    global global_current_state

    global score
    global stage

    print(
        "Вам удалось уговорить бабу Галю с помощью своей харизмы и вы получили работу. Во время привоза продуктов вы вышли под предлогом покурить и спрятались в грузовике и когда они доехали до следующей точки вы сбежали."
    )
    score += 50
    stage += 1
    print(
        f"Ваш текущий результат: респекты {score}, найденные предметы (отмычка) {has_lockpick}, жизни {lives}"
    )
    print(
        "ПОЗДРРАВЛЯЕМ ВЫ СБЕЖАЛИ! Предлагаем сыграть снова и попытаться найти новую концовку"
    )
    global_current_state = STATE_MAIN_MENU


def process_state_pmq_m_p1_money():
    global global_current_state

    global score
    global stage
    global lives

    print(
        "Вы смогли подкупить подкупить охраника и вас не запирали в комнате, но когда вы шли по коридорам вашего подкупленного охраника не было и вас поймали и отправили в карцер на год ."
    )
    score += 20
    stage += 1
    lives -= 1
    print(
        f"Ваш текущий результат: респекты {score}, найденные предметы (отмычка) {has_lockpick}, жизни {lives}"
    )

    print(
        "ПОЗДРРАВЛЯЕМ ВЫ СБЕЖАЛИ! Предлагаем сыграть снова и попытаться найти новую концовку"
    )
    global_current_state = STATE_MAIN_MENU


def check_lives():
    global global_current_state

    global dies
    global lives

    if lives == 0:
        print(
            "У вас закончились жизни.Вы отправляетесь на смертную казнь. Ну ничего сбежите в следующей жизни"
        )
        dies += 1
        lives += 3

        global_current_state = STATE_MAIN_MENU


is_run = True

while is_run == True:
    if global_current_state == STATE_START_GAME:
        process_state_start_game()
    elif global_current_state == STATE_MAIN_MENU:
        process_state_main_menu()
    elif global_current_state == STATE_PRISON_START:
        process_state_prison_start()
    elif global_current_state == STATE_PRISON_MAIN_QUESTION:
        process_state_prison_main_question()
    elif global_current_state == STATE_PMQ_MEET:
        process_state_pmq_meet()
    elif global_current_state == STATE_PMQ_M_PLAN1:
        process_state_pmq_m_plan1()
    elif global_current_state == STATE_PMQ_M_P1_NIGH:
        process_state_pmq_m_p1_nigh()
    elif global_current_state == STATE_PMQ_M_P1_WORK:
        process_state_pmq_m_p1_work()
    elif global_current_state == STATE_PMQ_M_P1_MONEY:
        process_state_pmq_m_p1_money()

    check_lives()
