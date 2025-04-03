import tkinter as tk
from tkinter import messagebox  # Import messagebox
from game_logic import Game

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=3,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.board[row][col])
            if self.check_winner():
                self.show_winner(self.game.current_player)
            elif self.game.is_draw():
                self.show_winner("No one")  # Handle draw condition

    def ai_move(self):
        row, col = self.game.get_best_move()
        if self.game.make_move(row, col):
            self.update_display()
            if self.game.check_winner():
                self.show_winner("AI")
            elif self.game.is_draw():
                self.show_winner("Draw")

    def update_display(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game.board[row][col])

    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_game()

    def reset_game(self):
        self.game.reset()
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()