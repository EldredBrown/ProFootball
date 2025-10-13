from app.data.db_context import DbContext
from app.data.entities.team_season_schedule_averages import TeamSeasonScheduleAverages
from app.data.entities.team_season_schedule_totals import TeamSeasonScheduleTotals
from app.data.base import engine


class TeamSeasonScheduleRepository:
    """
    Provides CRUD access to a data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the TeamSeasonScheduleRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_team_season_schedule_totals(self, team_name: str, season_year: int) -> TeamSeasonScheduleTotals:
        """
        Gets the TeamSeasonScheduleTotals in the data store with the specified team_id and season_id.

        :param team_name: The id of the team for which this TeamSeasonScheduleTotals will be fetched.
        :param season_year: The id of the seasons for which this TeamSeasonScheduleTotals will be fetched.

        :return: The fetched TeamSeasonScheduleTotals.
        """
        with engine.connect() as connection:
            statement = f"CALL get_team_season_schedule_totals('{team_name}', {season_year});"
            self._db_context.execute_query(statement, connection)

            statement = "SELECT * FROM team_season_schedule_totals;"
            totals = self._db_context.execute_query(statement, connection).first()

        if totals is None:
            return TeamSeasonScheduleTotals()

        return TeamSeasonScheduleTotals(
            games=totals[0],
            points_for=totals[1],
            points_against=totals[2],
            schedule_wins=totals[3],
            schedule_losses=totals[4],
            schedule_ties=totals[5],
            schedule_winning_percentage=totals[6],
            schedule_games=totals[7],
            schedule_points_for=totals[8],
            schedule_points_against=totals[9]
        )

    def get_team_season_schedule_averages(self, team_name: str, season_year: int) -> TeamSeasonScheduleAverages:
        """
        Gets the TeamSeasonScheduleAverages in the data store with the specified team_id and season_id.

        :param team_name: The id of the team for which this TeamSeasonScheduleAverages will be fetched.
        :param season_year: The id of the seasons for which this TeamSeasonScheduleAverages will be fetched.

        :return: The fetched TeamSeasonScheduleAverages.
        """
        statement = f"CALL get_team_season_schedule_averages('{team_name}', {season_year});"
        totals = self._db_context.execute_query(statement).first()

        if totals is None:
            return TeamSeasonScheduleAverages()

        return TeamSeasonScheduleAverages(
            points_for=totals[0],
            points_against=totals[1],
            schedule_points_for=totals[2],
            schedule_points_against=totals[3]
        )


if __name__ == '__main__':
    repo = TeamSeasonScheduleRepository()

    team_name = 'Chicago Bears'
    season_year = 2022
    repo.get_team_season_schedule_totals(team_name, season_year)
    repo.get_team_season_schedule_averages(team_name, season_year)
