class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.has_moved = False

    def list_allowed_moves(self, chessboard):
        moves = []

        direction = 1 if self.color == "white" else -1

        if not (0 <= self.y + direction <= 7):
            return []

        moves.append((self.x, self.y + direction))

        if not self.has_moved:
            if 0 <= self.y + 2 * direction <= 7:
                moves.append((self.x, self.y + 2 * direction))

        return moves

    def move(self, x, y):
        super().move(x, y)
        self.has_moved = True