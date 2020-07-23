from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.exceptions.exceptions import InvalidPostId


class CreateCommentInteractor:
    def __init__(self, storage:StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def create_comment(self, user_id: int, post_id :int, comment_content: str):
        
        try:
            self.storage.validate_post_id(post_id=post_id)
        except InvalidPostId:
            self.presenter.raise_exception_for_invalid_post()
            return

        new_comment_id = self.storage.create_comment(
            user_id = user_id,
            post_id = post_id,
            comment_content = comment_content
            )
            
        return self.presenter.get_create_comment_response(
                comment_id = new_comment_id
            )
