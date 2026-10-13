from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        
        islands = 0
        for i in range(cols):
            for j in range(rows):
                if grid[i][j] != '0':
                    islands += 1
                    q = deque([[i,j]])
                    while q:
                        coords = q.popleft()
                        a = coords[0]
                        b = coords[1]
                        if a+ 1 < cols and grid[a+1][b] == '1':
                            grid[a+1][b] = '0'
                            q.append([a+1, b])

                        if a-1 > -1 and grid[a-1][b] == '1':
                            grid[a-1][b] = '0'
                            q.append([a-1, b])
                        if b+1 < rows and grid[a][b+1] == '1':
                            grid[a][b+1] = '0'
                            q.append([a, b+1])

                        if b-1 > -1 and grid[a][b-1] == '1':
                            grid[a][b-1] = '0'
                            q.append([a, b-1])
        
        return islands
                    
                    