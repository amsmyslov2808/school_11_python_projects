from post import Post
from posts_functions import *

posts: list[Post] = []

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
        pass
    elif choose_action == 2:
        pass
    elif choose_action == 3:
        pass
    elif choose_action == 4:
        pass
    elif choose_action == 0:
        pass

    print("=" * 50)
    input("Для продолжения нажмите <Enter>")

# new_post = input_post_data()
# new_post.id = get_next_post_id()

# add_new_post_to_end_of_list(posts, new_post)

# new_post = input_post_data()
# new_post.id = get_next_post_id()

# add_new_post_to_end_of_list(posts, new_post)

post_1 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-21T14:30:00Z",
    media_url="https://example.com",
    description="Прекрасный закат на побережье! #отпуск #море",
)

# Второй мок-объект (без id, видео)
post_2 = Post(
    id=get_next_post_id(),
    posting_datetime="2026-07-21T20:00:00Z",
    media_url="https://example.com",
    description="Пошаговый рецепт идеальной итальянской пасты за 15 минут.",
)

add_new_post_to_end_of_list(posts, post_1)
add_new_post_to_end_of_list(posts, post_2)

print_posts(posts)
