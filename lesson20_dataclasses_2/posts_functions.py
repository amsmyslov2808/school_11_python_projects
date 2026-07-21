from post import Post

global_post_id = 0


def get_next_post_id() -> int:
    global global_post_id
    global_post_id += 1

    return global_post_id


def input_post_data() -> Post:
    posting_datetime = input(
        "введите дату-время выхода поста в формате hh:mm:ss dd.MM.YYYY "
    )
    media_url = input("введите url видео или картинки которая будет вставлена в пост: ")
    description = input("введите текст подписи к медиа файлу: ")

    return Post(
        posting_datetime=posting_datetime,
        media_url=media_url,
        description=description,
    )


def add_new_post_to_end_of_list(posts: list[Post], new_post: Post):
    posts.append(new_post)


def get_post_by_id(posts: list[Post], id: int) -> Post | None:
    for post in posts:
        if post.id == id:
            return post

    return None


def delete_post_by_id(posts: list[Post], id: int) -> bool:
    found_post = get_post_by_id(posts, id)

    if found_post == None:
        return False

    posts.remove(found_post)

    return True


def update_post_by_id(posts: list[Post], post: Post) -> bool:
    found_post = get_post_by_id(posts, post.id)

    if found_post == None:
        return False

    found_post.posting_datetime = post.posting_datetime
    found_post.media_url = post.media_url
    found_post.description = post.description

    return True


def print_post_header():
    print(f"{'ИД':<5}{'Дата публикации':<25}{'Медиа URL':<25}{'Описание':<25}")


def print_one_post(post: Post):
    print(
        f"{post.id:<5}{post.posting_datetime:<25}{post.media_url:<25}{post.description:<25}"
    )


def print_posts(posts: list[Post]):
    print_post_header()

    if len(posts) > 0:
        for post in posts:
            print_one_post(post)
    else:
        print("список постов пуст")
