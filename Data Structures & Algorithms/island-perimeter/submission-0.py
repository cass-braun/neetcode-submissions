from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        startR, startC = 0,0

        while grid[startR][startC] != 1:
            if startC == len(grid[0])-1 and startR == len(grid)-1:
                return 0
            elif startC == len(grid[0])-1:
                startC = 0
                startR += 1
            else:
                startC += 1
        
        q = deque([[startR, startC]])
        grid[startR][startC] = '#'
        perim = 0
    
        while q:
            r, c = q.pop()
            

            for dr, dc in d:
                nr, nc = r + dr, c + dc

                if -1 < nr < len(grid) and -1 < nc < len(grid[0]) and grid[nr][nc] == 1:
                    q.append([nr, nc])
                    grid[nr][nc] = '#'
                elif (-1 < nr < len(grid) and -1 < nc < len(grid[0]) and grid[nr][nc] == 0) or not (-1 < nr < len(grid) and -1 < nc < len(grid[0])):
                    perim +=1
        return perim
