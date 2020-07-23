# pylint: disable=wrong-import-position

APP_NAME = "usha"
OPERATION_NAME = "react_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comment/{comment_id}/react/"

from .test_case_01 import TestCase01ReactToCommentAPITestCase

__all__ = [
    "TestCase01ReactToCommentAPITestCase"
]
