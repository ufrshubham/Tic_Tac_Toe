from ttt_core.player import Player
from ttt_core.player import Status


class Game:
    """This is the core game class responsible for all the actions that take place in current game."""

    def __init__(self):
        """This will initialize current game with two players."""
        self.__players = [Player(), Player()]
        self.player1.status = Status.PLAYING
        self.player1.symbol = 'X'
        self.player2.status = Status.WAITING
        self.player2.symbol = 'O'

    @property
    def player1(self):
        """Returns the first player."""
        return self.__players[0]

    @property
    def player2(self):
        """Returns the second player."""
        return self.__players[1]

    def playing_player(self):
        """Returns the current playing player. Will raise if called before the game actually begins."""

        if self.player1.status == Status.PLAYING:
            return self.player1
        elif self.player2.status == Status.PLAYING:
            return self.player2
        else:
            raise Exception("No one is playing")

    def win_check(self):
        p1_positions = self.player1.positions
        p2_positions = self.player2.positions

        if 1 in p1_positions and 2 in p1_positions and 3 in p1_positions \
                or 4 in p1_positions and 5 in p1_positions and 6 in p1_positions \
                or 7 in p1_positions and 8 in p1_positions and 9 in p1_positions \
                or 1 in p1_positions and 4 in p1_positions and 7 in p1_positions \
                or 2 in p1_positions and 5 in p1_positions and 8 in p1_positions \
                or 3 in p1_positions and 6 in p1_positions and 9 in p1_positions \
                or 1 in p1_positions and 5 in p1_positions and 9 in p1_positions \
                or 2 in p1_positions and 5 in p1_positions and 7 in p1_positions:
            return 'Player 1 won'

        elif 1 in p2_positions and 2 in p2_positions and 3 in p2_positions \
                or 4 in p2_positions and 5 in p2_positions and 6 in p2_positions \
                or 7 in p2_positions and 8 in p2_positions and 9 in p2_positions \
                or 1 in p2_positions and 4 in p2_positions and 7 in p2_positions \
                or 2 in p2_positions and 5 in p2_positions and 8 in p2_positions \
                or 3 in p2_positions and 6 in p2_positions and 9 in p2_positions \
                or 1 in p2_positions and 5 in p2_positions and 9 in p2_positions \
                or 2 in p2_positions and 5 in p2_positions and 7 in p2_positions:
            return 'Player 2 won'

        return ''
