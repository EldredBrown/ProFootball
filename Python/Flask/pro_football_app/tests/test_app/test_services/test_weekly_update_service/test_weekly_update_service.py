from decimal import Decimal

import unittest
from unittest.mock import Mock, call

from app.data.entities.game import Game
from app.data.entities.league_season import LeagueSeason
from app.data.entities.league_season_totals import LeagueSeasonTotals
from app.data.entities.season import Season
from app.data.entities.team_season import TeamSeason
from app.data.entities.team_season_schedule_averages import TeamSeasonScheduleAverages
from app.data.entities.team_season_schedule_totals import TeamSeasonScheduleTotals

from app.data.repositories.game_repository import GameRepository
from app.data.repositories.league_season_repository import LeagueSeasonRepository
from app.data.repositories.league_season_totals_repository import LeagueSeasonTotalsRepository
from app.data.repositories.season_repository import SeasonRepository
from app.data.repositories.team_season_repository import TeamSeasonRepository
from app.data.repositories.team_season_schedule_repository import TeamSeasonScheduleRepository

from app.services.weekly_update_service.weekly_update_service import WeeklyUpdateService


class TestWeeklyUpdateService(unittest.TestCase):

    def setUp(self) -> None:
        self._season_repository = Mock(SeasonRepository)
        self._game_repository = Mock(GameRepository)
        self._league_season_repository = Mock(LeagueSeasonRepository)
        self._team_season_repository = Mock(TeamSeasonRepository)
        self._league_season_totals_repository = Mock(LeagueSeasonTotalsRepository)
        self._team_season_schedule_repository = Mock(TeamSeasonScheduleRepository)
        self._test_service = WeeklyUpdateService(self._season_repository,
                                                 self._game_repository,
                                                 self._league_season_repository,
                                                 self._team_season_repository,
                                                 self._league_season_totals_repository,
                                                 self._team_season_schedule_repository)

    def test_run_weekly_update_should_not_update_anything_when_league_season_totals_is_none_and_games_is_none(self):
        # Arrange
        self._league_season_totals_repository.get_league_season_totals.return_value = None

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = None

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_not_called()
        fake_league_season.update_games_and_points.assert_not_called()
        self._league_season_repository.update_league_season.assert_not_called()
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_anything_when_league_season_totals_total_games_is_none_and_games_is_none(self):
        # Arrange
        self._league_season_totals_repository.get_league_season_totals.return_value \
            = LeagueSeasonTotals(total_games=None, total_points=None)

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = None

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_not_called()
        fake_league_season.update_games_and_points.assert_not_called()
        self._league_season_repository.update_league_season.assert_not_called()
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_anything_when_league_season_totals_total_points_is_none_and_games_is_none(self):
        # Arrange
        self._league_season_totals_repository.get_league_season_totals.return_value \
            = LeagueSeasonTotals(total_games=0, total_points=None)

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = None

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_not_called()
        fake_league_season.update_games_and_points.assert_not_called()
        self._league_season_repository.update_league_season.assert_not_called()
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_anything_when_league_season_is_none_and_games_is_none(self):
        # Arrange
        self._league_season_totals_repository.get_league_season_totals.return_value = LeagueSeasonTotals()

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = None

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_not_called()
        self._league_season_repository.update_league_season.assert_not_called()
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_update_league_season_total_points_and_games_when_league_season_totals_and_league_season_are_not_none_and_games_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_week_count_when_games_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        self._game_repository.get_games.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(
            fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_week_count_when_games_is_empty(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        self._game_repository.get_games.return_value = []

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_week_count_when_games_has_no_games_for_specified_year(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        self._game_repository.get_games.return_value = [Game(1921, 0, "Guest", 0, "Host", 0)]

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_not_called()
        self._season_repository.update_season.assert_not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_week_count_when_games_has_games_for_specified_year_and_season_for_specified_year_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        self._game_repository.get_games.return_value = [Game(season_year, 1, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = None

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == 0
        self._season_repository.update_season.not_called()
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_update_week_count_when_games_has_games_for_specified_year_and_season_for_specified_year_is_not_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 1
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_when_week_count_is_less_than_three(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 2
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_update_rankings_when_week_count_is_three(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 3
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        self._team_season_repository.get_team_seasons_by_season.return_value = None

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_update_rankings_when_week_count_is_greater_than_three(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        self._team_season_repository.get_team_seasons_by_season.return_value = None

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        self._team_season_repository.get_team_seasons_by_season.return_value = None

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_empty(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        self._team_season_repository.get_team_seasons_by_season.return_value = []

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_not_called()
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value = None

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=None)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_not_called()
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_averages_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value = None

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_average_points_for_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        team_season_schedule_averages = TeamSeasonScheduleAverages(points_for=None, points_against=None)
        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value \
            = team_season_schedule_averages

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_average_points_against_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        self._league_season_repository.get_league_season_by_league_and_season.return_value = fake_league_season

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        team_season_schedule_averages = TeamSeasonScheduleAverages(points_for=Decimal('0'), points_against=None)
        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value \
            = team_season_schedule_averages

        league_name = "APFA"

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_called_once_with(league_name,
                                                                                                      season_year)
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_average_points_for_and_points_against_are_not_none_and_league_season_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        league_season = None
        self._league_season_repository.get_league_season_by_league_and_season.side_effect = (fake_league_season,
                                                                                             league_season)

        season_year = 1920
        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        league_name = "APFA"
        fake_team_season.league_name = league_name
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        team_season_schedule_averages = TeamSeasonScheduleAverages(points_for=Decimal('0'), points_against=Decimal('0'))
        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value \
            = team_season_schedule_averages

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_has_calls([
            call(league_name, season_year),
            call(fake_team_season.league_name, fake_team_season.season_year)
        ])
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_not_update_rankings_for_any_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_average_points_for_and_points_against_are_not_none_and_league_season_average_points_is_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        league_name = "APFA"
        season_year = 1920
        league_season = LeagueSeason(league_name, season_year, average_points=None)
        self._league_season_repository.get_league_season_by_league_and_season.side_effect = (fake_league_season,
                                                                                             league_season)

        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        fake_team_season.league_name = league_name
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        team_season_schedule_averages = TeamSeasonScheduleAverages(points_for=Decimal('0'), points_against=Decimal('0'))
        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value \
            = team_season_schedule_averages

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_has_calls([
            call(league_name, season_year),
            call(fake_team_season.league_name, fake_team_season.season_year)
        ])
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_not_called()
        self._team_season_repository.update_team_season.not_called()

    def test_run_weekly_update_should_update_rankings_for_team_season_when_week_count_is_greater_than_three_and_team_seasons_for_specified_year_is_not_empty_and_team_season_schedule_totals_schedule_games_is_not_none_and_team_season_schedule_average_points_for_and_points_against_are_not_none_and_league_season_average_points_is_not_none(self):
        # Arrange
        league_season_totals = LeagueSeasonTotals()
        league_season_totals.total_games = 1
        league_season_totals.total_points = 2
        self._league_season_totals_repository.get_league_season_totals.return_value = league_season_totals

        fake_league_season = Mock(LeagueSeason)
        league_name = "APFA"
        season_year = 1920
        league_season = LeagueSeason(league_name, season_year, average_points=Decimal('0'))
        self._league_season_repository.get_league_season_by_league_and_season.side_effect = (fake_league_season,
                                                                                             league_season)

        week_count = 4
        self._game_repository.get_games.return_value = [Game(season_year, week_count, "Guest", 0, "Host", 0)]

        season = Season(season_year, num_of_weeks_completed=0)
        self._season_repository.get_season_by_year.return_value = season

        fake_team_season = Mock(TeamSeason)
        fake_team_season.team_name = "Team"
        fake_team_season.season_year = season_year
        fake_team_season.league_name = league_name
        self._team_season_repository.get_team_seasons_by_season.return_value = [fake_team_season]

        team_season_schedule_totals = TeamSeasonScheduleTotals(schedule_games=3)
        self._team_season_schedule_repository.get_team_season_schedule_totals.return_value \
            = team_season_schedule_totals

        team_season_schedule_averages = TeamSeasonScheduleAverages(points_for=Decimal('1'), points_against=Decimal('2'))
        self._team_season_schedule_repository.get_team_season_schedule_averages.return_value \
            = team_season_schedule_averages

        # Act
        self._test_service.run_weekly_update(league_name, season_year)

        # Assert
        self._league_season_totals_repository.get_league_season_totals.assert_any_call(league_name, season_year)
        self._league_season_repository.get_league_season_by_league_and_season.assert_has_calls([
            call(league_name, season_year),
            call(fake_team_season.league_name, fake_team_season.season_year)
        ])
        fake_league_season.update_games_and_points.assert_any_call(league_season_totals.total_games,
                                                                   league_season_totals.total_points)
        self._league_season_repository.update_league_season.assert_any_call(fake_league_season)
        self._game_repository.get_games.assert_called()
        self._season_repository.get_season_by_year.assert_any_call(season_year)
        assert season.num_of_weeks_completed == week_count
        self._season_repository.update_season.assert_any_call(season)
        self._team_season_repository.get_team_seasons_by_season.assert_any_call(season_year)
        self._team_season_schedule_repository.get_team_season_schedule_totals.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        self._team_season_schedule_repository.get_team_season_schedule_averages.assert_any_call(
            fake_team_season.team_name, fake_team_season.season_year
        )
        fake_team_season.update_rankings.assert_any_call(team_season_schedule_averages.points_for,
                                                         team_season_schedule_averages.points_against,
                                                         league_season.average_points)
        self._team_season_repository.update_team_season.any_call(fake_team_season)
