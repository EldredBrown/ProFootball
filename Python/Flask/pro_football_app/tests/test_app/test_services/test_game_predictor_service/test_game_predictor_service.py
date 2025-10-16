from unittest.mock import patch

from app.data.models.team_season import TeamSeason
from app.services.game_predictor_service.game_predictor_service import GamePredictorService


@patch('app.services.game_predictor_service.game_predictor_service.TeamSeasonRepository')
def test_predict_game_score_should_return_none_when_guest_season_is_none(fake_team_season_repository):
    # Arrange
    guest_id = 1
    guest_season_id = 1
    guest_season = None

    host_id = 2
    host_season_id = 1
    host_season = None

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    # Act
    test_service = GamePredictorService(fake_team_season_repository)
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_id, guest_season_id,
                                                                                  host_id, host_season_id)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_id, guest_season_id)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_id, host_season_id)

    assert predicted_guest_score is None
    assert predicted_host_score is None


@patch('app.services.game_predictor_service.game_predictor_service.TeamSeasonRepository')
def test_predict_game_score_should_return_none_when_host_season_is_none(fake_team_season_repository):
    # Arrange
    league_id = 1

    guest_id = 1
    guest_season_id = 1
    guest_season = TeamSeason(team_id=guest_id, season_id=guest_season_id, league_id=league_id)
    guest_season.offensive_average = 1.000
    guest_season.offensive_factor = 2.000
    guest_season.defensive_average = 3.000
    guest_season.defensive_factor = 4.000

    host_id = 2
    host_season_id = 1
    host_season = None

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    # Act
    test_service = GamePredictorService(fake_team_season_repository)
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_id, guest_season_id,
                                                                                  host_id, host_season_id)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_id, guest_season_id)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_id, host_season_id)

    assert predicted_guest_score is None
    assert predicted_host_score is None


@patch('app.services.game_predictor_service.game_predictor_service.TeamSeasonRepository')
def test_predict_game_score_should_return_correctly_calculated_prediction_when_guest_season_and_host_season_are_not_none(
    fake_team_season_repository
):
    # Arrange
    league_id = 1

    guest_id = 1
    guest_season_id = 1
    guest_season = TeamSeason(team_id=guest_id, season_id=guest_season_id, league_id=league_id)
    guest_season.offensive_average = 1.000
    guest_season.offensive_factor = 2.000
    guest_season.defensive_average = 3.000
    guest_season.defensive_factor = 4.000

    host_id = 2
    host_season_id = 1
    host_season = TeamSeason(team_id=host_id, season_id=host_season_id, league_id=league_id)
    host_season.offensive_average = 5.000
    host_season.offensive_factor = 6.000
    host_season.defensive_average = 7.000
    host_season.defensive_factor = 8.000

    fake_team_season_repository.get_team_season_by_team_and_season.side_effect = (guest_season, host_season)

    # Act
    test_service = GamePredictorService(fake_team_season_repository)
    predicted_guest_score, predicted_host_score = test_service.predict_game_score(guest_id, guest_season_id,
                                                                                  host_id, host_season_id)

    # Assert
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(guest_id, guest_season_id)
    fake_team_season_repository.get_team_season_by_team_and_season.assert_any_call(host_id, host_season_id)

    assert predicted_guest_score == round(((guest_season.offensive_factor * host_season.defensive_average
                                            + host_season.defensive_factor * guest_season.offensive_average) / 2), 1)
    assert predicted_host_score == round(((host_season.offensive_factor * guest_season.defensive_average
                                           + guest_season.defensive_factor * host_season.offensive_average) / 2), 1)
