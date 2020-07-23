from usha.models.post import Post

from .validity import is_user_valid, is_post_content_valid

def create_post(user_id, post_content):
    is_post_content_valid(post_content)
    is_user_valid(user_id)

    new_post_obj = Post.objects.create(content=post_content, posted_by_id=user_id)
    new_post_obj_id = new_post_obj.id
    return new_post_obj
