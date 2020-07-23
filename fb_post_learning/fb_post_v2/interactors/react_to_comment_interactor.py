from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.exceptions.exceptions import InvalidCommentId, \
    ReactionDoesNotExist
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


class ReactToCommentInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def react_to_comment(self, user_id: int,
                      comment_id: int,
                      reaction_type: ReactionType):
        try:
            self.storage.validate_comment_id(comment_id=comment_id)
        except InvalidCommentId:
            self.presenter.raise_exception_for_invalid_comment()

        try:
            old_reaction_type = self.storage. \
                validate_comment_reaction_if_exists_get_reaction_type(
                    user_id=user_id,
                    comment_id=comment_id
                )
        except ReactionDoesNotExist:
            self.storage.create_comment_reaction(
                comment_id=comment_id, user_id=user_id, reaction_type=reaction_type)
            return

        is_undo_reaction = old_reaction_type == reaction_type

        if is_undo_reaction:
            self.storage.undo_comment_reaction(comment_id=comment_id, user_id=user_id)
        else:
            self.storage.update_comment_reaction(user_id=user_id, comment_id=comment_id,
                                              reaction_type=reaction_type)
