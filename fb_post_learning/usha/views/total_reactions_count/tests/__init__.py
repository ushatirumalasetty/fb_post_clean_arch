# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "total_reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "reactions/count/"

from .test_case_01 import TestCase01TotalReactionsCountAPITestCase

__all__ = [
    "TestCase01TotalReactionsCountAPITestCase"
]
