import sqlite3
import pytest

from unittest.mock import Mock, patch

from app.data.models.game import Game
from app.data.models.season import Season
from app.data.models.league_season import LeagueSeason
from app.data.models.team_season import TeamSeason
from app.data.repositories.season_repository import SeasonRepository
from instance.test_db.db_init import init_db
from test_app import create_app


@pytest.fixture()
def test_conn():
    init_db()
    db_abs_path = 'D:\\Source\\Repos\\ProFootball\\Python\\Flask\\pro_football_app\\tests\\instance\\test_db\\test_db.sqlite3'
    conn = sqlite3.connect(db_abs_path)
    return conn


def teardown(conn):
    conn.close()
    init_db()


def test_get_seasons_should_get_seasons(test_conn):
    # Arrange
    seasons = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        seasons = test_repo.get_seasons()

    # Assert
    for season in seasons:
        assert isinstance(season, Season)

    # Clean up test.
    teardown(test_conn)


def test_get_season_when_seasons_is_empty_should_return_none():
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season = test_repo.get_season(year=1)

    # Assert
    assert season is None


def test_get_season_when_seasons_is_not_empty_and_season_with_year_is_not_found_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season = test_repo.get_season(year=4)

    # Assert
    assert season is None

    # Clean up test.
    teardown(test_conn)


def test_get_season_when_seasons_is_not_empty_and_season_with_year_is_found_should_return_season(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season = test_repo.get_season(year=2)

    # Assert
    assert isinstance(season, Season)
    assert season.year == 2

    # Clean up test.
    teardown(test_conn)


def test_add_season_should_add_season(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season_in = Season(year=4)
        season_out = test_repo.add_season(season_in)

    # Assert
    assert season_out is season_in
    c = test_conn.cursor()
    seasons = c.execute("SELECT * FROM Season").fetchall()
    assert len(seasons) == 4

    # Clean up test.
    teardown(test_conn)


def test_add_seasons_should_add_seasons(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        seasons_in = (Season(year=4), Season(year=5), Season(year=6))
        seasons_out = test_repo.add_seasons(seasons_in)

    # Assert
    assert seasons_out is seasons_in
    c = test_conn.cursor()
    seasons = c.execute("SELECT * FROM Season").fetchall()
    assert len(seasons) == 6

    # Clean up test.
    teardown(test_conn)


def test_season_exists_when_season_does_not_exist_should_return_false(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        result = test_repo.season_exists(year=4)

    # Assert
    assert not result

    # Clean up test.
    teardown(test_conn)


def test_season_exists_when_season_exists_should_return_true(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        result = test_repo.season_exists(year=2)

    # Assert
    assert result

    # Clean up test.
    teardown(test_conn)


def test_update_season_when_season_does_not_exist_should_return_season(test_conn):
    # Arrange
    #
    # Populate test_db with test data.
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season_to_update = Season(year=4, num_of_weeks_scheduled=1, num_of_weeks_completed=1)
        season_updated = test_repo.update_season(season_to_update)

    # Assert
    assert season_updated is season_to_update

    # Clean up test.
    teardown(test_conn)


def test_update_season_when_season_exists_should_update_and_return_season(test_conn):
    # Arrange
    #
    # Populate test_db with test data.
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season_to_update = Season(year=2, num_of_weeks_scheduled=1, num_of_weeks_completed=1)
        season_out = test_repo.update_season(season_to_update)

    # Assert
    assert season_out is season_to_update

    c = test_conn.cursor()

    row = c.execute("SELECT * FROM Season WHERE year = 2").fetchone()
    season_updated = Season(year=row[0], num_of_weeks_scheduled=row[1], num_of_weeks_completed=row[2])
    assert season_updated.year == 2
    assert season_updated.num_of_weeks_scheduled == 1
    assert season_updated.num_of_weeks_completed == 1

    # Clean up test.
    teardown(test_conn)


def test_delete_season_when_season_does_not_exist_should_return_none(test_conn):
    # Arrange
    #
    # Populate test_db with test data.
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season_deleted = test_repo.delete_season(year=4)

    # Assert
    assert season_deleted is None

    # Clean up test.
    teardown(test_conn)


def test_delete_season_when_season_exists_should_return_season(test_conn):
    # Arrange
    #
    # Populate test_db with test data.
    # Arrange
    seasons = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = SeasonRepository()
        season_deleted = test_repo.delete_season(year=2)

    # Assert
    assert isinstance(season_deleted, Season)
    assert season_deleted.year == 2

    c = test_conn.cursor()

    rows = c.execute("SELECT * FROM Season").fetchall()
    assert len(rows) == len(seasons) - 1

    row = c.execute("SELECT * FROM Season WHERE id = 2").fetchone()
    assert row is None

    # Clean up test.
    teardown(test_conn)


def _populate_test_db_with_default_data(conn):
    c = conn.cursor()
    seasons = [
        (1,),
        (2,),
        (3,)
    ]
    c.executemany("INSERT INTO Season (year) VALUES (?)", seasons)
    conn.commit()
    return seasons
