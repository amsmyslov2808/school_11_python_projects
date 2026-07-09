STATE_START = 1
STATE_INPUT_NAME = 2
STATE_PRINT_PHRASE = 3

g_current_state = STATE_START


def process_state_start():
    global g_current_state

    g_current_state = STATE_INPUT_NAME


def process_print_phrase():
    global g_current_state

    g_current_state = STATE_INPUT_NAME


while True:
    if g_current_state == STATE_START:
        process_state_start()
    elif g_current_state == STATE_PRINT_PHRASE:
        process_print_phrase()
