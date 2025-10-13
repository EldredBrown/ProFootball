from unittest.mock import Mock

from app.data.db_context import DbContext
from app.data.entities.game import Game
from app.data.repositories.game_repository import GameRepository


def test_get_games_should_get_games():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    test_repository.get_games()

    # Assert
    fake_db_context.get_entities.assert_called_once_with(Game)


def test_get_game_should_return_none_when_db_games_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_out = test_repository.get_game(id=1)

    # Assert
    assert game_out is None


def test_get_game_should_return_game_when_db_games_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    test_game_id = 2

    # Act
    test_repository.get_game(id=test_game_id)

    # Assert
    fake_db_context.get_entity.assert_called_once_with(Game, test_game_id)


def test_add_game_should_add_game():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    game_to_add = Game(id=4, season_year=2022, week=1,
                       guest_name="San Francisco 49ers", guest_score=10,
                       host_name="Chicago Bears", host_score=19)

    # Act
    game_out = test_repository.add_game(game_to_add)

    # Assert
    fake_db_context.add_entity.assert_called_once_with(game_to_add)
    assert game_out is game_to_add


def test_add_games_should_add_games():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    games_to_add = (
        Game(id=4, season_year=2022, week=1,
             guest_name="San Francisco 49ers", guest_score=10,
             host_name="Chicago Bears", host_score=19),
        Game(id=5, season_year=2022, week=1,
             guest_name="Pittsburgh Steelers", guest_score=23,
             host_name="Cincinnati Bengals", host_score=20),
        Game(id=6, season_year=2022, week=1,
             guest_name="Philadelphia Eagles", guest_score=38,
             host_name="Detroit Lions", host_score=35)
    )

    # Act
    games_out = test_repository.add_games(games_to_add)

    # Assert
    fake_db_context.add_entities.assert_called_once_with(games_to_add)
    assert games_out is games_to_add


def test_update_game_should_return_game_when_db_games_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = GameRepository(db_context=fake_db_context)

    game_to_update = Game(id=1, season_year=2022, week=1,
                          guest_name="Buffalo Bills", guest_score=31,
                          host_name="Los Angeles Rams", host_score=10)

    # Act
    game_out = test_repository.update_game(game_to_update)

    # Assert
    assert game_out is game_to_update


def test_update_game_should_return_game_when_game_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]
    fake_db_context.get_entity.return_value = None

    test_repository = GameRepository(db_context=fake_db_context)

    game_to_update = Game(id=1, season_year=2022, week=1,
                          guest_name="Buffalo Bills", guest_score=31,
                          host_name="Los Angeles Rams", host_score=10)

    # Act
    game_out = test_repository.update_game(game_to_update)

    # Assert
    assert game_out is game_to_update


def test_update_game_should_update_and_return_game_when_db_games_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    game_to_update = Game(id=1, season_year=2022, week=1,
                          guest_name="Los Angeles Rams", guest_score=10,
                          host_name="Buffalo Bills", host_score=31)

    # Act
    game_out = test_repository.update_game(game_to_update)

    # Assert
    assert game_out is game_to_update


def test_delete_game_should_return_none_when_db_games_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = None

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_out = test_repository.delete_game(id=1)

    # Assert
    assert game_out is None


def test_delete_game_should_return_none_when_game_is_none():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]
    fake_db_context.get_entity.return_value = None

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_out = test_repository.delete_game(id=4)

    # Assert
    assert game_out is None


def test_delete_game_should_remove_and_return_game_when_game_is_not_none():
    # Arrange
    fake_db_context = Mock(DbContext)

    game1 = Game(id=1, season_year=2022, week=1,
                 guest_name="Buffalo Bills", guest_score=31,
                 host_name="Los Angeles Rams", host_score=10),
    game2 = Game(id=2, season_year=2022, week=1,
                 guest_name="New Orleans Saints", guest_score=27,
                 host_name="Atlanta Falcons", host_score=26),
    game3 = Game(id=3, season_year=2022, week=1,
                 guest_name="Cleveland Browns", guest_score=26,
                 host_name="Carolina Panthers", host_score=24)
    fake_db_context.get_entities.return_value = [game1, game2, game3]
    fake_db_context.get_entity.return_value = game1

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_out = test_repository.delete_game(id=1)

    # Assert
    assert fake_db_context.delete_entity.called_once_with(game_out)
    assert game_out is game1


def test_game_exists_should_return_true_when_game_exists():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_exists = test_repository.game_exists(id=2)

    # Assert
    assert game_exists


def test_game_exists_should_return_false_when_game_does_not_exist():
    # Arrange
    fake_db_context = Mock(DbContext)
    fake_db_context.get_entities.return_value = [
        Game(id=1, season_year=2022, week=1,
             guest_name="Buffalo Bills", guest_score=31,
             host_name="Los Angeles Rams", host_score=10),
        Game(id=2, season_year=2022, week=1,
             guest_name="New Orleans Saints", guest_score=27,
             host_name="Atlanta Falcons", host_score=26),
        Game(id=3, season_year=2022, week=1,
             guest_name="Cleveland Browns", guest_score=26,
             host_name="Carolina Panthers", host_score=24)
    ]

    test_repository = GameRepository(db_context=fake_db_context)

    # Act
    game_exists = test_repository.game_exists(id=4)

    # Assert
    assert game_exists
