from ttt_core.game import Game
from ttt_core.player import POSITIONS
from ttt_core.player import Status
from ttt_ui.grid_maker import Grid

game = Game()

def on_click(value):
    global game

    game.playing_player().mark(POSITIONS[value])
    print(POSITIONS[value])

    #if THE_GAME.playing_player() == THE_GAME.player1:
    #    THE_GAME.player2.status = Status.PLAYING
    #    THE_GAME.player1.status = Status.WAITING
    #else:
    #    THE_GAME.player1.status = Status.PLAYING
    #    THE_GAME.player2.status = Status.WAITING


def main():
    global game

    #game = Game()
    game.grid = Grid()
    game.player1.status = Status.PLAYING
    game.player2.status = Status.WAITING
    game.start()


if __name__ == '__main__':
    main()
