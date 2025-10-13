from decimal import Decimal
from unittest.mock import Mock

from app.data.entities.team_season import TeamSeason
from app.data.repositories.team_season_repository import TeamSeasonRepository
from app.services.game_predictor_service.game_predictor_service import GamePredictorService


def test_predict_game_score_should_return_none_when_guest_season_is_none():
    # Arrange
    fake_team_season_repository = Mock(TeamSeasonRepository)

    guest_name = "Guest"
    guest_season_year = 1
    guest_season = None

    host_name = "Host"
    host_season_year = 1
    host_season = None

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    test_service = GamePredictorService(fake_team_season_repository)

    # Act
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_name, guest_season_year,
                                                                                  host_name, host_season_year)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_name, guest_season_year)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_name, host_season_year)

    assert predicted_guest_score is None
    assert predicted_host_score is None


def test_predict_game_score_should_return_none_when_host_season_is_none():
    # Arrange
    fake_team_season_repository = Mock(TeamSeasonRepository)

    league_name = "NFL"

    guest_name = "Guest"
    guest_season_year = 1
    guest_season = TeamSeason(guest_name, guest_season_year, league_name)
    guest_season.offensive_average = Decimal('1')
    guest_season.offensive_factor = Decimal('2')
    guest_season.defensive_average = Decimal('3')
    guest_season.defensive_factor = Decimal('4')

    host_name = "Host"
    host_season_year = 1
    host_season = None

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    test_service = GamePredictorService(fake_team_season_repository)

    # Act
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_name, guest_season_year,
                                                                                  host_name, host_season_year)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_name, guest_season_year)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_name, host_season_year)

    assert predicted_guest_score is None
    assert predicted_host_score is None


def test_predict_game_score_should_return_correctly_calculated_prediction_when_guest_season_and_host_season_are_not_none():
    # Arrange
    fake_team_season_repository = Mock(TeamSeasonRepository)

    league_name = "NFL"

    guest_name = "Guest"
    guest_season_year = 1
    guest_season = TeamSeason(guest_name, guest_season_year, league_name)
    guest_season.offensive_average = Decimal('1')
    guest_season.offensive_factor = Decimal('2')
    guest_season.defensive_average = Decimal('3')
    guest_season.defensive_factor = Decimal('4')

    host_name = "Host"
    host_season_year = 1
    host_season = TeamSeason(host_name, host_season_year, league_name)
    host_season.offensive_average = Decimal('5')
    host_season.offensive_factor = Decimal('6')
    host_season.defensive_average = Decimal('7')
    host_season.defensive_factor = Decimal('8')

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    test_service = GamePredictorService(fake_team_season_repository)

    # Act
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_name, guest_season_year,
                                                                                  host_name, host_season_year)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_name, guest_season_year)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_name, host_season_year)

    assert predicted_guest_score == round(((guest_season.offensive_factor * host_season.defensive_average
                                            + host_season.defensive_factor * guest_season.offensive_average) / 2), 1)
    assert predicted_host_score == round(((host_season.offensive_factor * guest_season.defensive_average
                                           + guest_season.defensive_factor * host_season.offensive_average) / 2), 1)
