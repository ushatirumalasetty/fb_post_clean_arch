from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface

class GetTotalReactionsCountInteractor:
    def __init__(self, storage:StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
        
    def get_total_reaction_count(self):
        count = self.storage.get_total_reaction_count()
        return self.presenter.get_response_for_total_reaction_count(count = count)