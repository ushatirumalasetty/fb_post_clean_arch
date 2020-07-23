# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "delete_post"
REQUEST_METHOD = "delete"
URL_SUFFIX = "post/{post_id}/delete/"

from .test_case_01 import TestCase01DeletePostAPITestCase

__all__ = [
    "TestCase01DeletePostAPITestCase"
]
