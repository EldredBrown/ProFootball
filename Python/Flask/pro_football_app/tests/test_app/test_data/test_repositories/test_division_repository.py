import sqlite3
import pytest

from unittest.mock import Mock, patch

from app.data.models.division import Division
from app.data.models.game import Game
from app.data.models.league_season import LeagueSeason
from app.data.models.team_season import TeamSeason
from app.data.repositories.division_repository import DivisionRepository
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


def test_get_divisions_should_get_divisions(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        divisions = test_repo.get_divisions()

    # Assert
    for division in divisions:
        assert isinstance(division, Division)

    # Clean up test.
    teardown(test_conn)


def test_get_division_when_divisions_is_empty_should_return_none():
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division = test_repo.get_division(name="NFC East")

    # Assert
    assert division is None


def test_get_division_when_divisions_is_not_empty_and_division_with_short_name_is_not_found_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division = test_repo.get_division(name="AFC East")

    # Assert
    assert division is None

    # Clean up test.
    teardown(test_conn)


def test_get_division_when_divisions_is_not_empty_and_division_with_short_name_is_found_should_return_division(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division = test_repo.get_division(name="NFC East")

    # Assert
    assert isinstance(division, Division)
    assert division.name == "NFC East"

    # Clean up test.
    teardown(test_conn)


def test_add_division_should_add_division(test_conn):
    # Arrange
    divisions_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division_in = Division(
            name="AFC East", league_name="NFL", conference_name="AFC",
            first_season_year=1, last_season_year=2
        )
        division_out = test_repo.add_division(division_in)

    # Assert
    assert division_out is division_in
    c = test_conn.cursor()
    divisions_after_add = c.execute("SELECT * FROM Division").fetchall()
    assert len(divisions_after_add) == len(divisions_before_add) + 1

    # Clean up test.
    teardown(test_conn)


def test_add_divisions_when_divisions_arg_is_empty_should_add_no_divisions(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        divisions_in = ()
        divisions_out = test_repo.add_divisions(divisions_in)

    # Assert
    assert divisions_out is divisions_in
    c = test_conn.cursor()
    divisions = c.execute("SELECT * FROM Division").fetchall()
    assert len(divisions) == 4

    # Clean up test.
    teardown(test_conn)


def test_add_divisions_when_divisions_arg_is_not_empty_should_add_divisions(test_conn):
    # Arrange
    divisions_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        divisions_in = (
            Division(
                name="AFC East", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Division(
                name="AFC North", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Division(
                name="AFC South", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
            Division(
                name="AFC West", league_name="NFL", conference_name="AFC", first_season_year=1, last_season_year=2
            ),
        )
        divisions_out = test_repo.add_divisions(divisions_in)

    # Assert
    assert divisions_out is divisions_in
    c = test_conn.cursor()
    divisions_after_add = c.execute("SELECT * FROM Division").fetchall()
    assert len(divisions_after_add) == len(divisions_before_add) + len(divisions_in)

    # Clean up test.
    teardown(test_conn)


def test_division_exists_when_divisions_is_empty_should_return_false():
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        result = test_repo.division_exists(name="NFC East")

    # Assert
    assert not result


def test_division_exists_when_divisions_is_not_empty_and_division_does_not_exist_should_return_false(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        result = test_repo.division_exists(name="NFC Central")

    # Assert
    assert not result

    # Clean up test.
    teardown(test_conn)


def test_division_exists_when_divisions_is_not_empty_and_division_exists_should_return_true(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        result = test_repo.division_exists(name="NFC East")

    # Assert
    assert result

    # Clean up test.
    teardown(test_conn)


def test_update_division_when_division_does_not_exist_should_return_division(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division_to_update = Division(
            name="NFC Central", league_name="NFL", conference_name="NFC", first_season_year=98, last_season_year=99
        )
        division_updated = test_repo.update_division(division_to_update)

    # Assert
    assert division_updated is division_to_update

    # Clean up test.
    teardown(test_conn)


def test_update_division_when_division_exists_should_update_and_return_division(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division_to_update = Division(
            name="NFC East", league_name="NFL", conference_name="NFC", first_season_year=98, last_season_year=99
        )
        division_out = test_repo.update_division(division_to_update)

    # Assert
    assert division_out is division_to_update

    c = test_conn.cursor()
    row = c.execute("SELECT * FROM Division WHERE name = 'NFC East'").fetchone()
    division_updated = Division(
        name=row[0], league_name=row[1], conference_name=row[2], first_season_year=row[3], last_season_year=row[4]
    )
    assert division_updated.name == "NFC East"
    assert division_updated.league_id == "NFL"
    assert division_updated.conference_id == "NFC"
    assert division_updated.first_season_id == 98
    assert division_updated.last_season_id == 99

    # Clean up test.
    teardown(test_conn)


def test_delete_division_when_division_does_not_exist_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division_deleted = test_repo.delete_division(name="NFC Central")

    # Assert
    assert division_deleted is None

    # Clean up test.
    teardown(test_conn)


def test_delete_division_when_division_exists_should_return_division(test_conn):
    # Arrange
    divisions = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = DivisionRepository()
        division_deleted = test_repo.delete_division(name="NFC East")

    # Assert
    assert isinstance(division_deleted, Division)
    assert division_deleted.name == "NFC East"

    c = test_conn.cursor()

    rows = c.execute("SELECT * FROM Division").fetchall()
    assert len(rows) == len(divisions) - 1

    row = c.execute("SELECT * FROM Division WHERE name = 'NFC East'").fetchone()
    assert row is None

    # Clean up test.
    teardown(test_conn)


def _populate_test_db_with_default_data(conn):
    c = conn.cursor()
    divisions = [
        ("NFC East", "NFL", "NFC", 1, None),
        ("NFC North", "NFL", "NFC", 1, None),
        ("NFC South", "NFL", "NFC", 1, None),
        ("NFC West", "NFL", "NFC", 1, None),
    ]
    c.executemany(
        "INSERT INTO Division ("
        "   name, league_id, conference_id, first_season_id, last_season_id"
        ") VALUES (?, ?, ?, ?, ?)",
        divisions
    )
    conn.commit()
    return divisions
