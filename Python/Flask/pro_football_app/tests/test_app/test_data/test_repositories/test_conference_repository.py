import sqlite3
import pytest

from app.data.models.conference import Conference
from app.data.models.game import Game
from app.data.models.league_season import LeagueSeason
from app.data.models.team_season import TeamSeason
from app.data.repositories.conference_repository import ConferenceRepository
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


def test_get_conferences_should_get_conferences(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conferences = test_repo.get_conferences()

    # Assert
    for conference in conferences:
        assert isinstance(conference, Conference)

    # Clean up test.
    teardown(test_conn)


def test_get_conference_when_conferences_is_empty_should_return_none(test_conn):
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference(id=1)

    # Assert
    assert conference is None


def test_get_conference_when_conferences_is_not_empty_and_conference_is_not_found_should_return_none(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference(id=len(conferences) + 1)

    # Assert
    assert conference is None

    # Clean up test.
    teardown(test_conn)


def test_get_conference_when_conferences_is_not_empty_and_conference_is_found_should_return_conference(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    id = len(conferences) - 1
    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference(id=id)

    # Assert
    assert isinstance(conference, Conference)
    assert conference.id == id

    # Clean up test.
    teardown(test_conn)


def test_get_conference_by_name_when_conferences_is_empty_should_return_none(test_conn):
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference_by_name(short_name="NFC")

    # Assert
    assert conference is None


def test_get_conference_by_name_when_conferences_is_not_empty_and_conference_with_short_name_is_not_found_should_return_none(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference_by_name(short_name="XFC")

    # Assert
    assert conference is None

    # Clean up test.
    teardown(test_conn)


def test_get_conference_by_name_when_conferences_is_not_empty_and_conference_with_short_name_is_found_should_return_conference(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    conference_name = "AFC"
    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference = test_repo.get_conference_by_name(short_name=conference_name)

    # Assert
    assert isinstance(conference, Conference)
    assert conference.short_name == conference_name

    # Clean up test.
    teardown(test_conn)


def test_add_conference_should_add_conference(test_conn):
    # Arrange
    conferences_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_in = Conference(
            short_name="XFC", long_name="Exotic Football Conference", league_id=1,
            first_season_id=9998, last_season_id=9999
        )
        conference_out = test_repo.add_conference(conference_in)

    # Assert
    assert conference_out is conference_in
    c = test_conn.cursor()
    conferences_after_add = c.execute("SELECT * FROM Conference").fetchall()
    assert len(conferences_after_add) == len(conferences_before_add) + 1

    # Clean up test.
    teardown(test_conn)


def test_add_conferences_when_conferences_arg_is_empty_should_add_no_conferences(test_conn):
    # Arrange
    _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conferences_in = ()
        conferences_out = test_repo.add_conferences(conferences_in)

    # Assert
    assert conferences_out is conferences_in
    c = test_conn.cursor()
    conferences = c.execute("SELECT * FROM Conference").fetchall()
    assert len(conferences) == 3

    # Clean up test.
    teardown(test_conn)


def test_add_conferences_when_conferences_arg_is_not_empty_should_add_conferences(test_conn):
    # Arrange
    conferences_before_add = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conferences_in = (
            Conference(
                short_name="NFC4", long_name="National Football Conference 4", league_id=1,
                first_season_id=7, last_season_id=8
            ),
            Conference(
                short_name="NFC5", long_name="National Football Conference 5", league_id=1,
                first_season_id=9, last_season_id=10
            ),
            Conference(
                short_name="NFC6", long_name="National Football Conference 6", league_id=1,
                first_season_id=11, last_season_id=12
            ),
        )
        conferences_out = test_repo.add_conferences(conferences_in)

    # Assert
    assert conferences_out is conferences_in
    c = test_conn.cursor()
    conferences_after_add = c.execute("SELECT * FROM Conference").fetchall()
    assert len(conferences_after_add) == len(conferences_before_add) + len(conferences_in)

    # Clean up test.
    teardown(test_conn)


def test_conference_exists_when_conferences_is_empty_should_return_false(test_conn):
    # Arrange

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_exists = test_repo.conference_exists(id=1)

    # Assert
    assert not conference_exists


def test_conference_exists_when_conferences_is_not_empty_and_conference_does_not_exist_should_return_false(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_exists = test_repo.conference_exists(id=len(conferences) + 1)

    # Assert
    assert not conference_exists

    # Clean up test.
    teardown(test_conn)


def test_conference_exists_when_conferences_is_not_empty_and_conference_exists_should_return_true(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_exists = test_repo.conference_exists(id=len(conferences) - 1)

    # Assert
    assert conference_exists

    # Clean up test.
    teardown(test_conn)


def test_update_conference_when_conference_does_not_exist_should_return_conference(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_to_update = Conference(
            id=len(conferences) + 1, short_name="XFC", long_name="Exotic Football Conference",
            league_id=97, first_season_id=98, last_season_id=99
        )
        conference_updated = test_repo.update_conference(conference_to_update)

    # Assert
    assert conference_updated is conference_to_update

    # Clean up test.
    teardown(test_conn)


def test_update_conference_when_conference_exists_should_update_and_return_conference(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_to_update = Conference(
            id=len(conferences) - 1, short_name="XFC", long_name="Exotic Football Conference", league_id=97,
            first_season_id=98, last_season_id=99
        )
        conference_out = test_repo.update_conference(conference_to_update)

    # Assert
    assert conference_out is conference_to_update

    c = test_conn.cursor()
    row = c.execute("SELECT * FROM Conference WHERE id = 2").fetchone()
    assert row[1] == "XFC"
    assert row[2] == "Exotic Football Conference"
    assert row[3] == 97
    assert row[4] == 98
    assert row[5] == 99

    # Clean up test.
    teardown(test_conn)


def test_delete_conference_when_conference_does_not_exist_should_return_none(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_deleted = test_repo.delete_conference(id=len(conferences) + 1)

    # Assert
    assert conference_deleted is None

    # Clean up test.
    teardown(test_conn)


def test_delete_conference_when_conference_exists_should_return_conference(test_conn):
    # Arrange
    conferences = _populate_test_db_with_default_data(test_conn)

    id = len(conferences) - 1
    test_app = create_app()
    with test_app.app_context():
        # Act
        test_repo = ConferenceRepository()
        conference_deleted = test_repo.delete_conference(id=id)

    # Assert
    assert isinstance(conference_deleted, Conference)
    assert conference_deleted.id == id

    c = test_conn.cursor()

    rows = c.execute("SELECT * FROM Conference").fetchall()
    assert len(rows) == len(conferences) - 1

    row = c.execute("SELECT * FROM Conference WHERE id = 2").fetchone()
    assert row is None

    # Clean up test.
    teardown(test_conn)


def _populate_test_db_with_default_data(conn):
    c = conn.cursor()
    conferences = [
        ("NFC", "National Football Conference", "NFL", 1970, None),
        ("AFC", "American Football Conference", "NFL", 1970, None),
        ("AAFC", "All-American Football Conference", "NFL", 1946, 1949),
    ]
    c.executemany(
        '''
        INSERT INTO Conference (
           short_name, long_name, league_id, first_season_id, last_season_id
        ) VALUES (?, ?, ?, ?, ?)
        ''', conferences
    )
    conn.commit()
    return conferences
