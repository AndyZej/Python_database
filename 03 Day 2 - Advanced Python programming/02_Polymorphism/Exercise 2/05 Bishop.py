class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_diagonal_moves()