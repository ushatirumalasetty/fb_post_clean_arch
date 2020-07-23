from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import InvalidPostId, \
    ReactionDoesNotExist
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class ReactToPostInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def react_to_post(self, user_id: int,
                      post_id: int,
                      reaction_type: ReactionType):
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            self.presenter.raise_exception_for_invalid_post()

        try:
            old_reaction_type = self.storage. \
                validate_post_reaction_if_exists_get_reaction_type(
                    user_id=user_id,
                    post_id=post_id
                )
        except ReactionDoesNotExist:
            self.storage.create_post_reaction(
                post_id=post_id, user_id=user_id, reaction_type=reaction_type)
            return

        is_undo_reaction = old_reaction_type == reaction_type

        if is_undo_reaction:
            self.storage.undo_post_reaction(post_id=post_id, user_id=user_id)
        else:
            self.storage.update_post_reaction(user_id=user_id, post_id=post_id,
                                              reaction_type=reaction_type)
