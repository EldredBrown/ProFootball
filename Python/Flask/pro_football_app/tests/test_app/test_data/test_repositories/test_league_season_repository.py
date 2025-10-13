from unittest.mock import Mock

from app.data.db_context import DbContext
from app.data.entities.league_season import LeagueSeason
from app.data.repositories.league_season_repository \
    import LeagueSeasonRepository


def test_get_league_seasons_should_get_league_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    test_repository.get_league_seasons()

    # Assert
    fake_db_context.get_entities.assert_called_once_with(LeagueSeason)


def test_get_league_seasons_by_season_should_get_league_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1920),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    test_repository.get_league_seasons_by_season(1920)

    # Assert
    fake_db_context.get_entities.assert_called_once_with(LeagueSeason)


def test_get_league_season_should_return_none_when_db_league_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.get_league_season(id=1)

    # Assert
    assert lsa_out is None


def test_get_league_season_should_return_league_season_when_db_league_seasons_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    test_lsa_id = 2

    # Act
    test_repository.get_league_season(id=test_lsa_id)

    # Assert
    fake_db_context.get_entity.assert_called_once_with(LeagueSeason, test_lsa_id)


def test_get_league_season_by_league_and_season_should_return_none_when_db_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.get_league_season_by_league_and_season(league_name="APFA", season_year=1920)

    # Assert
    assert lsa_out is None


def test_get_season_by_year_should_return_season_when_db_seasons_is_not_none_and_matching_league_season_is_found():
    # Arrange
    fake_db_context = Mock(DbContext)
    lsa_list_in = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]
    fake_db_context.get_entities.return_value = lsa_list_in

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.get_league_season_by_league_and_season(league_name="APFA", season_year=1921)

    # Assert
    assert lsa_out is lsa_list_in[1]


def test_get_season_by_year_should_return_season_when_db_seasons_is_not_none_and_matching_league_season_is_not_found():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.get_league_season_by_league_and_season(league_name="APFA", season_year=1923)

    # Assert
    assert lsa_out is None


def test_add_league_season_should_add_league_season():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    lsa_to_add = LeagueSeason(id=4, league_name="NFL", season_year=1923)

    # Act
    lsa_out = test_repository.add_league_season(lsa_to_add)

    # Assert
    fake_db_context.add_entity.assert_called_once_with(lsa_to_add)
    assert lsa_out is lsa_to_add


def test_add_league_seasons_should_add_league_seasons():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    lsa_collection_to_add = (
        LeagueSeason(id=4, league_name="NFL", season_year=1923),
        LeagueSeason(id=5, league_name="NFL", season_year=1924),
        LeagueSeason(id=6, league_name="NFL", season_year=1925)
    )

    # Act
    lsa_list_out = test_repository.add_league_seasons(lsa_collection_to_add)

    # Assert
    fake_db_context.add_entities.assert_called_once_with(lsa_collection_to_add)
    assert lsa_list_out is lsa_collection_to_add


def test_update_league_season_should_return_league_season_when_db_league_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    lsa_to_update = LeagueSeason(id=4, league_name="NFL", season_year=1923)

    # Act
    lsa_out = test_repository.update_league_season(lsa_to_update)

    # Assert
    assert lsa_out is lsa_to_update
    fake_db_context.update_entity.assert_not_called()


def test_update_league_season_should_return_league_season_when_league_season_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]
    fake_db_context.get_entity.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    lsa_to_update = LeagueSeason(id=4, league_name="NFL", season_year=1923)

    # Act
    lsa_out = test_repository.update_league_season(lsa_to_update)

    # Assert
    assert lsa_out is lsa_to_update
    fake_db_context.update_entity.assert_not_called()


def test_update_league_season_should_update_and_return_league_season_when_db_league_seasons_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [LeagueSeason(id=1, league_name="APFA", season_year=1920)]

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    lsa_to_update = LeagueSeason(id=1, league_name="NFL", season_year=1923)

    # Act
    lsa_out = test_repository.update_league_season(lsa_to_update)

    # Assert
    fake_db_context.update_entity.assert_called_once()
    assert lsa_out is lsa_to_update


def test_delete_league_season_should_return_none_when_db_league_seasons_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.delete_league_season(id=1)

    # Assert
    assert lsa_out is None


def test_delete_league_season_should_return_none_when_league_season_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        LeagueSeason(id=1, league_name="APFA", season_year=1920),
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]
    fake_db_context.get_entity.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.delete_league_season(id=4)

    # Assert
    assert lsa_out is None


def test_delete_league_season_should_remove_and_return_league_season_when_league_season_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)

    lsa1 = LeagueSeason(id=1, league_name="APFA", season_year=1920)
    lsa_list = [
        lsa1,
        LeagueSeason(id=2, league_name="APFA", season_year=1921),
        LeagueSeason(id=3, league_name="NFL", season_year=1922)
    ]
    fake_db_context.get_entities.return_value = lsa_list
    fake_db_context.get_entity.return_value = lsa1

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_out = test_repository.delete_league_season(id=1)

    # Assert
    assert fake_db_context.delete_entity.called_once_with(lsa_out)
    assert lsa_out is lsa1


def test_league_season_exists_should_return_true_when_league_season_exists():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entity.return_value = LeagueSeason(id=2, league_name="APFA", season_year=1921)

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_exists = test_repository.league_season_exists(id=2)

    # Assert
    assert lsa_exists


def test_league_season_exists_should_return_false_when_league_season_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entity.return_value = None

    test_repository = LeagueSeasonRepository(db_context=fake_db_context)

    # Act
    lsa_exists = test_repository.league_season_exists(id=4)

    # Assert
    assert not lsa_exists
