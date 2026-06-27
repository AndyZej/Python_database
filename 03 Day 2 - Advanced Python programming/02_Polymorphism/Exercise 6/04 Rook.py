class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_horizontal_and_vertical_moves(chessboard)