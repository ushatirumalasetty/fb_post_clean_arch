from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from usha.utils.get_reaction_metrics import get_reaction_metrics
from .validator_class import ValidatorClass
from usha.constants.exception_messages import INVALID_POST, INVALID_REACTION_TYPE
from django_swagger_utils.drf_server.exceptions import BadRequest
from usha.exceptions import *


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    post_id = kwargs['post_id']
    try:
        dict_of_metrics= get_reaction_metrics(post_id=post_id)
    except InvalidPostException:
        raise BadRequest(*INVALID_POST)
    data = json.dumps({'reaction_metrics': dict_of_metrics})
    response = HttpResponse(data, status=201)
    return response