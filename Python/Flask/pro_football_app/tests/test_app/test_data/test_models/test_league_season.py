import pytest

from app.data.models.game import Game
from app.data.models.league_season import LeagueSeason
from app.data.models.team_season import TeamSeason
from test_app import create_app


@pytest.fixture
def test_league_season() -> LeagueSeason:
    return LeagueSeason(league_id=1, season_id=1)


def test_validate_not_empty_when_league_id_is_none_should_raise_value_error():
    # Arrange
    test_app = create_app()
    with test_app.app_context():
        # Act
        with pytest.raises(ValueError) as err:
            test_league_season = LeagueSeason(league_id=None)

    # Assert
    assert isinstance(err.value, ValueError)
    assert err.value.args[0] == "league_id is required."


def test_validate_not_empty_when_league_id_is_zero_should_not_raise_value_error():
    # Arrange
    test_err = None

    test_app = create_app()
    with test_app.app_context():
        # Act
        try:
            test_league_season = LeagueSeason(league_id=0)
        except ValueError as err:
            test_err = err

    # Assert
    assert test_err is None


def test_validate_not_empty_when_league_id_is_greater_than_zero_should_validate_league_id_is_unique():
    # Arrange
    test_err = None

    test_app = create_app()
    with test_app.app_context():
        # Act
        try:
            test_league_season = LeagueSeason(league_id=1)
        except ValueError as err:
            test_err = err

    # Assert
    assert test_err is None


def test_validate_not_empty_when_season_id_is_none_should_raise_value_error():
    # Arrange
    test_app = create_app()
    with test_app.app_context():
        # Act
        with pytest.raises(ValueError) as err:
            test_league_season = LeagueSeason(season_id=None)

    # Assert
    assert isinstance(err.value, ValueError)
    assert err.value.args[0] == "season_id is required."


def test_validate_not_empty_when_season_id_is_zero_should_not_raise_value_error():
    # Arrange
    test_err = None

    test_app = create_app()
    with test_app.app_context():
        # Act
        try:
            test_league_season = LeagueSeason(season_id=0)
        except ValueError as err:
            test_err = err

    # Assert
    assert test_err is None


def test_validate_not_empty_when_season_id_is_greater_than_zero_should_validate_season_id_is_unique():
    # Arrange
    test_err = None

    test_app = create_app()
    with test_app.app_context():
        # Act
        try:
            test_league_season = LeagueSeason(season_id=1)
        except ValueError as err:
            test_err = err

    # Assert
    assert test_err is None


def test_update_games_and_points_when_games_equal_zero_should_update_only_games_and_points(test_league_season):
    # Arrange
    test_league_season.total_games = 1
    test_league_season.total_points = 1

    # Act
    test_league_season.update_games_and_points(total_games=0, total_points=0)

    # Assert
    assert test_league_season.total_games == 0
    assert test_league_season.total_points == 0
    assert test_league_season.average_points is None


def test_update_games_and_points_when_games_not_equal_zero_should_update_games_points_and_averages(test_league_season):
    # Arrange
    test_league_season.total_games = 0
    test_league_season.total_points = 0

    # Act
    test_league_season.update_games_and_points(total_games=2, total_points=1)

    # Assert
    assert test_league_season.total_games == 2
    assert test_league_season.total_points == 1
    assert test_league_season.average_points == 0.5
