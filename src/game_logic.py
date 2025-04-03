class Game:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def reset_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Horizontal
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Vertical
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]                             # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0][0]][combo[0][1]] == self.board[combo[1][0]][combo[1][1]] == self.board[combo[2][0]][combo[2][1]] != None:
                return self.board[combo[0][0]][combo[0][1]]
        return None

    def is_draw(self):
        # Check if all cells are filled and there is no winner
        for row in self.board:
            if None in row:
                return False
        return True