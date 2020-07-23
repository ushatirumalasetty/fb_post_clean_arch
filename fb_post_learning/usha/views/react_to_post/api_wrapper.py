from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.react_to_post import react_to_post
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_COMMENT_CONTENT, INVALID_POST, INVALID_REACTION_TYPE
from django_swagger_utils.drf_server.exceptions import BadRequest
from usha.exceptions import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    post_id = kwargs['post_id']
    request_data = kwargs['request_data']
    reaction_type = request_data['reaction_type']
    try:
        react_to_post(user_id=user.id, post_id=post_id,
                       reaction_type=reaction_type)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
    except InvalidReactionTypeException:
        raise BadRequest(*INVALID_REACTION_TYPE)