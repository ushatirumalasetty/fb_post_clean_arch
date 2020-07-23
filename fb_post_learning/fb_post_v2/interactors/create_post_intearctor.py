from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface

class CreatePostInteractor:
    def __init__(self, storage:StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_post(self, user_id: int, post_content: str):
        new_post_id = self.storage.create_post(
            user_id = user_id,
            post_content = post_content
        )
        return self.presenter.get_create_post_response(
                    post_id = new_post_id
                )
