from app.data.db_context import DbContext
from app.data.entities.team import Team


class TeamRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the TeamRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_teams(self) -> iter:
        """
        Gets all the teams in the data store.

        :return: A list of all fetched teams.
        """
        return self._db_context.get_entities(Team)

    def get_team(self, id: int) -> Team | None:
        """
        Gets the team in the data store with the specified id.

        :param id: The id of the team to fetch.

        :return: The fetched team.
        """
        if self.get_teams() is None:
            return None

        return self._db_context.get_entity(Team, id)

    def add_team(self, team: Team) -> Team:
        """
        Adds a team to the data store.

        :param team: The team to add.

        :return: The added team.
        """
        self._db_context.add_entity(team)

        return team

    def add_teams(self, teams: tuple) -> tuple:
        """
        Adds a collection of teams to the data store.

        :param teams: The teams to add.

        :return: The added teams.
        """
        self._db_context.add_entities(teams)

        return teams

    def update_team(self, team: Team) -> Team:
        """
        Updates a team in the data store.

        :param team: The team to update.

        :return: The updated team.
        """
        if (self.get_teams() is None) or (not self.team_exists(team.id)):
            return team

        team_to_update = self.get_team(team.id)
        team_to_update.name = team.name
        self._db_context.update_entity()

        return team

    def delete_team(self, id: int) -> Team | None:
        """
        Deletes a team from the data store.

        :param id: The id of the team to delete.

        :return: The deleted team.
        """
        if self.get_teams() is None:
            return None

        team = self.get_team(id)
        if team is None:
            return None

        self._db_context.delete_entity(team)

        return team

    def team_exists(self, id: int) -> bool:
        """
        Checks to verify whether a specific team exists in the data store.

        :param id: The id of the team to verify.

        :return: True if the team with the specified id exists in the data store; otherwise false.
        """
        return self.get_team(id) is not None


if __name__ == '__main__':
    repo = TeamRepository()

    for team in repo.get_teams():
        repo.delete_team(team.id)

    teams = repo.add_teams((
        Team("Arizona Cardinals"),
        Team("Atlanta Falcons"),
        Team("Baltimore Ravens"),
        Team("Buffalo Bills"),
        Team("Carolina Panthers"),
        Team("Chicago Bears"),
        Team("Cincinnati Bengals"),
        Team("Cleveland Browns"),
        Team("Dallas Cowboys"),
        Team("Denver Broncos"),
        Team("Detroit Lions"),
        Team("Green Bay Packers"),
        Team("Houston Texans"),
        Team("Indianapolis Colts"),
        Team("Jacksonville Jaguars"),
        Team("Kansas City Chiefs"),
        Team("Las Vegas Raiders"),
        Team("Los Angeles Chargers"),
        Team("Los Angeles Rams"),
        Team("Miami Dolphins"),
        Team("Minnesota Vikings"),
        Team("New England Patriots"),
        Team("New Orleans Saints"),
        Team("New York Giants"),
        Team("New York Jets"),
        Team("Philadelphia Eagles"),
        Team("Pittsburgh Steelers"),
        Team("San Francisco 49ers"),
        Team("Seattle Seahawks"),
        Team("Tampa Bay Buccaneers"),
        Team("Tennessee Titans"),
        Team("Washington Commanders"),
    ))

    teams_from_db = repo.get_teams()
    for team in teams:
        print(team)
