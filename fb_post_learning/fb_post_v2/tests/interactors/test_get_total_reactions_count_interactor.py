from fb_post_v2.interactors.get_total_reactions_count_interactor import \
    GetTotalReactionsCountInteractor
from unittest.mock import create_autospec

from fb_post_v2.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_v2.interactors.storages.storage_interface import \
    StorageInterface


def test_get_total_reactions_count_interactor_returns_reactions_count():
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(StorageInterface)
    interactor = GetTotalReactionsCountInteractor(storage=storage, presenter=presenter)
    reactions_count = 6
    expected_total_reactions_count = {
        "reactions_count": reactions_count
    }
    storage.get_total_reaction_count.return_value = reactions_count
    presenter.get_response_for_total_reaction_count.return_value = \
        expected_total_reactions_count
    actual_total_reactions_count = interactor. \
        get_total_reaction_count()

    assert expected_total_reactions_count == actual_total_reactions_count
    storage.get_total_reaction_count.assert_called_once()
    presenter.get_response_for_total_reaction_count.\
        assert_called_once_with(count=reactions_count)
