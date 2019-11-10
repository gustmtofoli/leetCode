class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.toe = [[0 for i in range(n)] for i in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        toe = self.toe
        
        if row < 0 and col < 0:
            return
        
        if toe[row][col] == 0:
            toe[row][col] = player
        
        winner1 = [1 for i in range(self.n)]
        winner2 = [2 for i in range(self.n)]
        
        for k in range(self.n):
            if toe[k] == winner1:
                return 1
            
            if toe[k] == winner2:
                return 2
        
        toeT = [[toe[j][i] for j in range(self.n)] for i in range(self.n)]
        for k in range(self.n):
            if toeT[k] == winner1:
                return 1
            
            if toeT[k] == winner2:
                return 2
        
        diagPrim = []
        diagSec = []
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    diagPrim.append(toe[i][j])
                    
                if i + j == self.n - 1:
                    diagSec.append(toe[i][j])
                    
        if diagPrim == winner1 or diagSec == winner1:
            return 1

        if diagPrim == winner2 or diagSec == winner2:
            return 2
        
        return 0
            
'''
Approach: Brute force. this approach walks through all the matrix more than one time to find the winner.
Time complexity: O(n²)

Obs.: This approach got 'time limit exceeded' in the last test 
'''