class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        return (
            self._get_diagonal_moves() +
            self._get_horizontal_and_vertical_moves()
        )