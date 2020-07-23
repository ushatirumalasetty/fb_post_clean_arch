from fb_post_v2.exceptions.exceptions import InvalidPostId
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class DeletePostInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def delete_post_interactor(self,post_id: int):
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            return self.presenter.raise_exception_for_invalid_post()
        self.storage.delete_post(post_id=post_id)