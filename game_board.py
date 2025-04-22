class GameBoard:
    def __init__(self):
        self.board = [''] * 9
    
    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.board[position] = player
            return True
        return False
    
    def is_valid_move(self, position):
        return 0 <= position < 9 and self.board[position] == ''
    
    def get_empty_cells(self):
        return [i for i, val in enumerate(self.board) if val == '']
    
    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        
        return False
    
    def is_full(self):
        return '' not in self.board
    
    def reset(self):
        self.board = [''] * 9 