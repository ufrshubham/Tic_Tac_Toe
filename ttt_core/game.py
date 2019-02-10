from ttt_core.player import Player
from ttt_core.player import Status

class Game:
    """This is the core game class responsible for all the actions that take place in current game."""

    def __init__(self):
        """This is initialize current game with two players."""
        self.__players = [Player(), Player()]
        self.grid = ""

    @property
    def player1(self):
        """Returns the first player."""
        return self.__players[0]

    @property
    def player2(self):
        """Returns the second player."""
        return self.__players[1]

    def playing_player(self):
        """Returns the current playing player. Will raise is called before the game actually begins."""

        if self.player1.status == Status.PLAYING:
            return self.player1
        elif self.player2.status == Status.PLAYING:
            return self.player2
        else:
            raise Exception("No one is playing")

    def start(self):
        self.grid.mainloop()
