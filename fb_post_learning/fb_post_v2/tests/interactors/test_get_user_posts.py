import pytest
from fb_post_v2.exceptions.exceptions import NotFound
from unittest.mock import create_autospec
from fb_post_v2.interactors.get_user_post_interactor import GetUserPostInteractor
from fb_post_v2.interactors.storages.storage_interface import StorageInterface
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.dtos.dtos import *
class TestGetUserPostInteractor:
    def test_given_valid_post_id_returns_post_details(self,
                                                      list_of_post_dtos,
                                                      user_dtos,
                                                      comment_dtos,
                                                      reactions_dtos,
                                                      list_of_post_reactions,
                                                      comment_reactions,
                                                      comment_replies_dtos,
                                                      get_user_posts_response):
        user_id = 1
        post_dtos = list_of_post_dtos
        user_dtos = user_dtos
        comment_dtos = comment_dtos
        reactions_dtos = reactions_dtos
        expected_user_post_details_dict = get_user_posts_response
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetUserPostInteractor(storage=storage, presenter=presenter)

        get_user_post_dto = UserPostCompleteDetailsDto(post_dtos=post_dtos,
                                              user_dtos=user_dtos,
                                              comment_dtos=comment_dtos,
                                              reactions_dtos=reactions_dtos)

        storage.get_user_post.return_value = get_user_post_dto

        presenter.get_response_for_get_user_post_details.return_value = \
            expected_user_post_details_dict

        RESPONSE = interactor.get_user_post(
            user_id=user_id)
        assert RESPONSE == expected_user_post_details_dict
        presenter.get_response_for_get_user_post_details.assert_called_once_with(
            user_post_complete_details_dto=get_user_post_dto,
            get_user_comment_reaction_metrics=comment_reactions,
            get_user_post_reactions_metrics=list_of_post_reactions,
            get_user_comment_replies_metrics=comment_replies_dtos)
