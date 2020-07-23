import pytest
from fb_post_v2.interactors.get_reaction_metrices import \
    GetReactionMetricesInteractor
from unittest.mock import create_autospec
from fb_post_v2.interactors.storages.dtos import ReactionMetricesDto

from fb_post_v2.exceptions.exceptions import InvalidPostId, NotFound
from fb_post_v2.constants.enums import ReactionType
from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface
from fb_post_v2.interactors.storages.dtos import \
    ReactionMetricesDto



class TestGetReactionMetricsOfAPostInteractor:

    def test_given_invalid_post_raise_exception(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.validate_post_id.side_effect = InvalidPostId
        presenter.raise_exception_for_invalid_post.side_effect = NotFound
        interactor = GetReactionMetricesInteractor(storage=storage, presenter=presenter)
        with pytest.raises(NotFound):
            interactor.get_reaction_metrices(
                post_id=post_id
            )
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        presenter.raise_exception_for_invalid_post.assert_called_once()

    def test_given_valid_post_id_returns_reaction_metrics(self):
        post_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetReactionMetricesInteractor(storage=storage, presenter=presenter)
        expected_output = [
            {
                "reaction_type": "WOW",
                "count": 5
            },
            {
                "reaction_type": "HAHA",
                "count": 4
            }
        ]
        reaction_metrics_details_dto = [
            ReactionMetricesDto(
                reaction_type=ReactionType.WOW.value,
                count=5),
            ReactionMetricesDto(
                reaction_type=ReactionType.HAHA.value,
                count=4)
        ]
        storage.get_reaction_metrices.return_value = \
            reaction_metrics_details_dto
        presenter.get_response_for_reaction_metrices.return_value = expected_output
        
        actual_result = interactor.get_reaction_metrices(post_id=post_id)
        print("ekkthrthkkeek3i3io")
        assert actual_result == expected_output
        
        storage.validate_post_id.assert_called_once_with(post_id=post_id)
        storage.get_reaction_metrices.assert_called_once_with(
            post_id=post_id)
        presenter.get_response_for_reaction_metrices. \
            assert_called_once_with(result=
                                    reaction_metrics_details_dto)
