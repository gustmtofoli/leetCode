class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        
        if rows == 0:
            return 0
        
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)

'''
Approach: Using DFS(Depth First Search) to find all neighborhood when an element is '1'. All the time an element is '1' the counter is incremented, and then I call dfs to find all element of the island.

Time complexity: O(R*C) where R is the number of rows and C is the number os columns of the grid.
'''