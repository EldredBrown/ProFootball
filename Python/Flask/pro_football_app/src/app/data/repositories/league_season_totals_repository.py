from app.data.db_context import DbContext
from app.data.entities.league_season_totals import LeagueSeasonTotals


class LeagueSeasonTotalsRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the LeagueSeasonTotalsRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_league_season_totals(self, league_name: str, season_year: int) -> LeagueSeasonTotals:
        """
        Gets the league_season_totals in the data store with the specified league_id and season_id.

        :return: The fetched league_season_totals.
        """
        statement = f"CALL get_league_season_totals('{league_name}', {season_year});"
        totals = self._db_context.execute_query(statement).first()
        return LeagueSeasonTotals(total_games=totals[0], total_points=totals[1])


if __name__ == '__main__':
    repo = LeagueSeasonTotalsRepository()
    league_season_totals = repo.get_league_season_totals("NFL", 2022)
    print(league_season_totals)
