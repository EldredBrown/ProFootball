from app.data.db_context import DbContext
from app.data.entities.game import Game


class GameRepository:
    """
    Provides CRUD access to an external data store.
    """

    def __init__(self, db_context: DbContext = None) -> None:
        """
        Initializes a new instance of the GameRepository class.

        :param db_context: In-memory representation of the database.
        """
        self._db_context = db_context or DbContext()

    def get_games(self) -> iter:
        """
        Gets all the games in the data store.

        :return: A list of all fetched games.
        """
        return self._db_context.get_entities(Game)

    def get_game(self, id: int) -> Game | None:
        """
        Gets the game in the data store with the specified id.

        :param id: The id of the game to fetch.

        :return: The fetched game.
        """
        if self.get_games() is None:
            return None

        return self._db_context.get_entity(Game, id)

    def add_game(self, game: Game) -> Game:
        """
        Adds a game to the data store.

        :param game: The game to add.

        :return: The added game.
        """
        self._db_context.add_entity(game)

        return game

    def add_games(self, games: tuple) -> tuple:
        """
        Adds a game to the data store.

        :param games: The games to add.

        :return: The added games.
        """
        self._db_context.add_entities(games)

        return games

    def update_game(self, game: Game) -> Game:
        """
        Updates a game in the data store.

        :param game: The game to update.

        :return: The updated game.
        """
        if (self.get_games() is None) or (not self.game_exists(game.id)):
            return game

        game_to_update = self.get_game(game.id)
        game_to_update.id = game.id
        game_to_update.season_id = game.season_id
        game_to_update.week = game.week
        game_to_update.guest_id = game.guest_id
        game_to_update.guest_score = game.guest_score
        game_to_update.host_id = game.host_id
        game_to_update.host_score = game.host_score
        game_to_update.winner_id = game.winner_id
        game_to_update.winner_score = game.winner_score
        game_to_update.loser_id = game.loser_id
        game_to_update.loser_score = game.loser_score
        game_to_update.is_playoff = game.is_playoff
        game_to_update.notes = game.notes
        self._db_context.update_entity()

        return game

    def delete_game(self, id: int) -> Game | None:
        """
        Deletes a game from the data store.

        :param id: The id of the game to delete.

        :return: The deleted game.
        """
        if self.get_games() is None:
            return None

        game = self.get_game(id)
        if game is None:
            return None

        self._db_context.delete_entity(game)

        return game

    def game_exists(self, id: int) -> bool:
        """
        Checks to verify whether a specific game exists in the data store.

        :param id: The id of the game to verify.

        :return: True if the game with the specified id exists in the data store; otherwise false.
        """
        return self.get_game(id) is not None


if __name__ == '__main__':
    repo = GameRepository()
    for game in repo.get_games():
        repo.delete_game(game.id)
