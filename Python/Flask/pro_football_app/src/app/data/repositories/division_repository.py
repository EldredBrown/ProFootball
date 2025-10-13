from typing import List

from app.data.models.division import Division
from app.data.sqla import sqla


class DivisionRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the DivisionRepository class.
        """
        pass

    def get_divisions(self) -> List[Division]:
        """
        Gets all the divisions in the data store.

        :return: A list of all fetched divisions.
        """
        return Division.query.all()

    def get_division(self, name: str) -> Division | None:
        """
        Gets the division in the data store with the specified name.

        :param name: The name of the division to fetch.

        :return: The fetched division.
        """
        divisions = self.get_divisions()
        if len(divisions) == 0:
            return None
        return Division.query.get(name)

    def add_division(self, division: Division) -> Division:
        """
        Adds a division to the data store.

        :param division: The division to add.

        :return: The added division.
        """
        sqla.session.add(division)
        sqla.session.commit()
        return division

    def add_divisions(self, divisions: tuple) -> tuple:
        """
        Adds a collection of divisions to the data store.

        :param divisions: The divisions to add.

        :return: The added divisions.
        """
        for division in divisions:
            sqla.session.add(division)
        sqla.session.commit()
        return divisions

    def update_division(self, division: Division) -> Division | None:
        """
        Updates a division in the data store.

        :param division: The division to update.

        :return: The updated division.
        """
        if not self.division_exists(division.name):
            return division

        division_to_update = self.get_division(division.name)
        division_to_update.league_id = division.league_id
        division_to_update.conference_id = division.conference_id
        division_to_update.first_season_id = division.first_season_id
        division_to_update.last_season_id = division.last_season_id
        sqla.session.add(division_to_update)
        sqla.session.commit()
        return division

    def delete_division(self, name: str) -> Division | None:
        """
        Deletes a division from the data store.

        :param name: The name of the division to delete.

        :return: The deleted division.
        """
        if not self.division_exists(name):
            return None

        division = self.get_division(name)
        sqla.session.delete(division)
        sqla.session.commit()
        return division

    def division_exists(self, name: str) -> bool:
        """
        Checks to verify whether a specific division exists in the data store.

        :param name: The name of the division to verify.

        :return: True if the division with the specified name exists in the data store; otherwise false.
        """
        return self.get_division(name) is not None
