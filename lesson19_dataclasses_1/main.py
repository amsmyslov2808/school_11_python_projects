from post import Post
from posts_functions import *

global_post_id = 0


def get_next_post_id() -> int:
    global global_post_id
    global_post_id += 1

    return global_post_id


posts: list[Post] = []

new_post = input_post_data()
new_post.id = get_next_post_id()

add_new_post_to_end_of_list(posts, new_post)

new_post = input_post_data()
new_post.id = get_next_post_id()

add_new_post_to_end_of_list(posts, new_post)

print_posts(posts)
