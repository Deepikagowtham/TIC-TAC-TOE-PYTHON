import tkinter as tk
from tkinter import messagebox  # Ensure messagebox is imported correctly
from board import Board
from game import Game
from player import Player

class TicTacToeUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.players = [self.create_player(1), self.create_player(2)]  # Initialize players
        self.board = Board(3, '-')
        self.game = Game(self.players, self.board)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_player(self, player_number):
        name = input(f"Please enter the name of Player {player_number}: ")
        symbol = input(f"Please enter the symbol of Player {player_number}: ")
        return Player(name, symbol)


    def create_board(self):
        for x in range(3):
            for y in range(3):
                button = tk.Button(self.root, text='', font='normal 20 bold', height=2, width=5,
                                   command=lambda x=x, y=y: self.on_click(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button

    def create_player(self, player_number):
        name = input(f"Please enter the name of Player {player_number}: ")
        symbol = input(f"Please enter the symbol of Player {player_number}: ")
        return Player(name, symbol)

    def on_click(self, x, y):
        result = self.game.make_move(x, y)
        self.update_board()
        if result:
            messagebox.showinfo("Game Over", result)  # Use messagebox here
            choice = messagebox.askyesno("Play Again", "Do you want to play again?")
            if choice:
                self.reset_board()
            else:
                self.root.destroy()  # Close the application if players choose not to play again

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

if __name__ == "__main__":
    TicTacToeUI().run()
