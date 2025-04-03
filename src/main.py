# filepath: tic-tac-toe/src/main.py

import tkinter as tk
from gui import TicTacToeGUI

def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game_gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()