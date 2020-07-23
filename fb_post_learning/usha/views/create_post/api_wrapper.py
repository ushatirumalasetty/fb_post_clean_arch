from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.create_post import create_post
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_POST_CONTENT
from django_swagger_utils.drf_server.exceptions import BadRequest


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']
    post_content = request_data['content']
    is_post_content_invalid = not post_content
    if is_post_content_invalid:
        raise BadRequest(*INVALID_POST_CONTENT)

    post = create_post(user_id=user.id,
                       post_content=post_content)

    data = json.dumps({'post_id': post.id})
    response = HttpResponse(data, status=201)
    return response