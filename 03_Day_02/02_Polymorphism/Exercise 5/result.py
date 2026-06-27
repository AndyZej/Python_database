class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def setup(self):
        ...

    def list_allowed_moves(self, x, y):
        piece = self.board[x][y]
        if piece is None or piece.color != self.color:
            return None
        return piece.list_allowed_moves(self)

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)

        # No piece or wrong color
        if allowed_moves is None:
            raise ValueError("Illegal move")

        # Target square not allowed
        if (to_x, to_y) not in allowed_moves:
            raise ValueError("Illegal move")

        piece = self.board[from_x][from_y]

        # Move the piece object
        piece.move(to_x, to_y)

        # Update the board
        self.board[to_x][to_y] = piece
        self.board[from_x][from_y] = None

        # Switch player
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"