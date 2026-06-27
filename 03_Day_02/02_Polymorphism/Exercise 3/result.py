# ======================
# Chessboard
# ======================

class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def setup(self):
        # Pawns
        for x in range(8):
            self.board[x][1] = Pawn("white", x, 1)
            self.board[x][6] = Pawn("black", x, 6)

        # Rooks
        self.board[0][0] = Rook("white", 0, 0)
        self.board[7][0] = Rook("white", 7, 0)
        self.board[0][7] = Rook("black", 0, 7)
        self.board[7][7] = Rook("black", 7, 7)

        # Knights
        self.board[1][0] = Knight("white", 1, 0)
        self.board[6][0] = Knight("white", 6, 0)
        self.board[1][7] = Knight("black", 1, 7)
        self.board[6][7] = Knight("black", 6, 7)

        # Bishops
        self.board[2][0] = Bishop("white", 2, 0)
        self.board[5][0] = Bishop("white", 5, 0)
        self.board[2][7] = Bishop("black", 2, 7)
        self.board[5][7] = Bishop("black", 5, 7)

        # Queens
        self.board[3][0] = Queen("white", 3, 0)
        self.board[3][7] = Queen("black", 3, 7)

        # Kings
        self.board[4][0] = King("white", 4, 0)
        self.board[4][7] = King("black", 4, 7)


# ======================
# Base Class
# ======================

class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def _get_diagonal_moves(self):
        moves = []
        for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
            nx, ny = self.x + dx, self.y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

    def _get_horizontal_and_vertical_moves(self):
        moves = []
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = self.x + dx, self.y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves


# ======================
# Pawn
# ======================

class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.has_moved = False

    def list_allowed_moves(self, chessboard):
        moves = []
        direction = 1 if self.color == "white" else -1

        if 0 <= self.y + direction < 8:
            moves.append((self.x, self.y + direction))

            if not self.has_moved and 0 <= self.y + 2 * direction < 8:
                moves.append((self.x, self.y + 2 * direction))

        return moves

    def move(self, x, y):
        super().move(x, y)
        self.has_moved = True


# ======================
# Knight
# ======================

class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []
        for dx, dy in [
            (2,1),(2,-1),(-2,1),(-2,-1),
            (1,2),(1,-2),(-1,2),(-1,-2)
        ]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                moves.append((nx, ny))
        return moves


# ======================
# Rook
# ======================

class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_horizontal_and_vertical_moves()


# ======================
# Bishop
# ======================

class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_diagonal_moves()


# ======================
# Queen
# ======================

class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self._get_diagonal_moves() +
            self._get_horizontal_and_vertical_moves()
        )


# ======================
# King
# ======================

class King(Figure):
    def list_allowed_moves(self, chessboard):
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    moves.append((nx, ny))
        return moves