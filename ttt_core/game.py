from ttt_core.player import Player


class Game:
    """This is the core game class responsible for all the actions that take place in current game."""

    def __init__(self):
        """This is initialize current game with two players."""
        self.__players = [Player(), Player()]

    @property
    def player1(self):
        """Returns the first player."""
        return self.__players[0]

    @property
    def player2(self):
        """Returns the second player."""
        return self.__players[1]
