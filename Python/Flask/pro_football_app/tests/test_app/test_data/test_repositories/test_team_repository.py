import sqlite3
import pytest

from unittest.mock import Mock, patch

from app.data.models.team import Team
from app.data.repositories.team_repository import TeamRepository
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


def test_get_teams_should_get_teams(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        teams = test_repo.get_teams()

    # Assert
    for team in teams:
        assert isinstance(team, Team)

    # Clean up test.
    teardown(test_conn)


def test_get_team_when_teams_is_empty_should_return_none():
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team = test_repo.get_team(name="NFC East")

    # Assert
    assert team is None


def test_get_team_when_teams_is_not_empty_and_team_with_short_name_is_not_found_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team = test_repo.get_team(name="AFC East")

    # Assert
    assert team is None

    # Clean up test.
    teardown(test_conn)


def test_get_team_when_teams_is_not_empty_and_team_with_short_name_is_found_should_return_team(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team = test_repo.get_team(name="NFC East")

    # Assert
    assert isinstance(team, Team)
    assert team.name == "NFC East"

    # Clean up test.
    teardown(test_conn)


def test_add_team_should_add_team(test_conn):
    # Arrange
    teams_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team_in = Team(
            name="AFC East", league_name="NFL", conference_name="AFC",
            first_season_year=1, last_season_year=2
        )
        team_out = test_repo.add_team(team_in)

    # Assert
    assert team_out is team_in
    c = test_conn.cursor()
    teams_after_add = c.execute("SELECT * FROM Team").fetchall()
    assert len(teams_after_add) == len(teams_before_add) + 1

    # Clean up test.
    teardown(test_conn)


def test_add_teams_when_teams_arg_is_empty_should_add_no_teams(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        teams_in = ()
        teams_out = test_repo.add_teams(teams_in)

    # Assert
    assert teams_out is teams_in
    c = test_conn.cursor()
    teams = c.execute("SELECT * FROM Team").fetchall()
    assert len(teams) == 4

    # Clean up test.
    teardown(test_conn)


def test_add_teams_when_teams_arg_is_not_empty_should_add_teams(test_conn):
    # Arrange
    teams_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        teams_in = (
            Team(
                name="AFC East", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Team(
                name="AFC North", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Team(
                name="AFC South", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Team(
                name="AFC West", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
        )
        teams_out = test_repo.add_teams(teams_in)

    # Assert
    assert teams_out is teams_in
    c = test_conn.cursor()
    teams_after_add = c.execute("SELECT * FROM Team").fetchall()
    assert len(teams_after_add) == len(teams_before_add) + len(teams_in)

    # Clean up test.
    teardown(test_conn)


def test_team_exists_when_teams_is_empty_should_return_false():
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        result = test_repo.team_exists(name="NFC East")

    # Assert
    assert not result


def test_team_exists_when_teams_is_not_empty_and_team_does_not_exist_should_return_false(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        result = test_repo.team_exists(name="NFC Central")

    # Assert
    assert not result

    # Clean up test.
    teardown(test_conn)


def test_team_exists_when_teams_is_not_empty_and_team_exists_should_return_true(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        result = test_repo.team_exists(name="NFC East")

    # Assert
    assert result

    # Clean up test.
    teardown(test_conn)


def test_update_team_when_team_does_not_exist_should_return_team(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team_to_update = Team(
            name="NFC Central", league_name="NFL", conference_name="NFC", first_season_year=98, last_season_year=99
        )
        team_updated = test_repo.update_team(team_to_update)

    # Assert
    assert team_updated is team_to_update

    # Clean up test.
    teardown(test_conn)


def test_update_team_when_team_exists_should_update_and_return_team(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team_to_update = Team(
            name="NFC East", league_name="NFL", conference_name="NFC", first_season_year=98, last_season_year=99
        )
        team_out = test_repo.update_team(team_to_update)

    # Assert
    assert team_out is team_to_update

    c = test_conn.cursor()
    row = c.execute("SELECT * FROM Team WHERE name = 'NFC East'").fetchone()
    team_updated = Team(
        name=row[0], league_name=row[1], conference_name=row[2], first_season_year=row[3], last_season_year=row[4]
    )
    assert team_updated.name == "NFC East"
    assert team_updated.league_name == "NFL"
    assert team_updated.conference_name == "NFC"
    assert team_updated.first_season_year == 98
    assert team_updated.last_season_year == 99

    # Clean up test.
    teardown(test_conn)


def test_delete_team_when_team_does_not_exist_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team_deleted = test_repo.delete_team(name="NFC Central")

    # Assert
    assert team_deleted is None

    # Clean up test.
    teardown(test_conn)


def test_delete_team_when_team_exists_should_return_team(test_conn):
    # Arrange
    teams = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = TeamRepository()
        team_deleted = test_repo.delete_team(name="NFC East")

    # Assert
    assert isinstance(team_deleted, Team)
    assert team_deleted.name == "NFC East"

    c = test_conn.cursor()

    rows = c.execute("SELECT * FROM Team").fetchall()
    assert len(rows) == len(teams) - 1

    row = c.execute("SELECT * FROM Team WHERE name = 'NFC East'").fetchone()
    assert row is None

    # Clean up test.
    teardown(test_conn)


def _populate_test_db_with_default_data(conn):
    c = conn.cursor()
    teams = [
        ("NFC East", "NFL", "NFC", 1, None),
        ("NFC North", "NFL", "NFC", 1, None),
        ("NFC South", "NFL", "NFC", 1, None),
        ("NFC West", "NFL", "NFC", 1, None),
    ]
    c.executemany(
        "INSERT INTO Team ("
        "   name, league_id, conference_id, first_season_id, last_season_id"
        ") VALUES (?, ?, ?, ?, ?)",
        teams
    )
    conn.commit()
    return teams
