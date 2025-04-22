import random

class AIPlayer:
    def __init__(self, marker):
        self.marker = marker
    
    def get_move(self, game_board):
        # Try to win
        winning_move = self._find_winning_move(game_board, self.marker)
        if winning_move is not None:
            return winning_move
        
        # Try to block opponent
        opponent = 'X' if self.marker == 'O' else 'O'
        blocking_move = self._find_winning_move(game_board, opponent)
        if blocking_move is not None:
            return blocking_move
        
        # Make random move
        empty_cells = game_board.get_empty_cells()
        return random.choice(empty_cells) if empty_cells else None
    
    def _find_winning_move(self, game_board, player):
        for position in game_board.get_empty_cells():
            # Try move
            game_board.board[position] = player
            if game_board.is_winner(player):
                game_board.board[position] = ''  # Undo move
                return position
            game_board.board[position] = ''  # Undo move
        return None 