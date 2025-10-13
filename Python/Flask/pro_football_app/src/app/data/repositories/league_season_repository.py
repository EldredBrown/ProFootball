from app.data.db_context import DbContext
from app.data.entities.league_season import LeagueSeason


class LeagueSeasonRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the LeagueSeasonRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_league_seasons(self) -> iter:
        """
        Gets all the league_seasons in the data store.

        :return: A list of all fetched league_seasons.
        """
        return self._db_context.get_entities(LeagueSeason)

    def get_league_seasons_by_season(self, season_year: int) -> iter:
        """
        Gets all the league_seasons in the data store for the specified seasons.

        :return: A list of all fetched league_seasons.
        """
        return [ls for ls in self._db_context.get_entities(LeagueSeason) if ls.season_id == season_year]

    def get_league_season(self, id: int) -> LeagueSeason | None:
        """
        Gets the league_season in the data store with the specified id.

        :param id: The id of the league_season to fetch.

        :return: The fetched league_season.
        """
        if self.get_league_seasons() is None:
            return None

        return self._db_context.get_entity(LeagueSeason, id)

    def get_league_season_by_league_and_season(self, league_name: str, season_year: int) -> LeagueSeason | None:
        """
        Gets the league_season in the data store with the specified league_id and season_id.

        :return: The fetched league_season.
        """
        if self.get_league_seasons() is None:
            return None

        try:
            return [ls for ls in self.get_league_seasons()
                    if ls.league_id == league_name and ls.season_id == season_year][0]
        except IndexError:
            return None

    def add_league_season(self, league_season: LeagueSeason) -> LeagueSeason:
        """
        Adds a league_season to the data store.

        :param league_season: The league_season to add.

        :return: The added league_season.
        """
        self._db_context.add_entity(league_season)

        return league_season

    def add_league_seasons(self, league_seasons: tuple) -> tuple:
        """
        Adds a collection of league_seasons to the data store.

        :param league_seasons: The league_seasons to add.

        :return: The added league_seasons.
        """
        self._db_context.add_entities(league_seasons)

        return league_seasons

    def update_league_season(self, league_season: LeagueSeason) -> LeagueSeason:
        """
        Updates a league_season in the data store.

        :param league_season: The league_season to update.

        :return: The updated league_season.
        """
        if (self.get_league_seasons() is None) or (not self.league_season_exists(league_season.id)):
            return league_season

        league_season_to_update = self.get_league_season(league_season.id)
        league_season_to_update.league_id = league_season.league_id
        league_season_to_update.season_id = league_season.season_id
        league_season_to_update.total_games = league_season.total_games
        league_season_to_update.total_points = league_season.total_points
        league_season_to_update.average_points = league_season.average_points
        self._db_context.update_entity()

        return league_season

    def delete_league_season(self, id: int) -> LeagueSeason | None:
        """
        Deletes a league_season from the data store.

        :param id: The id of the league_season to delete.

        :return: The deleted league_season.
        """
        if self.get_league_seasons() is None:
            return None

        league_season = self.get_league_season(id)
        if league_season is None:
            return None

        self._db_context.delete_entity(league_season)

        return league_season

    def league_season_exists(self, id: int) -> bool:
        """
        Checks to verify whether a specific league_season exists in the data store.

        :param id: The id of the league_season to verify.

        :return: True if the league_season with the specified id exists in the data store; otherwise false.
        """
        return self.get_league_season(id) is not None


if __name__ == '__main__':
    repo = LeagueSeasonRepository()

    for league_season in repo.get_league_seasons():
        repo.delete_league_season(league_season.id)

    league_season = repo.add_league_season(LeagueSeason("NFL", 2022))

    league_season_from_db = repo.get_league_season(league_season.id)
    print(league_season_from_db)
