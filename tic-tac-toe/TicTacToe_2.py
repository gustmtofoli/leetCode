class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [[0, 0] for _ in range(self.n)]
        self.cols = [[0, 0] for _ in range(self.n)]
        self.diagPrim = [0, 0]
        self.diagSec = [0, 0]
        

    def move(self, row: int, col: int, player: int) -> int:
        i = player - 1
        self.rows[row][i] += 1
        self.cols[col][i] += 1
        
        if row == col:
            self.diagPrim[i] += 1
        
        if row + col == self.n - 1:
            self.diagSec[i] += 1
        
        if self.rows[row][i] == self.n or self.cols[col][i] == self.n or self.diagPrim[i] == self.n or self.diagSec[i] == self.n:
            return player
        
        return 0
            