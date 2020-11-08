''' Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first. '''

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