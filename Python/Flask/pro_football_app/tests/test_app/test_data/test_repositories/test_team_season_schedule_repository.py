import pytest
from unittest.mock import ANY, Mock

from sqlalchemy.engine import CursorResult

from app.data.db_context import DbContext
from app.data.entities.team_season_schedule_averages import TeamSeasonScheduleAverages
from app.data.entities.team_season_schedule_totals import TeamSeasonScheduleTotals
from app.data.repositories.team_season_schedule_repository import TeamSeasonScheduleRepository


@pytest.fixture
def fake_db_context():
    return Mock(DbContext)


@pytest.fixture
def fake_cursor_result():
    return Mock(CursorResult)


def test_get_team_season_schedule_totals_should_get_empty_team_season_schedule_totals_when_query_returns_none(
        fake_db_context, fake_cursor_result):
    # Arrange
    fake_cursor_result.first.return_value = None
    fake_db_context.execute_query.side_effect = [None, fake_cursor_result]
    test_repository = TeamSeasonScheduleRepository(fake_db_context)

    team_name = "Team"
    season_year = 1920

    # Act
    tssta = test_repository.get_team_season_schedule_totals(team_name, season_year)

    # Assert
    statement1 = f"CALL get_team_season_schedule_totals('{team_name}', {season_year});"
    fake_db_context.execute_query.assert_any_call(statement1, ANY)

    statement2 = "SELECT * FROM team_season_schedule_totals;"
    fake_db_context.execute_query.assert_any_call(statement2, ANY)

    fake_cursor_result.first.assert_called()
    assert isinstance(tssta, TeamSeasonScheduleTotals)
    assert tssta.games is None
    assert tssta.points_for is None
    assert tssta.points_against is None
    assert tssta.schedule_wins is None
    assert tssta.schedule_losses is None
    assert tssta.schedule_ties is None
    assert tssta.schedule_winning_percentage is None
    assert tssta.schedule_games is None
    assert tssta.schedule_points_for is None
    assert tssta.schedule_points_against is None


def test_get_team_season_schedule_totals_should_get_not_empty_team_season_schedule_totals_when_query_does_not_return_none(
        fake_db_context, fake_cursor_result):
    # Arrange
    games = 0
    points_for = 1
    points_against = 2
    schedule_wins = 3
    schedule_losses = 4
    schedule_ties = 5
    schedule_winning_percentage = 6
    schedule_games = 7
    schedule_points_for = 8
    schedule_points_against = 9
    fake_cursor_result.first.return_value = (games, points_for, points_against, schedule_wins, schedule_losses,
                                             schedule_ties, schedule_winning_percentage, schedule_games,
                                             schedule_points_for, schedule_points_against)
    fake_db_context.execute_query.side_effect = [None, fake_cursor_result]
    test_repository = TeamSeasonScheduleRepository(fake_db_context)

    team_name = "Team"
    season_year = 1920

    # Act
    tssta = test_repository.get_team_season_schedule_totals(team_name, season_year)

    # Assert
    statement1 = f"CALL get_team_season_schedule_totals('{team_name}', {season_year});"
    fake_db_context.execute_query.assert_any_call(statement1, ANY)

    statement2 = "SELECT * FROM team_season_schedule_totals;"
    fake_db_context.execute_query.assert_any_call(statement2, ANY)

    fake_cursor_result.first.assert_called()
    assert isinstance(tssta, TeamSeasonScheduleTotals)
    assert tssta.games == games
    assert tssta.points_for == points_for
    assert tssta.points_against == points_against
    assert tssta.schedule_wins == schedule_wins
    assert tssta.schedule_losses == schedule_losses
    assert tssta.schedule_ties == schedule_ties
    assert tssta.schedule_winning_percentage == schedule_winning_percentage
    assert tssta.schedule_games == schedule_games
    assert tssta.schedule_points_for == schedule_points_for
    assert tssta.schedule_points_against == schedule_points_against


def test_get_team_season_schedule_averages_should_get_empty_team_season_schedule_averages_when_query_returns_none(
        fake_db_context, fake_cursor_result):
    # Arrange
    fake_cursor_result.first.return_value = None
    fake_db_context.execute_query.return_value = fake_cursor_result
    test_repository = TeamSeasonScheduleRepository(fake_db_context)

    team_name = "Team"
    season_year = 1920

    # Act
    tssaa = test_repository.get_team_season_schedule_averages(team_name, season_year)

    # Assert
    statement = f"CALL get_team_season_schedule_averages('{team_name}', {season_year});"
    fake_db_context.execute_query.assert_called_once_with(statement)
    fake_cursor_result.first.assert_called_once()
    assert isinstance(tssaa, TeamSeasonScheduleAverages)
    assert tssaa.points_for is None
    assert tssaa.points_against is None
    assert tssaa.schedule_points_for is None
    assert tssaa.schedule_points_against is None


def test_get_team_season_schedule_averages_should_get_not_empty_team_season_schedule_averages_when_query_does_not_return_none(
        fake_db_context, fake_cursor_result):
    # Arrange
    points_for = 1
    points_against = 2
    schedule_points_for = 3
    schedule_points_against = 4
    fake_cursor_result.first.return_value = (points_for, points_against, schedule_points_for, schedule_points_against)
    fake_db_context.execute_query.return_value = fake_cursor_result
    test_repository = TeamSeasonScheduleRepository(fake_db_context)

    team_name = "Team"
    season_year = 1920

    # Act
    tssaa = test_repository.get_team_season_schedule_averages(team_name, season_year)

    # Assert
    statement = f"CALL get_team_season_schedule_averages('{team_name}', {season_year});"
    fake_db_context.execute_query.assert_called_once_with(statement)
    fake_cursor_result.first.assert_called_once()
    assert isinstance(tssaa, TeamSeasonScheduleAverages)
    assert tssaa.points_for == points_for
    assert tssaa.points_against == points_against
    assert tssaa.schedule_points_for == schedule_points_for
    assert tssaa.schedule_points_against == schedule_points_against
