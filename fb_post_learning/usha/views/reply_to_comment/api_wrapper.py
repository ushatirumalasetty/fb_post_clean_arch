from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.reply_to_comment import reply_to_comment
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_COMMENT_CONTENT, INVALID_POST
from django_swagger_utils.drf_server.exceptions import BadRequest
from usha.exceptions import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    post_id = kwargs['post_id']
    request_data = kwargs['request_data']
    comment_content = request_data['content']
    is_comment_content_invalid = not comment_content

    if is_comment_content_invalid:
        raise BadRequest(*INVALID_COMMENT_CONTENT)

    try:
        comment = create_comment(user_id=user.id, post_id=post_id,
                       comment_content=comment_content)
    except:
        raise BadRequest(*INVALID_POST)
        
    data = json.dumps({'comment_id': comment.id})
    response = HttpResponse(data, status=201)
    return response