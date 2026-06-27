class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []
        deltas = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]

        for dx, dy in deltas:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx <= 7 and 0 <= ny <= 7:
                moves.append((nx, ny))

        return moves