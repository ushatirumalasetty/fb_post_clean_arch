from usha.exceptions import InvalidCommentContent
from usha.exceptions import InvalidUserException
from usha.exceptions import InvalidPostException
from usha.exceptions import InvalidPostContent
from usha.exceptions import InvalidCommentException
from usha.exceptions import InvalidReactionTypeException
from usha.exceptions import InvalidReplyContent

from usha.models import User, Post, Comment, Reaction


def is_comment_content_valid(comment_content):
    is_comment_content_valid = not comment_content
    if is_comment_content_valid:
        raise InvalidCommentContent

def is_user_valid(user_id):
    try:
        User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise InvalidUserException

def is_post_valid(post_id):
    try:
        post_obj = Post.objects.get(id=post_id)
        return post_obj
    except Post.DoesNotExist:
        raise InvalidPostException


def is_comment_valid(comment_id):
    try:
        Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        raise  InvalidCommentException

def is_post_content_valid(post_content):
    is_post_content_valid = not post_content
    if is_post_content_valid:
        raise InvalidPostContent

def is_reaction_type_valid(reaction_type):
    #TODO  enums
    reactions_list =["WOW", "LIT", "LOVE", "HAHA", "THUMBS-UP",
                     "THUMBS-DOWN", "ANGRY", "SAD"]
    if reaction_type not in reactions_list:
        raise InvalidReactionTypeException

def is_reply_content_valid(reply_content):
    is_reply_content_valid = not reply_content
    if is_reply_content_valid:
        raise InvalidReplyContent
