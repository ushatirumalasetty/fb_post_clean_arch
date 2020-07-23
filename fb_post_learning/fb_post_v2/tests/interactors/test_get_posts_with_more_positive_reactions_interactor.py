from unittest.mock import create_autospec

from fb_post_v2.interactors. \
    get_posts_with_more_positive_reactions_interactor import \
    GetPostsWithMorePositiveReactionsInteractor
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class TestGetPostsWithMorePositiveReactionsInteractor:
    def test_returns_post_ids(self):
        expected_post_ids = [1, 2, 3]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostsWithMorePositiveReactionsInteractor(storage, presenter)
        storage.get_posts_with_more_positive_reactions. \
            return_value = expected_post_ids
        presenter.get_response_for_get_posts_with_more_positive_reaction. \
            return_value = expected_post_ids
    
        actual_posts_ids = interactor. \
            get_posts_with_more_positive_reactions()
    
        assert expected_post_ids == actual_posts_ids
        presenter.get_response_for_get_posts_with_more_positive_reaction. \
            assert_called_once_with(post_ids=actual_posts_ids)
        storage.get_posts_with_more_positive_reactions. \
            assert_called_once()
