class King(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx <= 7 and 0 <= ny <= 7:
                    moves.append((nx, ny))

        return moves