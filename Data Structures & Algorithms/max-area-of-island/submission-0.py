from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    size = 1

                    q = deque([[i,j]])
                    while q:
                        coords = q.popleft()

                        x = coords[0]
                        z = coords[1]
                        if x+1 < len(grid) and grid[x+1][z] == 1:
                            size +=1
                            grid[x+1][z] = 0
                            q.append([x+1,z])

                        if x-1> -1 and grid[x-1][z] == 1:
                            size +=1
                            grid[x-1][z] = 0
                            q.append([x-1,z])
                        

                        if z+1 < len(grid[0]) and grid[x][z+1] == 1:
                            size +=1
                            grid[x][z+1] = 0
                            q.append([x,z+1])

                        if z-1 > -1 and grid[x][z-1] == 1:
                            size +=1
                            grid[x][z-1] = 0
                            q.append([x,z-1])
                        
                    maxSize = max(size, maxSize)
        return maxSize


        