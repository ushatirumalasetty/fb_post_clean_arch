import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.interactors.create_comment_interactor import CreateCommentInteractor
from fb_post_v2.exceptions.exceptions import *

class TestCreateCommentInteractor:

    def test_given_invalid_post_id_raises_exception(self):
        post_id = 1
        comment_content = "usha"
        user_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = CreateCommentInteractor(storage, presenter)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.create_comment(user_id=user_id,
                                      post_id=post_id,
                                      comment_content=comment_content)

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_creates_comment_and_returns_comment_id_dict(
            self):
        post_id = 1
        comment_content = "usha"
        user_id = 1
        expected_comment_id = 1
        expected_comment_id_dict = {
            "comment_id": expected_comment_id
        }
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = CreateCommentInteractor(storage, presenter)
        storage.create_comment.return_value = \
            expected_comment_id
        presenter.get_create_comment_response.return_value = \
            expected_comment_id_dict

        actual_comment_id_dict = interactor.create_comment(
            user_id=user_id,
            post_id=post_id,
            comment_content=comment_content)

        assert expected_comment_id_dict == actual_comment_id_dict
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.create_comment.assert_called_once_with(
            user_id=user_id,
            post_id=post_id,
            comment_content=comment_content)
        presenter.get_create_comment_response.assert_called_once_with(
            comment_id=expected_comment_id)
