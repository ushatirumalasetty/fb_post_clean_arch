# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "reaction_metrices"
REQUEST_METHOD = "get"
URL_SUFFIX = "reaction_metrices/{post_id}/"

from .test_case_01 import TestCase01ReactionMetricesAPITestCase

__all__ = [
    "TestCase01ReactionMetricesAPITestCase"
]
