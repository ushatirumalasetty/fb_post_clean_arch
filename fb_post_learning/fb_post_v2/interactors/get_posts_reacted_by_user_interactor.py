from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class GetUserReactedPostInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_user_reacted_posts(self):
        list_of_post_ids = self.storage.get_posts_reacted_by_user()
        return self.presenter.\
        get_response_for_user_reacted_posts(post_ids=list_of_post_ids)