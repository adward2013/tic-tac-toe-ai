import tkinter as tk
from tkinter import messagebox
from game_board import GameBoard
from ai_player import AIPlayer

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe vs AI")
        
        self.game_board = GameBoard()
        self.ai = AIPlayer('O')
        self.current_player = 'X'
        self.buttons = []
        
        self._create_gui()
    
    def _create_gui(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text='',
                    font=('Arial', 20),
                    width=6,
                    height=3,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)
    
    def make_move(self, row, col):
        index = row * 3 + col
        
        if self.game_board.make_move(index, self.current_player):
            self.buttons[index].config(text=self.current_player)
            
            if self.game_board.is_winner(self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif self.game_board.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O'
                self.ai_move()
    
    def ai_move(self):
        ai_position = self.ai.get_move(self.game_board)
        if ai_position is not None:
            self.game_board.make_move(ai_position, 'O')
            self.buttons[ai_position].config(text='O')
            
            if self.game_board.is_winner('O'):
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_game()
            elif self.game_board.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            
            self.current_player = 'X'
    
    def reset_game(self):
        self.game_board.reset()
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='')
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
