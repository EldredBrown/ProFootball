from unittest.mock import Mock

from sqlalchemy.engine import CursorResult

from app.data.db_context import DbContext
from app.data.entities.league_season_totals import LeagueSeasonTotals
from app.data.repositories.league_season_totals_repository import LeagueSeasonTotalsRepository


def test_get_league_season_totals_should_get_league_season_totals():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_cursor_result = Mock(CursorResult)

    total_games = 1
    total_points = 2
    fake_cursor_result.first.return_value = (total_games, total_points)
    fake_db_context.execute_query.return_value = fake_cursor_result
    test_repository = LeagueSeasonTotalsRepository(fake_db_context)

    league_name = "APFA"
    season_year = 1920

    # Act
    lsta = test_repository.get_league_season_totals(league_name, season_year)

    # Assert
    statement = f"CALL get_league_season_totals('{league_name}', {season_year});"
    fake_db_context.execute_query.assert_called_once_with(statement)
    fake_cursor_result.first.assert_called_once()
    assert isinstance(lsta, LeagueSeasonTotals)
    assert lsta.total_games == total_games
    assert lsta.total_points == total_points
