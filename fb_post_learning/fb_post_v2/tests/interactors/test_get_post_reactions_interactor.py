import pytest
from unittest.mock import create_autospec

from fb_post_v2.exceptions.exceptions import InvalidPostId, NotFound
from fb_post_v2.interactors.get_post_reactions_interactor import \
    GetPostReactionsInteractor
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface
from fb_post_v2.interactors.storages.dtos import *
from .conftest import *

class TestGetPostReactionsInteractor:

    def test_given_invalid_post_id_raises_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostReactionsInteractor(storage=storage, presenter=presenter)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound

        with pytest.raises(NotFound):
            interactor.get_post_reactions(
                post_id=post_id
            )
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_return_post_reactions_dict(
            self, user_dtos, reaction_dtos):
        user_dto = user_dtos
        reaction_dto = reaction_dtos

        post_reaction_dtos = PostReactionCompleteDetailsDto(user_dtos=user_dto,
                                                            reaction_dtos=reaction_dto)
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        expected_output = [
            {
                "user_id":  1,
                "name": "usha",
                "profile_pic_url": "www.gmail.com",
                "reaction": "WOW"
            }
        ]
        
        interactor = GetPostReactionsInteractor(storage=storage, presenter=presenter)
        storage.get_post_reaction_dtos.return_value = post_reaction_dtos       
        presenter.get_response_for_get_post_reactions.return_value = \
            expected_output

        post_reactions = interactor.get_post_reactions(
            post_id=post_id)

        index = 0
        for user in post_reactions:
            assert user["user_id"] == expected_output[index]["user_id"]
            index += 1

        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_post_reaction_dtos.assert_called_once_with(post_id=post_id)
        presenter.get_response_for_get_post_reactions.assert_called_once_with(
            post_reaction_dtos=post_reaction_dtos)
