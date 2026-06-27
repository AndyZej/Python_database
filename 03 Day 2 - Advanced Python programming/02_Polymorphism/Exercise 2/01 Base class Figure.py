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
            while 0 <= nx <= 7 and 0 <= ny <= 7:
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return moves

    def _get_horizontal_and_vertical_moves(self):
        moves = []

        for i in range(8):
            if i != self.x:
                moves.append((i, self.y))
            if i != self.y:
                moves.append((self.x, i))

        return moves