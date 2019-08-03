from tkinter import *

from ttt_core.game import Game
from ttt_core.player import POSITIONS
from ttt_core.player import Status

THE_GAME = Game()


def on_click(grid_index, grid):
    grid.mark_with_symbol(grid_index, THE_GAME.playing_player().symbol)
    THE_GAME.playing_player().mark(grid_index)

    win_string = THE_GAME.win_check()

    if win_string != '':
        grid.status_text.set(win_string)

        for grid_index in range(1, 10):
            grid.index_to_button[grid_index].config(state=DISABLED)
    else:
        if THE_GAME.playing_player() == THE_GAME.player1:
            THE_GAME.player2.status = Status.PLAYING
            THE_GAME.player1.status = Status.WAITING
            grid.status_text.set('Current Player: Player 2')
        else:
            THE_GAME.player1.status = Status.PLAYING
            THE_GAME.player2.status = Status.WAITING
            grid.status_text.set('Current Player: Player 1')


class Grid(Tk):
    """This class is responsible for generating the 3x3 grid."""

    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("240x240")
        self.resizable(0, 0)
        self.index_to_button = {}

        self.main_frame = Frame(master=self)
        self.status_frame = Frame(master=self)

        for grid_index in range(1, 10):
            button = Button(
                master=self.main_frame,
                text='',
                height=3,
                width=6,
                command=lambda value=grid_index, grid=self: on_click(value, grid))

            button.grid(row=POSITIONS[grid_index][0], column=POSITIONS[grid_index][1])

            self.index_to_button[grid_index] = button

        self.main_frame.pack()

        self.status_text = StringVar()
        self.status_text.set('Current Player: Player 1')
        label = Label(master=self.status_frame, textvariable=self.status_text)
        label.pack()
        self.status_frame.pack()

    def mark_with_symbol(self, grid_index, symbol):
        button = self.index_to_button[grid_index]
        button.config(text=symbol, state=DISABLED)

