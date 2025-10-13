import pytest

import unittest
from unittest.mock import Mock

from app.data.entities.game import Game
from app.data.errors import EntityNotFoundError
from app.data.repositories.game_repository import GameRepository
from app.data.repositories.team_season_repository import TeamSeasonRepository
from app.services.constants import Direction
from app.services.game_service.game_service import GameService
from app.services.game_service.process_game_strategy.add_game_strategy import AddGameStrategy
from app.services.game_service.process_game_strategy.process_game_strategy import ProcessGameStrategy
from app.services.game_service.process_game_strategy.process_game_strategy_factory \
    import ProcessGameStrategyFactory
from app.services.game_service.process_game_strategy.subtract_game_strategy import SubtractGameStrategy


class TestGameService(unittest.TestCase):

    def setUp(self) -> None:
        self._game_repository = Mock(GameRepository)
        self._team_season_repository = Mock(TeamSeasonRepository)
        self._process_game_strategy_factory = Mock(ProcessGameStrategyFactory)
        self._test_service = GameService(self._game_repository, self._team_season_repository,
                                         self._process_game_strategy_factory)

    def test_add_game_should_raise_value_error_when_new_game_arg_is_none(self):
        # Act and Assert
        with pytest.raises(ValueError):
            self._test_service.add_game(None)

    def test_add_game_should_add_game_to_repository_when_new_team_season_with_new_game_guest_and_season_is_in_datastore(self):
        # Arrange
        self._team_season_repository.team_season_exists_with_name_and_year.side_effect = (True, False)
        strategy = Mock(ProcessGameStrategy)
        self._process_game_strategy_factory.create_strategy.return_value = strategy

        fake_game = Mock(Game)

        # Act
        try:
            self._test_service.add_game(fake_game)
        except EntityNotFoundError:
            assert False

        # Assert
        self._team_season_repository.team_season_exists_with_name_and_year.assert_called_once_with(
            fake_game.guest_name, fake_game.season_year
        )
        fake_game.decide_winner_and_loser.assert_called_once()
        self._game_repository.add_game.assert_any_call(fake_game)
        self._process_game_strategy_factory.create_strategy.assert_any_call(Direction.UP)
        strategy.process_game.assert_called_once_with(fake_game)

    def test_add_game_should_add_game_to_repository_when_new_team_seasons_with_new_game_guest_and_season_and_with_new_game_host_and_season_are_in_datastore(self):
        # Arrange
        self._team_season_repository.team_season_exists_with_name_and_year.side_effect = (False, True)
        strategy = Mock(ProcessGameStrategy)
        self._process_game_strategy_factory.create_strategy.return_value = strategy

        fake_game = Mock(Game)

        # Act
        try:
            self._test_service.add_game(fake_game)
        except EntityNotFoundError:
            assert False

        # Assert
        self._team_season_repository.team_season_exists_with_name_and_year.assert_any_call(
            fake_game.guest_name, fake_game.season_year
        )
        self._team_season_repository.team_season_exists_with_name_and_year.assert_any_call(
            fake_game.host_name, fake_game.season_year
        )
        fake_game.decide_winner_and_loser.assert_called_once()
        self._game_repository.add_game.assert_any_call(fake_game)
        self._process_game_strategy_factory.create_strategy.assert_any_call(Direction.UP)
        strategy.process_game.assert_called_once_with(fake_game)

    def test_add_game_should_raise_entity_not_found_error_when_team_season_with_new_game_guest_and_season_and_team_season_with_new_game_host_and_season_not_in_datastore(self):
        # Arrange
        self._team_season_repository.team_season_exists_with_name_and_year.side_effect = (False, False)

        new_game = Game(season_year=1, week=1, guest_name="Guest", guest_score=0, host_name="Host", host_score=0)

        # Act and Assert
        with pytest.raises(EntityNotFoundError):
            self._test_service.add_game(new_game)

        self._team_season_repository.team_season_exists_with_name_and_year.assert_any_call(
            new_game.guest_id, new_game.season_id
        )

    def test_edit_game_should_raise_value_error_when_new_game_arg_is_none(self):
        # Act and Assert
        with pytest.raises(ValueError):
            self._test_service.edit_game(None, None)

    def test_edit_game_should_raise_value_error_when_old_game_arg_is_none(self):
        # Arrange
        new_game = Game(season_year=1, week=1, guest_name="Guest", guest_score=0, host_name="Host", host_score=0)

        # Act and Assert
        with pytest.raises(ValueError):
            self._test_service.edit_game(new_game, None)

    @pytest.mark.skip("WIP")
    def test_edit_game_should_raise_entity_not_found_error_when_selected_game_not_found(self):
        # Arrange
        self._game_repository.get_game.return_value = None

        new_game = Game(season_year=1, week=1, guest_name="Guest", guest_score=0, host_name="Host", host_score=0)
        old_game = Game(season_year=1, week=1, guest_name="Guest", guest_score=0, host_name="Host", host_score=0)

        # Act and Assert
        with pytest.raises(EntityNotFoundError):
            self._test_service.edit_game(new_game, old_game)

    def test_edit_game_should_edit_game_in_repository_when_args_are_not_none_and_selected_game_is_found(self):
        # Arrange
        selected_game = Mock(Game)
        self._game_repository.get_game.return_value = selected_game

        subtract_strategy = Mock(SubtractGameStrategy)
        add_strategy = Mock(AddGameStrategy)
        self._process_game_strategy_factory.create_strategy.side_effect = (subtract_strategy, add_strategy)

        new_game = Mock(Game)
        old_game = Mock(Game)

        # Act
        self._test_service.edit_game(new_game, old_game)

        # Assert
        new_game.decide_winner_and_loser.assert_called()
        self._game_repository.update_game.assert_called_once_with(new_game)

        self._process_game_strategy_factory.create_strategy.assert_any_call(Direction.DOWN)
        subtract_strategy.process_game.assert_called_once_with(old_game)

        self._process_game_strategy_factory.create_strategy.assert_any_call(Direction.UP)
        add_strategy.process_game.assert_called_once_with(new_game)

    @pytest.mark.skip("WIP")
    def test_delete_game_should_raise_entity_not_found_error_when_game_with_passed_id_is_not_found(self):
        # Arrange
        self._game_repository.get_game.return_value = None

        # Act and Assert
        id = 1
        with pytest.raises(EntityNotFoundError):
            self._test_service.delete_game(id)

    def test_delete_game_should_delete_game_from_repository_when_game_with_passed_id_is_found(self):
        # Arrange
        old_game = Mock(Game)
        self._game_repository.get_game.return_value = old_game

        strategy = Mock(SubtractGameStrategy)
        self._process_game_strategy_factory.create_strategy.return_value = strategy

        # Act
        id = 1
        self._test_service.delete_game(id)

        # Assert
        self._game_repository.get_game.assert_any_call(id)
        self._game_repository.delete_game.assert_any_call(id)
        self._process_game_strategy_factory.create_strategy.assert_any_call(Direction.DOWN)
        strategy.process_game.assert_called_once_with(old_game)
