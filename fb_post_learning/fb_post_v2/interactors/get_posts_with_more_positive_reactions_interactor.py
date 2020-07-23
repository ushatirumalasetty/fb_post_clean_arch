from typing import List

from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class GetPostsWithMorePositiveReactionsInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_posts_with_more_positive_reactions(self):
        post_ids = self.storage.get_posts_with_more_positive_reactions()
        return self.presenter.get_response_for_get_posts_with_more_positive_reaction(
            post_ids=post_ids
        )
