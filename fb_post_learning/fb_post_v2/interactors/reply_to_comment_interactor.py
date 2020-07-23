from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.exceptions.exceptions import InvalidCommentId

class ReplyToCommentInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def reply_to_comment(self, user_id: int, comment_id: int, reply_content: str):
        try:
            self.storage.validate_comment_id(comment_id=comment_id)
        except InvalidCommentId:
            self.presenter.raise_exception_for_invalid_comment()
            return

        parent_comment_id = self.storage.validate_comment_id_return_parent_comment_id(user_id=user_id,comment_id=comment_id)

        if parent_comment_id:
            reply_comment_id = self.storage.reply_to_comment(user_id=user_id,comment_id=parent_comment_id,reply_content=reply_content)

        else:
            reply_comment_id = self.storage.reply_to_comment(user_id=user_id,comment_id=comment_id,reply_content=reply_content)
        return self.presenter.get_reply_to_comment_response(reply_id = reply_comment_id)
