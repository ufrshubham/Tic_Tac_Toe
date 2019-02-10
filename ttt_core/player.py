# These are the statuses that a player object can have
SPAWNED = 0
PLAYING = 1
WAITING = 2

# This is a map of positions on board to corresponding co-ordinates
POSITIONS = {
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (-1, 0),
    5: (0, 0),
    6: (1, 0),
    7: (-1, -1),
    8: (0, -1),
    9: (1, -1)
}


class Player:
    """This class represents a player."""

    def __init__(self):
        """Creates a player object with status set to SPAWNED and with zero positions."""
        self.__status = SPAWNED
        self.__positions = []

    @property
    def status(self):
        """Gets player status."""
        return self.__status

    @status.setter
    def status(self, value):
        """Sets player status."""
        self.__status = value

    @property
    def positions(self):
        """Returns list of current player positions."""
        return self.__positions

    def mark(self, value):
        """This method will add given value to players position list."""
        self.__positions.append(value)
