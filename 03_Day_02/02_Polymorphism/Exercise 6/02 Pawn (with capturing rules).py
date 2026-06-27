class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.has_moved = False

    def list_allowed_moves(self, chessboard):
        moves = []
        direction = 1 if self.color == "white" else -1

        # forward move
        nx, ny = self.x, self.y + direction
        if self._in_bounds(nx, ny) and chessboard.board[nx][ny] is None:
            moves.append((nx, ny))

            # first move: two squares
            if not self.has_moved:
                ny2 = self.y + 2 * direction
                if self._in_bounds(nx, ny2) and chessboard.board[nx][ny2] is None:
                    moves.append((nx, ny2))

        # diagonal captures
        for dx in [-1, 1]:
            cx, cy = self.x + dx, self.y + direction
            if self._in_bounds(cx, cy):
                piece = chessboard.board[cx][cy]
                if piece is not None and piece.color != self.color:
                    moves.append((cx, cy))

        return moves

    def move(self, x, y):
        super().move(x, y)
        self.has_moved = True