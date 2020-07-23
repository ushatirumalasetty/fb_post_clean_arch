from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.get_posts_with_more_positive_reactions import get_posts_with_more_positive_reactions
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_COMMENT_CONTENT, INVALID_POST
from django_swagger_utils.drf_server.exceptions import BadRequest
from usha.exceptions import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    list_of_post_ids = get_posts_with_more_positive_reactions()
    data = json.dumps({'post_ids': list_of_post_ids})
    response = HttpResponse(data, status=201)
    return response