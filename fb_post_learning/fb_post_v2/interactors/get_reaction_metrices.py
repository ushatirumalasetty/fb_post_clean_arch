from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.exceptions.exceptions import InvalidPostId
from fb_post_v2.interactors.storages.dtos import ReactionMetricesDto

class GetReactionMetricesInteractor():
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
        
    def get_reaction_metrices(self, post_id):
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            self.presenter.raise_exception_for_invalid_post()
            return
        result = self.storage.get_reaction_metrices(post_id = post_id)
        return self.presenter.get_response_for_reaction_metrices(result = result)