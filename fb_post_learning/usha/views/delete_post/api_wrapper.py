from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.delete_post import delete_post
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_POST, USER_CANNOT_DELETE_POST
from django_swagger_utils.drf_server.exceptions import BadRequest
from usha.exceptions import *

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    post_id = kwargs['post_id']
    try:
        delete_post(user_id=user.id, post_id=post_id)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
    except UserCannotDeletePostException:
        raise BadRequest(*USER_CANNOT_DELETE_POST)
   
    response = HttpResponse(status=202)
    return response
