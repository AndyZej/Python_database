class Chessboard:
    def move(self, from_x, from_y, to_x, to_y):
        allowed = self.list_allowed_moves(from_x, from_y)
        if allowed is None or (to_x, to_y) not in allowed:
            raise ValueError("Illegal move")

        moving_piece = self.board[from_x][from_y]
        target_piece = self.board[to_x][to_y]

        # ✅ GAME END DETECTION
        if isinstance(target_piece, King):
            if target_piece.color == "white":
                return "BLACK WON"
            else:
                return "WHITE WON"

        # perform move
        moving_piece.move(to_x, to_y)
        self.board[to_x][to_y] = moving_piece
        self.board[from_x][from_y] = None

        # switch player
        self.color = "black" if self.color == "white" else "white"