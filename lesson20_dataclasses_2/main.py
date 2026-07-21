from post import Post
from posts_functions import *

posts: list[Post] = []

post_1 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-21T14:30:00Z",
    media_url="https://example.com",
    description="Прекрасный закат на побережье! #отпуск #море",
)

post_2 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-21T20:00:00Z",
    media_url="https://example.com",
    description="Пошаговый рецепт идеальной итальянской пасты за 15 минут.",
)

post_3 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-22T09:00:00Z",
    media_url="https://example.com",
    description="Утреннее кардио: 10-минутная зарядка для бодрости на весь день. Комплекс упражнений внутри.",
)

post_4 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-22T14:30:00Z",
    media_url="https://example.com",
    description="Топ-5 книг по личной эффективности, которые изменят ваше отношение к тайм-менеджменту.",
)

post_5 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-23T18:15:00Z",
    media_url="https://example.com",
    description="Итоги нашей поездки в горы: честный отзыв об отелях, маршрутах и скрытых локациях.",
)

add_new_post_to_end_of_list(posts, post_1)
add_new_post_to_end_of_list(posts, post_2)
add_new_post_to_end_of_list(posts, post_3)
add_new_post_to_end_of_list(posts, post_4)
add_new_post_to_end_of_list(posts, post_5)

is_run = True

while is_run == True:

    print("*" * 20)

    print_posts(posts)

    print("*" * 20)

    print("Меню:")
    print("1. Вывести пост по ИД")
    print("2. Добавить новый пост")
    print("3. Обновить пост по ИД")
    print("4. Удалить пост по ИД")
    print("0. Выйти из программы")

    choose_action = int(input("Введите номер выбранного пункта меню: "))

    if choose_action == 1:
        id = int(input("Введите ИД поста: "))

        found_post = get_post_by_id(posts, id)

        if found_post != None:
            print_post_header()
            print_one_post(found_post)
        else:
            print("Пост не найден")

    elif choose_action == 2:
        pass
    elif choose_action == 3:
        pass
    elif choose_action == 4:
        pass
    elif choose_action == 0:
        is_run = False

    print("=" * 50)
    input("Для продолжения нажмите <Enter>")
