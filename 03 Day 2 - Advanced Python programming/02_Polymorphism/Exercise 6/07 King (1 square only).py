class King(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x, y = self.x + dx, self.y + dy
                if self._in_bounds(x, y):
                    piece = chessboard.board[x][y]
                    if piece is None or piece.color != self.color:
                        moves.append((x, y))
        return moves