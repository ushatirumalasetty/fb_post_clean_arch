import pytest
from unittest.mock import create_autospec
from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import PresenterInterface
from fb_post_v2.interactors.reply_to_comment_interactor import ReplyToCommentInteractor
from fb_post_v2.exceptions.exceptions import *

class TestReplyToCommentInteractor:
    def test_given_invalid_comment_id_raises_exception(self):
        user_id = 1
        comment_id = 1
        reply_content = "usha"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = ReplyToCommentInteractor(storage, presenter)
        storage.validate_comment_id.side_effect = InvalidCommentId
        presenter.raise_exception_for_invalid_comment.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.reply_to_comment(user_id=user_id,
                                        comment_id=comment_id,
                                        reply_content=reply_content)

        storage.validate_comment_id.assert_called_once_with(comment_id=comment_id)
        presenter.raise_exception_for_invalid_comment.assert_called_once()
    
    def test_reply_to_comment_if_reply_given_to_comment(self):
        user_id = 1
        comment_id = 1
        reply_content = "usha"
        parent_comment_id = 1
        expected_comment_id =1
        mock_comment_id ={"comment_id": expected_comment_id}
        
        storage = create_autospec(StorageInterface)        
        presenter = create_autospec(PresenterInterface)
       
        storage.validate_comment_id_return_parent_comment_id.return_value = parent_comment_id
        storage.reply_to_comment.return_value = expected_comment_id
        presenter.get_reply_to_comment_response.return_value = mock_comment_id
        interactor = ReplyToCommentInteractor(storage=storage, presenter=presenter)
        actual_comment_id_dic = interactor.reply_to_comment(user_id=user_id,
                                                            comment_id=comment_id,
                                                            reply_content=reply_content)

        assert actual_comment_id_dic == mock_comment_id
        
        storage.reply_to_comment.assert_called_once_with(user_id=user_id,comment_id=comment_id,reply_content=reply_content )
        presenter.get_reply_to_comment_response.assert_called_once_with(reply_id=expected_comment_id)
