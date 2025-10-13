from unittest.mock import Mock

from app.data.db_context import DbContext
from app.data.entities.team_season import TeamSeason
from app.data.repositories.team_season_repository import TeamSeasonRepository


def test_get_team_seasons_should_get_team_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    test_repository.get_team_seasons()

    # Assert
    fake_db_context.get_entities.assert_called_once_with(TeamSeason)


def test_get_team_seasons_by_season_should_get_team_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team1", season_year=1921, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    test_repository.get_team_seasons_by_season(1920)

    # Assert
    fake_db_context.get_entities.assert_called_once_with(TeamSeason)


def test_get_team_season_should_return_none_when_db_team_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_repository.get_team_season(id=1)

    # Assert
    assert tsa_out is None


def test_get_team_season_should_return_team_season_when_db_team_seasons_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    test_tsa_id = 2

    # Act
    tsa_out = test_repository.get_team_season(id=test_tsa_id)

    # Assert
    fake_db_context.get_entity.assert_called_once_with(TeamSeason, test_tsa_id)


def test_get_team_season_by_team_and_season_should_return_none_when_db_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None
    test_season_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_season_repository.get_team_season_by_team_and_season(team_name="Team1", season_year=1920)

    # Assert
    assert tsa_out is None


def test_get_team_season_by_team_and_season_should_return_team_season_when_db_seasons_is_not_none_and_matching_team_season_is_found():
    # Arrange
    fake_db_context = Mock(DbContext)
    tsa_collection_in = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    fake_db_context.get_entities.return_value = tsa_collection_in
    test_season_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_season_repository.get_team_season_by_team_and_season(team_name="Team2", season_year=1920)

    # Assert
    assert tsa_out is tsa_collection_in[1]


def test_get_team_season_by_team_and_season_should_return_none_when_db_seasons_is_not_none_and_matching_team_season_is_not_found():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_repository.get_team_season_by_team_and_season(team_name="Team4", season_year=1920)

    # Assert
    assert tsa_out is None


def test_add_team_season_should_add_team_season():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    tsa_to_add = TeamSeason(id=4, team_name="Team4", season_year=1920, league_name="NFL")

    # Act
    tsa_out = test_repository.add_team_season(tsa_to_add)

    # Assert
    fake_db_context.add_entity.assert_called_once_with(tsa_to_add)
    assert tsa_out is tsa_to_add


def test_add_team_seasons_should_add_team_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    tsa_collection_to_add = (
        TeamSeason(id=1, team_name="Team1", season_year=1921, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1922, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1923, league_name="NFL")
    )

    # Act
    tsa_collection_out = test_repository.add_team_seasons(tsa_collection_to_add)

    # Assert
    fake_db_context.add_entities.assert_called_once_with(tsa_collection_to_add)
    assert tsa_collection_out is tsa_collection_to_add


def test_update_team_season_should_return_team_season_when_db_team_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    tsa_to_update = TeamSeason(id=4, team_name="Team1", season_year=1920, league_name="NFL")

    # Act
    tsa_out = test_repository.update_team_season(tsa_to_update)

    # Assert
    assert tsa_out is tsa_to_update
    fake_db_context.update_entity.assert_not_called()


def test_update_team_season_should_return_team_season_when_team_season_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    fake_db_context.get_entity.return_value = None
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    tsa_to_update = TeamSeason(id=4, team_name="Team1", season_year=1921, league_name="NFL")

    # Act
    tsa_out = test_repository.update_team_season(tsa_to_update)

    # Assert
    assert tsa_out is tsa_to_update
    fake_db_context.update_entity.assert_not_called()


def test_update_team_season_should_update_and_return_team_season_when_db_team_seasons_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    tsa_to_update = TeamSeason(id=1, team_name="Team2", season_year=1921, league_name="NFL")

    # Act
    tsa_out = test_repository.update_team_season(tsa_to_update)

    # Assert
    fake_db_context.update_entity.assert_called_once()
    assert tsa_out is tsa_to_update


def test_delete_team_season_should_return_none_when_db_team_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_repository.delete_team_season(id=1)

    # Assert
    assert tsa_out is None


def test_delete_team_season_should_return_none_when_team_season_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL"),
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    fake_db_context.get_entity.return_value = None

    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_repository.delete_team_season(id=4)

    # Assert
    assert tsa_out is None


def test_delete_team_season_should_remove_and_return_team_season_when_team_season_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)

    tsa1 = TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL")
    tsa_list = [
        tsa1,
        TeamSeason(id=2, team_name="Team2", season_year=1920, league_name="NFL"),
        TeamSeason(id=3, team_name="Team3", season_year=1920, league_name="NFL")
    ]
    fake_db_context.get_entities.return_value = tsa_list
    fake_db_context.get_entity.return_value = tsa1

    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_out = test_repository.delete_team_season(id=1)

    # Assert
    assert fake_db_context.delete_entity.called_once_with(tsa_out)
    assert tsa_out is tsa1


def test_team_season_exists_should_return_true_when_team_season_exists():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entity.return_value = TeamSeason(id=1, team_name="Team2", season_year=1920,
                                                         league_name="NFL")

    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_exists = test_repository.team_season_exists(id=1)

    # Assert
    assert tsa_exists


def test_team_season_exists_should_return_false_when_team_season_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entity.return_value = None
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_exists = test_repository.team_season_exists(id=1)

    # Assert
    assert not tsa_exists


def test_team_season_exists_with_name_and_year_should_return_true_when_team_season_exists():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL")
    ]

    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_exists = test_repository.team_season_exists_with_name_and_year("Team1", 1920)

    # Assert
    assert tsa_exists


def test_team_season_exists_with_name_and_year_should_return_false_when_team_season_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        TeamSeason(id=1, team_name="Team1", season_year=1920, league_name="NFL")
    ]
    test_repository = TeamSeasonRepository(db_context=fake_db_context)

    # Act
    tsa_exists = test_repository.team_season_exists_with_name_and_year("Team2", 1921)

    # Assert
    assert not tsa_exists
