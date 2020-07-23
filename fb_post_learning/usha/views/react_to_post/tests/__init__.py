# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "react_to_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/{post_id}/react/"

from .test_case_01 import TestCase01ReactToPostAPITestCase

__all__ = [
    "TestCase01ReactToPostAPITestCase"
]
