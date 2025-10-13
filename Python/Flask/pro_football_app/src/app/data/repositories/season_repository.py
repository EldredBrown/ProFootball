from typing import List

from app.data.models.season import Season
from app.data.sqla import sqla


class SeasonRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the SeasonRepository class.
        """
        pass

    def get_seasons(self) -> List[Season]:
        """
        Gets all the seasons in the data store.

        :return: A list of all fetched seasons.
        """
        return Season.query.all()

    def get_season(self, year: int) -> Season | None:
        """
        Gets the season in the data store with the specified id.

        :param year: The id of the season to fetch.

        :return: The fetched season.
        """
        seasons = self.get_seasons()
        if len(seasons) == 0:
            return None
        return Season.query.get(year)

    def add_season(self, season: Season) -> Season:
        """
        Adds a season to the data store.

        :param season: The season to add.

        :return: The added season.
        """
        sqla.session.add(season)
        sqla.session.commit()
        return season

    def add_seasons(self, seasons: tuple) -> tuple:
        """
        Adds a collection of seasons to the data store.

        :param seasons: The seasons to add.

        :return: The added seasons.
        """
        for season in seasons:
            sqla.session.add(season)
        sqla.session.commit()
        return seasons

    def update_season(self, season: Season) -> Season | None:
        """
        Updates a season in the data store.

        :param season: The season to update.

        :return: The updated season.
        """
        if not self.season_exists(season.year):
            return season

        season_to_update = self.get_season(season.year)
        season_to_update.num_of_weeks_scheduled = season.num_of_weeks_scheduled
        season_to_update.num_of_weeks_completed = season.num_of_weeks_completed
        sqla.session.add(season_to_update)
        sqla.session.commit()
        return season

    def delete_season(self, year: int) -> Season | None:
        """
        Deletes a season from the data store.

        :param year: The id of the season to delete.

        :return: The deleted season.
        """
        if not self.season_exists(year):
            return None

        season = self.get_season(year)
        sqla.session.delete(season)
        sqla.session.commit()
        return season

    def season_exists(self, year: int) -> bool:
        """
        Checks to verify whether a specific season exists in the data store.

        :param year: The id of the season to verify.

        :return: True if the season with the specified id exists in the data store; otherwise false.
        """
        return self.get_season(year) is not None
