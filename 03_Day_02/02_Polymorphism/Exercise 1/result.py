class Chessboard:
    def __init__(self):
        # player to move first
        self.color = "white"

        # 8x8 board filled with None
        self.board = []
        for _ in range(8):
            self.board.append([None] * 8)