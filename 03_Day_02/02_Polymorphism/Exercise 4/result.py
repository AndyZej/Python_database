class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def setup(self):
        # (same setup code as before)
        ...

    def list_allowed_moves(self, x, y):
        piece = self.board[x][y]

        # No piece on this square
        if piece is None:
            return None

        # Not the active player's piece
        if piece.color != self.color:
            return None

        # Ask the piece for its allowed moves
        return piece.list_allowed_moves(self)