from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        
        rotten = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append([i,j]) 
                    
        minutes = 0
        q = deque([rotten])

        while q:
            rottens = q.popleft()

            newRottens = []
            for [i, j] in rottens:
                if i+1 < rows and grid[i+1][j] == 1:
                    newRottens.append([i+1,j])
                    grid[i+1][j] = 2
                if i-1 > -1 and grid[i-1][j] == 1:
                    newRottens.append([i-1,j])
                    grid[i-1][j] = 2
                if j+1 < cols and grid[i][j+1] == 1:
                    newRottens.append([i,j+1])
                    grid[i][j+1] = 2
                if j-1 > -1 and grid[i][j-1] == 1:
                    newRottens.append([i,j-1])
                    grid[i][j-1] = 2
            
            if newRottens:
                q.append(newRottens)
                minutes +=1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1


        return minutes
                    




