# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "create_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{post_id}/create/"

from .test_case_01 import TestCase01CreateCommentAPITestCase

__all__ = [
    "TestCase01CreateCommentAPITestCase"
]
