# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "more_positive_reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/reaction/more_positive/count/"

from .test_case_01 import TestCase01MorePositiveReactionsCountAPITestCase

__all__ = [
    "TestCase01MorePositiveReactionsCountAPITestCase"
]
