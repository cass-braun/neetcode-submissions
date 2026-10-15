class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        visitedCount = 0
        r, c = 0,0

        direction = 0
        while visitedCount < rows*cols:
            visitedCount += 1
            res.append(matrix[r][c])
            matrix[r][c] = '#'
            
            if direction == 0:
                if c+1 < cols and matrix[r][c+1] != '#':
                    c+=1
                else:
                    direction = 1
                    r+=1
            elif direction == 1:
                if r+1 < rows and matrix[r+1][c] != '#':
                    r+=1
                else:
                    c-=1
                    direction = 2
            elif direction == 2:
                if c-1 > -1 and matrix[r][c-1] != '#':
                    c-=1
                else:
                    r-=1
                    direction = 3
            elif direction == 3:
                if r-1 > -1 and matrix[r-1][c] != '#':
                    r-=1
                else:
                    c+=1
                    direction = 0
            
        return res

