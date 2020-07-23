from unittest.mock import create_autospec

from fb_post_v2.interactors.get_posts_reacted_by_user_interactor import \
    GetUserReactedPostInteractor

from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


def test_get_user_reacted_posts_interactor_given_user_id_return_post_ids():
    post_ids = [1, 2, 3]
    expected_output = {
        "post_ids": post_ids
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserReactedPostInteractor(storage=storage, presenter=presenter)
    storage.get_posts_reacted_by_user.return_value = post_ids
    presenter.get_response_for_user_reacted_posts.return_value = \
        expected_output

    post_ids_dict = interactor.get_user_reacted_posts()

    assert post_ids_dict == expected_output
    storage.get_posts_reacted_by_user.assert_called_once_with()
    presenter.get_response_for_user_reacted_posts.assert_called_once_with(
        post_ids=post_ids)
