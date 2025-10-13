import pytest

import unittest
from unittest.mock import Mock

from app.data.entities.game import Game
from app.data.entities.team_season import TeamSeason
from app.data.repositories.team_season_repository import TeamSeasonRepository
from app.services.game_service.process_game_strategy.process_game_strategy import ProcessGameStrategy


class TestProcessGameStrategy(unittest.TestCase):

    def setUp(self) -> None:
        self._team_season_repository = Mock(TeamSeasonRepository)

        self._test_strategy = ProcessGameStrategy(team_season_repository=self._team_season_repository)

    def test_process_game_should_raise_value_error_when_game_arg_is_none(self):
        # Arrange
        game = None

        # Act & Assert
        with pytest.raises(ValueError):
            self._test_strategy.process_game(game)

    def test_process_game_should_process_game_and_raise_not_implemented_error_when_game_arg_is_not_none(self):
        # Arrange
        game = Game(season_year=1, week=1, guest_name="Guest", guest_score=0, host_name="Host", host_score=0)
        guest_season = Mock(TeamSeason)
        host_season = Mock(TeamSeason)
        self._team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

        # Act
        with pytest.raises(NotImplementedError):
            self._test_strategy.process_game(game)

        # Assert
        assert self._team_season_repository.get_team_season_by_team_and_season.call_count == 2
        self._team_season_repository.get_team_season_by_team_and_season.assert_any_call(game.guest_id,
                                                                                        game.season_id)
        self._team_season_repository.get_team_season_by_team_and_season.assert_any_call(game.host_id,
                                                                                        game.season_id)
