import tkinter as tk
from board import Board
from game import Game
from player import Player

class TicTacToeUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.board = Board(3, '-')
        self.game = Game(self.players, self.board)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for x in range(3):
            for y in range(3):
                button = tk.Button(self.root, text='', font='normal 20 bold', height=2, width=5,
                                   command=lambda x=x, y=y: self.on_click(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button

    def on_click(self, x, y):
        result = self.game.make_move(x, y)
        self.update_board()
        if result:
            tk.messagebox.showinfo("Game Over", result)
            self.reset_board()

    def update_board(self):
        for x in range(3):
            for y in range(3):
                symbol = self.board.board[x][y]
                self.buttons[x][y].config(text=symbol)

    def reset_board(self):
        self.board = Board(3, '-')
        self.game = Game(self.players, self.board)
        self.update_board()

    def run(self):
        self.root.mainloop()
