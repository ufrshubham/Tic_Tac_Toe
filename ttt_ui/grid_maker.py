from tkinter import *

from ttt_core.player import POSITIONS
from ttt_ui.tic_tac_toe import on_click


class Grid(Tk):
    """This class is responsible for generating the 3x3 grid."""

    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("240x200")
        self.resizable(0, 0)

        self.main_frame = Frame(master=self)

        for i in range(1, 10):
            Button(
                master=self.main_frame,
                text=str(i),
                height=3,
                width=6,
                command=lambda value=i: on_click(value)) \
                .grid(row=POSITIONS[i][0], column=POSITIONS[i][1])

        self.main_frame.pack()
