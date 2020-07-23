from fb_post_v2.exceptions.exceptions import InvalidPostId
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface
from fb_post_v2.interactors.storages.dtos import *


class GetPostReactionsInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter

    def get_post_reactions(self, post_id: int):
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            return self.presenter.raise_exception_for_invalid_post()
        post_reaction_dtos = self.storage.get_post_reaction_dtos(
            post_id=post_id)
        return self.presenter.get_response_for_get_post_reactions(
            post_reaction_dtos=post_reaction_dtos)
