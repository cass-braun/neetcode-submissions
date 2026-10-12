from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #inf = 2**31 - 1
        rows = len(grid)
        cols = len(grid[0])            


        q = deque()
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 0):
                    q.append([i,j])


        while q:
            i, j = q.popleft()
            value = grid[i][j]
            if i+1 < rows and value+1 < grid[i+1][j] :
                grid[i+1][j] = value +1
                q.append([i+1, j])
            
            if j+1 < cols and value+1 < grid[i][j+1] :
                grid[i][j+1] = value +1
                q.append([i, j+1])

            if i-1 > -1 and value+1 < grid[i-1][j] :
                grid[i-1][j] = value +1
                q.append([i-1, j])
            
            if j-1 > -1 and value+1 < grid[i][j-1] :
                grid[i][j-1] = value +1
                q.append([i, j-1])

                

