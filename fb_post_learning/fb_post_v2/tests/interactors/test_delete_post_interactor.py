import pytest
from fb_post_v2.interactors.delete_post import \
    DeletePostInteractor
from unittest.mock import create_autospec
from fb_post_v2.exceptions.exceptions import InvalidPostId, NotFound
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class TestDeletePostInteractor:

    def test_given_invalid_post_raise_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DeletePostInteractor(storage, presenter)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound
        with pytest.raises(NotFound):
            interactor.delete_post_interactor(
                post_id=post_id
            )

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()


    def test_given_valid_post_id_delete_post(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = DeletePostInteractor(storage, presenter)
        interactor.delete_post_interactor(
            post_id=post_id
        )
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.delete_post.assert_called_once_with(post_id=post_id)
