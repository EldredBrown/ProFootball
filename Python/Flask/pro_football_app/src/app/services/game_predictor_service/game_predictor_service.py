from app.data.repositories.team_season_repository import TeamSeasonRepository


class GamePredictorService:
    """
    A service for predicting the scores of future games.
    """

    def __init__(self, team_season_repository: TeamSeasonRepository = None) -> None:
        """
        Initializes a new instance of the GamePredictorService class.

        :param team_season_repository: The repository by which team_season data will be fetched
        for both teams.
        """
        self._team_season_repository = team_season_repository or TeamSeasonRepository()

    def __repr__(self):
        return f"{type(self).__name__}(team_season_repository={self._team_season_repository})"

    def predict_game_score(self,
                           guest_id: int, guest_season_id: int,
                           host_id: int, host_season_id: int) -> tuple:
        guest_season = self._team_season_repository.get_team_season_by_team_and_season(guest_id, guest_season_id)
        host_season = self._team_season_repository.get_team_season_by_team_and_season(host_id, host_season_id)
        if guest_season is None or host_season is None:
            return None, None

        guest_score = round(((guest_season.offensive_factor * host_season.defensive_average
                             + host_season.defensive_factor * guest_season.offensive_average) / 2), 1)
        host_score = round(((host_season.offensive_factor * guest_season.defensive_average
                            + guest_season.defensive_factor * host_season.offensive_average) / 2), 1)

        return guest_score, host_score
