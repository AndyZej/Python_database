class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []
        jumps = [
            (1,2),(2,1),(2,-1),(1,-2),
            (-1,-2),(-2,-1),(-2,1),(-1,2)
        ]

        for dx, dy in jumps:
            x, y = self.x + dx, self.y + dy
            if self._in_bounds(x, y):
                piece = chessboard.board[x][y]
                if piece is None or piece.color != self.color:
                    moves.append((x, y))
        return moves