from app.data.db_context import DbContext
from app.data.entities.team_season import TeamSeason


class TeamSeasonRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the TeamSeasonRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_team_seasons(self) -> iter:
        """
        Gets all the team_seasons in the data store.

        :return: A list of all fetched team_seasons.
        """
        return self._db_context.get_entities(TeamSeason)

    def get_team_seasons_by_season(self, season_year: int) -> iter:
        """
        Gets all the team_seasons in the data store for the specified seasons.

        :return: A list of all fetched team_seasons.
        """
        return [team_season for team_season in self.get_team_seasons() if team_season.season_id == season_year]

    def get_team_season(self, id: int) -> TeamSeason | None:
        """
        Gets the team_season in the data store with the specified id.

        :param id: The id of the team_season to fetch.

        :return: The fetched team_season.
        """
        if self.get_team_seasons() is None:
            return None

        return self._db_context.get_entity(TeamSeason, id)

    def get_team_season_by_team_and_season(self, team_name: str, season_year: int) -> TeamSeason | None:
        """
        Gets the team_season in the data store with the specified team_id and season_id.

        :return: The fetched team_season.
        """
        if self.get_team_seasons() is None:
            return None

        try:
            return [ts for ts in self.get_team_seasons()
                    if ts.team_id == team_name and ts.season_id == season_year][0]
        except IndexError:
            return None

    def add_team_season(self, team_season: TeamSeason) -> TeamSeason:
        """
        Adds a team_season to the data store.

        :param team_season: The team_season to add.

        :return: The added team_season.
        """
        self._db_context.add_entity(team_season)

        return team_season

    def add_team_seasons(self, team_seasons: tuple) -> tuple:
        """
        Adds a collection of team_seasons to the data store.

        :param team_seasons: The team_seasons to add.

        :return: The added team_seasons.
        """
        self._db_context.add_entities(team_seasons)

        return team_seasons

    def update_team_season(self, team_season: TeamSeason) -> TeamSeason | None:
        """
        Updates a team_season in the data store.

        :param team_season: The team_season to update.

        :return: The updated team_season.
        """
        if (self.get_team_seasons() is None) or (team_season is None) or (not self.team_season_exists(team_season.id)):
            return team_season

        team_season_to_update = self.get_team_season(team_season.id)
        team_season_to_update.team_id = team_season.team_id
        team_season_to_update.season_id = team_season.season_id
        team_season_to_update.league_id = team_season.league_id
        team_season_to_update.conference_id = team_season.conference_id
        team_season_to_update.division_name = team_season.division_name
        team_season_to_update.games = team_season.games
        team_season_to_update.wins = team_season.wins
        team_season_to_update.losses = team_season.losses
        team_season_to_update.ties = team_season.ties
        team_season_to_update.winning_percentage = team_season.winning_percentage
        team_season_to_update.points_for = team_season.points_for
        team_season_to_update.points_against = team_season.points_against
        team_season_to_update.expected_wins = team_season.expected_wins
        team_season_to_update.expected_losses = team_season.expected_losses
        team_season_to_update.offensive_average = team_season.offensive_average
        team_season_to_update.offensive_factor = team_season.offensive_factor
        team_season_to_update.offensive_index = team_season.offensive_index
        team_season_to_update.defensive_average = team_season.defensive_average
        team_season_to_update.defensive_factor = team_season.defensive_factor
        team_season_to_update.defensive_index = team_season.defensive_index
        team_season_to_update.final_expected_winning_percentage = team_season.final_expected_winning_percentage
        self._db_context.update_entity()

        return team_season

    def delete_team_season(self, id: int) -> TeamSeason | None:
        """
        Deletes a team_season from the data store.

        :param id: The id of the team_season to delete.

        :return: The deleted team_season.
        """
        if self.get_team_seasons() is None:
            return None

        team_season = self.get_team_season(id)
        if team_season is None:
            return None

        self._db_context.delete_entity(team_season)

        return team_season

    def team_season_exists(self, id: int) -> bool:
        """
        Checks to verify whether a specific team_season exists in the data store.

        :param id: The id of the team_season to verify.

        :return: True if the team_season with the specified id exists in the data store; otherwise false.
        """
        return self.get_team_season(id) is not None

    def team_season_exists_with_name_and_year(self, team_name: str, season_year: int) -> bool:
        """
        Checks to verify whether a specific team_season exists in the data store with the specified id and id.

        :param team_name: The team_id of the team_season to verify.
        :param season_year: The season_id of the team_season to verify.

        :return: True if the team_season with the specified id and id exists in the data store; otherwise false.
        """
        return self.get_team_season_by_team_and_season(team_name, season_year) is not None


if __name__ == '__main__':
    repo = TeamSeasonRepository()

    for team_season in repo.get_team_seasons():
        repo.delete_team_season(team_season.id)

    team_seasons = repo.add_team_seasons((
        TeamSeason("Arizona Cardinals", 2022, "NFL", conference_name="NFC", division_name="NFC West"),
        TeamSeason("Atlanta Falcons", 2022, "NFL", conference_name="NFC", division_name="NFC South"),
        TeamSeason("Baltimore Ravens", 2022, "NFL", conference_name="AFC", division_name="AFC North"),
        TeamSeason("Buffalo Bills", 2022, "NFL", conference_name="AFC", division_name="AFC East"),
        TeamSeason("Carolina Panthers", 2022, "NFL", conference_name="NFC", division_name="NFC South"),
        TeamSeason("Chicago Bears", 2022, "NFL", conference_name="NFC", division_name="NFC North"),
        TeamSeason("Cincinnati Bengals", 2022, "NFL", conference_name="AFC", division_name="AFC North"),
        TeamSeason("Cleveland Browns", 2022, "NFL", conference_name="AFC", division_name="AFC North"),
        TeamSeason("Dallas Cowboys", 2022, "NFL", conference_name="NFC", division_name="NFC East"),
        TeamSeason("Denver Broncos", 2022, "NFL", conference_name="AFC", division_name="AFC West"),
        TeamSeason("Detroit Lions", 2022, "NFL", conference_name="NFC", division_name="NFC North"),
        TeamSeason("Green Bay Packers", 2022, "NFL", conference_name="NFC", division_name="NFC North"),
        TeamSeason("Houston Texans", 2022, "NFL", conference_name="AFC", division_name="AFC South"),
        TeamSeason("Indianapolis Colts", 2022, "NFL", conference_name="AFC", division_name="AFC South"),
        TeamSeason("Jacksonville Jaguars", 2022, "NFL", conference_name="AFC", division_name="AFC South"),
        TeamSeason("Kansas City Chiefs", 2022, "NFL", conference_name="AFC", division_name="AFC West"),
        TeamSeason("Las Vegas Raiders", 2022, "NFL", conference_name="AFC", division_name="AFC West"),
        TeamSeason("Los Angeles Chargers", 2022, "NFL", conference_name="AFC", division_name="AFC West"),
        TeamSeason("Los Angeles Rams", 2022, "NFL", conference_name="NFC", division_name="NFC West"),
        TeamSeason("Miami Dolphins", 2022, "NFL", conference_name="AFC", division_name="AFC East"),
        TeamSeason("Minnesota Vikings", 2022, "NFL", conference_name="NFC", division_name="NFC North"),
        TeamSeason("New England Patriots", 2022, "NFL", conference_name="AFC", division_name="AFC East"),
        TeamSeason("New Orleans Saints", 2022, "NFL", conference_name="NFC", division_name="NFC South"),
        TeamSeason("New York Giants", 2022, "NFL", conference_name="NFC", division_name="NFC East"),
        TeamSeason("New York Jets", 2022, "NFL", conference_name="AFC", division_name="AFC East"),
        TeamSeason("Philadelphia Eagles", 2022, "NFL", conference_name="NFC", division_name="NFC East"),
        TeamSeason("Pittsburgh Steelers", 2022, "NFL", conference_name="AFC", division_name="AFC North"),
        TeamSeason("San Francisco 49ers", 2022, "NFL", conference_name="NFC", division_name="NFC West"),
        TeamSeason("Seattle Seahawks", 2022, "NFL", conference_name="NFC", division_name="NFC West"),
        TeamSeason("Tampa Bay Buccaneers", 2022, "NFL", conference_name="NFC", division_name="NFC South"),
        TeamSeason("Tennessee Titans", 2022, "NFL", conference_name="AFC", division_name="AFC South"),
        TeamSeason("Washington Commanders", 2022, "NFL", conference_name="NFC", division_name="NFC East")
    ))

    for team_season_from_db in repo.get_team_seasons():
        print(team_season_from_db)
